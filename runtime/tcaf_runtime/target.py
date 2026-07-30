from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .errors import TcafError


ARCHIVE_SUFFIXES = (".zip", ".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tbz2")
EXTERNAL_ROLE_PREFIX = "external:"


@dataclass(frozen=True)
class TargetBinding:
    locator: str
    kind: str
    exists: bool
    access_mode: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _is_archive(path: Path) -> bool:
    name = path.name.lower()
    return any(name.endswith(suffix) for suffix in ARCHIVE_SUFFIXES)


def _overlaps_framework(path: Path, framework_root: Path) -> bool:
    resolved = path.resolve()
    root = framework_root.resolve()
    if resolved == root:
        return True
    if resolved.is_dir() and resolved in root.parents:
        return True
    return False


def bind_target(
    raw_target: str | None,
    framework_root: Path,
    target_policy: dict[str, Any],
) -> TargetBinding:
    if raw_target and raw_target.startswith(("host:", "attachment:")):
        kind = "host-resource"
        binding = TargetBinding(raw_target, kind, True, "host")
    else:
        path = Path(raw_target or ".").expanduser().resolve()
        if _overlaps_framework(path, framework_root):
            raise TcafError("Target overlaps the installed framework")
        exists = path.exists()
        if not exists:
            kind = "planned-directory"
        elif path.is_dir():
            kind = "directory"
        elif _is_archive(path):
            kind = "archive"
        else:
            kind = "file"
        binding = TargetBinding(str(path), kind, exists, "local")

    if target_policy.get("must_exist") and not binding.exists:
        raise TcafError("This operation requires an existing target")
    allowed = target_policy.get("allowed_kinds", [])
    if binding.kind not in allowed:
        raise TcafError(
            f"Target kind '{binding.kind}' is not allowed; expected one of: {', '.join(allowed)}"
        )
    return binding


def bind_input(raw_input: str | None, framework_root: Path) -> dict[str, Any] | None:
    if not raw_input:
        return None
    if raw_input.startswith(("host:", "attachment:")):
        return {
            "locator": raw_input,
            "kind": "host-resource",
            "content": None,
        }

    path = Path(raw_input).expanduser().resolve()
    if not path.exists():
        raise TcafError(f"Input does not exist: {path}")
    if _overlaps_framework(path, framework_root):
        raise TcafError("Input cannot be read from the installed framework")

    kind = "directory" if path.is_dir() else ("archive" if _is_archive(path) else "file")
    content = None
    if kind == "file":
        if path.stat().st_size > 1_000_000:
            raise TcafError("Text input exceeds the 1 MB run-envelope limit")
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise TcafError("Input file is not UTF-8 text; provide it as a host resource") from exc
    return {"locator": str(path), "kind": kind, "content": content}


def parse_project_manifest(target_root: Path) -> dict[str, str]:
    manifest_path = target_root / "docs" / "method" / "project-manifest.md"
    if not manifest_path.is_file():
        return {}
    mappings: dict[str, str] = {}
    pattern = re.compile(r"^-\s+([^:]+):\s+`([^`]+)`\s*$")
    text = manifest_path.read_text(encoding="utf-8")
    section = re.search(
        r"(?ms)^## Role-to-path mappings\s*$\n(.*?)(?=^##\s|\Z)",
        text,
    )
    if not section:
        return mappings
    for line in section.group(1).splitlines():
        match = pattern.match(line.strip())
        if match:
            role = match.group(1).strip().casefold()
            if role in mappings:
                raise TcafError(
                    f"Duplicate project manifest role mapping: {match.group(1).strip()}"
                )
            mappings[role] = match.group(2).strip()
    return mappings


def is_external_role_mapping(value: str) -> bool:
    return value.casefold().startswith(EXTERNAL_ROLE_PREFIX)


def external_role_source(value: str) -> str:
    return value[len(EXTERNAL_ROLE_PREFIX) :].strip()


def resolve_target_role(
    target_root: Path,
    role_id: str,
    project_schema: dict[str, Any],
) -> Path | None:
    role = project_schema.get("roles", {}).get(role_id)
    if not role:
        raise TcafError(f"Unknown target document role: {role_id}")

    mappings = parse_project_manifest(target_root)
    declared = mappings.get(str(role.get("label", "")).casefold())
    relative = declared or role.get("default_path")
    if not relative:
        return None
    if is_external_role_mapping(relative):
        return None

    candidate = (target_root / relative).resolve()
    root = target_root.resolve()
    if candidate != root and root not in candidate.parents:
        raise TcafError(f"Target role path escapes the target: {relative}")
    return candidate if candidate.is_file() else None
