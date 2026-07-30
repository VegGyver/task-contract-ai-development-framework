# Codex Adapter

Use the Universal Run Protocol through a globally installed Codex integration.

- Pass adapter ID `codex` to the runner.
- Bind the active project as the single target.
- Let the runner resolve the agent, manifest and modules.
- Keep the installed framework outside the project workspace.
- Use Codex access only for the target files and permissions declared by the task.
- Preserve the runner's review gate and exact output state.

The integration may expose native commands or a skill, but the public operations remain `bootstrap`, `adopt`, `task`, and `run`.
