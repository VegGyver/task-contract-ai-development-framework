# Procedure — Run a Development Task

1. Select one backlog item or bounded request.
2. Invoke the same runner against the project:

   ```txt
   tcaf task --target <project-path> --request <bounded request>
   ```

3. The runner discovers project rules, task naming and capability baseline through approved role mappings or canonical paths.
4. Review and approve the generated contract.
5. The adapter supplies compact rules and the approved contract to the coding tool.
6. The tool edits only the allowed surface and stops.
7. The developer reviews the diff, runs one to three checks and verifies UI/console when relevant.
8. Accept and commit, or issue a new bounded correction task.
9. Start the next step only with a new approved contract.
