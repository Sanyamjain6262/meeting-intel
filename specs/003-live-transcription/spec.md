# 003: Live transcription

Status: Draft (stub — expand when 002 is Done)

## Goal

A client can stream audio to the backend and receive a live transcript with speaker labels, which is saved to the meeting.

## Draft acceptance criteria

- **AC-1** `/ws/meetings/{id}` accepts a connection only with a valid token for the meeting's owner.
- **AC-2** Given 16 kHz mono PCM audio frames, the server relays them to the speech-to-text provider and sends back interim and final transcript messages in a documented JSON format, with speaker label and timestamps.
- **AC-3** Each final utterance is saved as a segment.
- **AC-4** The provider is used through a `SpeechToText` interface; tests run against a fake provider and use no quota.
- **AC-5** `scripts/stream_wav.py` streams a sample WAV file to a running server and prints the transcript as it arrives (manual check against real Deepgram).
- **AC-6** If the client disconnects or the provider fails, the provider connection is closed, saved segments are kept, and the meeting is marked ended.

## Out of scope

Capturing audio from a browser (004); tagging (005).

## Dependencies

002. Deepgram account and API key.

## Open questions

- Audio format on the wire (raw PCM or Opus).
- Language setting: English only or multilingual (affects price).
