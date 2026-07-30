#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import runpy
import sys
from pathlib import Path


def main() -> None:
    install_home = Path(__file__).resolve().parent
    active_path = install_home / "active.json"
    if not active_path.is_file():
        raise SystemExit("TCAF installation has no active version")
    active = json.loads(active_path.read_text(encoding="utf-8"))
    version = active.get("version")
    runtime = install_home / "versions" / str(version) / "runtime" / "tcaf.py"
    if not runtime.is_file():
        raise SystemExit(f"TCAF active runtime is missing: {version}")
    os.environ["TCAF_INSTALL_HOME"] = str(install_home)
    configured_adapter = active.get("adapter")
    if configured_adapter and configured_adapter != "auto":
        os.environ.setdefault("TCAF_ADAPTER", configured_adapter)
    sys.path.insert(0, str(runtime.parent))
    runpy.run_path(str(runtime), run_name="__main__")


if __name__ == "__main__":
    main()
