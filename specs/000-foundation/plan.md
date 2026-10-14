# 000: Foundation — Plan

## Approach

Create a `backend/` uv project with FastAPI built through an app factory (`create_app()`), so tests can build an app with their own settings. Settings come from one `pydantic-settings` class reading `.env`. The database layer is an async SQLAlchemy engine and session dependency; no models exist yet, only the declarative `Base` that Alembic points at. Two health routes prove the app and the database connection work. Tooling (ruff, mypy, pytest) is configured in `pyproject.toml`, and a GitHub Actions workflow runs the same commands against a Postgres service container.

## Files and modules

| Path | New or changed | Purpose |
|---|---|---|
| `.gitignore`, `README.md` | New | Repository basics and setup commands |
| `backend/pyproject.toml` | New | Dependencies and ruff, mypy, pytest configuration |
| `backend/.env.example` | New | Every setting, no real values |
| `backend/app/config.py` | New | `Settings` class and cached `get_settings()` |
| `backend/app/db.py` | New | Async engine, session factory, `get_session` dependency, `Base` |
| `backend/app/main.py` | New | `create_app()` and router registration |
| `backend/app/api/health.py` | New | `GET /health`, `GET /health/db` |
| `backend/alembic.ini`, `backend/alembic/env.py` | New | Async Alembic setup reading the URL from `Settings` |
| `backend/tests/conftest.py` | New | Test settings, app and `httpx.AsyncClient` fixtures |
| `backend/tests/test_config.py`, `test_health.py` | New | Tests for AC-2, AC-3, AC-4 |
| `.github/workflows/ci.yml` | New | Lint, type check, tests with a Postgres service |

Dependencies: `fastapi`, `uvicorn[standard]`, `pydantic-settings`, `sqlalchemy[asyncio]`, `asyncpg`, `alembic`. Development: `pytest`, `pytest-asyncio`, `httpx`, `ruff`, `mypy`.

## API and schema changes

| Method | Path | Success | Failure |
|---|---|---|---|
| GET | `/health` | 200 `{"status": "ok"}` | none |
| GET | `/health/db` | 200 `{"status": "ok"}` after `SELECT 1` | 503 `{"status": "unavailable"}` |

Settings: `DATABASE_URL`, `SECRET_KEY` (both required), `ENVIRONMENT` (default `development`).

No tables. Two local databases: `meeting_intel` and `meeting_intel_test`.

## Test strategy

| Acceptance criterion | Test type | Where |
|---|---|---|
| AC-1 | manual | `uv sync` on this machine, and in CI |
| AC-2 | unit | `tests/test_config.py`: loads values; missing `DATABASE_URL` raises a validation error naming it |
| AC-3 | integration | `tests/test_health.py` |
| AC-4 | integration | `tests/test_health.py`: real test database for 200; an app built with an unreachable URL for 503 |
| AC-5 | manual, and CI step | `alembic upgrade head` |
| AC-6, AC-7 | command | `pytest`, `ruff`, `mypy` |
| AC-8 | manual | Push and check the Actions tab |
| AC-9 | review | Files present; `git status` shows `.env` ignored |

Nothing is mocked; the database tests use real Postgres.

## Risks

- **Python 3.13 wheels:** if a dependency has no 3.13 wheel on Windows, pin the previous release or have uv install Python 3.12 for the project.
- **asyncpg on Windows event loop:** if tests hit event-loop errors, set the loop scope in the pytest-asyncio configuration to session.
- **Local Postgres password:** kept only in `.env`, which is ignored by Git.
