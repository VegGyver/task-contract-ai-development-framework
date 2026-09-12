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
from tcaf_runtime.target import resolve_target_role
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

    def test_adoption_envelope_exposes_all_canonical_generation_templates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "adopt",
                direct_agent=False,
                raw_target=temporary,
                request=None,
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )

        module_paths = {
            Path(module["path"]).relative_to(FRAMEWORK_ROOT).as_posix()
            for module in envelope["instruction_modules"]
        }
        expected_templates = {
            "project-brief.md",
            "architecture-overview.md",
            "backlog.md",
            "project-rules.md",
            "ai-workflow.md",
            "capability-baseline.md",
            "task-naming.md",
            "project-manifest.md",
        }
        self.assertTrue(
            {
                f"templates/project-docs/{name}" for name in expected_templates
            }.issubset(module_paths)
        )

    def test_adoption_bundle_requires_evidence_normalization(self) -> None:
        bundle = FRAMEWORK_ROOT / "agent-bundles" / "existing-project-adoption"
        instructions = "\n".join(
            (bundle / name).read_text(encoding="utf-8")
            for name in ("AGENT.md", "START.md", "OUTPUT-SCHEMA.md")
        )
        self.assertIn("source evidence by default", instructions)
        self.assertIn("schema-compatible", instructions)
        self.assertIn("preserve it byte-for-byte", instructions)
        self.assertIn("approved alternate path", instructions)
        self.assertIn("VALIDATION PENDING", instructions)
        self.assertIn("tcaf validate --target .", instructions)

    def test_adoption_arbitrary_project_proposes_full_minimal_normalization_set(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            (target / "docs").mkdir()
            (target / "docs" / "overview.md").write_text(
                "# Project overview\n\nA real application.\n", encoding="utf-8"
            )
            (target / "docs" / "architecture.md").write_text(
                "# Architecture notes\n\nA service and a database.\n", encoding="utf-8"
            )
            (target / "docs" / "roadmap.md").write_text(
                "# Roadmap\n\n- Ship the first release.\n", encoding="utf-8"
            )
            (target / "package.json").write_text(
                '{"scripts":{"test":"pytest"}}\n', encoding="utf-8"
            )
            (target / "src").mkdir()
            (target / "src" / "app.py").write_text("def run(): pass\n", encoding="utf-8")
            (target / ".github").mkdir()
            (target / ".github" / "ci.yml").write_text("name: test\n", encoding="utf-8")

            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "adopt",
                direct_agent=False,
                raw_target=str(target),
                request=None,
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )

        instructions = "\n".join(
            module["content"] for module in envelope["instruction_modules"]
        )
        for role in (
            "project-brief.md",
            "architecture-overview.md",
            "backlog.md",
            "project-rules.md",
            "ai-workflow.md",
            "capability-baseline.md",
            "task-naming.md",
        ):
            self.assertIn(role, instructions)
        self.assertIn("minimum missing or non-conformant canonical role set", instructions)
        self.assertIn("Do not propose roles already satisfied", instructions)
        self.assertIn("source evidence by default", instructions)
        self.assertIn("Do not map an arbitrary or schema-incompatible source document directly", instructions)
        self.assertIn("INSPECT_ONLY", instructions)
        self.assertIn("READY FOR REVIEW", instructions)
        self.assertNotIn("only the standard missing core method documents", instructions)

    def test_adoption_preserves_arbitrary_default_path_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._canonical_project(target)
            brief = target / "docs" / "project-brief.md"
            original = b"# Existing project notes\n\nFree-form context.\n"
            brief.write_bytes(original)

            canonical = target / "docs" / "canonical" / "project-brief.md"
            canonical.parent.mkdir(parents=True)
            shutil.copy2(
                FRAMEWORK_ROOT / "templates" / "project-docs" / "project-brief.md",
                canonical,
            )
            manifest = target / "docs" / "method" / "project-manifest.md"
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(
                (
                    FRAMEWORK_ROOT
                    / "templates"
                    / "project-docs"
                    / "project-manifest.md"
                ).read_text(encoding="utf-8").replace(
                    "- Project brief: `docs/project-brief.md`",
                    "- Project brief: `docs/canonical/project-brief.md`",
                ),
                encoding="utf-8",
            )

            result = validate_target(FRAMEWORK_ROOT, target)
            resolved = resolve_target_role(
                target, "project_brief", load_project_schema(FRAMEWORK_ROOT)
            )
            preserved = brief.read_bytes()

        self.assertTrue(result["valid"], result["issues"])
        self.assertEqual(resolved, canonical)
        self.assertEqual(preserved, original)

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
            for source, name in (
                ("project-rules.md", "rules.md"),
                ("task-naming.md", "naming.md"),
                ("capability-baseline.md", "capabilities.md"),
            ):
                template = FRAMEWORK_ROOT / "templates" / "project-docs" / source
                (method / name).write_text(template.read_text(encoding="utf-8"), encoding="utf-8")

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
        self.assertEqual(
            set(envelope["unresolved_optional_target_roles"]),
            {"project_brief", "architecture_overview", "backlog", "ai_workflow"},
        )

    def test_task_uses_canonical_project_state_before_preserved_source_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._canonical_project(target)
            docs = target / "docs"
            (docs / "PROJECT_CONTEXT.md").write_text(
                "# Preserved context\n\nHistorical project notes.\n",
                encoding="utf-8",
            )
            (docs / "PROJECT_PLAN.md").write_text(
                "# Preserved plan\n\n- Historical roadmap item.\n",
                encoding="utf-8",
            )
            architecture = docs / "architecture"
            architecture.mkdir()
            (architecture / "legacy.html").write_text(
                "<h1>Historical architecture</h1>", encoding="utf-8"
            )

            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "task",
                direct_agent=False,
                raw_target=str(target),
                request="Implement the current backlog item.",
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )

        target_roles = {
            item["role"]: Path(item["path"])
            for item in envelope["instruction_modules"]
            if item["source"] == "target"
        }
        self.assertEqual(
            set(target_roles),
            {
                "project_brief",
                "architecture_overview",
                "backlog",
                "project_rules",
                "ai_workflow",
                "capability_baseline",
                "task_naming",
            },
        )
        self.assertEqual(
            target_roles["project_brief"], target / "docs" / "project-brief.md"
        )
        self.assertEqual(
            target_roles["backlog"], target / "docs" / "backlog.md"
        )
        instructions = "\n".join(
            module["content"] for module in envelope["instruction_modules"]
        )
        self.assertIn("primary project state", instructions)
        self.assertIn("Preserved free-form project documents are supporting evidence only", instructions)
        self.assertIn("Do not identify arbitrary source documents as the primary source of truth", instructions)
        self.assertNotIn("docs/PROJECT_CONTEXT.md as the primary source", instructions)

    def test_task_can_fall_back_to_source_evidence_when_canonical_role_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            docs = target / "docs"
            docs.mkdir()
            (docs / "PROJECT_CONTEXT.md").write_text(
                "# Existing context\n\nA usable project description.\n",
                encoding="utf-8",
            )
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "task",
                direct_agent=False,
                raw_target=str(target),
                request="Inspect the current behavior.",
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )

        self.assertEqual(envelope["agent_id"], "task-contract-generator")
        instructions = "\n".join(
            module["content"] for module in envelope["instruction_modules"]
        )
        self.assertIn("when a canonical role is missing or unusable", instructions)
        self.assertIn("Missing supporting evidence must not block", instructions)

    def test_task_backlog_is_authoritative_over_preserved_project_plan(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._canonical_project(target)
            docs = target / "docs"
            (docs / "PROJECT_PLAN.md").write_text(
                "# Old plan\n\nTask-OLD is planned.\n", encoding="utf-8"
            )
            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "task",
                direct_agent=False,
                raw_target=str(target),
                request="Use the current backlog task.",
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )

        instructions = "\n".join(
            module["content"] for module in envelope["instruction_modules"]
        )
        self.assertIn("canonical `backlog` first", instructions)
        self.assertIn("Resolve task identity, status, dependencies", instructions)
        self.assertIn("and intent from the canonical", instructions)
        self.assertIn("never", instructions)
        self.assertIn("override canonical", instructions)

    def test_task_contract_schema_separates_developer_view_and_execution_constraints(self) -> None:
        template = (
            FRAMEWORK_ROOT / "templates" / "task-contracts" / "task-contract.md"
        ).read_text(encoding="utf-8")
        instructions = (
            FRAMEWORK_ROOT
            / "agent-bundles"
            / "task-contract-generator"
            / "AGENT.md"
        ).read_text(encoding="utf-8")
        self.assertLess(
            template.index("## Developer task view"),
            template.index("## AI execution constraints"),
        )
        for field in (
            "Concrete changes:",
            "Implementation surface:",
            "Relevant components:",
            "Test expectations:",
            "Expected developer verification:",
        ):
            self.assertIn(field, template)
        self.assertIn("two clearly labelled parts", instructions)
        self.assertIn("failed check", instructions)
        self.assertIn("confirmed cause from probable cause", instructions)
        self.assertIn("contract amendment", instructions)

    def test_backlog_template_separates_stable_status_from_lifecycle_evidence(self) -> None:
        backlog = (
            FRAMEWORK_ROOT / "templates" / "project-docs" / "backlog.md"
        ).read_text(encoding="utf-8")
        for status in ("Proposed", "Approved", "In progress", "Completed", "Blocked"):
            self.assertIn(f"`{status}`", backlog)
        for field in ("Implementation:", "Review:", "Verification:", "Commit:"):
            self.assertIn(field, backlog)
        self.assertIn("do not infer it from `Status`", backlog)

    def test_task_ignores_non_canonical_role_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            method_dir = target / "docs" / "method"
            method_dir.mkdir(parents=True)
            (method_dir / "project-rules.md").write_text(
                "# Notes\n\n## Project context\n\n- The app will be rebuilt.\n",
                encoding="utf-8",
            )
            (method_dir / "project-manifest.md").write_text(
                "# Project Documentation Manifest\n\n"
                "## Role-to-path mappings\n\n"
                "- Project rules: `docs/method/project-rules.md`\n",
                encoding="utf-8",
            )

            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "task",
                direct_agent=False,
                raw_target=str(target),
                request="Inspect the current behavior.",
                raw_input=None,
                selectors=[],
                requested_adapter="generic-cli",
            )

        roles = {
            item["role"]
            for item in envelope["instruction_modules"]
            if item["source"] == "target"
        }
        self.assertNotIn("project_rules", roles)
        self.assertTrue(
            any(
                item["role"] == "fallback:project_rules"
                for item in envelope["instruction_modules"]
            )
        )

    def test_bootstrap_ignores_arbitrary_non_canonical_docs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "greenfield"
            docs = target / "docs"
            docs.mkdir(parents=True)
            (docs / "PROJECT_CONTEXT.md").write_text(
                "# Project context\n\nWe are building a task tool.\n",
                encoding="utf-8",
            )
            (docs / "ROADMAP.md").write_text(
                "# Roadmap\n\n- Phase 1: research\n- Phase 2: ship\n",
                encoding="utf-8",
            )
            (docs / "architecture-notes.md").write_text(
                "# Architecture notes\n\nThe app will have a service layer.\n",
                encoding="utf-8",
            )
            for name in ("project-brief.md", "architecture-overview.md", "backlog.md"):
                (docs / name).write_text(
                    f"# {name}\n\nThis file is user-provided and not canonical TCAF documentation.\n",
                    encoding="utf-8",
                )

            schema = load_project_schema(FRAMEWORK_ROOT)
            for role_id in ("project_brief", "architecture_overview", "backlog"):
                self.assertIsNone(
                    resolve_target_role(target, role_id, schema),
                    msg=f"non-canonical {role_id} should not resolve as a canonical target role",
                )

    def test_bootstrap_envelope_exposes_canonical_templates_for_missing_roles(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "greenfield"
            input_dir = Path(temporary) / "input"
            input_dir.mkdir()
            (input_dir / "PROJECT_CONTEXT.md").write_text(
                "# Project context\n\nThis is free-form analysis.\n",
                encoding="utf-8",
            )
            (input_dir / "ROADMAP.md").write_text(
                "# Roadmap\n\n- Step 1: discover\n",
                encoding="utf-8",
            )
            (input_dir / "architecture-notes.md").write_text(
                "# Architecture\n\nSingle-process service.\n",
                encoding="utf-8",
            )

            envelope = assemble_run(
                FRAMEWORK_ROOT,
                "bootstrap",
                direct_agent=False,
                raw_target=str(target),
                request=None,
                raw_input=str(input_dir),
                selectors=[],
                requested_adapter="generic-cli",
            )

        module_paths = [module["path"] for module in envelope["instruction_modules"]]
        self.assertTrue(
            any(path.endswith("templates/project-docs/project-brief.md") for path in module_paths)
        )
        self.assertTrue(
            any(path.endswith("templates/project-docs/architecture-overview.md") for path in module_paths)
        )
        self.assertTrue(
            any(path.endswith("templates/project-docs/backlog.md") for path in module_paths)
        )
        self.assertTrue(
            any(path.endswith("core/project-documentation-schema.md") for path in module_paths)
        )

    def test_bootstrap_normalizes_free_form_sources_and_runtime_validation_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "project"
            docs = target / "docs"
            docs.mkdir(parents=True)
            source_documents = {
                "PROJECT_CONTEXT.md": "# Project context\n\nBuild a small task service.\n",
                "reality-error-logical-architecture-v0.1.html": (
                    "<h1>Architecture notes</h1><p>Use a service layer.</p>"
                ),
                "PROJECT_PLAN.md": "# Project plan\n\n- Discover the first milestone.\n",
            }
            source_bytes: dict[str, bytes] = {}
            for name, content in source_documents.items():
                path = docs / name
                path.write_text(content, encoding="utf-8")
                source_bytes[name] = path.read_bytes()

            # This is the approved bootstrap write step: incompatible source
            # evidence is preserved while canonical roles come from templates.
            self._canonical_project(target)

            for name, original in source_bytes.items():
                self.assertEqual((docs / name).read_bytes(), original)
            schema = load_project_schema(FRAMEWORK_ROOT)
            for role_id in ("project_brief", "architecture_overview", "backlog"):
                resolved = resolve_target_role(target, role_id, schema)
                self.assertEqual(
                    resolved,
                    target / schema["roles"][role_id]["default_path"],
                )
            self.assertFalse((target / "docs" / "method" / "project-manifest.md").exists())

            result = validate_target(FRAMEWORK_ROOT, target)

        self.assertTrue(result["valid"], result["issues"])

    def test_bootstrap_bundle_requires_normalization_and_pending_validation(self) -> None:
        bundle = FRAMEWORK_ROOT / "agent-bundles" / "project-bootstrap"
        agent = (bundle / "AGENT.md").read_text(encoding="utf-8")
        start = (bundle / "START.md").read_text(encoding="utf-8")
        output = (bundle / "OUTPUT-SCHEMA.md").read_text(encoding="utf-8")

        self.assertIn("Treat every supplied file and directory as source evidence by default", agent)
        self.assertIn("compare it with that role's machine\nschema", agent)
        self.assertIn("preserve the source file byte-for-byte", agent)
        self.assertIn("approved alternate canonical path", agent)
        self.assertIn("Never map source evidence directly to a canonical\nrole", start)
        self.assertIn("VALIDATION PENDING", start)
        self.assertIn("tcaf validate --target .", output)
        self.assertIn("Do not use `Validation: PASS`", output)

    def test_validation_evidence_rules_are_shared_across_relevant_bundles(self) -> None:
        evidence = (FRAMEWORK_ROOT / "core" / "validation-evidence.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Validation: PASS", evidence)
        self.assertIn("Validation: PENDING", evidence)
        self.assertIn("Validation: FAILED", evidence)
        self.assertIn("tcaf validate --target <target>", evidence)
        self.assertIn("Aggregate task verification is `passed` only", evidence)
        self.assertIn("Status:\nCompleted", evidence)

        for bundle in (
            "project-bootstrap",
            "existing-project-adoption",
            "task-contract-generator",
        ):
            manifest = json.loads(
                (FRAMEWORK_ROOT / "agent-bundles" / bundle / "manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertIn("../../core/validation-evidence.md", manifest["required_modules"])

    def test_bootstrap_and_adoption_require_pending_validation_before_execution(self) -> None:
        for bundle in ("project-bootstrap", "existing-project-adoption"):
            content = "\n".join(
                (FRAMEWORK_ROOT / "agent-bundles" / bundle / name).read_text(
                    encoding="utf-8"
                )
                for name in ("AGENT.md", "START.md", "OUTPUT-SCHEMA.md")
            )
            self.assertIn("VALIDATION PENDING", content)
            self.assertIn("tcaf validate --target .", content)
            self.assertIn("Validation: FAILED", content)
            self.assertIn("Validation: PASS", content)

    def test_task_checks_cannot_hide_aggregate_failure_or_completed_status(self) -> None:
        content = "\n".join(
            (FRAMEWORK_ROOT / path).read_text(encoding="utf-8")
            for path in (
                "core/task-contract.md",
                "agent-bundles/task-contract-generator/AGENT.md",
                "agent-bundles/task-contract-generator/OUTPUT-SCHEMA.md",
            )
        )
        self.assertIn("aggregate `Verification: passed`", content)
        self.assertIn("lower-level diagnostics pass", content)
        self.assertIn("Do not infer review approval, executed verification, or a commit from `Status`", content)

    def test_resolve_target_role_reuses_valid_canonical_documents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            docs = target / "docs"
            docs.mkdir()
            for role_id, file_name in (
                ("project_brief", "project-brief.md"),
                ("architecture_overview", "architecture-overview.md"),
                ("backlog", "backlog.md"),
            ):
                source = FRAMEWORK_ROOT / "templates" / "project-docs" / file_name
                (docs / file_name).write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

            schema = load_project_schema(FRAMEWORK_ROOT)
            for role_id in ("project_brief", "architecture_overview", "backlog"):
                resolved = resolve_target_role(target, role_id, schema)
                self.assertIsNotNone(resolved)
                self.assertEqual(resolved, target / schema["roles"][role_id]["default_path"])

    def test_resolve_target_role_uses_manifest_alternate_path_for_collision(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            docs = target / "docs"
            docs.mkdir()
            original = docs / "project-brief.md"
            original.write_text(
                "# Project context\n\nThis is an arbitrary user document that should not be overwritten.\n",
                encoding="utf-8",
            )
            approved = docs / "approved"
            approved.mkdir()
            canonical = approved / "project-brief.md"
            canonical.write_text(
                (FRAMEWORK_ROOT / "templates" / "project-docs" / "project-brief.md").read_text(
                    encoding="utf-8"
                ),
                encoding="utf-8",
            )
            manifest = target / "docs" / "method" / "project-manifest.md"
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(
                "# Project Documentation Manifest\n\n"
                "## Role-to-path mappings\n\n"
                "- Project brief: `docs/approved/project-brief.md`\n",
                encoding="utf-8",
            )

            resolved = resolve_target_role(target, "project_brief", load_project_schema(FRAMEWORK_ROOT))
            self.assertEqual(resolved, canonical)
            self.assertTrue(original.exists())
            self.assertTrue(canonical.is_file())

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
            {
                "project_brief",
                "architecture_overview",
                "backlog",
                "task_naming",
                "capability_baseline",
                "ai_workflow",
            },
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

    def test_cli_rendered_task_contract_labels_canonical_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            self._canonical_project(target)
            docs = target / "docs"
            (docs / "backlog.md").write_text(
                "# Backlog\n\nTask ID: RE-003\nTitle: API foundation\n"
                "Goal: Start the API.\nStatus: Proposed.\n",
                encoding="utf-8",
            )
            (docs / "PROJECT_PLAN.md").write_text(
                "# Preserved plan\n\nHistorical RE-003 provenance.\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    str(FRAMEWORK_ROOT / "runtime" / "tcaf.py"),
                    "task",
                    "--target",
                    str(target),
                    "--request",
                    "Prepare the backlog task for review.",
                    "--adapter",
                    "generic-cli",
                    "--format",
                    "markdown",
                ],
                cwd=FRAMEWORK_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        rendered = result.stdout
        self.assertIn("Origin: Canonical backlog / canonical task state", rendered)
        self.assertIn("Source of truth: canonical TCAF project documents", rendered)
        self.assertIn(
            "Supporting evidence: preserved/free-form source documents", rendered
        )
        self.assertNotIn("Origin: Project plan (`docs/PROJECT_PLAN.md`)", rendered)

    def test_cli_rendered_task_contract_uses_conditional_fallback_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            docs = target / "docs"
            docs.mkdir()
            (docs / "PROJECT_CONTEXT.md").write_text(
                "# Existing context\n\nFallback project evidence.\n",
                encoding="utf-8",
            )
            (docs / "PROJECT_PLAN.md").write_text(
                "# Existing plan\n\nFallback task evidence.\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    str(FRAMEWORK_ROOT / "runtime" / "tcaf.py"),
                    "task",
                    "--target",
                    str(target),
                    "--request",
                    "Use the available project evidence.",
                    "--adapter",
                    "generic-cli",
                    "--format",
                    "markdown",
                ],
                cwd=FRAMEWORK_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        rendered = result.stdout
        self.assertIn("Origin: preserved/external/direct-request fallback evidence", rendered)
        self.assertIn("Source of truth: available fallback/project evidence", rendered)
        self.assertIn("Supporting evidence: preserved/free-form source documents", rendered)
        self.assertNotIn("Origin: Canonical backlog / canonical task state", rendered)
        self.assertNotIn("Source of truth: canonical TCAF project documents", rendered)

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
