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
