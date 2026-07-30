# Task Contract

The task contract defines permission. The execution profile defines order.

## Minimum contract

```txt
Task ID:
Type:
Goal:
Inspect:
Modify:
Allowed:
Forbidden:
Check mode:
Checks:
Stop:
```

Optional:

```txt
Profile:
Source of truth:
Expected behavior:
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
- When uncertain, stop and ask; do not guess.
