# Acceptance Test Log

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
