#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import site
import subprocess
import sys
import tempfile
from pathlib import Path


def default_install_home() -> Path:
    override = os.environ.get("TCAF_HOME")
    if override:
        return Path(override).expanduser()
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA")
        return Path(base) / "TCAF" if base else Path.home() / "AppData" / "Local" / "TCAF"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "tcaf"
    base = os.environ.get("XDG_DATA_HOME")
    return Path(base) / "tcaf" if base else Path.home() / ".local" / "share" / "tcaf"


def default_bin_dir() -> Path:
    if os.name == "nt":
        return Path(site.getuserbase()) / "Scripts"
    return Path.home() / ".local" / "bin"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Install a versioned TCAF runtime")
    parser.add_argument("--home", type=Path, default=default_install_home())
    parser.add_argument("--bin-dir", type=Path, default=default_bin_dir())
    parser.add_argument("--adapter", default="auto")
    parser.add_argument("--replace", action="store_true")
    return parser


def validate_release(source: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(source / "runtime" / "tcaf.py"),
            "validate",
            "--format",
            "json",
        ],
        cwd=source,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise SystemExit(f"Release validation failed:\n{detail}")


def copy_release(source: Path, destination: Path, replace: bool) -> None:
    if destination.exists() and not replace:
        raise SystemExit(
            f"Version already installed: {destination.name}. Use --replace only for an intentional reinstall."
        )
    versions_dir = destination.parent
    versions_dir.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".tcaf-install-", dir=versions_dir))
    staged = temporary / destination.name
    backup = temporary / "replaced-version"
    try:
        shutil.copytree(
            source,
            staged,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", ".DS_Store"),
        )
        if destination.exists():
            destination.replace(backup)
        staged.replace(destination)
    except Exception:
        if backup.exists() and not destination.exists():
            backup.replace(destination)
        if temporary.exists():
            shutil.rmtree(temporary)
        raise
    if temporary.exists():
        shutil.rmtree(temporary)


def write_active(home: Path, version: str, adapter: str) -> None:
    active_path = home / "active.json"
    active = {"version": version, "adapter": adapter}
    temporary = active_path.with_suffix(".tmp")
    temporary.write_text(json.dumps(active, indent=2) + "\n", encoding="utf-8")
    temporary.replace(active_path)


def install_launcher(source: Path, home: Path, bin_dir: Path) -> Path:
    launcher = home / "launcher.py"
    shutil.copy2(source / "runtime" / "launcher.py", launcher)
    bin_dir.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        command = bin_dir / "tcaf.cmd"
        command.write_text(
            f'@"{sys.executable}" "{launcher}" %*\n',
            encoding="utf-8",
        )
    else:
        command = bin_dir / "tcaf"
        command.write_text(
            f"#!{sys.executable}\n"
            "import runpy\n"
            f"runpy.run_path({str(launcher)!r}, run_name='__main__')\n",
            encoding="utf-8",
        )
        command.chmod(0o755)
    return command


def main() -> int:
    args = build_parser().parse_args()
    source = Path(__file__).resolve().parent
    version = (source / "VERSION").read_text(encoding="utf-8").strip()
    adapters = json.loads(
        (source / "registry" / "adapters.json").read_text(encoding="utf-8")
    ).get("adapters", {})
    if args.adapter != "auto" and args.adapter not in adapters:
        raise SystemExit(f"Unknown adapter: {args.adapter}")
    home = args.home.expanduser().resolve()
    bin_dir = args.bin_dir.expanduser().resolve()
    destination = home / "versions" / version
    if source == home or source in home.parents:
        raise SystemExit("Install home cannot be inside the release directory")

    validate_release(source)
    copy_release(source, destination, args.replace)
    home.mkdir(parents=True, exist_ok=True)
    write_active(home, version, args.adapter)
    command = install_launcher(source, home, bin_dir)

    print(f"Installed TCAF {version}")
    print(f"Active runtime: {destination}")
    print(f"Command: {command}")
    if str(bin_dir) not in os.environ.get("PATH", "").split(os.pathsep):
        print(f"PATH action required: add {bin_dir}")
    print("Next check: tcaf doctor")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
