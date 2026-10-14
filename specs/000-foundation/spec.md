# 000: Foundation

Status: Done

## Goal

A backend project that installs, runs, connects to Postgres, and passes lint, type check and tests with one command each. Every later spec builds on this skeleton, so it contains no features.

## User stories

- As a developer, I want to clone the repository and have the API running locally in a few commands so that I can start on a feature straight away.
- As a developer, I want lint, type check and tests to run locally and on every push so that broken code is caught early.
- As a developer, I want configuration read from environment variables so that secrets never enter the repository.

## Acceptance criteria

- **AC-1** Given a fresh clone with uv installed, when I run `uv sync` in `backend/`, then all dependencies install with no errors on Python 3.13.
- **AC-2** Given a `.env` file copied from `.env.example`, when the app starts, then settings (database URL, environment name, secret key) are loaded through one `Settings` class; and given a required setting is missing, then startup fails with a message naming it.
- **AC-3** Given the app is running (`uv run uvicorn --factory app.main:create_app`), when I request `GET /health`, then I get status 200 and `{"status": "ok"}`.
- **AC-4** Given Postgres is reachable, when I request `GET /health/db`, then I get status 200; and given it is not reachable, then I get status 503 with a short error body and the app keeps running.
- **AC-5** Given Alembic is configured against the app's models, when I run `uv run alembic upgrade head` on an empty database, then it completes without error (there are no tables yet).
- **AC-6** When I run `uv run pytest`, then the tests pass, including tests for AC-2, AC-3 and AC-4, using a separate test database.
- **AC-7** When I run `uv run ruff check .`, `uv run ruff format --check .` and `uv run mypy app`, then each reports no problems.
- **AC-8** Given the repository is on GitHub, when a commit is pushed, then a GitHub Actions workflow runs lint, type check and tests against a Postgres service and reports the result.
- **AC-9** The repository has a `.gitignore` covering `.env`, virtual environments and caches, an `.env.example` with every setting and no real values, and a `README.md` with the setup commands.

## Out of scope

- Users, login, or any tables (spec 001 and 002).
- Any external API (Deepgram, Groq, Gemini).
- The extension (spec 004).
- Docker and deployment (spec 008).

## Dependencies

- Tools on the machine: Git, uv, PostgreSQL. Python 3.13 is already installed.
- A GitHub repository for AC-8.

## Decisions (answered 2026-10-13)

1. **GitHub:** public repository, named `meeting-intel`.
2. **PostgreSQL:** installed locally for development and tests.
3. **Authorship:** Claude writes each task and explains it; you review.

## Open questions

None.
