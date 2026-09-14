# Planning Rules — Minimal

Apply these rules whenever TCAF creates, evaluates, decomposes or sequences units of work.

- A step is the smallest useful complete change: one primary goal, one reason to change, a bounded surface, a verification method, a stop condition and a valid project state afterward.
- Derive task boundaries from the architecture and responsibilities actually present. Do not introduce or force frontend, backend, shared or other layers merely to satisfy a generic profile.
- Split work that mixes unrelated layers, behavior and refactor, feature and tooling, or code and history. Do not split work into incomplete or meaningless fragments.
- Dependencies represent real prerequisites only. Task IDs, backlog order, roadmap order, phase order and preferred execution order do not create dependencies.
- Reuse existing tasks and capabilities where valid; preserve existing task IDs, task intent and completed history.
- Execution profiles express preferred implementation order only. They do not grant permission and do not create semantic dependencies.
- When parallel developers/agents or separate ownership are actually applicable, define ownership before work, preserve separate bounded edit surfaces, and make a shared contract, schema, interface or API boundary a dedicated approved task only when it is itself a coherent, independently reviewable and meaningfully verifiable outcome or materially unlocks independent workstreams that otherwise cannot proceed safely. Do not create a dedicated boundary task merely when it already exists and is reusable, belongs in another coherent bounded task, would be incomplete or meaningless, or merely mirrors ownership or manufactures parallelism. Do not treat parallel completion as integration completion.
- Integration of independently owned work requires an explicit gate for contract compatibility, conflicts, supported cross-boundary checks and combined review.
- Keep tests with the behavior they validate; do not create a generic test task automatically.
- Keep the semantic dependency graph separate from the execution schedule: `DEPENDENCY GRAPH != EXECUTION SCHEDULE`.
- Organizational profile values are `unspecified`, `single-developer`, `team`, and `multi-team`. Without approved planning-policy evidence, use `unspecified` and standard TCAF architecture-aware decomposition.
- Under `standard` decomposition, all organizational profiles preserve the same architecture/outcome-driven task boundaries, semantic dependencies and readiness for the same evidence and requested outcome. Profiles may affect execution or organization presentation only; they do not merge or serialize independently executable work.
- `unspecified` remains team-capable: do not invent owners, but do not serialize independent work merely because organization is unknown.
- `single-developer` may make the recommended execution schedule sequential but does not change task boundaries, dependencies or readiness.
- `team` and `multi-team` may expose independent parallel-ready work and evidence-backed ownership or convergence; never invent owners or teams.
- If an approved planning policy is present, obey its decomposition mode. `custom` may refine grouping, ownership conventions and examples only; it cannot waive a non-waivable TCAF invariant or the contextual BP-31 shared-boundary rule.
