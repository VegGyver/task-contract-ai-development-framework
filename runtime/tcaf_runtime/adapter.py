from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .errors import TcafError
from .registry import load_adapters_registry, safe_framework_path


def select_adapter(
    framework_root: Path, requested: str | None
) -> tuple[str, dict[str, Any], Path]:
    registry = load_adapters_registry(framework_root)
    adapters = registry.get("adapters", {})

    adapter_id = requested
    if not adapter_id or adapter_id == "auto":
        adapter_id = os.environ.get("TCAF_ADAPTER")
    if not adapter_id or adapter_id == "auto":
        keys = tuple(os.environ)
        for candidate_id, descriptor in adapters.items():
            prefixes = descriptor.get("detect_environment_prefixes", [])
            if prefixes and any(
                key.startswith(prefix) for key in keys for prefix in prefixes
            ):
                adapter_id = candidate_id
                break
    if not adapter_id or adapter_id == "auto":
        adapter_id = registry.get("default")

    if adapter_id not in adapters:
        raise TcafError(f"Unknown adapter: {adapter_id}")
    descriptor = adapters[adapter_id]
    instructions = safe_framework_path(
        framework_root, framework_root, descriptor.get("instructions", "")
    )
    return adapter_id, descriptor, instructions
