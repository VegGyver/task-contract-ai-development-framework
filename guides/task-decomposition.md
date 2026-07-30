# Task Decomposition

A step is the smallest useful complete change, not the smallest number of lines.

A valid step has:

- one primary goal
- one reason to change
- one bounded edit surface
- one verification method
- one stop condition
- a valid project state afterward

## Context rules

- **New code:** build one complete logical block.
- **Existing code:** integrate minimally and preserve working logic.
- **Bug fix:** change only the demonstrated cause.
- **Refactor:** restructure only under an explicit `REFACTOR` task.

Split when a step mixes unrelated layers, behavior and refactor, feature and tooling, or code and history updates.

Do not split into empty files, isolated imports or incomplete fragments.

Execution order comes from `guides/execution-profiles.md`; this guide decides size, not order.

## Proposal format

```txt
Proposed steps:
1. <one-sentence result>
   Modify: ...
   Check: ...
   Stop: ...

No files changed.
```

The agent may propose several steps but executes only the approved current step.
