# Procedure — Start a New Project

1. Install the framework once outside project folders.
2. Bind one existing or planned target and provide the available input:

   ```txt
   tcaf bootstrap --target <project-path> [--request <idea-or-first-task> | --input <analysis-or-roadmap>]
   ```

   Input may be a complete analysis, a product idea, an initialized target, a first task or a partial roadmap.

3. The runner resolves the bootstrap agent, complete manifest, target and adapter.
4. The agent separates current state, desired state, confirmed decisions, proposals and open decisions.
5. Choose the task source:
   - generate a proposed backlog when the analysis supports it;
   - map an external tracker; or
   - map `external:Developer requests` and start without a repository backlog.
6. Follow the transport declared in the envelope. For Cline `manual-envelope`, use a fresh `WRITE <path>` task for each document.
7. The agent generates documentation only and stops after each approved write.
8. Review scope, decision classifications, planned-versus-available capabilities, task source, unresolved decisions and deviations.
9. Run one final `VALIDATE` step, then commit accepted documentation before implementation begins.
10. Select the first task from the backlog, analysis, external issue or a direct request and continue through the standard Task Contract flow.

The target does not need to exist or use Git. Bootstrap does not write application code unless a later approved task explicitly does so. No framework runtime files are copied into the target.
