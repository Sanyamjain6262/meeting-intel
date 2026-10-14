# Constitution

Rules that hold for every spec. Changing one of these is a deliberate decision recorded here, not something that happens in passing during a feature.

1. **Spec first.** No code without an approved spec. Nothing is Done until every acceptance criterion has been demonstrated.
2. **Tests come from acceptance criteria.** Each criterion maps to at least one test, written before or alongside the code.
3. **External services sit behind an interface.** Deepgram, Groq and Gemini are each wrapped in a small class with a base protocol, and are mocked in unit tests. Tests never spend free-tier quota.
4. **Secrets stay on the server.** API keys live only in backend environment variables. They never appear in the extension, the repository, or logs.
5. **Free-tier limits are a design input.** Batch, cache and fall back before adding a paid dependency. Any number we rely on is recorded in `architecture.md` with its source.
6. **Python holds the logic.** The extension captures audio and displays results. Anything that decides, stores or transforms lives in the backend.
7. **Scope changes go through the spec.** If the work needs to differ from the spec, edit the spec first, then the code.
8. **Small steps.** One task from `tasks.md` per commit, with lint, type check and tests passing.
