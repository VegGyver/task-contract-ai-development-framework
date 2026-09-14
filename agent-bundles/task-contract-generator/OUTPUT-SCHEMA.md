# Output Schema — Task Contract Generator

## Ready

```txt
READY — Task Contract generated.
Next action:

## Developer task view

Task ID:
Title:
Type:
Origin: <actual task origin>
Source of truth: <actual project-state source>
Supporting evidence: <only when actually available and used>
Goal:
Expected behavior:
Concrete changes:
Implementation surface:
Relevant components:
Data models / schemas / DTOs / configuration:
Dependencies / libraries:
Test expectations:
Acceptance criteria:
Expected developer verification:
Open decisions:

## AI execution constraints

Inspect:
Modify:
Allowed:
Forbidden:
Scope boundaries:
Stop conditions:
Check mode:
Checks:
Stop:
```

Provenance values are conditional: use canonical values only when the
corresponding canonical evidence was used; otherwise name the actual fallback.
Include Supporting evidence only when it was available and used.

Required-check failures must retain the failed check and observed error,
separate confirmed from probable cause, state proposed remediation and its
impact surface, classify approval/amendment needs, rerun affected checks after
approval, and report the final result. Do not claim aggregate `PASS` while a
required check remains failed. For every required check, use `PASS` only for
an executed successful check, `FAILED` for an executed failed check, and
`NOT RUN`/`PENDING` when it was not executed. If an aggregate check fails,
retain that failure even when lower-level diagnostics pass. Every command
listed under `Checks` is a required check, including a prerequisite, and must
report exactly one evidence state. Under `DEVELOPER_RUN`, render each
not-yet-executed check as `NOT RUN` or `PENDING`.

Use stable task `Status` values (`Proposed`, `Approved`, `In progress`,
`Completed`, `Blocked`) and separate `Implementation`, `Review`,
`Verification`, and `Commit` lifecycle evidence. Do not infer lifecycle events
from `Status`. When canonical task state exists, preserve the authoritative
meaning of each lifecycle field. Do not translate absent, unknown, unclear,
`not recorded`, or equivalent evidence into a stronger negative assertion such
as `not started`, `not requested`, `not run`, `not completed`, or `not
approved`. Optional lifecycle fields with no useful information may be
omitted.

Each `Modify` path or path group must correspond to a specific concrete change
supported by project/task evidence. Omit speculative or precautionary modify
paths; `Inspect` may be broader. A later required path outside `Modify`
requires the normal amendment/approval process.

An open decision may remain in a READY executable contract only when execution
is fully bounded and identical regardless of that decision. If an unresolved
decision determines `Concrete changes`, `Modify`, expected behavior,
acceptance criteria, or required checks, use the existing BLOCKED output and
state the needed decision until it is resolved. Do not express alternative or
conditional paths in `Modify` or emit a check that assumes one unresolved
choice.

Optional fields may be omitted when they add no useful information.

## Active-task change

Return one of:

- `CLARIFICATION — <result>`
- `CORRECTION — <result>`
- `LOCAL ADAPTATION — <result>`
- `AMENDMENT REQUIRED — <result>`
- `SEPARATE TASK — <result>`
- `BLOCKED — <result>`

For `AMENDMENT REQUIRED`, include:

```txt
Next action:
Task Contract — Amendment <n>
Requested change:
Contract fields changed:
Contract fields unchanged:
Work already completed:
Checks added or repeated:
State: WAITING FOR APPROVAL
```

## Blocked

```txt
BLOCKED — Task Contract cannot be generated safely.
Blocked:
- ...
Needed decision:
- ...
No task contract generated.
```

## Decomposition required

```txt
DECOMPOSITION REQUIRED — The request is too broad for one safe Task Contract.
Proposed steps:
1. ...
2. ...
Recommended first step:
- ...
Stop before generating an executable contract.
```
