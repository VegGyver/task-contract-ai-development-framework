# Existing Project Adoption Bundle Manifest

Human-readable mirror of `manifest.json`. The JSON manifest is machine-authoritative.

## Required bundle files

- `AGENT.md`
- `START.md`
- `OUTPUT-SCHEMA.md`

## Required framework modules

- `../../runtime/standalone-rules-compact.md`
- `../../core/project-documentation-schema.md`
- `../../guides/architecture-capability-baseline.md`
- `../../guides/change-management-and-history.md`

Canonical project-document templates are required modules in `manifest.json`,
so every role the adoption agent may generate is available in the Run Envelope.
Optional selectors remain limited to at most one current contextual guide.
