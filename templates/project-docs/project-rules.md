# Project Rules

## Scope

Use this document as the canonical tool-agnostic project rules source. Tool adapters should remain compact and derived from it.

## Source of truth

- Repository files and approved project documentation are authoritative.
- Use the project task naming convention and approved path mappings.
- Use one approved operational source for task states; do not create parallel status sources.

## Working rules

- Work through small, reviewable tasks.
- Read and modify only task-relevant, explicitly authorized files.
- Re-read current relevant files before continuing after a pause or developer edit.
- Preserve compatible manual or concurrent changes; never restore uncertain work automatically.
- Preserve working code and existing behavior.
- Reuse existing functions, validations, guards, utilities, and local patterns.
- Add or minimally adjust only what the approved task requires.
- Do not rewrite, merge, optimize, rename, or restructure working logic unless authorized by an explicit `REFACTOR` task.
- If no local pattern answers the task, follow official documentation compatible with the versions used by the project.
- Use established ecosystem practice only when official guidance is insufficient.
- Report and stop on conflicts involving official security, compatibility, or correctness requirements.
- Use only verified existing project capabilities; planned or documented capabilities are not available without repository evidence.
- Suggest or run only the smallest one to three relevant checks allowed by the task. In the default `DEVELOPER_RUN` mode, provide exact commands, wait for developer-reported results, and never execute, infer or invent results. Describe commands by effective scope; use `targeted` only when the existing script and runner semantics establish selectivity.
- Record scope-neutral clarifications. Stop for an approved Task Contract amendment when behavior, acceptance criteria, edit surface, dependency, interface, risk or an exclusion changes.
- Begin operational responses with outcome, completed action and next developer step. Add detail only for decisions, deviations, failures or ambiguity.

## Restrictions

- No implicit refactor, dependency, tooling, architecture, migration, or status change.
- Completed task history is preserved.
- Stop after the approved step for developer review.
