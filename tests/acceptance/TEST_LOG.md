# Acceptance Test Log

## TCAF 0.4 — Feature planner semantic-model BLACK_BOX acceptance

These were BLACK_BOX runs of the planner's semantic model, distinct from the
deterministic/static runtime and governance suites. Final passing runs used the
planner bundle and project evidence without an external corrective prompt.

Original team-profile run failed: it merged independent API and web work,
removed their parallel readiness, and allocated the feature ID from task
numbering. After narrow planner hardening, the corrected retest kept the work
separate, preserved the semantic DAG and parallel readiness, used `RE-F001`,
invented no ownership, and expressed convergence as a review gate.

Passing observations across the completed runs:

- Clean Verified Story planning kept the feature distinct from tasks, separated
  bounded domain/persistence, verification, API, and web work, reused existing
  capabilities, treated RE-005 as an external prerequisite only when required,
  and surfaced canonical/documentation drift.
- Unspecified, single-developer, team, and multi-team standard profiles kept
  the same API/web task boundaries and semantic readiness. The
  single-developer profile recommended sequential execution without inventing a
  dependency; team and multi-team profiles invented neither owners nor teams.
- The approved custom policy kept independently useful HTTP endpoints separate,
  retained direct tests with the behavior they verify, avoided micro-tasks, and
  left both endpoint tasks parallel-ready on the existing API foundation.
- The classification/validation retest stopped emitting unrelated RE-005 as an
  external prerequisite and used the bound target locator in its pending
  validation command.

Scope limits: these runs do not demonstrate feature-level acceptance distinct
from task verification, generalized convergence behavior, sync/drift
reconciliation, or cross-operation principle propagation.

## TCAF 0.4 — BP-31 contextual shared-contract decomposition

These were semantic-model BLACK_BOX planner runs using the `team` profile and
`standard` mode. Final passing runs used the planner bundle and project evidence
without external corrective prompts.

### A — no dedicated boundary task

For a NestJS `GET /release-info` endpoint displayed by Next.js, the response
shape was already specified and root package metadata remained the source.
The planner created RE-006 for API behavior and RE-007 for web behavior, with
no API-contract task. It stated that the boundary was small, already specified
and coherently belonged with the API producer. API and web work remained
independently executable, integration verification remained separate, and no
ownership was invented. Result: **PASS**.

### B — dedicated boundary task justified

For NestJS `POST /stories/:id/publish` and a worker consuming the canonical
typed `StoryPublished` event, the planner created RE-006 for the event
contract, RE-007 for the API producer and RE-008 for the worker consumer.
RE-006 was justified as independently verifiable and as materially unlocking
the producer and consumer; dependencies were RE-006 → RE-007 and RE-006 →
RE-008. No ownership was invented, and convergence remained contract/integration
verification rather than an artificial implementation task. Result: **PASS**.

Together, A and B verify BP-31's contextual directions: no automatic
shared-boundary task when an existing specified boundary coherently belongs in
another task, and a dedicated task when the boundary is independently
reviewable/verifiable or materially unlocks independent workstreams.

## Calibration test 1

Result: partial pass.

Observed issues:

- historical immutability applied too broadly to status fields
- unavailable inferred from incomplete inspection
- unnecessary canonical pointer files proposed
- parallel status reconciliation document proposed
- canonical/adaptor project-rule relationship unclear

## Calibration test 2

Result: expected corrected output obtained after explicit correction prompt.

Action: corrections incorporated into the framework and canonical adoption bundle.

## Retest requirement

Run the existing-project adoption test from a clean task using only the updated bundle. No external correction prompt is allowed. Pass only if the first output satisfies `existing-project-adoption.md`.

## Calibration 2 — multi-root boundary test

Observed improvement: canonical mapping, history/status distinction and minimum file set were mostly correct.
Remaining defects: framework/project read surfaces were not explicit; hidden or uninspected paths were still classified as unavailable.
Resolution: v0.2.5 adds manifest-only framework loading, target-root confirmation and stricter absence evidence rules.
Status: pending clean retest.

## v0.3.0 — Architecture A runtime

Scope:

- versioned installation outside target projects
- central registry and deterministic manifests
- one-target binding and adapter selection
- run-envelope assembly
- framework and project-document validation
- repository-standard extraction rules

Automated runtime suite: **22/22 passed** on 2026-07-29 with:

```txt
python -m unittest discover -s tests/runtime -v
```

Framework preflight: **passed with 0 errors and 0 warnings**.

Model acceptance remains pending for:

- `universal-run-protocol.md`
- clean `existing-project-adoption.md`
- `manifest-and-artifact-validation.md` mutation scenarios

No external correction prompt, multi-root workspace or alternate run procedure is allowed.

## v0.3.0 — Cline bootstrap calibration

Result: final generated documentation passed after segmented corrective prompts.

Findings incorporated:

- external trackers can satisfy the Backlog role without a parallel repository file;
- supplied open decisions must be propagated and must occur once per applicable section;
- Cline uses registered `manual-envelope` transport with one write confirmation per task and explicit `Pending` recovery;
- native Cline invocation remains unverified and must not be claimed;
- the e2e TypeScript fixture requires a passing preflight baseline before model attribution.

Automated runtime suite after correction: **22/22 passed**.
Framework validation: **passed with 0 errors and 0 warnings**.
Fixture baseline: `npm ci`, `npm test` and `npm run typecheck` passed.

Retest requirement: run bootstrap from a clean target with `bootstrap-input.md`, the public Cline adapter markers and no external corrective prompt. Pass only if both model validation and `tcaf validate --target bootstrap-project` succeed on the first complete run.

## v0.3.0 — Cline adoption inspection calibration

Result: safe read-only completion, acceptance failed.

Observed issues:

- direct reads of absent canonical paths reached Cline's consecutive-error limit;
- relevant `.github` and `.clinerules` evidence was omitted;
- one explicitly legacy JavaScript exception was classified `Conflicting` instead of `Localized`.

Resolution: require read-only existence checks before reads, task-relevant dot-config inspection and multiple active patterns before using `Conflicting`.

Automated runtime suite after correction: **23/23 passed**. Framework preflight: **0 errors, 0 warnings**.

Retest requirement: rerun adoption from a clean kit extraction. Pass only if the first `INSPECT` task completes without corrective prompts or failed-read recovery and satisfies `existing-project-adoption.md`.

## v0.3.1 — Native Codex daily-task acceptance

Result: passed with verification-guidance findings.

Authoritative evidence:

- TCAF 0.3.1 was invoked through the active native Codex adapter for Software Delivery Planner task B-016.
- The workflow completed contract preparation, developer review, implementation, `DEVELOPER_RUN` verification, code review, correction, documentation/status reconciliation and local checkpoint commit.
- Software Delivery Planner checkpoint `72706ed` records the accepted implementation.
- Developer-reported verification was Feature tests 5/5 and API suite 11/11.

Accepted follow-up for v0.3.2:

- make `DEVELOPER_RUN` command ownership and result provenance explicit;
- require command descriptions to match effective scope;
- mark native Codex invocation verified in the adapter registry.

## v0.3.3 — Task evolution and outcome-first workflow

Scope:

- complete or partial greenfield input with a declared task source;
- backlog, issue, analysis and direct-request convergence;
- clarification, correction, local adaptation, amendment, separate-task and blocker handling;
- preservation of developer and concurrent changes;
- outcome-first operational responses and final verification labels.

Automated runtime suite: **26/26 passed** on 2026-07-30.
Framework preflight: **passed with 0 errors and 0 warnings**.

Clean model acceptance remains required for bootstrap, task generation, in-task amendment handling and final outcome reporting.

## TCAF 0.4 — 040-05 project-sync semantic-model BLACK_BOX acceptance

Fixture/baseline: `/tmp/reality-error-sync-drift`, with Reality Error RE-001
through RE-004 completed and RE-005 proposed/planned. Manual developer evidence
was the untracked `prisma/schema.prisma` (Prisma PostgreSQL datasource/generator
only), preserved throughout with SHA-256
`d6ba2e4d55dc9336acb9fece8e4ba1361aac8bdb4203aa06150c48035f67286a`.

### A — default inspect/propose: PASS

Without `--request` or `--input`, sync independently inspected canonical and
repository evidence, detected stale canonical documentation and the untracked
Prisma file, identified RE-005 as affected but did not infer completion or
authorship. It surfaced the root `prisma/schema.prisma` versus planned
`packages/database` mismatch as uncertain, preserved completed history, proposed
bounded documentation reconciliation with no RE-005/backlog update, stopped at
WAITING FOR APPROVAL, made no mutation, and reported validation NOT RUN with
the bound-target command. Post-run repository evidence confirmed the proposal
pass was read-only.

### B — approved bounded apply: initial semantic reporting failure

The Run Envelope approved only `docs/project-brief.md` and
`docs/architecture-overview.md` to reflect the RE-001–RE-004 foundation, and
prohibited backlog, RE-005, Prisma, source, and completed-history changes.
Writes were correctly bounded, but the final report incorrectly stated that no
affected planned task/conflict remained although RE-005/Prisma uncertainty was
unresolved. This run is failure evidence, not a passing acceptance run.

Corrective change: the sync instruction surface now keeps approval/write scope
separate from the current finding state.

### B2 — corrected approved bounded apply: PASS

After restoring the two canonical docs while preserving the same Prisma
evidence, sync re-derived findings and changed only
`docs/project-brief.md` and `docs/architecture-overview.md`. It kept RE-005
proposed and affected, preserved the unresolved Prisma evidence, distinguished
findings resolved by approved writes from findings unresolved outside approval,
and made no backlog, task/history, source, Prisma, staging, commit, or push
change. It ran exactly:

```txt
tcaf validate --target /tmp/reality-error-sync-drift
```

Result: **PASS — 0 errors, 0 warnings**.

Mechanical post-run preservation evidence:

```txt
git status: M docs/architecture-overview.md; M docs/project-brief.md; ?? prisma/
git diff --name-only: docs/architecture-overview.md; docs/project-brief.md
docs/backlog.md: no diff
prisma/schema.prisma SHA-256: d6ba2e4d55dc9336acb9fece8e4ba1361aac8bdb4203aa06150c48035f67286a
```

Accepted semantic scope: manual repository drift is read-only by default;
explicit current-envelope approval bounds canonical writes; and unresolved
findings survive an apply when outside its approved write set. This demonstrates
the canonical-intent/observed-evidence distinction, planned-task impact without
false completion, preservation of developer evidence and completed history, and
bound-target validation.

Scope limits: this sync semantic-model BLACK_BOX does not demonstrate
generalized BP-02 or BP-35 behavior across every operation, BP-32 convergence,
BP-37 cross-operation propagation, feature-level acceptance distinct from task
verification, 040-06 CLI UX, 040-07 release-gate coverage, or 040-08.

## TCAF 0.4 — 040-07 semantic-model BLACK_BOX acceptance

**Result: COMPLETE / BLACK_BOX PASS.** These acceptance results are semantic
BLACK_BOX evidence; deterministic/static tests provide regression coverage but
do not alone prove this behavior. The clean runs used the applicable TCAF
bundle and project evidence without expert chat preprocessing.

### A — greenfield arbitrary-document bootstrap: PASS

Fixture: `/tmp/reality-error-bootstrap-blackbox`. Input contained only the
arbitrary source documents `docs/PROJECT_CONTEXT.md` and
`docs/PROJECT_PLAN.md`; no canonical TCAF project documents were supplied.

The clean bootstrap generated the seven minimum canonical project documents
while preserving both original source documents byte-for-byte. It kept current
and planned state separate, inferred no false capability availability,
preserved proposed backlog state and open decisions, and respected the
developer review gate. The following bound-target validation passed with 0
errors and 0 warnings:

```txt
tcaf validate --target /tmp/reality-error-bootstrap-blackbox
```

### B — existing-project adopt: PASS

Fixture: `/tmp/reality-error-adopt-blackbox`. The fixture contained real
implementation/configuration and arbitrary source documentation, but no
canonical TCAF project state before adoption.

**B1 — inspect-only.** Repository capabilities were derived from
implementation/configuration evidence and the arbitrary documents were treated
as source evidence. The run inferred no false completion for RE-001 through
RE-004, proposed exactly seven canonical candidate files, proposed no
unnecessary project manifest or planning policy, preserved every original hash,
and added no files during inspection.

**B2 — explicitly approved bounded apply.** Exactly these seven canonical
files were created:

- `docs/project-brief.md`
- `docs/architecture-overview.md`
- `docs/backlog.md`
- `docs/method/project-rules.md`
- `docs/method/ai-workflow.md`
- `docs/method/capability-baseline.md`
- `docs/method/task-naming.md`

All pre-existing files remained byte-for-byte unchanged and no unauthorized
files were created. Canonical task lifecycle state was not inferred from
repository implementation; current and planned capabilities remained separate;
and the unresolved application-containerization decision remained unresolved.
Bound-target validation passed with 0 errors and 0 warnings:

```txt
tcaf validate --target /tmp/reality-error-adopt-blackbox
```

### C — feature planning: PASS

Feature planning is covered by the existing TCAF 0.4 planner semantic-model
BLACK_BOX acceptance evidence recorded above. Its clean passing runs preserved
task boundaries, semantic readiness and parallelism, avoided invented
ownership, and used the planner bundle and project evidence without external
corrective prompts.

### D — developer modification and sync: PASS

Developer modification and synchronization are covered by the existing 040-05
project-sync semantic-model BLACK_BOX evidence recorded above. Its corrected
approved bounded apply preserved developer Prisma evidence and completed
history, kept RE-005 proposed/affected rather than falsely complete, retained
unresolved findings outside the approved write set, and passed bound-target
validation with 0 errors and 0 warnings.

### E — Task Contract generation: final clean PASS, with historical failures preserved

Target: `/tmp/reality-error-adopt-blackbox`; task: canonical backlog item
RE-005.

The initial BLACK_BOX run exposed unsupported lifecycle-evidence strengthening
and an over-broad Modify surface. Narrow hardening was applied only to Task
Contract generator instruction surfaces, with deterministic regression
coverage. This observation is failure evidence, not a passing acceptance run.

A clean retest confirmed the lifecycle and Modify corrections but exposed
missing evidence state on a prerequisite check. A second narrow hardening then
required every listed check, including prerequisites, to carry exactly one
evidence state. This retest is likewise intermediate failure evidence, not a
passing acceptance run.

A further clean retest confirmed those corrections but exposed conditional
Modify/check surfaces controlled by an unresolved execution-affecting decision.
Final narrow hardening established that a READY executable contract may keep an
Open decision only when execution remains fully bounded and identical regardless
of that decision; otherwise existing BLOCKED / needed-decision behavior applies.
This observation remains historical failure evidence, not a passing acceptance
run.

The final clean BLACK_BOX retest confirmed canonical task identity and
provenance; preserved canonical lifecycle evidence exactly; produced one bounded
RE-005 task; tied the Modify surface only to concrete changes; left no unresolved
execution-affecting decision; marked every listed DEVELOPER_RUN check explicitly
NOT RUN; introduced no product-domain scope creep; respected the developer
approval gate; and left the target byte-for-byte and file-set unchanged.

**Final result: Task Contract generation — BLACK_BOX PASS.**

### F — no expert chat preprocessing: PASS

No expert chat preprocessing was required across the clean greenfield bootstrap,
existing-project adoption, and Task Contract generation runs.

### 040-07 summary

- Greenfield arbitrary-document bootstrap: **PASS**
- Existing-project adopt: **PASS**
- Feature planning: **PASS**
- Developer modification + sync: **PASS**
- Task Contract generation: **PASS**
- No expert chat preprocessing: **PASS**
