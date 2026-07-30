# Team and Multi-Agent Work

Use only for parallel developers/agents or separate frontend/backend ownership.

- Define ownership before work starts.
- Shared contracts and API boundaries require a dedicated approved task.
- Frontend work must not modify backend-owned files; backend work must not modify frontend-owned files unless explicitly authorized.
- Each agent receives its own task contract and edit surface.
- Parallel completion does not equal integration completion.
- Integrate through a separate gate: compare contracts, resolve conflicts, run supported cross-layer checks, review the combined diff, then accept.
- Do not let one agent silently repair or rewrite another agent's accepted work.
