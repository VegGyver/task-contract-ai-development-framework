# Procedure — Start a New Project

1. Install the framework once outside project folders.
2. Bind one existing or planned target:

   ```txt
   tcaf bootstrap --target <project-path> --input <project-analysis>
   ```

3. The runner resolves the bootstrap agent, complete manifest, target and adapter.
4. Follow the transport declared in the envelope. For Cline `manual-envelope`, use a fresh `WRITE <path>` task for each document.
5. The agent generates documentation only and stops after each approved write.
6. Review generated documentation, unresolved decisions and deviations.
7. Run one final `VALIDATE` step, then commit accepted documentation before implementation begins.

The target does not need to exist and does not need a Git repository. No framework runtime files are copied into it.
