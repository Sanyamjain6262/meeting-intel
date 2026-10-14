# Meeting Intel

Live meeting transcription, live tagging of questions, decisions, action items, updates and concerns, end-of-meeting summaries, and searchable history. A thin Chrome extension in front of a Python (FastAPI) backend, built on free-tier services.

The project is built spec by spec. Start with [docs/ROADMAP.md](docs/ROADMAP.md); design is in [docs/architecture.md](docs/architecture.md).

## Backend setup

Requires Python 3.13, [uv](https://docs.astral.sh/uv/) and PostgreSQL 17.

```powershell
# 1. Create the databases (once)
createdb -U postgres meeting_intel
createdb -U postgres meeting_intel_test

# 2. Install dependencies
cd backend
uv sync

# 3. Configure: copy the example and fill in your Postgres password and a secret key
Copy-Item .env.example .env

# 4. Apply migrations and run
uv run alembic upgrade head
uv run uvicorn --factory app.main:create_app --reload
```

The API is then at http://localhost:8000, with interactive docs at http://localhost:8000/docs.

## Checks

```powershell
cd backend
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy app
```
