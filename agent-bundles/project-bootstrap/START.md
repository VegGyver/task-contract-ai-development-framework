# Start — Project Bootstrap

Use the Project Bootstrap Agent.

Input may be a complete analysis, a project idea, an initialized target, a first task or a partial roadmap.

Generate the minimum useful documentation from canonical templates. Separate current state, desired state, confirmed decisions, proposals and open decisions. Do not write application code. Do not invent missing decisions; use `To be decided` when non-blocking.

Treat supplied documentation as source evidence by default. Before reusing an
existing file for a canonical role, verify its required headings, order and
role-specific schema rules. If it is incompatible, preserve it unchanged and
normalize supported evidence into a fresh official-template document. Use the
canonical default path when free; if non-canonical user content occupies that
path, use an approved alternate canonical path and record that canonical path
in the project manifest. Never map source evidence directly to a canonical
role.

A complete repository backlog is optional. Declare its source as a repository file, approved external tracker or `external:Developer requests`.

Return the generation report defined in `OUTPUT-SCHEMA.md` and stop for developer review.

Under `DEVELOPER_RUN`, report `VALIDATION PENDING` and the exact command
`tcaf validate --target .`. Report `Validation: PASS` only when that runtime
command was actually executed and passed.
