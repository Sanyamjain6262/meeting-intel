# 008: Release

Status: Draft (stub — expand when 007 is Done)

## Goal

The project is presentable to a recruiter or interviewer: easy to understand, easy to run, and visibly working.

## Draft acceptance criteria

- **AC-1** The README explains what it does, shows an architecture diagram and a demo GIF, and gives setup steps that work from a fresh clone.
- **AC-2** A Dockerfile builds the backend, and one documented command runs it with Postgres.
- **AC-3** Either a public demo is deployed on a free host, or the README states why not and how to run locally.
- **AC-4** Each meeting logs speech-to-text minutes and LLM tokens used, so usage can be compared with free-tier limits.
- **AC-5** CI is green and the repository contains no secrets.

## Out of scope

Chrome Web Store listing; paid hosting.

## Dependencies

007. Hosting account; hosted Postgres.

## Open questions

- Which free host, after checking current limits and WebSocket support.
