# TCAF — Task-Contract AI Development Framework

**Clear constraints for AI. Control and flexibility for the developer.**

TCAF is a model-agnostic framework for controlled AI-assisted software development.

It lets developers and engineering teams delegate selected work to AI tools while keeping scope, technical decisions, verification and final acceptance explicit and human-owned.

**Current version: 0.3.3 · Public preview**

## Why TCAF

AI coding agents can accelerate development, but greater autonomy can also produce:

- unintended changes outside the requested scope;
- opportunistic refactoring;
- assumptions treated as requirements;
- modifications that are difficult to review or verify;
- loss of clarity about what the developer actually authorized.

TCAF addresses this through bounded, reviewable tasks.

The AI can work freely **inside the approved task boundary**.  
The developer remains in control of the software.

## How it works

A typical TCAF task follows this flow:

```text
Developer request
      ↓
Project inspection
      ↓
Task Contract
      ↓
Developer review
      ↓
Implementation
      ↓
Verification
      ↓
Evidence + outcome
      ↓
Human acceptance
```

The **Task Contract** makes the work explicit before implementation begins:

- objective;
- authorized change surface;
- behaviour and areas to preserve;
- acceptance criteria;
- verification checks;
- stop conditions.

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

## Choose your starting point

### Start a new project

```bash
tcaf bootstrap --target <target> --request "<what you want to build>"
```

Use `bootstrap` when you are starting from an idea, analysis, scaffold, roadmap or initial task.

### Adopt an existing project

```bash
tcaf adopt --target <project-path>
```

TCAF inspects the existing project before proposing canonical project evidence. Adoption does not silently modify application code.

### Run a development task

```bash
tcaf task --target <project-path> --request "<bounded change>"
```

TCAF analyses the relevant project context and prepares a Task Contract for developer review before implementation authority expands.

## Example

Suppose you want to add a status filter to an existing application:

```bash
tcaf task \
  --target ./my-app \
  --request "Add an All / Active / Completed filter to the task list"
```

Before implementation, TCAF establishes the task boundary.

For example:

```text
Objective
Add a three-state filter to the existing task list.

Allowed
- task-list UI
- local filtering logic
- tests directly related to the filter

Preserve
- existing persistence
- routing
- unrelated styling
- current task creation behaviour

Acceptance
- All shows every task
- Active shows incomplete tasks
- Completed shows completed tasks
- existing behaviour still works
```

Only after review does implementation proceed.

The result is then verified and reported with executed evidence and any remaining limitations.

## Core principles

TCAF is designed around a few rules:

- **Engineering-owned** — architecture, product intent and final decisions remain human decisions.
- **Bounded delegation** — AI receives an explicit scope rather than open-ended authority.
- **Inspect-first** — the current project is examined before changes are proposed.
- **Preservation-first** — working behaviour and local patterns are preserved unless change is explicitly authorized.
- **Minimum-first** — implement the smallest coherent change that satisfies the task.
- **Evidence before acceptance** — verification claims require executed evidence.
- **Model-agnostic** — the framework is not tied to one AI model or provider.

## Adapter coverage

TCAF 0.3.3 currently includes:

- **Codex** — native invocation verified;
- **Cline** — manual-envelope workflow verified with documented limitations;
- **Generic CLI** and **Generic Chat** transports for compatible environments, with broader validation still in progress.

Adapter coverage can expand without changing the core authorization model.

## Validation

You can validate the installed release and, when relevant, a target project:

```bash
tcaf validate
tcaf validate --target <project-path>
```

TCAF 0.3.3 is a **public pre-1.0 release**.

The runtime, installation flow and selected adapter/workflow paths have been exercised on real or representative software-development scenarios. Validation is intentionally scoped: support for additional models, hosts and project configurations is being expanded progressively.

## Documentation

**Quick start and full documentation**

- English: https://framework.angelinilabs.dev/en/docs/
- Italiano: https://framework.angelinilabs.dev/it/docs/

The documentation is organized to let new users install TCAF, run a first workflow and see a complete example before moving into concepts and reference material.

## Project status

TCAF is under active development.

The framework core is intentionally model-agnostic. Current work focuses on expanding validation coverage, improving reproducibility across environments and testing additional model/provider profiles while preserving explicit developer authority over AI execution.

## AngeliniLabs

TCAF is developed as part of the AngeliniLabs R&D work on controlled AI-assisted software development and software-delivery governance.

https://angelinilabs.dev/
