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
6. Compare explicit candidate files with the machine schema for their proposed
   canonical role. Treat all other documentation as source evidence.
7. Report capabilities, observed standards, naming, gaps and conflicts.
8. Propose the smallest necessary file set.
9. Wait for approval.
10. Create only approved files from canonical templates.

## Existing-project rules

- Canonical document roles are required; canonical filenames are preferred, not mandatory.
- Existing documentation is source evidence by default. A file may be reused
  as a canonical role only when it was explicitly selected for that role, it
  satisfies the complete role schema, and reuse does not create a conflicting
  project-state source.
- When a source document is not schema-compatible, preserve it byte-for-byte,
  derive only supported facts from it, and generate the canonical role from
  the official template. Keep missing or unclear information explicit; never
  invent decisions, capabilities, conventions or status.
- Inspect implementation evidence separately from documentation, including
  package/config files, representative source paths, CI/tooling/config paths,
  task/backlog evidence and repository-local rules. Planned or documented
  functionality is not an implemented capability.
- Record approved path mappings in `docs/method/project-manifest.md` instead of creating unnecessary aliases.
- If a non-canonical file occupies a canonical default path, preserve it and
  use an approved alternate path for the generated canonical document. Record
  only that canonical role-to-path mapping using the parser-supported
  manifest syntax; a manifest must not map arbitrary source evidence to a role.
- Do not create parallel sources for backlog status or project state.
- Completed task title, description, scope, acceptance criteria, original dependencies and implementation notes are immutable.
- Task status is operational data and may be changed only by a separate approved `DOCS_STATUS_UPDATE` task after evidence is verified.
- Use `Not available` only when authoritative docs exclude a capability or its relevant expected paths were directly inspected and support is absent.
- If path visibility, hidden files, workspace scope or evidence is incomplete, use `Unclear`.
- Use existing tracker/task naming.
- `docs/method/project-rules.md` is the tool-agnostic canonical rules source; tool files such as `.clinerules` are compact adapters.
- The standard adoption candidate set is the minimum missing or
  non-conformant canonical role set required for a valid adopted project:
  `project-brief.md`, `architecture-overview.md`, `backlog.md`,
  `project-rules.md`, `ai-workflow.md`, `capability-baseline.md`, and
  `task-naming.md`. Include `project-manifest.md` only when a genuine approved
  path deviation exists. Do not propose roles already satisfied by
  schema-compatible canonical documents.
- Do not invent templates or extra documentation “for completeness”.
- Generate canonical project documents only from the official templates exposed
  in the adoption Run Envelope instruction surface.
- Generated project rules must explicitly preserve working code, reuse existing functions/validations/patterns, forbid implicit restructuring, and keep developer verification mandatory.
- Planned or documented functionality is not an available capability.
- Extract local standards only from target evidence. Distinguish `Established`, `Localized`, `Conflicting`, and `Unclear`.
- Treat one isolated or explicitly legacy exception as `Localized`; use `Conflicting` only when multiple active patterns materially disagree.
- Record representative evidence paths; do not scan every occurrence or infer project-wide rules from one file.
- Preserve conflicting patterns as findings. Standardization requires a separate approved task.
- Keep task ID/title separate from framework task type; do not invent follow-up naming conventions.

Validation reporting is evidence-based. Report `Validation: FAILED` when
`tcaf validate --target .` was executed and failed, including its issues. Do
not claim `Validation: PASS` unless that command was actually executed and
passed. Under `DEVELOPER_RUN`, report exactly `VALIDATION PENDING` and the
command `tcaf validate --target .`.

Stop before any project file change in inspect-only mode. After approval,
create only the approved normalized canonical documents.
