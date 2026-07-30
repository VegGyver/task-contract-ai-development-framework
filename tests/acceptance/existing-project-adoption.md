# Acceptance Test — Existing Project Adoption

## Input scenario

Existing partially implemented project with:

- established non-canonical backlog/workflow filenames
- completed and planned tasks
- operational task status fields
- incomplete evidence for some capabilities
- compact tool-specific rules
- framework installed outside the target

## Required behavior

The agent must:

- use the single target bound by the runner
- load only manifest-listed framework files
- keep instruction and target inspection surfaces separate
- never use framework files as project evidence
- map canonical roles to existing paths
- avoid alias/pointer files without operational need
- preserve completed task content
- allow future status-only reconciliation
- inspect relevant expected paths before `Not available`
- confirm paths through read-only listing or search before direct reads
- include relevant dot-prefixed CI and tool-rule config in the inspection
- use `Unclear` when visibility or evidence is incomplete
- avoid parallel status sources
- propose the minimum candidate file set
- define canonical project rules as tool-agnostic and tool rules as adapters
- extract representative local standards with evidence and classification
- make no changes in inspect-only mode

## Failure conditions

- browses unrelated framework files
- includes framework files in project inventory or evidence
- classifies an uninspected or hidden-path capability as unavailable
- freezes operational statuses permanently
- proposes duplicate backlog/workflow pointer files by default
- proposes a separate status document by default
- rewrites historical task content
- modifies application files
- requires a second workspace root, manual framework file selection or a corrective prompt
- reports a one-off source pattern as a project-wide convention
- reads absent or unconfirmed paths directly, or retries a failed read
- omits relevant dot-prefixed project config from the inspection


## Deterministic documentation decisions

Pass only if the agent:

- uses `docs/method/project-manifest.md` for approved role-to-path deviations
- proposes missing `project-rules.md`, `capability-baseline.md`, and `task-naming.md` as the standard core adoption set
- does not ask where mappings should live
- classifies an isolated or explicitly legacy exception as `Localized`, not `Conflicting`
