# Output Schema — Existing Project Adoption

Begin with:

```txt
READY FOR REVIEW — Inspection completed without project changes.
Next action: review the findings and approve or correct the candidate file set.
```

Use `BLOCKED — <reason>` instead when safe inspection cannot continue.

0. Scope confirmation
   - target project root
   - instruction files loaded
   - confirm framework files were not used as project evidence
1. Documentation inventory
2. Canonical role-to-path mapping (schema compatibility and source evidence)
3. Architecture capability baseline
4. Observed repository standards
5. Existing task naming convention
6. Completed, in-progress and planned groups
7. Historical content to preserve
8. Minimal candidate file set: missing or non-conformant canonical roles only
9. Missing, conflicting or unclear information
10. Bounded adoption steps
11. Decisions required

Do not ask the developer to choose where canonical path mappings live: use `docs/method/project-manifest.md`.
The candidate set is the minimum missing or non-conformant canonical role set
required for valid adoption. It may include `project-brief.md`,
`architecture-overview.md`, `backlog.md`, `project-rules.md`,
`ai-workflow.md`, `capability-baseline.md`, and `task-naming.md`.
Include `project-manifest.md` only for a genuine approved path deviation. Do
not propose roles already satisfied by schema-compatible canonical documents.

For every proposed file state:

- new file or additive update
- reason
- target-project evidence source

Do not map an arbitrary or schema-incompatible source document directly to a
canonical role. Report it as preserved evidence and propose the generated
canonical template path instead. Include an alternate mapping only when the
canonical document exists there and the deviation has been approved.

List target-project files inspected separately from instruction files loaded.
For every observed standard, include classification, representative evidence paths and scope/limits.
Do not generate files during inspect-only mode.
Keep successful sections concise. Add explanation only for missing, conflicting or unclear evidence and decisions.

Validation status must be evidence-based: under `DEVELOPER_RUN`, use
`VALIDATION PENDING` followed by `tcaf validate --target .`. Use
`Validation: PASS` only when that command was actually executed and passed.
