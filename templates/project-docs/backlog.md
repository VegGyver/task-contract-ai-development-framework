# Backlog

Use the approved project task naming convention.

A generated backlog is a proposal until developer review. It may coexist with later direct requests; both use the same Task Contract flow.

For each item:

```txt
Task ID:
Title:
Goal:
Dependencies:
Acceptance criteria:
Status:
Implementation:
Review:
Verification:
Commit:
```

Use one canonical `Status` value: `Proposed`, `Approved`, `In progress`,
`Completed`, or `Blocked`. Keep lifecycle evidence in the separate fields;
do not infer it from `Status`. Record verification and commit only from actual
evidence, and record review approval only after explicit developer approval.

Completed records are historical. Add later changes as linked tasks; do not rewrite completed scope.

For each required check, `PASS` means the check was executed and succeeded;
`FAILED` means it was executed and failed; `NOT RUN`/`PENDING` means no result
exists. Aggregate `Verification: passed` requires every required check to be
`PASS`. A failed aggregate check is not made successful by passing diagnostics.
