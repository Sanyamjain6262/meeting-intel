# Roadmap

Meeting intelligence platform: live transcription, live tagging, summaries, and searchable history. Python-first, free-tier only.

This is the file to follow. Work goes top to bottom through the spec list. Rules are in [constitution.md](constitution.md); stack and design are in [architecture.md](architecture.md).

## Workflow for every spec

| Step | Output | Who |
|---|---|---|
| 1. Specify | `spec.md`: goal, user stories, acceptance criteria, out of scope, open questions | Claude drafts, you review |
| 2. Plan | `plan.md`: modules, endpoints, schema changes, test strategy | Claude drafts, you review |
| 3. Tasks | `tasks.md`: ordered checklist, each task small enough for one commit | Claude |
| 4. Implement | Code and tests, one task at a time, ticking `tasks.md` | Claude, or you with Claude reviewing |
| 5. Verify | Each acceptance criterion demonstrated; status set to Done here | Both |

Templates for the three files are in [`specs/_template/`](../specs/_template/).

Status values: **Draft** (written, not reviewed), **Approved** (ready to plan and build), **In progress**, **Done**.

## Spec list

| # | Spec | Goal | Needs | Status |
|---|---|---|---|---|
| 000 | [Foundation](../specs/000-foundation/spec.md) | Runnable, tested project skeleton | none | In progress |
| 001 | [Auth](../specs/001-auth/spec.md) | Users can register and log in | 000 | Draft (stub) |
| 002 | [Meetings data](../specs/002-meetings-data/spec.md) | Store meetings, segments, notes | 001 | Draft (stub) |
| 003 | [Live transcription](../specs/003-live-transcription/spec.md) | Audio in, transcript out | 002 | Draft (stub) |
| 004 | [Extension](../specs/004-extension/spec.md) | Capture a real call in Chrome | 003 | Draft (stub) |
| 005 | [Live tagging](../specs/005-live-tagging/spec.md) | Tagged notes during the meeting | 003 | Draft (stub) |
| 006 | [Summary](../specs/006-summary/spec.md) | Summary when the meeting ends | 005 | Draft (stub) |
| 007 | [History and search](../specs/007-history-search/spec.md) | Find things later | 006 | Draft (stub) |
| 008 | [Release](../specs/008-release/spec.md) | Presentable portfolio project | 007 | Draft (stub) |

A stub has the goal and draft acceptance criteria only. It is expanded into a full spec when the one before it is Done.

Possible later specs: semantic search with `pgvector`, Google Speech-to-Text adapter, Markdown export, desktop app capture.

## Prerequisites

Checked on 2026-10-13: Python 3.13 is installed; Git, uv, PostgreSQL, Node.js and Docker are not.

| Needed before | Install or create |
|---|---|
| Spec 000 | Git, uv, PostgreSQL (local) |
| Spec 003 | Deepgram account and API key |
| Spec 004 | Node.js LTS |
| Spec 005 | Groq account and API key |
| Spec 006 | Google AI Studio API key |
| Spec 008 | Hosting account (Render or similar), hosted Postgres (Supabase); Docker optional |

## Next action

Spec 000 needs only its last task: create the public GitHub repository, push, and confirm CI is green. See [`specs/000-foundation/tasks.md`](../specs/000-foundation/tasks.md). Then expand spec 001 (Auth).

Working agreement: Claude writes each task and explains it; you review. The GitHub repository is public and named `meeting-intel`.
