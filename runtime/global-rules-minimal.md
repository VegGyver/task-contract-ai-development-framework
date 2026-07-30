# Global AI Rules

Use repository files as source of truth.

Modify only explicitly allowed files and change types.

Inspect only relevant context.

Preserve working code and reuse existing logic, validations and patterns.

Do not refactor, add dependencies, change architecture or expand scope unless authorized; restructuring requires an explicit `REFACTOR` task.

Use verified existing project capabilities only; planned or documented capabilities are not available without repository evidence.

When no local pattern exists, follow official documentation compatible with the selected version. Report security, compatibility or correctness conflicts.

If unclear, stop and ask.

After editing, report changed files and the smallest one to three relevant checks for developer review. Default to `DEVELOPER_RUN`.
