from __future__ import annotations

from typing import Final


# Public workflow guidance is runtime metadata.  It is deliberately separate
# from instruction modules so it is never presented to an agent as policy.
OPERATION_GUIDANCE: Final[dict[str, dict[str, str]]] = {
    "bootstrap": {
        "summary": "Start or normalize a new project from requirements, documents, or source material.",
        "description": (
            "Start or normalize a new project from requirements, arbitrary documents, "
            "or source material when there is no implemented project to adopt. "
            "Use --request or --input to bind optional starting evidence."
        ),
        "phase": "Bootstrap normalization",
        "next_action": (
            "Submit this Run Envelope to the selected integration or agent workflow, "
            "then review its proposed normalized project state at the developer review gate."
        ),
    },
    "adopt": {
        "summary": "Normalize an existing implemented project while preserving its code and history.",
        "description": (
            "Normalize an existing implemented repository or project into TCAF canonical "
            "project state while preserving existing code and history. Use this instead of "
            "bootstrap when an implemented project already exists."
        ),
        "phase": "Existing-project adoption",
        "next_action": (
            "Submit this Run Envelope to the selected integration or agent workflow, "
            "then review its proposed canonical normalization at the developer review gate."
        ),
    },
    "plan": {
        "summary": "Turn a requested feature or change into a reviewable, dependency-aware task plan.",
        "description": (
            "Turn a feature, specification, or change request into a reviewable dependency-aware "
            "task plan against existing project state. Requires --request or --input."
        ),
        "phase": "Feature planning",
        "next_action": (
            "Submit this Run Envelope to the selected integration or agent workflow, "
            "then review the proposed task plan at the developer review gate before approval."
        ),
    },
    "task": {
        "summary": "Generate one bounded Task Contract for a specific requested unit of work.",
        "description": (
            "Generate one bounded Task Contract from approved or current project state and a "
            "specific requested unit of work. Requires --request or --input."
        ),
        "phase": "Task-contract generation",
        "next_action": (
            "Submit this Run Envelope to the selected integration or agent workflow, "
            "then review the proposed Task Contract at the developer review gate before approval."
        ),
    },
    "sync": {
        "summary": "Re-read project evidence, detect drift, and propose approval-gated reconciliation.",
        "description": (
            "Re-read current repository or project evidence after manual changes or new specification "
            "evidence, detect drift and affected planned work, and propose approval-gated reconciliation. "
            "Use --request or --input to bind optional new evidence."
        ),
        "phase": "Project synchronization",
        "next_action": (
            "Submit this Run Envelope to the selected integration or agent workflow, "
            "then review the proposed drift reconciliation at the developer review gate before approval."
        ),
    },
}


def operation_guidance(operation: str) -> dict[str, str] | None:
    """Return deterministic public guidance for a workflow operation."""
    return OPERATION_GUIDANCE.get(operation)
