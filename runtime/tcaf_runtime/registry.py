from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .errors import TcafError


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise TcafError(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise TcafError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise TcafError(f"Expected a JSON object in {path}")
    return value


def read_version(framework_root: Path) -> str:
    try:
        version = (framework_root / "VERSION").read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise TcafError("Missing VERSION file") from exc
    if not version:
        raise TcafError("VERSION is empty")
    return version


def load_agents_registry(framework_root: Path) -> dict[str, Any]:
    return load_json(framework_root / "registry" / "agents.json")


def load_adapters_registry(framework_root: Path) -> dict[str, Any]:
    return load_json(framework_root / "registry" / "adapters.json")


def load_project_schema(framework_root: Path) -> dict[str, Any]:
    return load_json(framework_root / "registry" / "project-schema.json")


def safe_framework_path(framework_root: Path, base: Path, declared_path: str) -> Path:
    candidate = (base / declared_path).resolve()
    root = framework_root.resolve()
    if candidate != root and root not in candidate.parents:
        raise TcafError(f"Framework module escapes installation root: {declared_path}")
    if not candidate.is_file():
        raise TcafError(f"Declared framework module is missing: {declared_path}")
    return candidate


def resolve_agent(
    framework_root: Path, operation_or_agent: str, direct_agent: bool = False
) -> tuple[str, dict[str, Any], Path]:
    registry = load_agents_registry(framework_root)
    agents = registry.get("agents", {})
    operations = registry.get("operations", {})

    if direct_agent:
        agent_id = operation_or_agent
    elif operation_or_agent in operations:
        agent_id = operations[operation_or_agent].get("agent")
    else:
        agent_id = ""
        for operation in operations.values():
            if operation_or_agent in operation.get("aliases", []):
                agent_id = operation.get("agent", "")
                break

    if not agent_id or agent_id not in agents:
        kind = "agent" if direct_agent else "operation"
        raise TcafError(f"Unknown {kind}: {operation_or_agent}")

    manifest_path = safe_framework_path(
        framework_root, framework_root, agents[agent_id].get("manifest", "")
    )
    manifest = load_json(manifest_path)
    if manifest.get("agent_id") != agent_id:
        raise TcafError(
            f"Registry/manifest agent mismatch: {agent_id} != {manifest.get('agent_id')}"
        )
    return agent_id, manifest, manifest_path
