# Output Schema — Project Bootstrap

- `READY FOR REVIEW — <one-sentence result>` or `BLOCKED — <one-sentence reason>`
- next developer action
- schema version
- role-to-path mappings
- generated files
- task source
- optional modules activated and reason
- proposals awaiting approval
- unresolved decisions
- approved deviations
- validation status and provenance

Validation status must be one of:

- `VALIDATION PENDING` — required under `DEVELOPER_RUN`, followed by the exact
  command `tcaf validate --target .`;
- `Validation: PASS` — only when `tcaf validate --target .` (or the equivalent
  runtime validator for the bound target) was executed and passed; or
- `Validation: FAILED` — only with the executed command and reported failures.

Do not use `Validation: PASS` for template inspection, heading inspection, or
an anticipated developer result.

When a source file was incompatible with a role, report it under approved
deviations only as source evidence preserved plus the generated canonical path;
do not report the source path as the role mapping. Include alternate mappings
only after the canonical document exists at the approved alternate path.

Omit empty explanatory detail. Do not omit unresolved decisions or required approvals.
