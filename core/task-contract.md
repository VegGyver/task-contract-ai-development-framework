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
Origin:
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
