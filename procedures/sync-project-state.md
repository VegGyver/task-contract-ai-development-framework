# Procedure — Synchronize Project State

Use sync after manual developer edits, a new specification, an external change,
or any repository change that happened outside the current AI run and may
affect planned work or documented project state.

1. Bind the project and, when useful, provide the new evidence:

   ```txt
   tcaf sync --target <project-path> [--request <new-information> | --input <new-specification-or-material>]
   ```

2. Sync re-reads the current repository and canonical project evidence. It
   identifies material drift, affected planned tasks, and the smallest proposed
   reconciliation; it does not treat a request or input as automatically
   approved project truth.
3. Review the findings and the proposed canonical or backlog updates. The first
   pass is read-only and preserves developer changes, completed history, and
   unresolved conflicts.
4. Approve only a sufficiently identified, bounded update set when a change is
   appropriate. Without that current approval, sync does not write or overwrite
   developer work.
5. Send implementation work through planning or a Task Contract as appropriate;
   sync reconciles project state and planned work rather than implementing a
   feature.
