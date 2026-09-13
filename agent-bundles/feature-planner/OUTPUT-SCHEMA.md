# Output Schema — Feature Planner

Return this concise developer review:

```txt
READY — Feature plan prepared. State: WAITING FOR APPROVAL.

## Feature
Feature ID:
Title:
Goal / outcome:
Expected behavior:

## Current project state
Canonical source of truth:
Relevant completed work:
Relevant unresolved work:
State inconsistencies:

## Existing capabilities reused
- capability — evidence

## External prerequisites
- Task ID — title — classification — state — reason

## Feature-member tasks
- Task ID — title — purpose — state — dependencies — contribution — test expectations
  Feature: <feature ID>

## Related / overlapping work
- Task ID — reason

## Missing work
Only genuinely necessary, materially distinct work. Explain why it cannot fit
an existing task. Proposed IDs are provisional until approval.

## Execution shape
Organizational profile:
Dependency graph:
Parallel-ready work:
Recommended execution schedule:
Ownership / convergence:

## Next executable work
Exact Task ID(s):
Reason / blockers:

## Feature specification after approval
docs/features/<feature-id>.md (or configured project location)

## Open decisions
Only real decisions.

## AI execution constraints
Inspect: target evidence and canonical project state.
Modify: nothing before approval.
Forbidden: application code, backlog, statuses, Task Contracts, permanent IDs.
Stop: at developer review and approval gate.

## Validation evidence
Validation: PENDING / NOT RUN / FAILED / PASS — include exact command and
authoritative result. Do not claim PASS without execution evidence. For
PENDING or NOT RUN, `<target>` in `tcaf validate --target <target>` must be the
bound TCAF Run Envelope Target `locator`, never the envelope path,
input-resource path, another inspected file, or the current working directory
unless that exact path is the bound target.
```

After explicit approval, a later approved workflow may persist the concise
feature specification and planning relationships. This output itself is not a
Task Contract and must not claim that persistence occurred.
