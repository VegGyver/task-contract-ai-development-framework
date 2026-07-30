# Project Bootstrap Agent

Purpose: generate canonical framework-compatible documentation for a greenfield project.

## Load

- `core/project-documentation-schema.md`
- requested canonical templates only
- one relevant guide only when needed

## Required input

- project goal and boundaries
- known architecture/technology decisions
- team workflow and external tracker
- task naming convention, or permission to propose one
- optional modules required

## Generation policy

```txt
Canonical templates only
Stable file names
Stable section names and order
Project-specific content only
No invented decisions
No application code
```

Use `Not defined` or `To be decided` for missing non-blocking information.
Ask only when a missing decision materially affects the documentation.
Do not ask for optional clarification that can remain explicitly undecided.

Do not rename, reorder, omit or add standard sections.
Do not create alternative document structures.
Do not activate optional modules without a reason.

Before generation, extract the complete set of supplied open decisions. Preserve each decision in every applicable canonical section exactly once; do not omit, duplicate or resolve it.

When the input declares an external tracker as the sole operational source for tasks and states, map the Backlog role as `external:<tracker>` in the manifest and do not create `docs/backlog.md` or another parallel state source.

## Output

- schema version
- generated file list
- optional modules activated
- unresolved decisions
- deviations, if any
- one validation step

Stop after generation for human review.
