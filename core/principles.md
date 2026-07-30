# Core Principles

1. **Repository first** — repository files are the source of truth; chat memory is not.
2. **Bounded tasks** — every edit has an explicit goal, edit surface, allowed changes and stop condition.
3. **Explicit permission** — if a file or change type is not allowed, do not change it.
4. **Minimum-first prompts** — start with the shortest safe instruction set; add detail only when repeated evidence shows it is needed.
5. **Outcome-first responses** — begin with the result, completed action and next step; add explanation only for decisions, deviations, failures or ambiguity.
6. **Selective context** — inspect only relevant files and load only required framework modules.
7. **Existing capabilities only** — do not introduce libraries, scripts, tools, architecture or test infrastructure without approval.
8. **Preservation first** — integrate with working code; do not rewrite, merge, optimize or restructure it unless the task is `REFACTOR`.
9. **Live workspace state** — re-read current files before continuing; preserve developer or concurrent changes and never restore uncertain work automatically.
10. **Reuse before adding** — reuse existing functions, guards, validations, helpers and local patterns; do not duplicate controls.
11. **Implementation source hierarchy** — existing projects follow verified local patterns first; greenfield work and missing local patterns follow official documentation compatible with the selected version, then established ecosystem practice only when official guidance is insufficient.
12. **No silent conflict** — if a local pattern conflicts with official security, compatibility or correctness requirements, report the conflict and stop for a decision.
13. **Smallest useful change** — one complete, bounded and verifiable reason to change.
14. **Logical gates** — gates depend on explicit task state, not on buttons or UI behavior of a tool.
15. **Tool resilience** — the workflow must work even when the agent cannot run commands.
16. **Human acceptance** — agent self-checks help, but the developer reviews, verifies, accepts and commits.
17. **Immutable history** — completed task scope is not rewritten; later work is appended as linked change, fix or extension records.
18. **Team naming** — the project or tracker defines task IDs; the framework does not impose one universal format.
