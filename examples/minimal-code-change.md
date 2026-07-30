# Minimal Existing-Code Change

```txt
Task ID: APP-FE-014-EXT-001
Type: CODE_CHANGE
Goal: support a premium price type
Inspect: price.service.ts, price.service.test.ts
Modify: price.service.ts, price.service.test.ts
Allowed: add premium behavior using the current branch and test pattern
Forbidden: rewrite pricing logic, add abstractions, add dependencies
Check mode: DEVELOPER_RUN
Checks: targeted price service test; typecheck
Stop: after edit and check instructions
```

Expected behavior: preserve standard and discounted paths; add only the premium case and its targeted test.
