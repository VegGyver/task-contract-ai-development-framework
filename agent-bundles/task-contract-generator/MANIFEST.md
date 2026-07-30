# Task Contract Generator Bundle Manifest

Human-readable mirror of `manifest.json`. The JSON manifest is machine-authoritative.

## Required bundle files

- `AGENT.md`
- `START.md`
- `OUTPUT-SCHEMA.md`

## Required framework modules

- `../../core/task-contract.md`
- `../../core/task-types.md`

The runner automatically resolves project rules, task naming and capability baseline from the bound target. Standalone rules are the declared fallback when project rules are absent.

Optional selectors are exact in `manifest.json`. Maximum: one.
