# Procedure — Run a Development Task

1. Select one executable task from a backlog, external issue, initial analysis, direct request or approved amendment.
2. Invoke the same runner against the project:

   ```txt
   tcaf task --target <project-path> --request <bounded request>
   ```

3. The runner discovers project rules, task naming and capability baseline through approved role mappings or canonical paths.
4. The agent inspects only pertinent context and returns the shortest safe Task Contract. A Task Contract is the explicit authorization boundary for one piece of work: it records the goal and expected outcome, concrete change surface, relevant files or components, allowed and forbidden change types, checks, stop conditions, and any relevant open decisions.
5. Review the contract and approve explicitly. If implementation later needs to change behavior, expand the approved surface, add a dependency, or otherwise exceed the boundary, the tool stops for a visible amendment or a new decision.
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
