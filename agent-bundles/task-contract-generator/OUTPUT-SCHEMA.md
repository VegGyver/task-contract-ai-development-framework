# Output Schema — Task Contract Generator

## Ready

```txt
READY — Task Contract generated.
Next action:

Task ID:
Type:
Origin:
Goal:
Expected behavior:
Inspect:
Modify:
Allowed:
Forbidden:
Acceptance criteria:
Check mode:
Checks:
Open decisions:
Stop:
```

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
