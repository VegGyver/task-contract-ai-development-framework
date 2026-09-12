# Task Contract

## Developer task view

```txt
Task ID:
Title:
Type:
Origin:
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
```

## AI execution constraints

```txt
Inspect:
Modify:
Allowed:
Forbidden:
Check mode: DEVELOPER_RUN
Checks:
Scope boundaries:
Stop conditions:
Stop:
```

Required-check evidence must use `PASS` only for an executed successful check,
`FAILED` for an executed failed check, and `NOT RUN` or `PENDING` otherwise.
Aggregate verification is `passed` only when every required check is `PASS`.
