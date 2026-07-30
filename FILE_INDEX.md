# File Index

## Start here

- `README.md`
- `guides/installation-and-versioning.md`
- `core/run-protocol.md`
- `procedures/start-new-project.md`
- `procedures/adopt-existing-project.md`
- `procedures/run-development-task.md`

## Operational runtime

- `VERSION`
- `install.py`
- `runtime/tcaf.py`
- `runtime/tcaf_runtime/`
- `registry/agents.json`
- `registry/adapters.json`
- `registry/project-schema.json`

## Agent bundles

- `agent-bundles/project-bootstrap/`
- `agent-bundles/existing-project-adoption/`
- `agent-bundles/task-contract-generator/`

Each canonical bundle has a machine-authoritative `manifest.json`. `MANIFEST.md` is its human-readable mirror.

## Framework modules

- `core/`: principles, run/target/adapter protocols, contracts, lifecycle, schema and module loading
- `guides/`: optional specialist guidance
- `runtime/`: compact model-facing rules
- `templates/`: canonical project and task templates
- `adapters/`: tool-specific notes
- `examples/`: compact examples
- `tests/acceptance/`: repeatable framework acceptance tests

Active-task amendments and developer/concurrent edits are defined in `core/task-contract.md` and `guides/change-management-and-history.md`. Outcome labels and concise response order are defined in `core/task-lifecycle.md` and `guides/review-and-verification.md`.

Legacy single-file agent profiles remain under `agents/` as unregistered references; the runner uses only registered canonical bundles.
