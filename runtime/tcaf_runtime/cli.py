from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from .adapter import select_adapter
from .errors import TcafError
from .formatters import format_json, format_run_markdown
from .loader import assemble_run
from .registry import load_agents_registry, read_version
from .validator import validate_framework, validate_target


def _framework_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _add_run_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--target", help="One project target; defaults to current directory")
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument("--request", help="Inline user request")
    input_group.add_argument("--input", help="One input file, directory, archive, or host resource")
    parser.add_argument(
        "--context",
        action="append",
        default=[],
        help="Public optional-context selector declared by the agent manifest",
    )
    parser.add_argument(
        "--adapter",
        default="auto",
        help="Adapter override for diagnostics; normal integrations select automatically",
    )
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tcaf", description="Task-Contract AI Development Framework runner"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for operation in ("bootstrap", "adopt", "task"):
        operation_parser = subparsers.add_parser(operation)
        _add_run_arguments(operation_parser)

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("agent_id")
    _add_run_arguments(run_parser)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--format", choices=("text", "json"), default="text")

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--target", help="Also validate canonical project documentation")
    validate_parser.add_argument("--format", choices=("text", "json"), default="text")

    doctor_parser = subparsers.add_parser("doctor")
    doctor_parser.add_argument("--format", choices=("text", "json"), default="text")

    version_parser = subparsers.add_parser("version")
    version_parser.add_argument("--format", choices=("text", "json"), default="text")

    versions_parser = subparsers.add_parser("versions")
    versions_parser.add_argument("--format", choices=("text", "json"), default="text")

    activate_parser = subparsers.add_parser("activate")
    activate_parser.add_argument("version")
    return parser


def _print_validation(result: dict[str, Any], output_format: str) -> None:
    if output_format == "json":
        print(format_json(result))
        return
    print("PASS" if result["valid"] else "FAIL")
    print(f"Errors: {result['errors']}  Warnings: {result['warnings']}")
    for issue in result["issues"]:
        suffix = f" [{issue['path']}]" if issue.get("path") else ""
        print(f"- {issue['level'].upper()} {issue['code']}: {issue['message']}{suffix}")


def _run_operation(args: argparse.Namespace, root: Path) -> int:
    if args.command == "task" and not args.request and not args.input:
        raise TcafError("The task operation requires --request or --input")
    direct_agent = args.command == "run"
    selected = args.agent_id if direct_agent else args.command
    envelope = assemble_run(
        root,
        selected,
        direct_agent=direct_agent,
        raw_target=args.target,
        request=args.request,
        raw_input=args.input,
        selectors=args.context,
        requested_adapter=args.adapter,
    )
    print(format_json(envelope) if args.format == "json" else format_run_markdown(envelope))
    return 0


def _installed_versions() -> dict[str, Any]:
    raw_home = os.environ.get("TCAF_INSTALL_HOME")
    if not raw_home:
        return {"installed": False, "active": None, "versions": []}
    home = Path(raw_home)
    active_path = home / "active.json"
    active = None
    if active_path.is_file():
        active = json.loads(active_path.read_text(encoding="utf-8")).get("version")
    versions_dir = home / "versions"
    versions = (
        sorted(path.name for path in versions_dir.iterdir() if path.is_dir())
        if versions_dir.is_dir()
        else []
    )
    return {"installed": True, "active": active, "versions": versions}


def _activate(version: str) -> int:
    raw_home = os.environ.get("TCAF_INSTALL_HOME")
    if not raw_home:
        raise TcafError("Version activation requires an installed TCAF launcher")
    home = Path(raw_home)
    version_root = home / "versions" / version
    if not (version_root / "VERSION").is_file():
        raise TcafError(f"Version is not installed: {version}")
    validation = validate_framework(version_root)
    if not validation["valid"]:
        raise TcafError(f"Version failed validation and was not activated: {version}")
    active_path = home / "active.json"
    current: dict[str, Any] = {}
    if active_path.is_file():
        current = json.loads(active_path.read_text(encoding="utf-8"))
    current["version"] = version
    temporary = active_path.with_suffix(".tmp")
    temporary.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
    temporary.replace(active_path)
    print(f"Activated TCAF {version}")
    return 0


def main(argv: list[str] | None = None) -> int:
    root = _framework_root()
    args = build_parser().parse_args(argv)
    try:
        if args.command in {"bootstrap", "adopt", "task", "run"}:
            return _run_operation(args, root)
        if args.command == "list":
            registry = load_agents_registry(root)
            if args.format == "json":
                print(format_json(registry))
            else:
                for operation, descriptor in registry["operations"].items():
                    print(f"{operation}: {descriptor['agent']}")
            return 0
        if args.command == "validate":
            framework_result = validate_framework(root)
            result: dict[str, Any] = {"framework": framework_result}
            valid = framework_result["valid"]
            if args.target:
                target_result = validate_target(root, Path(args.target))
                result["target"] = target_result
                valid = valid and target_result["valid"]
            result["valid"] = valid
            result["errors"] = sum(
                item["errors"]
                for item in result.values()
                if isinstance(item, dict) and "errors" in item
            )
            result["warnings"] = sum(
                item["warnings"]
                for item in result.values()
                if isinstance(item, dict) and "warnings" in item
            )
            result["issues"] = [
                issue
                for item in result.values()
                if isinstance(item, dict)
                for issue in item.get("issues", [])
            ]
            _print_validation(result, args.format)
            return 0 if valid else 1
        if args.command == "doctor":
            validation = validate_framework(root)
            adapter_id, _, _ = select_adapter(root, "auto")
            result = {
                "valid": validation["valid"],
                "framework_version": read_version(root),
                "framework_root": str(root),
                "adapter": adapter_id,
                "installation": _installed_versions(),
                "errors": validation["errors"],
                "warnings": validation["warnings"],
                "issues": validation["issues"],
            }
            _print_validation(result, args.format)
            return 0 if result["valid"] else 1
        if args.command == "version":
            value = read_version(root)
            print(format_json({"version": value}) if args.format == "json" else value)
            return 0
        if args.command == "versions":
            value = _installed_versions()
            if args.format == "json":
                print(format_json(value))
            else:
                print(f"Active: {value['active'] or 'not installed'}")
                for installed in value["versions"]:
                    marker = "*" if installed == value["active"] else " "
                    print(f"{marker} {installed}")
            return 0
        if args.command == "activate":
            return _activate(args.version)
    except TcafError as exc:
        print(f"TCAF error: {exc}", file=sys.stderr)
        return 2
    return 0
