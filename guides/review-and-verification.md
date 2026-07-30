# Review and Verification

Human review is mandatory. Agent self-checks are evidence, not acceptance.

## Check modes

- `DEVELOPER_RUN` — agent provides exact commands, does not execute them, waits for developer-reported results, and never infers or invents results. Default.
- `AGENT_RUN` — agent runs explicitly approved non-destructive checks.
- `CI` — pipeline provides verification.
- `MANUAL` — developer follows UI/behavior checks.
- `MIXED` — combine only what is necessary.

Suggest the smallest relevant set, normally one to three checks.
List checks in executable order. Include only necessary prerequisites, before the checks that depend on them; prerequisites count toward the one-to-three-check limit.
Describe each command by its effective scope. Use `targeted` only when the existing script and runner semantics establish selectivity.

After editing, report:

```txt
<OUTCOME> — <one-sentence result>
Next action:
Changed files:
Summary:
Checks run or to run:
Manual verification:
Out of scope:
State: IMPLEMENTED / VERIFICATION_PENDING / VERIFIED
```

Keep a normal success response brief. Add evidence, alternatives or explanation only for a failed check, blocker, deviation, ambiguity or requested decision.

## Outcome labels

- `PASS` — the contracted result is present and every required check already run has passed. This does not imply developer acceptance or commit.
- `READY FOR CHECK` — implementation is present and a declared developer or manual verification remains.
- `PARTIAL` — the contract is not fully satisfied; identify completed and remaining work.
- `BLOCKED` — state the invalid assumption or required decision and do not broaden the task.
- `FAIL` — identify the failed required check and preserve the bounded state for review.

Never report `PASS` when a mandatory check is still pending.

The developer reviews:

- scope and changed files
- absence of hidden refactor/dependencies
- reuse of existing logic and validations
- code coherence
- compile/type/test results where supported
- UI behavior and console errors where relevant

Do not commit, push, discard, reset or clean without explicit approval.

A commit should contain one accepted logical change and reference the project task ID when useful.
