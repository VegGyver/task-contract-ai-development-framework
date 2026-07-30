# Task-Contract AI Development Framework

A lightweight, model-agnostic framework for bounded, reviewable and incremental AI-assisted software development.

Version: **v0.3.0 architecture-A draft**

## Core formula

```txt
Repo-first
Task-contract driven
Minimum-first
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
tcaf task --target <target> --request <bounded request>
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

The envelope declares its adapter transport. Cline currently uses the verified `manual-envelope` procedure in `adapters/cline.md`; native runner-to-Cline invocation remains unverified.

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
- `procedures/run-development-task.md`

## Current status

This is a pre-1.0 draft implementing approved Architecture A from the v0.2.7 calibrated core. Version v0.2.8 is discarded. Runtime tests validate the operational layer; clean model acceptance tests remain required before a stable release.
