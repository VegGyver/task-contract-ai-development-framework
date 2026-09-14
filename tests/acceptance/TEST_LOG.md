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
