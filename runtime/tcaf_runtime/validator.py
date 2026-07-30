from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .registry import (
    load_adapters_registry,
    load_agents_registry,
    load_json,
    load_project_schema,
    read_version,
    safe_framework_path,
)
from .target import (
    external_role_source,
    is_external_role_mapping,
    parse_project_manifest,
)


@dataclass(frozen=True)
class Issue:
    level: str
    code: str
    message: str
    path: str | None = None


def _issue(
    issues: list[Issue],
    level: str,
    code: str,
    message: str,
    path: Path | None = None,
) -> None:
    issues.append(Issue(level, code, message, str(path) if path else None))


def validate_framework(framework_root: Path) -> dict[str, Any]:
    root = framework_root.resolve()
    issues: list[Issue] = []
    try:
        version = read_version(root)
        agents_registry = load_agents_registry(root)
        adapters_registry = load_adapters_registry(root)
        project_schema = load_project_schema(root)
    except Exception as exc:
        _issue(issues, "error", "registry-load", str(exc))
        return _result(issues)

    if agents_registry.get("framework_version") != version:
        _issue(
            issues,
            "error",
            "version-registry-mismatch",
            "VERSION and registry/agents.json framework_version differ",
        )

    readme = root / "README.md"
    if not readme.is_file() or f"Version: **v{version}" not in readme.read_text(
        encoding="utf-8"
    ):
        _issue(
            issues,
            "error",
            "version-readme-mismatch",
            "README does not declare the VERSION value",
            readme,
        )
    changelog = root / "CHANGELOG.md"
    if not changelog.is_file() or f"v{version}" not in changelog.read_text(
        encoding="utf-8"
    ):
        _issue(
            issues,
            "error",
            "version-changelog-mismatch",
            "CHANGELOG does not contain the VERSION value",
            changelog,
        )

    agents = agents_registry.get("agents", {})
    operations = agents_registry.get("operations", {})
    seen_aliases: set[str] = set(operations)
    for operation_id, descriptor in operations.items():
        agent_id = descriptor.get("agent")
        if agent_id not in agents:
            _issue(
                issues,
                "error",
                "unknown-operation-agent",
                f"Operation {operation_id} references unknown agent {agent_id}",
            )
        for alias in descriptor.get("aliases", []):
            if alias in seen_aliases:
                _issue(
                    issues,
                    "error",
                    "duplicate-operation-alias",
                    f"Operation alias is duplicated: {alias}",
                )
            seen_aliases.add(alias)

    registered_manifest_paths: set[Path] = set()
    for agent_id, descriptor in agents.items():
        try:
            manifest_path = safe_framework_path(
                root, root, descriptor.get("manifest", "")
            )
            registered_manifest_paths.add(manifest_path)
            manifest = load_json(manifest_path)
            _validate_manifest(
                root, agent_id, manifest, manifest_path, operations, project_schema, issues
            )
        except Exception as exc:
            _issue(
                issues,
                "error",
                "manifest-load",
                f"{agent_id}: {exc}",
            )

    for manifest_path in sorted((root / "agent-bundles").glob("*/manifest.json")):
        if manifest_path.resolve() not in registered_manifest_paths:
            _issue(
                issues,
                "error",
                "unregistered-manifest",
                "Agent manifest is not registered",
                manifest_path,
            )

    adapters = adapters_registry.get("adapters", {})
    default_adapter = adapters_registry.get("default")
    if default_adapter not in adapters:
        _issue(
            issues,
            "error",
            "unknown-default-adapter",
            f"Default adapter is not registered: {default_adapter}",
        )
    for adapter_id, descriptor in adapters.items():
        try:
            safe_framework_path(root, root, descriptor.get("instructions", ""))
        except Exception as exc:
            _issue(
                issues,
                "error",
                "adapter-instructions",
                f"{adapter_id}: {exc}",
            )
        if not descriptor.get("transport"):
            _issue(
                issues,
                "error",
                "adapter-transport",
                f"{adapter_id}: transport is required",
            )
        if not isinstance(descriptor.get("native_invocation_verified"), bool):
            _issue(
                issues,
                "error",
                "adapter-native-verification",
                f"{adapter_id}: native_invocation_verified must be boolean",
            )

    for role_id, role in project_schema.get("roles", {}).items():
        try:
            template = safe_framework_path(root, root, role.get("template", ""))
            text = template.read_text(encoding="utf-8")
            for heading in role.get("required_headings", []):
                if heading not in text:
                    _issue(
                        issues,
                        "error",
                        "template-heading",
                        f"{role_id} template is missing heading: {heading}",
                        template,
                    )
        except Exception as exc:
            _issue(
                issues,
                "error",
                "project-schema-template",
                f"{role_id}: {exc}",
            )

    return _result(issues)


def _validate_manifest(
    root: Path,
    agent_id: str,
    manifest: dict[str, Any],
    manifest_path: Path,
    operations: dict[str, Any],
    project_schema: dict[str, Any],
    issues: list[Issue],
) -> None:
    required_keys = {
        "schema_version",
        "agent_id",
        "operation",
        "agent_instructions",
        "entrypoint",
        "output_schema",
        "required_modules",
        "target",
        "target_modules",
        "optional_modules",
    }
    missing = sorted(required_keys - set(manifest))
    if missing:
        _issue(
            issues,
            "error",
            "manifest-fields",
            f"{agent_id} manifest missing: {', '.join(missing)}",
            manifest_path,
        )
        return
    if manifest.get("agent_id") != agent_id:
        _issue(
            issues,
            "error",
            "manifest-agent-mismatch",
            f"Expected agent_id {agent_id}",
            manifest_path,
        )
    operation = manifest.get("operation")
    if operations.get(operation, {}).get("agent") != agent_id:
        _issue(
            issues,
            "error",
            "manifest-operation-mismatch",
            f"Operation {operation} does not resolve to {agent_id}",
            manifest_path,
        )

    bundle = manifest_path.parent
    declared: list[str] = []
    for key in ("agent_instructions", "entrypoint", "output_schema"):
        declared.append(manifest.get(key, ""))
    declared.extend(manifest.get("required_modules", []))
    declared.extend(
        manifest.get("optional_modules", {}).get("selectors", {}).values()
    )
    declared.extend(
        item.get("fallback_module")
        for item in manifest.get("target_modules", [])
        if item.get("fallback_module")
    )
    duplicates = sorted({path for path in declared if declared.count(path) > 1})
    if duplicates:
        _issue(
            issues,
            "error",
            "duplicate-manifest-module",
            f"Duplicate module declarations: {', '.join(duplicates)}",
            manifest_path,
        )
    for declared_path in declared:
        try:
            safe_framework_path(root, bundle, declared_path)
        except Exception as exc:
            _issue(
                issues,
                "error",
                "manifest-module",
                f"{agent_id}: {exc}",
                manifest_path,
            )

    optional = manifest.get("optional_modules", {})
    if int(optional.get("max_selected", -1)) < 0:
        _issue(
            issues,
            "error",
            "optional-limit",
            "max_selected must be zero or greater",
            manifest_path,
        )
    for role in manifest.get("target_modules", []):
        if role.get("role") not in project_schema.get("roles", {}):
            _issue(
                issues,
                "error",
                "unknown-target-role",
                f"Unknown target role: {role.get('role')}",
                manifest_path,
            )


def validate_target(framework_root: Path, target_root: Path) -> dict[str, Any]:
    issues: list[Issue] = []
    target = target_root.resolve()
    if not target.is_dir():
        _issue(
            issues,
            "error",
            "target-not-directory",
            "Project documentation validation requires a directory target",
            target,
        )
        return _result(issues)

    schema = load_project_schema(framework_root)
    try:
        mappings = parse_project_manifest(target)
    except Exception as exc:
        _issue(
            issues,
            "error",
            "project-manifest-mapping",
            str(exc),
            target / "docs" / "method" / "project-manifest.md",
        )
        return _result(issues)
    for role_id, role in schema.get("roles", {}).items():
        if role_id == "project_manifest" and not mappings:
            continue
        declared = mappings.get(str(role.get("label", "")).casefold())
        if declared and is_external_role_mapping(declared):
            if not role.get("allow_external_source"):
                _issue(
                    issues,
                    "error",
                    "external-project-role-not-allowed",
                    f"{role_id} cannot be mapped to an external source",
                )
                continue
            if not external_role_source(declared):
                _issue(
                    issues,
                    "error",
                    "missing-external-project-source",
                    f"{role_id} external mapping has no source",
                )
                continue
            default_path = (target / role.get("default_path", "")).resolve()
            if default_path.is_file():
                _issue(
                    issues,
                    "error",
                    "parallel-project-role-source",
                    (
                        f"{role_id} maps to {declared}, but the default repository "
                        "document also exists"
                    ),
                    default_path,
                )
            continue
        relative = declared
        relative = relative or role.get("default_path")
        path = (target / relative).resolve()
        if path != target and target not in path.parents:
            _issue(
                issues,
                "error",
                "target-path-escape",
                f"{role_id} mapping escapes the target: {relative}",
                path,
            )
            continue
        if not path.is_file():
            if role.get("required"):
                _issue(
                    issues,
                    "error",
                    "missing-project-role",
                    f"Missing required project role {role_id}: {relative}",
                    path,
                )
            continue
        text = path.read_text(encoding="utf-8")
        positions = []
        for heading in role.get("required_headings", []):
            match = re.search(rf"(?m)^{re.escape(heading)}\s*$", text)
            if not match:
                _issue(
                    issues,
                    "error",
                    "missing-project-heading",
                    f"{role_id} is missing heading: {heading}",
                    path,
                )
            else:
                positions.append(match.start())
        if positions != sorted(positions):
            _issue(
                issues,
                "error",
                "project-heading-order",
                f"{role_id} headings are not in canonical order",
                path,
            )
        if role_id == "project_brief":
            _validate_open_decisions(text, path, issues)
    return _result(issues)


def _validate_open_decisions(
    text: str,
    path: Path,
    issues: list[Issue],
) -> None:
    section = re.search(
        r"(?ms)^## Open decisions\s*$\n(.*?)(?=^##\s|\Z)",
        text,
    )
    if not section or not section.group(1).strip():
        _issue(
            issues,
            "error",
            "empty-open-decisions",
            "Project brief must record open decisions or an explicit None marker",
            path,
        )
        return

    bullets = re.findall(r"(?m)^\s*[-*+]\s+(.+?)\s*$", section.group(1))
    normalized = [re.sub(r"\s+", " ", item).strip().casefold() for item in bullets]
    duplicates = sorted({item for item in normalized if normalized.count(item) > 1})
    if duplicates:
        _issue(
            issues,
            "error",
            "duplicate-open-decision",
            "Project brief contains a duplicate open decision",
            path,
        )


def _result(issues: list[Issue]) -> dict[str, Any]:
    errors = sum(issue.level == "error" for issue in issues)
    warnings = sum(issue.level == "warning" for issue in issues)
    return {
        "valid": errors == 0,
        "errors": errors,
        "warnings": warnings,
        "issues": [asdict(issue) for issue in issues],
    }
