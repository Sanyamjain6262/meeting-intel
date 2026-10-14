# 004: Extension

Status: Draft (stub — expand when 003 is Done)

## Goal

From a Chrome side panel, a user can start and stop capturing a meeting tab and watch the transcript appear.

## Draft acceptance criteria

- **AC-1** The user can log in from the side panel; the token is stored in extension storage.
- **AC-2** Pressing Start on a tab with audio creates a meeting, captures tab audio and microphone, and streams the mixed audio to the backend.
- **AC-3** The tab remains audible to the user while it is being captured.
- **AC-4** Interim and final transcript lines appear in the side panel within about one second of speech, with speaker labels.
- **AC-5** Pressing Stop ends the capture, closes the stream, and releases the microphone.
- **AC-6** It works on a YouTube tab and on a two-person Google Meet call (manual checks).
- **AC-7** The extension holds no API keys and requests only the permissions it uses.

## Out of scope

Tagged notes in the panel (005); history pages (007); publishing to the Chrome Web Store.

## Dependencies

003. Node.js LTS.

## Open questions

- Whether microphone capture is on by default or a toggle.
