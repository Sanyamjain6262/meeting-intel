# 002: Meetings data

Status: Draft (stub — expand when 001 is Done)

## Goal

The database can hold meetings, transcript segments and notes, and the API can create and read meetings for the logged-in user.

## Draft acceptance criteria

- **AC-1** An Alembic migration creates `meetings`, `segments` and `notes` with the columns in `docs/architecture.md`, including generated `tsvector` columns and GIN indexes.
- **AC-2** `POST /meetings` creates a meeting owned by the caller; `GET /meetings` lists only the caller's meetings, newest first, paginated.
- **AC-3** `GET /meetings/{id}` returns the meeting with its segments and notes; `PATCH` renames it; `DELETE` removes it and its segments and notes.
- **AC-4** Requesting another user's meeting gives 404.
- **AC-5** Note category accepts only `question`, `decision`, `action_item`, `update`, `concern`.

## Out of scope

Writing segments and notes from live audio (003, 005); search (007).

## Dependencies

001.

## Open questions

- Integer or UUID primary keys.
