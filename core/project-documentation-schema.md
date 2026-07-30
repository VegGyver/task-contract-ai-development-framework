# Project Documentation Schema

This schema defines canonical document roles and templates for framework-managed projects.

Machine schema version: `0.3.0` in `registry/project-schema.json`.

## Standardization rule

Use canonical templates. Keep section names, order and required fields stable. Only project-specific content changes.

## Canonical roles and default paths

```txt
docs/
  project-brief.md
  architecture-overview.md
  backlog.md
  method/
    project-rules.md
    ai-workflow.md
    capability-baseline.md
    task-naming.md
    project-manifest.md
```

For greenfield projects, use these paths unless the team explicitly chooses another convention or an approved external system is the sole operational source for a role.

The Backlog role declares the operational source of tasks; it does not require a complete repository backlog. It may map to an approved external tracker or `external:Developer requests` when tasks are supplied directly. Do not create `docs/backlog.md` beside an external mapping.

For existing projects, canonical roles are required but existing paths may be mapped and preserved. Do not create alias or pointer files only to match a canonical filename.

Store approved role-to-path mappings in `docs/method/project-manifest.md`. Create this manifest when any canonical path deviation exists.

Map an approved external role as `external:<source>`, for example `external:GitHub Issues`. When a role is external, do not create its default repository file or another parallel source. Only roles marked `allow_external_source` in the machine schema may use this mapping.

## Optional modules

Create only when required:

```txt
docs/
  changes/
  fixes/
  technical-debt/
  decisions/
  method/
    team-ownership.md
    integration-workflow.md
```

Do not create a parallel status source when an existing repository backlog or external tracker already owns operational task states.

## Template fidelity

- preserve canonical title, sections, order and required fields
- do not add explanatory sections
- do not remove empty required sections
- use `Not defined` or `To be decided` for missing non-blocking information
- do not invent project decisions
- preserve every supplied open decision in each applicable canonical section exactly once
- use an explicit `None` marker when no open decisions exist

## State and decision discipline

Bootstrap documentation must keep these categories visibly distinct:

- verified current state;
- desired or planned state;
- confirmed project decisions;
- agent proposals awaiting approval;
- open decisions.

Planned functionality is not an available capability. Agent proposals never become project decisions until approved. A generated backlog is a planning proposal until developer review.

## Existing-project adoption

- map existing files to canonical roles
- preserve approved path deviations in `docs/method/project-manifest.md`
- create missing standalone core method documents: `project-rules.md`, `capability-baseline.md`, and `task-naming.md`
- do not overwrite files automatically
- propose the minimum missing file set
- use additive updates only when explicitly approved
- preserve completed task history
- project rules must include preservation-first behavior and developer verification
- capability baselines must not classify planned functionality as available and must record representative observed local standards
- task naming docs must separate task identifiers from framework task types and must not invent linked-task conventions

## Generation result

```txt
Schema version:
Role-to-path mappings:
Files generated:
Optional modules activated:
Missing decisions:
Approved deviations:
```
