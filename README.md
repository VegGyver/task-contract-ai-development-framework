# TCAF — Task-Contract AI Development Framework

**Clear constraints for AI. Control and flexibility for the developer.**

TCAF is a model-agnostic framework for controlled AI-assisted software
development. It lets developers delegate selected work to AI tools while
keeping scope, technical decisions, review, verification, and final acceptance
explicit and human-owned.

Version: **v0.4.0 · Public preview**

## Why TCAF

AI coding agents can accelerate development, but open-ended prompts can also
turn into unintended changes, opportunistic refactoring, or assumptions that
are hard to review. They can make the repository's current state and the
developer's authorization depend too much on a chat's memory.

TCAF makes delegation bounded and reviewable. It grounds work in repository
evidence: the code and the ordinary materials already used to describe the
project, such as notes, specifications, architecture documents, plans, and
roadmaps. Those materials do not need to be manually converted into a special
TCAF format.

When a stable normalized working representation is useful, TCAF can derive
canonical project state from that evidence for developer review. Canonical
project state is not a mandatory input format; it is repository-grounded state
that TCAF can re-read rather than a claim about what a chat remembers.

## How it works

A typical TCAF task follows this flow:

```text
Developer request
      ↓
Project inspection and repository evidence
      ↓
Task Contract
      ↓
Developer review and approval
      ↓
Bounded execution
      ↓
Verification
      ↓
Evidence + outcome
      ↓
Human acceptance
```

The **Task Contract** is the explicit authorization and review boundary before
implementation. It records the goal, expected outcome, allowed change surface,
checks, exclusions, and stop conditions. The AI can execute the approved work inside that boundary. If work would exceed it, the AI stops for a visible
amendment or a new developer decision; it does not silently expand scope.

The developer owns technical decisions, approval, review, verification, and
final acceptance. Preservation-first behavior keeps existing verified behavior
and developer changes unless an approved request explicitly requires a change.

## Choose an operation

| If you need to… | Use | What happens |
| --- | --- | --- |
| Start a new project, or begin from ordinary notes, specifications, or a roadmap | `bootstrap` | Establish the minimum project state and first work source. |
| Bring an implemented project under TCAF without rewriting its code or history | `adopt` | Inspect the project and propose the minimum canonical state for review. |
| Turn a feature or outcome into reviewable, dependency-aware work | `plan` | Produce a proposed implementation plan; no code is implemented. |
| Prepare one specific piece of work | `task` | Generate one bounded Task Contract for review and approval. |
| Reconcile project state after manual, external, or out-of-run changes | `sync` | Re-read evidence and propose bounded updates without automatically overwriting developer work. |

`bootstrap` and `adopt` preserve ordinary project material as source evidence
and derive separate canonical project state only when needed. `sync` is a
read-and-reconcile workflow, not an automatic restore of developer work.

## Quick start

### 1. Get TCAF

```bash
git clone https://github.com/VegGyver/task-contract-ai-development-framework.git
cd task-contract-ai-development-framework
```

### 2. Install

```bash
python install.py
```

Then verify the installation:

```bash
tcaf doctor
```

A valid installation should report `PASS`.

### 3. Choose a starting workflow

```bash
tcaf bootstrap --target <target> --request "<what you want to build>"
tcaf adopt --target <project-path>
tcaf plan --target <project-path> --request "<feature or outcome>"
tcaf task --target <project-path> --request "<bounded change>"
tcaf sync --target <project-path>
```

Use `bootstrap` for a new project or an initial body of project material. Use
`adopt` to inspect an existing project before proposing normalized state. Use
`plan` when the outcome needs dependency-aware review before implementation.
Use `task` for a bounded change, and `sync` after changes made manually,
externally, or outside the current run.

## Concrete example

Suppose you want to add a status filter to an existing application:

```bash
tcaf task \
  --target ./my-app \
  --request "Add an All / Active / Completed filter to the task list"
```

Before implementation, TCAF establishes the task boundary. For example:

```text
Goal
Add a three-state filter to the existing task list.

Expected outcome
Users can view all, active, or completed tasks without changing task storage.

Allowed change surface
- task-list UI
- local filtering logic
- tests directly related to the filter

Preserve / exclusions
- existing persistence
- routing
- unrelated styling
- current task-creation behavior

Checks
- All shows every task
- Active shows incomplete tasks
- Completed shows completed tasks
- existing behavior still works

Stop condition
Request an amendment if the change requires persistence, routing, or another
area outside this boundary.
```

Only after developer review and approval does implementation proceed. The
result is verified and reported with executed evidence and any limitations that
remain.

## Core principles

- **Engineering-owned** — architecture, product intent, technical decisions,
  and final acceptance remain human decisions.
- **Bounded delegation** — AI receives explicit authority for a defined change,
  not open-ended permission.
- **Inspect-first** — repository evidence and the current project are examined
  before work is proposed.
- **Preservation-first** — existing behavior, local patterns, and developer
  changes are retained unless an approved request changes them.
- **Minimum-first** — make the smallest coherent change that satisfies the
  approved task.
- **Evidence before acceptance** — verification claims require executed
  evidence.
- **Model-agnostic** — the authorization model works across models and adapter
  transports rather than being tied to one provider.

## Adapter coverage

TCAF v0.4.0 includes:

- **Codex** — native invocation verified;
- **Cline** — verified `manual-envelope` workflow with documented
  limitations; native runner-to-Cline invocation remains unverified;
- **Generic CLI** and **Generic Chat** transports for compatible
  environments, with broader validation in progress.

Adapter coverage can expand without changing the core authorization model.

## Validation

Validate the installed release and, when relevant, a target project:

```bash
tcaf validate
tcaf validate --target <project-path>
```

Release validation checks version coherence, registries, manifests, module
paths, adapters, templates, and project-document structure. TCAF v0.4.0 also
has semantic BLACK_BOX acceptance evidence for its covered core workflows,
including workflows that use ordinary project material without expert manual
preprocessing.

This remains a scoped public-preview claim, not a guarantee that every model,
adapter, host, or project configuration has been validated.

## Documentation

**Quick start and full documentation**

- English: https://framework.angelinilabs.dev/en/docs/
- Italiano: https://framework.angelinilabs.dev/it/docs/

The documentation guides new users from installation and a first workflow to
concepts, complete examples, and reference material.

## Technical reference

The versioned runtime installs outside target projects. Framework files are not
copied into a project as a second workspace root for ordinary use.

- `registry/agents.json` resolves operations and agents.
- Each `agent-bundles/*/manifest.json` declares exact modules and target policy.
- `runtime/tcaf.py` is the reference Universal Runner.
- `registry/adapters.json` selects an adapter without changing core behavior.
- `registry/project-schema.json` validates canonical project-document roles.

The standard procedures are documented in:

- `procedures/start-new-project.md`
- `procedures/adopt-existing-project.md`
- `procedures/plan-feature.md`
- `procedures/run-development-task.md`
- `procedures/sync-project-state.md`

## Project status

TCAF v0.4.0 is a pre-1.0 public preview under active development. Its core
workflows are evidence-grounded and model-agnostic; validation coverage is
being expanded across additional models, adapters, hosts, and project
configurations while preserving explicit developer authority over AI execution.

## AngeliniLabs

TCAF is developed as part of the AngeliniLabs R&D work on controlled
AI-assisted software development and software-delivery governance.

https://angelinilabs.dev/
