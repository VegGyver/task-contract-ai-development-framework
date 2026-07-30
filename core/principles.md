# Core Principles

1. **Repository first** — repository files are the source of truth; chat memory is not.
2. **Bounded tasks** — every edit has an explicit goal, edit surface, allowed changes and stop condition.
3. **Explicit permission** — if a file or change type is not allowed, do not change it.
4. **Minimum-first prompts** — start with the shortest safe instruction set; add detail only when repeated evidence shows it is needed.
5. **Selective context** — inspect only relevant files and load only required framework modules.
6. **Existing capabilities only** — do not introduce libraries, scripts, tools, architecture or test infrastructure without approval.
7. **Preservation first** — integrate with working code; do not rewrite, merge, optimize or restructure it unless the task is `REFACTOR`.
8. **Reuse before adding** — reuse existing functions, guards, validations, helpers and local patterns; do not duplicate controls.
9. **Implementation source hierarchy** — existing projects follow verified local patterns first; greenfield work and missing local patterns follow official documentation compatible with the selected version, then established ecosystem practice only when official guidance is insufficient.
10. **No silent conflict** — if a local pattern conflicts with official security, compatibility or correctness requirements, report the conflict and stop for a decision.
11. **Smallest useful change** — one complete, bounded and verifiable reason to change.
12. **Logical gates** — gates depend on explicit task state, not on buttons or UI behavior of a tool.
13. **Tool resilience** — the workflow must work even when the agent cannot run commands.
14. **Human acceptance** — agent self-checks help, but the developer reviews, verifies, accepts and commits.
15. **Immutable history** — completed task scope is not rewritten; later work is appended as linked change, fix or extension records.
16. **Team naming** — the project or tracker defines task IDs; the framework does not impose one universal format.
