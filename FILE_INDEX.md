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
- `registry/applicability.json`
- `registry/adapters.json`
- `registry/project-schema.json`

## Agent bundles

- `agent-bundles/project-bootstrap/`
- `agent-bundles/existing-project-adoption/`
- `agent-bundles/task-contract-generator/`
- `agent-bundles/feature-planner/`

Each canonical bundle has a machine-authoritative `manifest.json`. `MANIFEST.md` is its human-readable mirror.

## Framework modules

- `core/`: principles, run/target/adapter protocols, contracts, lifecycle, validation evidence, schema and module loading
- `guides/`: optional specialist guidance
- `runtime/`: compact model-facing rules
- `runtime/cross-operation-rules-minimal.md`: compact rules applicable across operations
- `runtime/planning-rules-minimal.md`: compact planning applicability rules
- `templates/project-docs/planning-policy.md`: optional canonical planning policy role
- `templates/`: canonical project and task templates
- `adapters/`: tool-specific notes
- `examples/`: compact examples
- `tests/acceptance/`: repeatable framework acceptance tests

Active-task amendments and developer/concurrent edits are defined in `core/task-contract.md` and `guides/change-management-and-history.md`. Evidence-based validation and check reporting are defined in `core/validation-evidence.md`. Outcome labels and concise response order are defined in `core/task-lifecycle.md` and `guides/review-and-verification.md`.

## Framework development governance

- `governance/principles.json`
- `governance/CHANGE-CONTROL.md`
- `governance/changes/`: framework development change records
- `tests/governance/`

Governance files control development of TCAF itself and are not ordinary runtime instruction modules. The applicability registry maps operations to compact runtime behavioral context and is separate from framework-development governance.

Legacy single-file agent profiles remain under `agents/` as unregistered references; the runner uses only registered canonical bundles.
