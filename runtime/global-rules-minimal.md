# Global AI Rules

Use repository files as source of truth.

Modify only explicitly allowed files and change types.

Inspect only relevant context.

Preserve working code and reuse existing logic, validations and patterns.

Re-read current relevant files after a pause or developer edit. Preserve compatible manual or concurrent changes; never restore, discard or overwrite uncertain work automatically.

Do not refactor, add dependencies, change architecture or expand scope unless authorized; restructuring requires an explicit `REFACTOR` task.

Use verified existing project capabilities only; planned or documented capabilities are not available without repository evidence.

When no local pattern exists, follow official documentation compatible with the selected version. Report security, compatibility or correctness conflicts.

If unclear, stop and ask.

Record scope-neutral clarifications. Correct contract non-compliance in the same task. If behavior, acceptance criteria, edit surface, dependency, interface, risk or an exclusion changes, stop for an approved Task Contract amendment. Keep independent requests separate.

After editing, report changed files and the smallest one to three relevant checks for developer review. In the default `DEVELOPER_RUN` mode, provide exact commands, wait for developer-reported results, and never execute, infer or invent results. Describe commands by effective scope; use `targeted` only when the existing script and runner semantics establish selectivity.

Begin each operational response with the outcome, completed action and next developer step. Add detail only for decisions, deviations, failures or ambiguity.
