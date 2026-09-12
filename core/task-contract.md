# Task Contract

The task contract defines permission. The execution profile defines order.

## Developer task view

The contract first explains the task to the developer in concise operational
terms. Include only evidence-supported fields when applicable:

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

These fields authorize and constrain execution separately from the developer
description:

```txt
Inspect:
Modify:
Allowed:
Forbidden:
Check mode:
Checks:
Scope boundaries:
Stop conditions:
Stop:
```

Optional:

```txt
Profile:
Source of truth:
Origin:
Supporting evidence:
Expected behavior:
Acceptance criteria:
Open decisions:
```

## Rules

- `Modify` is the complete edit surface.
- `Allowed` is the complete set of permitted change types.
- `Forbidden` may narrow global or project permissions.
- `Check mode` is one of `DEVELOPER_RUN`, `AGENT_RUN`, `CI`, `MANUAL`, `MIXED`.
- Default check mode: `DEVELOPER_RUN`.
- In `DEVELOPER_RUN`, provide exact commands, do not execute them, wait for developer-reported results, and never infer or invent results.
- Describe each command by its effective scope. Use `targeted` only when the existing script and runner semantics establish selectivity.
- A complete task contract approved by the developer authorizes that step.
- A separate pre-edit approval is needed only when the task is ambiguous, complex or first requires decomposition.
- Approval never authorizes later steps.
- A clarification that leaves goal, behavior, acceptance criteria, edit surface and risk unchanged may be recorded without replacing the contract.
- A correction needed to satisfy the approved contract remains in the same task.
- A local technical adaptation may proceed only when it stays inside `Modify` and `Allowed`, introduces no new behavior or dependency, and is reported.
- Any change to behavior, acceptance criteria, edit surface, public interface, dependency, risk or an explicit exclusion requires a visible Task Contract amendment and developer approval before implementation.
- An independent or non-essential request becomes a separate task.
- If current repository evidence contradicts the contract, stop and report the invalid assumption.
- When uncertain, stop and ask; do not guess.

## Amendment

```txt
Task Contract — Amendment <n>
Requested change:
Contract fields changed:
Contract fields unchanged:
Work already completed:
Checks added or repeated:
State: WAITING FOR APPROVAL
```

Do not regenerate unaffected contract content. Replace the contract or create a new task when the primary goal changes.

## Failed-check remediation

When a required check fails, keep the failure visible and report the observed
error. Distinguish confirmed from probable cause, then propose a concrete
remediation only when evidence supports one. Identify the files,
configuration or dependencies it would change and classify it as either an
in-scope mechanical correction or a change requiring explicit developer
approval/contract amendment. Never expand scope silently. After an approved
remediation, rerun the failed check and any checks whose validity may have
been affected, then report the final result. If the cause is uncertain,
request developer input rather than inventing a fix. A failed required
aggregate check remains a failure until resolved.

## Canonical task status and lifecycle evidence

Use one stable task `Status` value: `Proposed`, `Approved`, `In progress`,
`Completed`, or `Blocked`. `Completed` is a value, not a generated sentence.
Keep lifecycle evidence separate:

```txt
Implementation: not started | in progress | completed
Review: not requested | approved
Verification: not run | pending | passed | failed
Commit: committed | not recorded
```

Do not infer review approval, executed verification, or a commit from `Status`.
Record `Commit: committed` and `Verification: passed` only with actual
evidence, and record `Review: approved` only after explicit developer approval.
