# Planning Rules — Minimal

Apply these rules whenever TCAF creates, evaluates, decomposes or sequences units of work.

- A step is the smallest useful complete change: one primary goal, one reason to change, a bounded surface, a verification method, a stop condition and a valid project state afterward.
- Derive task boundaries from the architecture and responsibilities actually present. Do not introduce or force frontend, backend, shared or other layers merely to satisfy a generic profile.
- Split work that mixes unrelated layers, behavior and refactor, feature and tooling, or code and history. Do not split work into incomplete or meaningless fragments.
- Dependencies represent real prerequisites only. Task IDs, backlog order, roadmap order, phase order and preferred execution order do not create dependencies.
- Reuse existing tasks and capabilities where valid; preserve existing task IDs, task intent and completed history.
- Execution profiles express preferred implementation order only. They do not grant permission and do not create semantic dependencies.
- When parallel developers/agents or separate ownership are actually applicable, define ownership before work, preserve separate bounded edit surfaces, require dedicated approved work for shared contracts or API boundaries under the current team rule, and do not treat parallel completion as integration completion.
- Integration of independently owned work requires an explicit gate for contract compatibility, conflicts, supported cross-boundary checks and combined review.
- Keep tests with the behavior they validate; do not create a generic test task automatically.
