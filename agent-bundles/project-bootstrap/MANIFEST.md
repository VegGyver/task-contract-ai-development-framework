# Project Bootstrap Bundle Manifest

Human-readable mirror of `manifest.json`. The JSON manifest is machine-authoritative.

## Required bundle files

- `AGENT.md`
- `START.md`
- `OUTPUT-SCHEMA.md`

## Required framework modules

- `../../core/validation-evidence.md`
- `../../core/project-documentation-schema.md`
- every canonical project-document template declared explicitly in `manifest.json`
- `../../templates/project-docs/schema-validation-checklist.md`

Optional selectors: `execution-profile`, `team`, `advanced-scenario`. Maximum: one.

Bootstrap source documents are evidence, not canonical role documents, unless
the runtime project schema confirms compatibility. Incompatible sources must
remain unchanged while canonical documents are generated from the declared
templates; any approved alternate canonical paths are recorded in the project
manifest.
