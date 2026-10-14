# Architecture

## Shape

A thin Chrome extension in front of a Python backend.

- **Extension (TypeScript, Manifest V3, WXT):** captures tab audio (`chrome.tabCapture`) and the microphone (`getUserMedia`), mixes them in an offscreen document, streams the audio to the backend over a WebSocket, and shows the live transcript and tagged notes in a side panel.
- **Backend (Python 3.13, FastAPI):** speech-to-text relay, batching, tagging, summary, storage, auth, search, and the history and search web pages.

It works on Google Meet, Zoom web, Teams web and any tab with audio, with no bot joining the call. It does not capture the Zoom or Teams desktop apps.

```
Meeting tab ──tabCapture──┐
Microphone ──getUserMedia─┤
                          ▼
        Offscreen document (mix to mono 16 kHz PCM, keep tab audible)
                          │ WebSocket /ws/meetings/{id}  (JWT)
                          ▼
┌──────────────────── FastAPI backend (Python) ─────────────────────────┐
│ audio relay ──► Deepgram streaming (Nova-3, diarize)                   │
│ final utterances ──► save segments ──► push to client                  │
│ buffer 30 s ──► tagger (Groq, Pydantic schema) ──► save notes ──► push │
│ on stop ──► summarizer (Gemini) ──► save summary                       │
│ REST: auth, meetings, search      HTML: Jinja2 + HTMX dashboard        │
└──────────────────────────────┬────────────────────────────────────────┘
                               ▼
                           Postgres
```

## Stack

| Layer | Choice |
|---|---|
| Language / runtime | Python 3.13, `uv` for dependencies |
| Web framework | FastAPI, `uvicorn`, native WebSockets, `asyncio` |
| Speech-to-text | `deepgram-sdk` (Nova-3 streaming, diarization) |
| LLM | `groq` and `google-genai` SDKs behind a small router with rate-limit fallback |
| Schemas / settings | Pydantic v2, `pydantic-settings` |
| Database | Postgres (local for development, Supabase free tier when deployed), SQLAlchemy 2 async with `asyncpg`, Alembic |
| Keyword search | Postgres `tsvector` with a GIN index, `websearch_to_tsquery`, `ts_headline` |
| Auth | JWT (`pyjwt`), Argon2 password hashing (`pwdlib`) |
| Dashboard | Jinja2 templates, HTMX, Tailwind (CDN) |
| Tests / quality | `pytest`, `pytest-asyncio`, `httpx`, `ruff`, `mypy` |
| CI / packaging | GitHub Actions; Docker for release |
| Extension | WXT, TypeScript |

## Models and free-tier limits

Checked on 2026-10-13. Rows marked *unverified* came only from third-party posts that disagreed with each other; confirm in the provider console before depending on them.

| Job | Service | Free allowance | Source |
|---|---|---|---|
| Live transcription | Deepgram Nova-3 streaming | $200 credit, no card, no expiry. $0.0048–0.0077/min plus $0.002/min for diarization: roughly 340–490 hours | [Deepgram pricing](https://deepgram.com/pricing) |
| Live tagging | Groq `openai/gpt-oss-20b` | 30 requests/min, 1K requests/day, 8K tokens/min, 200K tokens/day | [Groq rate limits](https://console.groq.com/docs/rate-limits) |
| Tagging fallback | Groq `openai/gpt-oss-120b`, `qwen/qwen3.8-27b` | Same limits, counted per model | same |
| Summary | Gemini Flash | About 20 requests/day (*unverified*) | [Gemini rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) points to AI Studio for the numbers |
| Summary fallback | Gemini Flash-Lite, or Groq `gpt-oss-120b` with chunking | About 500 requests/day (*unverified*) | same |
| Database (deployed) | Supabase Postgres | 500 MB; project pauses after 7 days idle (*third-party sources*) | [Supabase limits](https://automationatlas.io/answers/supabase-free-tier-limits-2026/) |

Why not the services in the original brief:

- **Google Cloud Speech-to-Text:** the free allowance is 60 minutes a month on the V1 API only, with billing enabled. The speech layer has an interface so a Google adapter can be added.
- **OpenAI:** there is no "decision API", and no free API tier. Tagging uses structured output (a JSON schema), which Groq provides free. The LLM layer has an interface so an OpenAI model can be swapped in.

Tagging budget: sentences are batched every 30 seconds (configurable), about 60–120 calls and 50–100K tokens per meeting hour.

## Data model

- `users` (id, email, password_hash, created_at)
- `meetings` (id, user_id, title, platform, started_at, ended_at, summary, summary_json)
- `segments` (id, meeting_id, speaker, start_ms, end_ms, text, `tsv` generated tsvector)
- `notes` (id, meeting_id, category, text, segment_ids[], at_ms, `tsv`)

Note categories: `question`, `decision`, `action_item`, `update`, `concern`. The tagger may also return `none`, which is dropped.

## Layout

```
meeting-intel/
  docs/                  # roadmap, constitution, this file
  specs/                 # one folder per spec
  backend/
    app/
      main.py            # app factory, routers
      config.py          # pydantic-settings
      db.py, models.py, schemas.py
      auth/              # routes, security, dependencies
      api/               # meetings.py, search.py
      ws/session.py      # WebSocket handler, per-meeting state
      services/
        stt/             # base.py, deepgram.py
        llm/             # base.py, groq.py, gemini.py, router.py
        tagger.py
        summarizer.py
        search.py
      web/               # Jinja2 routes, templates, static
    alembic/
    tests/
    scripts/stream_wav.py
    pyproject.toml
  extension/
    wxt.config.ts
    entrypoints/background.ts, offscreen/, sidepanel/
  .github/workflows/ci.yml
```

## To confirm before the spec that needs it

- Groq: free-plan limits for our account, and that `gpt-oss-20b` accepts the `json_schema` response format (spec 005).
- Gemini: free limits per model in AI Studio (spec 006).
- Deepgram: whether the promotional streaming price still applies (spec 003).
- Hosting: free-tier limits and WebSocket behaviour on Render or an alternative (spec 008).
