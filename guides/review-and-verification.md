# Review and Verification

Human review is mandatory. Agent self-checks are evidence, not acceptance.

## Check modes

- `DEVELOPER_RUN` — agent lists concise commands; developer runs them. Default.
- `AGENT_RUN` — agent runs explicitly approved non-destructive checks.
- `CI` — pipeline provides verification.
- `MANUAL` — developer follows UI/behavior checks.
- `MIXED` — combine only what is necessary.

Suggest the smallest relevant set, normally one to three checks.

After editing, report:

```txt
Changed files:
Summary:
Checks run or to run:
Manual verification:
Out of scope:
State: IMPLEMENTED / VERIFICATION_PENDING / VERIFIED
```

The developer reviews:

- scope and changed files
- absence of hidden refactor/dependencies
- reuse of existing logic and validations
- code coherence
- compile/type/test results where supported
- UI behavior and console errors where relevant

Do not commit, push, discard, reset or clean without explicit approval.

A commit should contain one accepted logical change and reference the project task ID when useful.
