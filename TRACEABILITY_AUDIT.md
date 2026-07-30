# Traceability Audit — v0.3.3

This audit maps the framework decisions to their authoritative modules and runtime coverage.

Status meanings:

- **Covered** — present in the authoritative guide/core and represented at runtime where needed.
- **Reference-only** — intentionally excluded from ordinary runtime; loaded only for the relevant scenario.
- **Added in v0.2.1** — missing or incomplete in v0.2 consolidated and restored without enlarging ordinary prompts.

| Principle / safeguard | Authoritative source | Runtime / template coverage | Status |
|---|---|---|---|
| Repository is source of truth; chat memory is not | `core/principles.md` | global, project and standalone rules | Covered |
| Explicit task boundary and allowed edit surface | `core/task-contract.md` | all task-contract templates | Covered |
| Unlisted files/change types are forbidden | `core/principles.md` | global/project rules and templates | Covered |
| Minimum-first prompts and selective loading | `core/principles.md`, `core/module-loading-guide.md` | runtime files remain compact | Covered |
| Outcome-first operational responses | principles, lifecycle, review guide | bundle schemas and compact runtime rules | Covered |
| One installed runtime outside target projects | run protocol, installation/versioning guide | installer, launcher and procedures | Covered |
| One stable operation protocol for every agent | run protocol | runner public commands and registry | Covered |
| Deterministic agent and module resolution | agent registry and machine manifests | loader and validator | Covered |
| Exactly one target; framework/target separation | target binding, adapter contract | loader overlap checks and run envelope labels | Covered |
| Automatic adapter selection without core changes | adapter contract and adapter registry | runner adapter selection | Covered |
| Adapter transport and native-invocation status are explicit | adapter contract and adapter registry | run envelope | Covered |
| Registry, manifest and artifact preflight | registries and project schema | `tcaf validate` | Covered |
| Inspect only relevant context; no whole-repo scan by default | principles, capability guide | global/standalone rules | Covered |
| Existing capabilities only; no implicit dependencies/tooling/tests | capability guide | global/project/standalone rules | Covered |
| Preservation-first for working code | principles, decomposition guide | global/project/standalone and code-change templates | Covered |
| Developer and concurrent changes are re-read and preserved | principles, change/history guide | global/project/standalone rules | Covered |
| Reuse existing functions, guards and validations; no duplicate controls | principles | global/project rules and code-change template | Covered |
| Local pattern first; official version-compatible docs when absent | implementation source hierarchy | compact runtime and project-rules template | Covered |
| Official safety/compatibility/correctness conflict is reported | implementation source hierarchy | compact runtime rules | Covered |
| Repository standards use representative target evidence | capability guide | adoption agent/output and baseline template | Covered |
| Smallest useful complete change | decomposition guide | task contracts and agent behavior | Covered |
| Execution profile defines order, not permission | execution profiles, task contract | project rules | Covered |
| Bug fix changes only demonstrated cause | task types, decomposition | bug-fix template | Covered |
| Refactor must be explicit and separate | task types, principles | runtime rules and templates | Covered |
| Docs status task changes only allowed status fields/lines | task types | docs-status example | Covered |
| Logical gates independent of tool buttons | lifecycle | Cline adapter | Covered |
| Developer-run verification supported and default | review guide | task contract and runtime rules | Covered |
| Usually one to three targeted checks | review guide | standalone rules and adapters | Covered |
| Human review, UI/console verification and acceptance are mandatory | lifecycle, review guide | response expectations | Covered |
| Agent does not commit, push or discard without permission | review guide | adapter/agent boundaries | Covered |
| Exact operational states: implemented is not accepted/completed | lifecycle | review response state | Covered |
| Clarifications, corrections, amendments and separate requests are explicit | task contract, change/history guide | task agent schema and compact runtime rules | Covered |
| Completed task history is immutable | change/history guide | project rules and adoption agent | Covered |
| Later changes/fixes/extensions are appended and linked | change/history guide | change templates | Covered |
| Task naming belongs to project/team/tracker | change/history guide | naming template and agents | Covered |
| Existing naming and historical IDs are never replaced | change/history guide | adoption agent | Covered |
| Framework adoption is additive-only and no-overwrite by default | task types | adoption agent | Covered |
| Greenfield agent asks or proposes naming rather than inventing it | change/history guide | bootstrap agent | Covered |
| External tracker can satisfy Backlog without parallel state | project documentation schema | manifest parser and target validator | Covered |
| Open project decisions are present and unique | project documentation schema | bootstrap agent, checklist and target validator | Covered |
| Greenfield separate FE/BE work uses shared contracts and ownership boundaries | team/multi-agent guide | loaded only for team scenarios | Added in v0.2.1 |
| Multi-agent work requires explicit ownership and integration gate | team/multi-agent guide | loaded only for team scenarios | Added in v0.2.1 |
| Database migration/backfill, security, performance and hotfix need dedicated bounded workflows | advanced-scenarios guide | loaded only for those task types | Added in v0.2.1 |
| Project bootstrap can generate a minimal project documentation set | project-doc templates | bootstrap agent | Added in v0.2.1 |
| Greenfield bootstrap supports partial input and optional repository backlog | project documentation schema, start procedure | bootstrap agent and output schema | Covered |
| Completed implementation notes and original dependencies are historical too | change/history guide | adoption policy | Added in v0.2.1 |

## Runtime-size conclusion

No new rule was added to the ordinary global runtime unless it is needed for almost every task. Scenario-specific safeguards remain in optional guides. A normal task still loads:

1. minimal global rules;
2. compact project rules;
3. one short task contract;
4. at most one optional specialist module when required.

## Audit result

All principles explicitly established through v0.3.3 are now either:

- present in ordinary runtime because they apply to nearly every task; or
- retained in a single authoritative optional module and loaded only for the applicable scenario.
