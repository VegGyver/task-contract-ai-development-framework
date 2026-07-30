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
2. Canonical role-to-path mapping
3. Architecture capability baseline
4. Observed repository standards
5. Existing task naming convention
6. Completed, in-progress and planned groups
7. Historical content to preserve
8. Minimal candidate file set
9. Missing, conflicting or unclear information
10. Bounded adoption steps
11. Decisions required

Do not ask the developer to choose where canonical path mappings live: use `docs/method/project-manifest.md`.
Treat missing `project-rules.md`, `capability-baseline.md`, and `task-naming.md` as standard adoption candidates, not optional structural inventions.

For every proposed file state:

- new file or additive update
- reason
- target-project evidence source

List target-project files inspected separately from instruction files loaded.
For every observed standard, include classification, representative evidence paths and scope/limits.
Do not generate files during inspect-only mode.
Keep successful sections concise. Add explanation only for missing, conflicting or unclear evidence and decisions.
