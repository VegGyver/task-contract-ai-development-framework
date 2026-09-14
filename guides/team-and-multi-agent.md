# Team and Multi-Agent Work

Use only for parallel developers/agents or separate frontend/backend ownership.

- Define ownership before work starts.
- A shared contract, schema, interface or API boundary becomes a dedicated
  approved task only when it is itself a coherent, independently reviewable
  and meaningfully verifiable outcome, or when establishing it materially
  unlocks independent implementation workstreams that otherwise cannot
  proceed safely. Do not create a dedicated boundary task merely when the
  required boundary already exists and is reusable, the change belongs in
  another coherent bounded task, separation is incomplete or meaningless, or
  the split merely mirrors ownership or manufactures parallelism.
- Frontend work must not modify backend-owned files; backend work must not modify frontend-owned files unless explicitly authorized.
- Each agent receives its own task contract and edit surface.
- Parallel completion does not equal integration completion.
- Integrate through a separate gate: compare contracts, resolve conflicts, run supported cross-layer checks, review the combined diff, then accept.
- Do not let one agent silently repair or rewrite another agent's accepted work.
