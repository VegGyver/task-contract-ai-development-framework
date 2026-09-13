# TCAF Development Change Control

This document governs development of the TCAF framework itself.

It is not ordinary target-project prompt material and must not be automatically loaded into normal TCAF runtime envelopes.

## Governing formula

```txt
NEW BEHAVIOR = EXISTING VERIFIED BEHAVIOR + EXPLICIT REQUESTED DELTA
```

A framework change extends a recovered, verified baseline. It does not authorize reinterpretation of the whole framework.

## Mandatory pre-change record

Before changing TCAF, identify:

- requested delta;
- affected principles;
- preserved invariants;
- change classification for each affected principle: `PRESERVE`, `EXTEND`, `CHANGE`, `NEW`, or `DEPRECATE`;
- allowed implementation surfaces;
- existing regression evidence that must remain valid;
- new verification required by the delta.

No implementation should begin from a broad instruction such as “rewrite this file with the new behavior” when narrower affected surfaces can be identified.

## Principle impact rule

When a framework file or implementation surface is touched:

1. identify every registered principle implemented or materially expressed by that surface;
2. preserve behavior for every unrelated principle;
3. modify only the surface required by the approved delta;
4. rerun the regression evidence mapped to affected and co-located principles;
5. do not treat a passing structural test as proof of unchanged semantic AI behavior.

A previously working or verified behavior is preserve-by-default unless an explicit delta changes it.

## Principle applicability versus context loading

A principle applies because its semantic trigger is true, not because a specialist file happened to be loaded.

This rule does not justify loading the whole framework into every model context.

The intended composition model is:

```txt
operation + project/work context
        ↓
applicable principles
        ↓
deterministic enforcement where possible
        ↓
minimum model-facing representation
        ↓
specialist guidance only when needed
```

`Minimum-first` and principle propagation are complementary requirements: all applicable behavior must be preserved using the minimum safe instruction/context surface.

## Verification ladder

### STRUCTURAL

Use when correctness can be established deterministically from framework artifacts.

Examples:

- registry/schema coherence;
- manifest references;
- unique IDs;
- allowed enum values;
- file existence;
- adapter/operation registration;
- governance isolation.

Structural success does not prove semantic model behavior.

### BEHAVIORAL

Use when the instruction system, runtime contract, or deterministic workflow behavior must be exercised beyond static structure.

Examples:

- evidence-state rules;
- lifecycle-state separation;
- canonical role resolution;
- read-only workflow gates;
- output/provenance rules.

Behavioral verification may be automated without requiring an AI model when the relevant behavior is deterministic.

### BLACK_BOX

Use when conformance depends materially on model interpretation, semantic planning, decomposition, classification or generation.

Black-box verification is required before semantic AI behaviors such as these are considered fully verified:

- task granularity;
- architecture-aware decomposition;
- semantic dependency reasoning;
- team-capable planning;
- readiness/parallelism reasoning;
- convergence/integration decisions;
- feature/task classification when real project context affects the answer.

String-presence assertions and successful envelope assembly do not constitute black-box verification.

## Evidence status and current health

Verification history and current health are separate concepts.

A principle may have historical verification evidence and still be in `REGRESSION_DETECTED` health after a later change.

Allowed health states are defined by `governance/principles.json`.

## Release and milestone gate

A milestone or release must not be accepted when an affected principle:

- has health `REGRESSION_DETECTED` or `BLOCKED`; or
- is below its declared required verification level for the behavior changed by that milestone.

`HEALTHY` does not authorize skipping the regression evidence mapped to a touched implementation surface.

## Explicit semantic changes

When an existing principle changes meaning, record the change explicitly.

Do not silently replace historical semantics in-place.

The registry must preserve enough provenance to distinguish:

- preserved behavior;
- extensions;
- explicit semantic changes;
- new principles;
- deprecated behavior.

## Governance isolation

The `governance/` directory governs development of TCAF itself.

Normal target-project agent manifests must not automatically load files from `governance/`.

Governance metadata may be inspected during TCAF framework development and release validation, but it is not project evidence and is not ordinary model-facing runtime guidance.

## Current 0.4 sequencing

The current controlled sequence is:

1. establish the framework-development governance baseline;
2. implement principle propagation (`BP-37`) without abandoning minimum-first context;
3. add the organizational execution profile and optional project custom planning/decomposition policy;
4. harden `tcaf plan` against principle-mapped behavioral and black-box regressions;
5. only then resume project-state synchronization work.

Until the relevant change contract is approved, existing 040-04 behavior is preserved and 040-05 work remains out of scope.
