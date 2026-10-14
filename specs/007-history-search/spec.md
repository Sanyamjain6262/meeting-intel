# 007: History and search

Status: Draft (stub — expand when 006 is Done)

## Goal

A user can browse past meetings and find what was said by keyword.

## Draft acceptance criteria

- **AC-1** A history page lists the user's meetings with title, date, duration and note counts, paginated.
- **AC-2** A meeting page shows the summary, the notes grouped by category, and the full transcript; selecting a note scrolls to its source segment.
- **AC-3** `GET /search?q=` searches segments and notes with Postgres full-text search and returns ranked results with the matching words highlighted and a link to the meeting and position.
- **AC-4** Results can be filtered by note category and date range.
- **AC-5** Results never include another user's data.
- **AC-6** The pages are served by FastAPI with Jinja2 and HTMX, and require login.

## Out of scope

Semantic search; editing transcripts.

## Dependencies

006.

## Open questions

- Search language configuration if meetings are not only in English.
