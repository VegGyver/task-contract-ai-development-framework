# Module Loading Guide

Use the minimum context required. Do not load the complete framework for ordinary tasks.

## Ordinary task

- `runtime/global-rules-minimal.md`
- project compact rules
- current task contract

## Agent operation

Invoke one public operation through the Universal Runner. `registry/agents.json` selects the agent and its machine-readable `manifest.json` is authoritative.

The agent must separate:

- instruction files loaded from the framework
- target-project files inspected as evidence

Do not browse framework files outside the manifest. Never treat framework content as target-project evidence.

`MANIFEST.md` is a human-readable mirror only. Validation fails when the registry or machine manifest references a missing or escaping module.

## Specialist modules

Load one only when needed:

| Scenario | Add |
|---|---|
| Task decomposition | `guides/task-decomposition.md` |
| Capability uncertainty | `guides/architecture-capability-baseline.md` |
| Status/history/naming | `guides/change-management-and-history.md` |
| Review/check dispute | `guides/review-and-verification.md` |
| Team/multi-agent | `guides/team-and-multi-agent.md` |
| Hotfix/migration/security/performance | `guides/advanced-scenarios.md` |
| Tool behavior | one adapter |
| Implementation-source uncertainty | `core/implementation-source-hierarchy.md` |

Never load all guides, examples or unrelated agents by default.
