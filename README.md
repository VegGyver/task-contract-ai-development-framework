# Task-Contract AI Development Framework

A lightweight, model-agnostic framework for bounded, reviewable, incremental AI-assisted software development.

Version: **v0.4.0 architecture-A draft**

## What TCAF does

TCAF helps a developer delegate useful software work to an AI without making
the repository, the requested scope, or the review process depend on chat
memory. It records project understanding in repository evidence and, where
needed, in canonical project state: TCAF's stable, normalized working
representation of the project.

This is different from an unconstrained agent workflow, where a broad prompt
can quietly turn into a broad change. TCAF uses bounded execution: before a
piece of work is implemented, a Task Contract makes its goal, expected outcome,
allowed change surface, checks, exclusions, and stop conditions visible for
developer review. If the work needs to exceed that boundary, the AI stops for a
visible amendment or new decision rather than expanding scope silently.

The developer remains responsible for decisions, approval, review, verification,
and acceptance. The AI can inspect relevant evidence, prepare plans and Task
Contracts, implement an approved bounded change, and report what happened.
Preservation-first means existing verified behavior and developer changes are
kept unless an approved request requires a change. TCAF works with different
models and adapters; its project state is not a claim about what a chat happens
to remember.

## Choose an operation

| If you need to… | Use | What happens |
| --- | --- | --- |
| Start a new project, or begin from ordinary notes, specs, or a roadmap | `bootstrap` | Establish the minimum project state and first work source. |
| Bring an implemented project under TCAF without rewriting its code or history | `adopt` | Inspect the project and propose the minimum canonical state. |
| Turn a feature or outcome into reviewable, dependency-aware work | `plan` | Produce a proposed implementation plan; no code is implemented. |
| Prepare one specific piece of work | `task` | Generate one bounded Task Contract for review and approval. |
| Reconcile project state after manual, external, or out-of-run changes | `sync` | Re-read evidence and propose bounded updates without overwriting developer work. |

Your existing project material does not need to be manually rewritten into a
TCAF format first. Notes, specifications, architecture documents, plans, and
roadmaps are source evidence. Bootstrap and adopt preserve that material and,
when needed, derive separate canonical project state for developer review.
Canonical documents are a working representation for TCAF,
not a mandatory input format.

## Core formula

```txt
Repo-first
Task-contract driven
Minimum-first
Outcome-first
Standardized
Model-agnostic
Tool-resilient
Human-reviewed
```

## Install once

```txt
python install.py
tcaf doctor
```

The versioned runtime is installed outside target projects. Framework files are never added as a second workspace root or copied into a project for ordinary use.

## One procedure

```txt
tcaf bootstrap --target <target> [--request <text> | --input <path>]
tcaf adopt --target <target>
tcaf plan --target <target> --request <feature or outcome>
tcaf task --target <target> --request <bounded request>
tcaf sync --target <target> [--request <text> | --input <path>]
tcaf run <future-agent-id> --target <target>
```

Every operation uses:

```txt
operation
→ registry
→ agent manifest
→ automatic module loading
→ exactly one target
→ adapter
→ run envelope
→ developer review gate
```

Users select an operation or public agent ID, not framework files. The same protocol applies to greenfield targets without a repository, existing projects, daily tasks and future agents.

A greenfield bootstrap may start from a complete analysis, a product idea, an initialized target, an initial roadmap or one first task. A repository backlog is optional when the manifest declares another task source, including direct developer requests.

The envelope declares its adapter transport. Native Codex invocation is verified. Cline currently uses the verified `manual-envelope` procedure in `adapters/cline.md`; native runner-to-Cline invocation remains unverified.

## Architecture

- `registry/agents.json` resolves operations and agents.
- Each `agent-bundles/*/manifest.json` declares exact modules and target policy.
- `runtime/tcaf.py` is the reference Universal Runner.
- `registry/adapters.json` selects one tool adapter without changing core behavior.
- `registry/project-schema.json` validates canonical project-document roles.
- framework instructions and target evidence remain separate.

## Validation

```txt
tcaf validate
tcaf validate --target <project-path>
```

Release validation checks version coherence, registries, manifests, module paths, adapters, templates and project-document structure.

## Standard procedures

- `procedures/start-new-project.md`
- `procedures/adopt-existing-project.md`
- `procedures/plan-feature.md`
- `procedures/run-development-task.md`
- `procedures/sync-project-state.md`

## Current status

This is a pre-1.0 draft implementing approved Architecture A from the v0.2.7 calibrated core. Version v0.2.8 is discarded. Runtime tests validate the operational layer; clean model acceptance tests remain required before a stable release.
