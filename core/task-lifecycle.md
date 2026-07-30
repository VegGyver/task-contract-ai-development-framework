# Task Lifecycle

Operational states are separate from backlog status.

```txt
PROPOSED
APPROVED
IMPLEMENTED
VERIFICATION_PENDING
VERIFIED
ACCEPTED
COMMITTED
```

## Flow

```txt
bounded contract
→ approved
→ edit only approved scope
→ report diff and checks
→ developer verification
→ acceptance or correction
→ commit
→ new task for next step
```

## Gates

- **Entry:** contract is sufficiently bounded.
- **Edit:** an approved complete contract authorizes the current step.
- **Post-edit:** agent stops and reports changed files, summary and checks.
- **Verification:** checks are run by the declared check mode.
- **Acceptance:** developer confirms code, behavior, UI/console where relevant, and scope compliance.
- **Commit:** accepted work becomes a stable checkpoint.

No gate may depend on a specific tool button, resume flow or terminal permission.

Do not call work `complete` when it is only implemented. Report the exact state.

## Operational outcome labels

- `PASS` — contracted implementation and required checks passed; developer acceptance may still be pending.
- `READY FOR CHECK` — implementation is ready, but one or more declared developer or manual checks remain.
- `PARTIAL` — only part of the approved contract is satisfied.
- `BLOCKED` — a decision, dependency or corrected contract is required.
- `FAIL` — an executed required check failed.

Every operational response starts with `<OUTCOME> — <one-sentence result>`, then the next developer action. Details follow only when needed.

## Changes while active

Clarification → record and continue.

Contract correction → correct and re-check.

Scope or behavior change → stop for an amendment.

Independent request → create a separate task.

Repository contradiction → report evidence and wait.

Before resuming after any external edit or pause, re-read the current relevant files and preserve compatible work already present.
