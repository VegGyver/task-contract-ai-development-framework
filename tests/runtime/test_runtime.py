from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


FRAMEWORK_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(FRAMEWORK_ROOT / "runtime"))

from tcaf_runtime.adapter import select_adapter
from tcaf_runtime.errors import TcafError
from tcaf_runtime.loader import assemble_run
from tcaf_runtime.registry import load_project_schema
from tcaf_runtime.validator import validate_framework, validate_target


class RuntimeTests(unittest.TestCase):
    def _canonical_project(self, target: Path) -> None:
        schema = load_project_schema(FRAMEWORK_ROOT)
        for role in schema["roles"].values():
            if not role["required"]:
                continue
            destination = target / role["default_path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(FRAMEWORK_ROOT / role["template"], destination)

    def _external_backlog_project(self, target: Path) -> None:
        schema = load_project_schema(FRAMEWORK_ROOT)
        for role_id, role in schema["roles"].items():
            if not role["required"] or role_id == "backlog":
                continue
            destination = target / role["default_path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(FRAMEWORK_ROOT / role["template"], destination)
        manifest = target / schema["roles"]["project_manifest"]["default_path"]
        manifest.parent.mkdir(parents=True, exist_ok=True)
        text = (FRAMEWORK_ROOT / schema["roles"]["project_manifest"]["template"]).read_text(
            encoding="utf-8"
        )
        manifest.write_text(
            text.replace(
                "- Backlog: `docs/backlog.md`",
                "- Backlog: `external:GitHub Issues`",
            ),
            encoding="utf-8",
        )

    def test_framework_is_coherent(self) -> None:
        result = validate_framework(FRAMEWORK_ROOT)
        self.assertTrue(result["valid"], result["issues"])

    def test_validator_detects_version_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "framework"
            shutil.copytree(FRAMEWORK_ROOT, copied)
            (copied / "VERSION").write_text("9.9.9\n", encoding="utf-8")
            result = validate_framework(copied)
        self.assertFalse(result["valid"])
        self.assertIn(
            "version-registry-mismatch",
            {issue["code"] for issue in result["issues"]},
        )

    def test_validator_detects_missing_manifest_module(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "framework"
            shutil.copytree(FRAMEWORK_ROOT, copied)
            manifest_path = (
                copied
                / "agent-bundles"
                / "task-contract-generator"
                / "manifest.json"
            )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["required_modules"].append("../../core/does-not-exist.md")
            manifest_path.write_text(
                json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
            )
            result = validate_framework(copied)
        self.assertFalse(result["valid"])
        self.assertIn("manifest-module", {issue["code"] for issue in result["issues"]})

    def test_project_schema_validation_passes_canonical_templates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._canonical_project(target)
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertTrue(result["valid"], result["issues"])

    def test_project_schema_validation_detects_missing_heading(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._canonical_project(target)
            brief = target / "docs" / "project-brief.md"
            brief.write_text(
                brief.read_text(encoding="utf-8").replace("## Goal\n", ""),
                encoding="utf-8",
            )
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertFalse(result["valid"])
        self.assertIn(
            "missing-project-heading", {issue["code"] for issue in result["issues"]}
        )

    def test_project_schema_accepts_external_backlog(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._external_backlog_project(target)
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertTrue(result["valid"], result["issues"])

    def test_project_schema_accepts_direct_developer_requests(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._external_backlog_project(target)
            manifest = target / "docs" / "method" / "project-manifest.md"
            manifest.write_text(
                manifest.read_text(encoding="utf-8").replace(
                    "external:GitHub Issues",
                    "external:Developer requests",
                ),
                encoding="utf-8",
            )
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertTrue(result["valid"], result["issues"])

    def test_project_schema_rejects_parallel_external_backlog(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._external_backlog_project(target)
            backlog = target / "docs" / "backlog.md"
            shutil.copy2(
                FRAMEWORK_ROOT / "templates" / "project-docs" / "backlog.md",
                backlog,
            )
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertFalse(result["valid"])
        self.assertIn(
            "parallel-project-role-source",
            {issue["code"] for issue in result["issues"]},
        )

    def test_project_schema_rejects_unapproved_external_role(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._external_backlog_project(target)
            manifest = target / "docs" / "method" / "project-manifest.md"
            manifest.write_text(
                manifest.read_text(encoding="utf-8").replace(
                    "- Project brief: `docs/project-brief.md`",
                    "- Project brief: `external:Notion`",
                ),
                encoding="utf-8",
            )
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertFalse(result["valid"])
        self.assertIn(
            "external-project-role-not-allowed",
            {issue["code"] for issue in result["issues"]},
        )

    def test_project_schema_rejects_duplicate_open_decision(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._canonical_project(target)
            brief = target / "docs" / "project-brief.md"
            brief.write_text(
                brief.read_text(encoding="utf-8").replace(
                    "- None",
                    (
                        "- Deployment provider: `To be decided`.\n"
                        "* Deployment provider: `To be decided`."
                    ),
                ),
                encoding="utf-8",
            )
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertFalse(result["valid"])
        self.assertIn(
            "duplicate-open-decision",
            {issue["code"] for issue in result["issues"]},
        )

    def test_project_schema_rejects_empty_open_decisions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._canonical_project(target)
            brief = target / "docs" / "project-brief.md"
            brief.write_text(
                brief.read_text(encoding="utf-8").replace("- None\n", ""),
                encoding="utf-8",
            )
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertFalse(result["valid"])
        self.assertIn(
            "empty-open-decisions",
            {issue["code"] for issue in result["issues"]},
        )

    def test_project_schema_rejects_duplicate_manifest_mapping(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._external_backlog_project(target)
            manifest = target / "docs" / "method" / "project-manifest.md"
            manifest.write_text(
                manifest.read_text(encoding="utf-8").replace(
                    "- Backlog: `external:GitHub Issues`",
                    (
                        "- Backlog: `external:GitHub Issues`\n"
                        "- Backlog: `external:GitHub Issues`"
                    ),
                ),
                encoding="utf-8",
            )
            result = validate_target(FRAMEWORK_ROOT, target)
        self.assertFalse(result["valid"])
        self.assertIn(
            "project-manifest-mapping",
            {issue["code"] for issue in result["issues"]},
        )

    def test_bootstrap_accepts_planned_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            planned = Path(temporary) / "new-project"
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "bootstrap",
                direct_agent=False,
                raw_target=str(planned),
                request="Create a small service.",
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )
        self.assertEqual(envelope["target"]["kind"], "planned-directory")
        self.assertEqual(envelope["agent_id"], "project-bootstrap")
        instructions = "\n".join(
            module["content"] for module in envelope["instruction_modules"]
        )
        self.assertIn("complete or partial analysis", instructions)
        self.assertIn("external:Developer requests", instructions)

    def test_host_resource_uses_same_target_contract(self) -> None:
        envelope = assemble_run(
            FRAMEWORK_ROOT,
            "adopt",
            direct_agent=False,
            raw_target="attachment:project.zip",
            request=None,
            raw_input=None,
            selectors=[],
            requested_adapter="generic-chat",
        )
        self.assertEqual(envelope["target"]["kind"], "host-resource")
        self.assertEqual(envelope["adapter"]["id"], "generic-chat")

    def test_configured_adapter_precedes_environment_detection(self) -> None:
        with mock.patch.dict(os.environ, {"TCAF_ADAPTER": "cline"}, clear=False):
            adapter_id, _, _ = select_adapter(FRAMEWORK_ROOT, "auto")
        self.assertEqual(adapter_id, "cline")

    def test_cline_envelope_declares_manual_transport(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "bootstrap",
                direct_agent=False,
                raw_target=str(Path(temporary) / "new-project"),
                request="Create project documentation.",
                raw_input=None,
                selectors=[],
                requested_adapter="cline",
            )
        self.assertEqual(envelope["adapter"]["transport"], "manual-envelope")
        self.assertFalse(envelope["adapter"]["native_invocation_verified"])

    def test_codex_envelope_declares_verified_native_transport(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "task",
                direct_agent=False,
                raw_target=temporary,
                request="Inspect one behavior.",
                raw_input=None,
                selectors=[],
                requested_adapter="codex",
            )
        self.assertEqual(envelope["adapter"]["transport"], "native")
        self.assertTrue(envelope["adapter"]["native_invocation_verified"])

    def test_task_envelope_includes_developer_run_scope_rules(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "task",
                direct_agent=False,
                raw_target=temporary,
                request="Change one behavior.",
                raw_input=None,
                selectors=[],
                requested_adapter="codex",
            )
        instructions = "\n".join(
            module["content"] for module in envelope["instruction_modules"]
        )
        self.assertIn("wait for developer-reported results", instructions)
        self.assertIn("never execute, infer or invent results", instructions)
        self.assertIn("Describe each command by its effective scope", instructions)
        self.assertIn(
            "existing script and runner semantics establish selectivity",
            instructions,
        )
        self.assertIn("Task Contract amendment", instructions)
        self.assertIn("Preserve compatible manual or concurrent changes", instructions)
        self.assertIn("Begin operational responses with outcome", instructions)

    def test_cline_adoption_envelope_includes_safe_inspection_rules(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "adopt",
                direct_agent=False,
                raw_target=temporary,
                request=None,
                raw_input=None,
                selectors=[],
                requested_adapter="cline",
            )
        instructions = "\n".join(
            module["content"] for module in envelope["instruction_modules"]
        )
        self.assertIn("confirm a path exists before reading it", instructions)
        self.assertIn("dot-prefixed project config", instructions)
        self.assertIn("explicitly legacy exception as `Localized`", instructions)

    def test_adoption_requires_existing_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "missing"
            with self.assertRaisesRegex(TcafError, "requires an existing target"):
                assemble_run(
                    FRAMEWORK_ROOT,
                    "adopt",
                    direct_agent=False,
                    raw_target=str(missing),
                    request=None,
                    raw_input=None,
                    selectors=[],
                    requested_adapter="generic-cli",
                )

    def test_target_cannot_contain_framework(self) -> None:
        with self.assertRaisesRegex(TcafError, "overlaps"):
            assemble_run(
                FRAMEWORK_ROOT,
                "adopt",
                direct_agent=False,
                raw_target=str(FRAMEWORK_ROOT.parent),
                request=None,
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )

    def test_task_discovers_mapped_project_modules(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            method = target / "project-docs"
            method.mkdir()
            (target / "docs" / "method").mkdir(parents=True)
            (target / "docs" / "method" / "project-manifest.md").write_text(
                "# Project Documentation Manifest\n\n"
                "## Role-to-path mappings\n\n"
                "- Project rules: `project-docs/rules.md`\n"
                "- Task naming: `project-docs/naming.md`\n"
                "- Capability baseline: `project-docs/capabilities.md`\n",
                encoding="utf-8",
            )
            for name in ("rules.md", "naming.md", "capabilities.md"):
                (method / name).write_text(f"# {name}\n", encoding="utf-8")

            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "task",
                direct_agent=False,
                raw_target=str(target),
                request="Change one label.",
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )

        roles = {
            item["role"]
            for item in envelope["instruction_modules"]
            if item["source"] == "target"
        }
        self.assertEqual(
            roles, {"project_rules", "task_naming", "capability_baseline"}
        )
        self.assertEqual(envelope["unresolved_optional_target_roles"], [])

    def test_task_uses_standalone_rules_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "task",
                direct_agent=False,
                raw_target=temporary,
                request="Inspect the current behavior.",
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )
        roles = {item["role"] for item in envelope["instruction_modules"]}
        self.assertIn("fallback:project_rules", roles)
        self.assertEqual(
            set(envelope["unresolved_optional_target_roles"]),
            {"task_naming", "capability_baseline"},
        )

    def test_optional_context_limit_is_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(TcafError, "At most 1"):
                assemble_run(
                    FRAMEWORK_ROOT,
                    "task",
                    direct_agent=False,
                    raw_target=temporary,
                    request="A broad request.",
                    raw_input=None,
                    selectors=["decomposition", "review"],
                    requested_adapter="generic-cli",
                )

    def test_cli_returns_machine_readable_run(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = subprocess.run(
                [
                    sys.executable,
                    str(FRAMEWORK_ROOT / "runtime" / "tcaf.py"),
                    "task",
                    "--target",
                    temporary,
                    "--request",
                    "Inspect one behavior.",
                    "--adapter",
                    "generic-cli",
                    "--format",
                    "json",
                ],
                cwd=FRAMEWORK_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["agent_id"], "task-contract-generator")
        self.assertEqual(payload["target"]["kind"], "directory")

    def test_installer_creates_versioned_launcher(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            home = base / "home"
            bin_dir = base / "bin"
            install = subprocess.run(
                [
                    sys.executable,
                    str(FRAMEWORK_ROOT / "install.py"),
                    "--home",
                    str(home),
                    "--bin-dir",
                    str(bin_dir),
                ],
                cwd=FRAMEWORK_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(install.returncode, 0, install.stderr)
            command = bin_dir / ("tcaf.cmd" if os.name == "nt" else "tcaf")
            version = subprocess.run(
                [str(command), "version"],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(version.returncode, 0, version.stderr)
            self.assertEqual(version.stdout.strip(), "0.3.3")
            active = json.loads((home / "active.json").read_text(encoding="utf-8"))
            self.assertEqual(active["version"], "0.3.3")


if __name__ == "__main__":
    unittest.main()
