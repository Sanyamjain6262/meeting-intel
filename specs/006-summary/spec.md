# 006: Summary

Status: Draft (stub — expand when 005 is Done)

## Goal

When a meeting ends, it gets a structured summary.

## Draft acceptance criteria

- **AC-1** Stopping a meeting starts summarisation in the background; the stop request does not wait for it.
- **AC-2** The summary contains an overview, decisions, action items with owners where stated, and open questions, validated against a Pydantic model and stored on the meeting.
- **AC-3** Transcripts too long for one request are summarised in chunks and then combined.
- **AC-4** If summarisation fails, the meeting and its transcript are unaffected, the failure is recorded, and `POST /meetings/{id}/summarize` retries it.
- **AC-5** The summariser falls back to the next model on a rate-limit response.
- **AC-6** Unit tests use a fake LLM.

## Out of scope

Emailing or exporting summaries.

## Dependencies

005. Google AI Studio API key.

## Open questions

- Confirm Gemini free-tier limits per model in AI Studio.
