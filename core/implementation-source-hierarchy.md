# Implementation Source Hierarchy

The approved task contract and architecture define **what** to build. The following order defines **how** to implement it.

## Existing project

1. verified working behavior and the nearest relevant local pattern;
2. approved project rules and architecture decisions;
3. official documentation compatible with the versions in the repository when no local pattern answers the question;
4. established ecosystem practice when official guidance is insufficient;
5. a custom abstraction only when the task demonstrably requires it.

Preserve and integrate with working code. Do not use external guidance as permission for an unrequested refactor.

## Greenfield project

1. approved architecture and task contract;
2. official documentation compatible with the selected versions;
3. official examples and migration/security guidance;
4. established ecosystem practice when official guidance is insufficient;
5. a custom abstraction only when required by an approved constraint.

## Verification rule

Consult current official documentation when behavior is unfamiliar, version-sensitive, security-relevant, deprecated, or disputed. A web lookup is not mandatory for a routine step already supported by verified local evidence.

If a local convention conflicts with official security, compatibility or correctness requirements, report:

```txt
Local pattern:
Official requirement:
Affected scope:
Decision needed:
```

Do not silently preserve the conflict or silently rewrite the project.
