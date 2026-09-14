# Output Schema — Project Sync

Return this concise developer review; omit unchanged state unless preservation needs to be explicit.

```txt
READY / BLOCKED — Project sync result. State: WAITING FOR APPROVAL / BLOCKED / APPLIED.

## Review gate and target
Target:
Evidence inspected:
Current approval boundary:

## Findings
Canonical versus observed state:
Material drift:
Affected planned tasks:
Preserved active or historical material:
Conflicts / uncertainty:

## Proposed bounded updates
- Canonical file and field — exact minimal change — reason

## Apply result
Only when current-envelope approval is explicit:
Changed files/fields:
Findings resolved by approved updates:
Still affected/unresolved outside approval (preserved, not changed):
Untouched developer and historical material:

## Decisions and next action
Required decision:
Exact approval or correction needed:

## Validation evidence
Validation: PENDING / NOT RUN / FAILED / PASS — include actual result or the exact bound-target command `tcaf validate --target <target>`. Never claim PASS without execution evidence.
```
