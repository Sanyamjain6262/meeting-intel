# 005: Live tagging

Status: Draft (stub — expand when 003 is Done)

## Goal

While a meeting runs, important sentences are turned into notes labelled question, decision, action item, update or concern, and shown live.

## Draft acceptance criteria

- **AC-1** Final utterances are buffered and sent to the tagger in batches every 30 seconds (configurable), with a few earlier sentences as context; remaining sentences are flushed when the meeting stops.
- **AC-2** The tagger calls the LLM with a JSON schema derived from Pydantic models; each returned note has exactly one of the five categories, a short text, and the ids of its source segments. Sentences labelled `none` produce no note.
- **AC-3** Output that fails validation is rejected and retried once; a second failure skips the batch and logs it without stopping the meeting.
- **AC-4** A rate-limit response moves the request to the next model in the fallback list.
- **AC-5** Notes are saved and pushed to the client over the meeting WebSocket; the side panel shows them grouped by category.
- **AC-6** The LLM is used through an interface; unit tests use a fake and spend no quota.
- **AC-7** On a hand-labelled test transcript run against the real model, at least 80% of labels agree (manual check, result recorded in the spec).

## Out of scope

Editing or deleting notes by hand; the end-of-meeting summary (006).

## Dependencies

003 (and 004 for the side-panel part of AC-5). Groq account and API key.

## Open questions

- Confirm `gpt-oss-20b` supports `json_schema` output on the free plan.
- Whether action items should capture an owner at this stage or only in the summary.
