# Procedure — Adopt an Existing Project

1. Install the framework once outside project folders.
2. Bind the existing project as the only target:

   ```txt
   tcaf adopt --target <project-path>
   ```

3. The runner resolves the adoption agent, exact manifest and adapter automatically.
4. Follow the transport declared in the envelope. For Cline `manual-envelope`, start with one `INSPECT` task.
5. The agent inspects only the bound target and returns the canonical inspect-only report.
6. Verify the capability baseline, observed standards, evidence paths and instruction/target separation.
7. Approve the minimum candidate files and path mappings.
8. Generate one approved file per bounded task; with Cline, use a fresh `WRITE <path>` task for each file.
9. Review each diff and verify manually.
10. Run status reconciliation only as a separate task with complete evidence.
11. Do not modify application code during adoption.

The procedure never adds the framework as another workspace root and never copies runtime files into the target.
