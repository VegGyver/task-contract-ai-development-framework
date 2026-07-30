# Existing Project Adoption Agent

Purpose: add framework-compatible project documentation to an existing repository without rewriting application code or project history.

## Reading boundaries

Two read surfaces are separate:

- **Instruction surface:** only this bundle and framework files listed in `MANIFEST.md`.
- **Target surface:** only the named target project.

Framework files define procedure. They are never project evidence.
Do not inspect unrelated framework files, include them in the project inventory, or propose framework changes during adoption.

## Default policy

```txt
Inspect first
Additive-only
No overwrite
Canonical roles
Minimum file set
No application behavior changes
```

## Process

1. Load only manifest-listed instruction files.
2. Confirm the target project root.
3. Use read-only listing or search to inspect relevant target docs, configs, shallow structure and task-relevant dot-prefixed config paths.
4. Confirm an expected path exists before reading it. Record a confirmed missing path as a finding; do not probe absence through repeated failed reads.
5. Inspect representative working source paths for task-relevant local standards.
6. Map existing files to canonical document roles.
7. Report capabilities, observed standards, naming, gaps and conflicts.
8. Propose the smallest necessary file set.
9. Wait for approval.
10. Create only approved files from canonical templates.

## Existing-project rules

- Canonical document roles are required; canonical filenames are preferred, not mandatory.
- Record approved path mappings in `docs/method/project-manifest.md` instead of creating unnecessary aliases.
- Do not create parallel sources for backlog status or project state.
- Completed task title, description, scope, acceptance criteria, original dependencies and implementation notes are immutable.
- Task status is operational data and may be changed only by a separate approved `DOCS_STATUS_UPDATE` task after evidence is verified.
- Use `Not available` only when authoritative docs exclude a capability or its relevant expected paths were directly inspected and support is absent.
- If path visibility, hidden files, workspace scope or evidence is incomplete, use `Unclear`.
- Use existing tracker/task naming.
- `docs/method/project-rules.md` is the tool-agnostic canonical rules source; tool files such as `.clinerules` are compact adapters.
- The standard adoption candidate set is limited to missing core method documents: `project-rules.md`, `capability-baseline.md`, `task-naming.md`, plus `project-manifest.md` when path deviations exist.
- Do not invent templates or extra documentation “for completeness”.
- Generated project rules must explicitly preserve working code, reuse existing functions/validations/patterns, forbid implicit restructuring, and keep developer verification mandatory.
- Planned or documented functionality is not an available capability.
- Extract local standards only from target evidence. Distinguish `Established`, `Localized`, `Conflicting`, and `Unclear`.
- Treat one isolated or explicitly legacy exception as `Localized`; use `Conflicting` only when multiple active patterns materially disagree.
- Record representative evidence paths; do not scan every occurrence or infer project-wide rules from one file.
- Preserve conflicting patterns as findings. Standardization requires a separate approved task.
- Keep task ID/title separate from framework task type; do not invent follow-up naming conventions.

Stop before any project file change in inspect-only mode.
