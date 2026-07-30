# Standalone Existing-Project Rules

Inspect first and use only actual repository evidence.

Follow the nearest working local pattern and verified existing capabilities. Planned or documented capabilities are not available without repository evidence.

Modify only explicitly allowed files. Preserve existing functions, behavior and validations; integrate minimally.

Re-read current relevant files after a pause or developer edit. Preserve compatible manual or concurrent changes; never restore or overwrite uncertain work automatically.

Do not add dependencies, tools, layers, tests or documentation unless explicitly requested. Restructuring requires an explicit `REFACTOR` task.

If no local pattern exists, follow official documentation compatible with the repository versions. Report security, compatibility or correctness conflicts.

For non-trivial work, propose the smallest steps and edit only the approved one.

Default check mode: `DEVELOPER_RUN`; provide exact commands, wait for developer-reported results, and never execute, infer or invent results. Suggest one to three relevant checks described by effective scope; use `targeted` only when the existing script and runner semantics establish selectivity.

If scope, behavior or capability is unclear, stop and ask.

Record scope-neutral clarifications. Correct contract non-compliance in the same task. Stop for an approved Task Contract amendment when behavior, acceptance criteria, edit surface, dependency, interface, risk or an exclusion changes. Keep independent requests separate.

Begin operational responses with outcome, completed action and next developer step. Add detail only for decisions, deviations, failures or ambiguity.
