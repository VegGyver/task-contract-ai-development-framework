# Advanced Scenario Safeguards

Load only for the matching scenario.

## Production hotfix

Confirm minimal scope → apply minimal fix → run the critical available check → review diff → preserve rollback path → document afterward. No cleanup or refactor.

## Database or data migration

Separate schema change, migration, backfill and application adaptation. Define rollback and verification. Never hide a migration inside ordinary feature work.

## Security or authentication

State the threat/requirement, affected boundary and expected behavior. Preserve existing auth patterns. Do not broaden permissions or alter secrets/environment without explicit authorization.

## Performance

Record baseline evidence first. Change only the measured bottleneck. Re-measure using the same method. Do not combine optimization with unrelated refactor.

## Testing-only

Use existing test infrastructure only. Adding test tooling is a separate `CONFIG_TOOLING` task.

## Backlog reprioritization

Change future order/scope only. Preserve completed task history and identifiers.
