# Start — Existing Project Adoption

Use the Existing Project Adoption Agent.

Mode: `INSPECT_ONLY`.

First identify the named target project root. Load only framework files listed in `MANIFEST.md`. Treat them as instructions, never as project evidence.

Inspect only the target project's existing documentation, relevant package/config files, shallow structure and representative source files needed to confirm capabilities, status and local standards. Include task-relevant dot-prefixed project config such as CI and active tool-rule paths.

Use read-only listing or search to confirm a path exists before reading it. Record a confirmed missing path as a finding; do not retry reads for absent paths. Before classifying a capability `Not available`, inspect its relevant expected target-project paths. If visibility or evidence is incomplete, use `Unclear`.

Classify observed standards as `Established`, `Localized`, `Conflicting`, or `Unclear`; cite target evidence and do not infer a project-wide convention from one implementation. Keep an isolated or explicitly legacy exception `Localized` unless multiple active patterns materially conflict.

Do not modify, create, rename, move or delete files. Do not run commands unless explicitly authorized.

Return `OUTPUT-SCHEMA.md`. Propose only the standard missing core method documents and, when path deviations exist, `docs/method/project-manifest.md`. Do not create aliases, parallel status sources or application changes.

Stop with:

```txt
No files changed.
Waiting for developer review.
```
