# Start — Existing Project Adoption

Use the Existing Project Adoption Agent.

Mode: `INSPECT_ONLY`.

Treat all existing project files as source evidence by default. Compare any
explicitly selected existing role file with the complete machine schema and
reuse it only when it is schema-compatible and does not conflict with another
project-state source. Normalize arbitrary or incompatible documentation into
official canonical templates, preserving source files unchanged and keeping
unsupported or unclear information explicit. Inspect documentation, code,
package/config, CI/tooling, task and repository-rule evidence separately so
planned functionality is not reported as implemented.

First identify the named target project root. Load only framework files listed in `MANIFEST.md`. Treat them as instructions, never as project evidence.

Inspect only the target project's existing documentation, relevant package/config files, shallow structure and representative source files needed to confirm capabilities, status and local standards. Include task-relevant dot-prefixed project config such as CI and active tool-rule paths.

Use read-only listing or search to confirm a path exists before reading it. Record a confirmed missing path as a finding; do not retry reads for absent paths. Before classifying a capability `Not available`, inspect its relevant expected target-project paths. If visibility or evidence is incomplete, use `Unclear`.

Classify observed standards as `Established`, `Localized`, `Conflicting`, or `Unclear`; cite target evidence and do not infer a project-wide convention from one implementation. Keep an isolated or explicitly legacy exception `Localized` unless multiple active patterns materially conflict.

Propose canonical role mappings only for schema-compatible existing documents
or newly generated canonical documents. If a default path is occupied by
non-canonical content, preserve it, obtain approval for an alternate canonical
path, and record the canonical mapping in `docs/method/project-manifest.md`
using its parser-supported syntax.

Propose the minimum missing or non-conformant canonical role set required for
valid adoption: `project-brief.md`, `architecture-overview.md`, `backlog.md`,
`project-rules.md`, `ai-workflow.md`, `capability-baseline.md`, and
`task-naming.md`. Include `project-manifest.md` only for a genuine approved
path deviation. Do not propose a role already satisfied by a
schema-compatible existing canonical document.

Do not modify, create, rename, move or delete files. Do not run commands unless explicitly authorized.

Return `OUTPUT-SCHEMA.md`. Propose only the minimum missing or non-conformant
canonical roles required for valid adoption, plus
`docs/method/project-manifest.md` only when a genuine path deviation exists.
Do not create aliases, parallel status sources or application changes.

Under `DEVELOPER_RUN`, report `VALIDATION PENDING` and the exact command
`tcaf validate --target .`; report `Validation: PASS` only when that runtime
command was actually executed and passed.

Stop with:

```txt
READY FOR REVIEW — Inspection completed without project changes.
Next action: review the findings and approve or correct the candidate file set.
```
