# Procedure — Run a Development Task

1. Select one executable task from a backlog, external issue, initial analysis, direct request or approved amendment.
2. Invoke the same runner against the project:

   ```txt
   tcaf task --target <project-path> --request <bounded request>
   ```

3. The runner discovers project rules, task naming and capability baseline through approved role mappings or canonical paths.
4. The agent inspects only pertinent context and returns the shortest safe Task Contract.
5. Review goal, expected behavior, edit surface, exclusions, acceptance criteria and checks; approve explicitly.
6. The adapter supplies compact rules and the approved contract to the coding tool.
7. The tool re-reads current relevant files, preserves existing and developer changes, edits only the allowed surface and stops.
8. During implementation:
   - record a scope-neutral clarification and continue;
   - correct contract non-compliance in the same task;
   - report a necessary local adaptation;
   - stop for approval before any contract amendment;
   - separate an independent request;
   - report repository contradictions or unrelated findings without silently fixing them.
9. The tool reports outcome first, changed files, checks and the next developer action.
10. The developer reviews the diff, runs the smallest one to three relevant checks and verifies UI/console when needed.
11. Accept and commit, request a bounded correction, approve an amendment or create a separate task.
12. Reconcile backlog, issue or documentation status only when separately authorized.
