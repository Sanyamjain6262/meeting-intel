# 000: Foundation — Tasks

One task per commit. Each task names the acceptance criteria it covers. Lint, type check and tests pass before a box is ticked.

- [x] 0. Prerequisites: Git, uv and PostgreSQL installed; databases `meeting_intel` and `meeting_intel_test` created (you run the installs)
- [x] 1. `git init`, `.gitignore`, `README.md` skeleton, first commit including `docs/` and `specs/` (AC-9)
- [x] 2. `backend/pyproject.toml` with dependencies and ruff, mypy, pytest configuration; `uv sync` succeeds (AC-1, AC-7)
- [x] 3. `app/config.py` and `.env.example`, with `tests/test_config.py` (AC-2)
- [x] 4 + 5. App factory, `app/db.py`, `GET /health` and `GET /health/db`, with tests for reachable and unreachable database (AC-3, AC-4, AC-6). One commit: the health router needs the session dependency.
- [x] 6. Alembic initialised for async and wired to `Settings`; `alembic upgrade head` runs clean (AC-5)
- [x] 7. `.github/workflows/ci.yml` with a Postgres service (AC-8)
- [x] 8. Create the public GitHub repository and push (AC-8)

## Verification

- [x] AC-1 demonstrated: `uv sync` installed 42 packages on Python 3.13.15
- [x] AC-2 demonstrated: config tests pass, including missing `DATABASE_URL` and `SECRET_KEY`
- [x] AC-3 demonstrated: running server returned `200 {"status":"ok"}` for `/health`
- [x] AC-4 demonstrated: `/health/db` returned 200 on a running server; the 503 case is covered by a test with an unreachable database
- [x] AC-5 demonstrated: `alembic upgrade head` completed against `meeting_intel`
- [x] AC-6 demonstrated: `uv run pytest` 6 passed
- [x] AC-7 demonstrated: ruff check, ruff format and mypy clean
- [x] AC-8 demonstrated: GitHub Actions run 38644916381 green (lint, types, migration, tests)
- [x] AC-9 demonstrated: files present, `backend/.env` and `backend/.venv` ignored
- [x] Status set to Done in `docs/ROADMAP.md`
