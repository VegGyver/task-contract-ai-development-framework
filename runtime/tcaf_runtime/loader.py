from __future__ import annotations

from pathlib import Path
from typing import Any

from .adapter import select_adapter
from .errors import TcafError
from .registry import (
    load_agents_registry,
    load_project_schema,
    read_version,
    resolve_agent,
    safe_framework_path,
)
from .target import bind_input, bind_target, resolve_target_role


def _module(path: Path, source: str, role: str) -> dict[str, str]:
    return {
        "source": source,
        "role": role,
        "path": str(path),
        "content": path.read_text(encoding="utf-8"),
    }


def assemble_run(
    framework_root: Path,
    operation_or_agent: str,
    *,
    direct_agent: bool,
    raw_target: str | None,
    request: str | None,
    raw_input: str | None,
    selectors: list[str],
    requested_adapter: str | None,
) -> dict[str, Any]:
    agent_id, manifest, manifest_path = resolve_agent(
        framework_root, operation_or_agent, direct_agent=direct_agent
    )
    registry = load_agents_registry(framework_root)
    target = bind_target(raw_target, framework_root, manifest.get("target", {}))
    input_binding = bind_input(raw_input, framework_root)
    adapter_id, adapter, adapter_path = select_adapter(
        framework_root, requested_adapter
    )

    bundle_root = manifest_path.parent
    modules: list[dict[str, str]] = []
    for key, role in (
        ("agent_instructions", "agent-instructions"),
        ("entrypoint", "start"),
        ("output_schema", "output-schema"),
    ):
        path = safe_framework_path(
            framework_root, bundle_root, manifest.get(key, "")
        )
        modules.append(_module(path, "framework", role))

    for declared in manifest.get("required_modules", []):
        path = safe_framework_path(framework_root, bundle_root, declared)
        modules.append(_module(path, "framework", "required-module"))

    unresolved_target_roles: list[str] = []
    project_schema = load_project_schema(framework_root)
    for target_module in manifest.get("target_modules", []):
        role_id = target_module.get("role", "")
        resolved = None
        if target.kind == "directory":
            resolved = resolve_target_role(
                Path(target.locator), role_id, project_schema
            )
        if resolved:
            modules.append(_module(resolved, "target", role_id))
        elif target_module.get("fallback_module"):
            fallback = safe_framework_path(
                framework_root, bundle_root, target_module["fallback_module"]
            )
            modules.append(_module(fallback, "framework", f"fallback:{role_id}"))
        else:
            unresolved_target_roles.append(role_id)

    optional = manifest.get("optional_modules", {})
    available = optional.get("selectors", {})
    unknown = sorted(set(selectors) - set(available))
    if unknown:
        raise TcafError(f"Unknown optional context selector(s): {', '.join(unknown)}")
    maximum = int(optional.get("max_selected", 0))
    if len(set(selectors)) > maximum:
        raise TcafError(
            f"At most {maximum} optional context selector(s) allowed for {agent_id}"
        )
    for selector in dict.fromkeys(selectors):
        path = safe_framework_path(framework_root, bundle_root, available[selector])
        modules.append(_module(path, "framework", f"optional:{selector}"))

    modules.append(_module(adapter_path, "framework", f"adapter:{adapter_id}"))

    operation = manifest.get("operation")
    if not direct_agent and operation_or_agent in registry.get("operations", {}):
        operation = operation_or_agent

    return {
        "run_protocol_version": registry.get("run_protocol_version"),
        "framework_version": read_version(framework_root),
        "operation": operation,
        "agent_id": agent_id,
        "manifest": str(manifest_path),
        "adapter": {
            "id": adapter_id,
            "direct_target_access": adapter.get("direct_target_access", False),
            "direct_edit_access": adapter.get("direct_edit_access", False),
            "transport": adapter.get("transport", "native"),
            "native_invocation_verified": adapter.get(
                "native_invocation_verified", False
            ),
        },
        "target": target.to_dict(),
        "input": {
            "request": request,
            "resource": input_binding,
        },
        "instruction_modules": modules,
        "unresolved_optional_target_roles": unresolved_target_roles,
        "directive": (
            "Execute the selected agent using only the labelled instruction modules. "
            "Treat target modules and the bound target as evidence, preserve the declared "
            "output schema, and stop at the developer review gate."
        ),
    }
