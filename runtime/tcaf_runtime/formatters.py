from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def format_json(value: dict[str, Any]) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False)


def format_run_markdown(envelope: dict[str, Any]) -> str:
    target = envelope["target"]
    adapter = envelope["adapter"]
    lines = [
        "# TCAF Run Envelope",
        "",
        f"- Protocol: `{envelope['run_protocol_version']}`",
        f"- Framework: `{envelope['framework_version']}`",
        f"- Operation: `{envelope['operation']}`",
        f"- Agent: `{envelope['agent_id']}`",
        f"- Adapter: `{adapter['id']}`",
        f"- Adapter transport: `{adapter['transport']}`",
        (
            "- Native invocation verified: "
            f"`{'yes' if adapter['native_invocation_verified'] else 'no'}`"
        ),
        f"- Target: `{target['locator']}`",
        f"- Target kind: `{target['kind']}`",
    ]
    guidance = envelope.get("guidance")
    if guidance:
        lines.extend(
            [
                f"- Phase: {guidance['phase']}",
                f"- Next action: {guidance['next_action']}",
            ]
        )
    lines.extend(["", "## Bound input", ""])
    request = envelope["input"].get("request")
    resource = envelope["input"].get("resource")
    lines.append(request if request else "Inline request: not provided.")
    if resource:
        lines.extend(["", f"Input resource: `{resource['locator']}` ({resource['kind']})"])
        if resource.get("content") is not None:
            lines.extend(
                [
                    "",
                    "<!-- TCAF INPUT BEGIN -->",
                    resource["content"],
                    "<!-- TCAF INPUT END -->",
                ]
            )

    if envelope.get("operation") == "task":
        lines.extend(["", "## Contract provenance", ""])
        target_roles = {
            module["role"]: module
            for module in envelope["instruction_modules"]
            if module["source"] == "target"
        }
        canonical_roles = {
            "project_brief",
            "architecture_overview",
            "backlog",
            "project_rules",
            "ai_workflow",
            "capability_baseline",
            "task_naming",
        }
        target_path = Path(target["locator"])
        source_paths = [
            relative
            for relative in (
                "docs/PROJECT_CONTEXT.md",
                "docs/PROJECT_PLAN.md",
            )
            if (target_path / relative).is_file()
        ]
        if (target_path / "docs" / "architecture").is_dir():
            source_paths.append("docs/architecture/")

        if "backlog" in target_roles:
            lines.append("Origin: Canonical backlog / canonical task state")
        else:
            lines.append("Origin: preserved/external/direct-request fallback evidence")
        if canonical_roles.intersection(target_roles):
            lines.append("Source of truth: canonical TCAF project documents")
        else:
            lines.append("Source of truth: available fallback/project evidence")
        if source_paths:
            lines.append(
                "Supporting evidence: preserved/free-form source documents "
                f"({', '.join(source_paths)})"
            )

    lines.extend(["", "## Instruction surface", ""])
    for module in envelope["instruction_modules"]:
        lines.extend(
            [
                f"### {module['role']}",
                "",
                f"Source: `{module['source']}` — `{module['path']}`",
                "",
                f"<!-- TCAF MODULE BEGIN {module['role']} -->",
                module["content"],
                f"<!-- TCAF MODULE END {module['role']} -->",
                "",
            ]
        )

    unresolved = envelope.get("unresolved_optional_target_roles", [])
    if unresolved:
        lines.extend(
            [
                "## Unresolved optional target roles",
                "",
                ", ".join(f"`{role}`" for role in unresolved),
                "",
            ]
        )
    lines.extend(["## Run directive", "", envelope["directive"]])
    return "\n".join(lines).rstrip() + "\n"
