from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "governance" / "principles.json"


class PrinciplesRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    def test_registry_scope_and_runtime_isolation(self) -> None:
        self.assertEqual(
            self.registry["scope"],
            "TCAF framework development governance",
        )
        self.assertIs(self.registry["runtime_exposure"], False)

    def test_exact_ordered_principle_ids(self) -> None:
        expected = [f"BP-{index:02d}" for index in range(1, 38)]
        actual = [item["id"] for item in self.registry["principles"]]
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(set(actual)))

    def test_principle_fields_and_enums(self) -> None:
        enums = self.registry["enums"]
        required_fields = {
            "id",
            "name",
            "classification",
            "origin",
            "definition",
            "applies",
            "trigger",
            "change",
            "implementation",
            "verification",
            "health",
            "custom",
        }

        for principle in self.registry["principles"]:
            with self.subTest(principle=principle["id"]):
                self.assertTrue(required_fields.issubset(principle))
                self.assertIn(
                    principle["classification"],
                    enums["classification"],
                )
                self.assertIn(principle["change"], enums["change"])
                self.assertIn(
                    principle["implementation"]["status"],
                    enums["implementation_status"],
                )
                self.assertIn(
                    principle["verification"]["required"],
                    enums["required_verification_level"],
                )
                self.assertIn(
                    principle["verification"]["status"],
                    enums["verification_status"],
                )
                self.assertIn(principle["health"], enums["health"])
                self.assertIsInstance(principle["custom"]["allowed"], bool)
                self.assertIsInstance(principle["custom"]["policy"], str)

    def test_all_referenced_implementation_surfaces_exist(self) -> None:
        for principle in self.registry["principles"]:
            for relative in principle["implementation"]["surfaces"]:
                with self.subTest(principle=principle["id"], path=relative):
                    self.assertTrue((ROOT / relative).exists(), relative)

    def test_all_referenced_verification_evidence_exists(self) -> None:
        for principle in self.registry["principles"]:
            for relative in principle["verification"]["evidence"]:
                with self.subTest(principle=principle["id"], path=relative):
                    self.assertTrue((ROOT / relative).exists(), relative)

    def test_applicability_uses_declared_operations_or_groups(self) -> None:
        allowed = set(self.registry["operations"]) | set(
            self.registry["applicability_groups"]
        )
        for principle in self.registry["principles"]:
            with self.subTest(principle=principle["id"]):
                self.assertTrue(principle["applies"])
                self.assertTrue(set(principle["applies"]).issubset(allowed))

    def test_applicability_groups_reference_only_declared_operations(self) -> None:
        operations = set(self.registry["operations"])
        for group, members in self.registry["applicability_groups"].items():
            with self.subTest(group=group):
                self.assertTrue(members)
                self.assertTrue(set(members).issubset(operations))

    def test_minimum_first_and_selective_context_are_preserved(self) -> None:
        by_id = {item["id"]: item for item in self.registry["principles"]}
        for principle_id in ("BP-05", "BP-06"):
            principle = by_id[principle_id]
            with self.subTest(principle=principle_id):
                self.assertEqual(principle["change"], "PRESERVE")
                self.assertEqual(principle["health"], "HEALTHY")
                self.assertEqual(principle["applies"], ["ALL"])

    def test_bp31_is_implemented_and_black_box_verified(self) -> None:
        by_id = {item["id"]: item for item in self.registry["principles"]}
        principle = by_id["BP-31"]
        self.assertEqual(principle["change"], "CHANGE")
        self.assertEqual(
            principle["implementation"]["status"],
            "IMPLEMENTED",
        )
        self.assertEqual(principle["verification"]["required"], "BLACK_BOX")
        self.assertEqual(principle["verification"]["status"], "BLACK_BOX_VERIFIED")
        self.assertEqual(principle["health"], "HEALTHY")
        self.assertIn(
            "tests/acceptance/TEST_LOG.md",
            principle["verification"]["evidence"],
        )

    def test_bp31_evidence_covers_active_instruction_surfaces(self) -> None:
        principle = {item["id"]: item for item in self.registry["principles"]}["BP-31"]
        self.assertIn("runtime/planning-rules-minimal.md", principle["implementation"]["surfaces"])
        self.assertIn("templates/project-docs/planning-policy.md", principle["implementation"]["surfaces"])
        self.assertIn("tests/runtime/test_runtime.py", principle["verification"]["evidence"])

    def test_organizational_profile_and_planning_policy_are_recorded(self) -> None:
        by_id = {item["id"]: item for item in self.registry["principles"]}
        principle = by_id["BP-26"]
        self.assertEqual(principle["change"], "NEW")
        self.assertEqual(principle["implementation"]["status"], "IMPLEMENTED")
        self.assertEqual(principle["verification"]["required"], "BLACK_BOX")
        self.assertEqual(principle["verification"]["status"], "BLACK_BOX_VERIFIED")
        self.assertEqual(principle["health"], "HEALTHY")
        self.assertIn(
            "tests/acceptance/TEST_LOG.md",
            principle["verification"]["evidence"],
        )
        requirement = self.registry["operational_requirements"]["planning_decomposition_policy"]
        self.assertEqual(requirement["status"], "IMPLEMENTED")
        self.assertEqual(requirement["canonical_role"], "planning_policy")
        self.assertEqual(requirement["default_path"], "docs/method/planning-policy.md")
        self.assertNotIn("BP-38", {item["id"] for item in self.registry["principles"]})
        self.assertEqual(by_id["BP-31"]["change"], "CHANGE")
        self.assertEqual(by_id["BP-31"]["implementation"]["status"], "IMPLEMENTED")
        self.assertTrue({"BP-03", "BP-07", "BP-12", "BP-13", "BP-14", "BP-15", "BP-29", "BP-31"}.issubset(requirement["non_waivable_principles"]))

    def test_planner_specific_black_box_evidence_does_not_promote_broader_principles(self) -> None:
        by_id = {item["id"]: item for item in self.registry["principles"]}
        for principle_id in ("BP-28", "BP-29", "BP-30"):
            principle = by_id[principle_id]
            with self.subTest(principle=principle_id):
                self.assertEqual(principle["implementation"]["status"], "PARTIAL")
                self.assertEqual(principle["verification"]["status"], "STATIC_VERIFIED")
                self.assertEqual(principle["health"], "REVIEW_REQUIRED")
                self.assertIn(
                    "tests/acceptance/TEST_LOG.md",
                    principle["verification"]["evidence"],
                )

    def test_principle_propagation_is_implemented_pending_black_box(self) -> None:
        by_id = {item["id"]: item for item in self.registry["principles"]}
        principle = by_id["BP-37"]
        self.assertEqual(principle["change"], "NEW")
        self.assertEqual(
            principle["implementation"]["status"],
            "IMPLEMENTED",
        )
        self.assertEqual(principle["verification"]["required"], "BLACK_BOX")
        self.assertEqual(principle["verification"]["status"], "BEHAVIOR_VERIFIED")
        self.assertEqual(principle["health"], "REVIEW_REQUIRED")
        self.assertEqual(principle["applies"], ["ALL"])

    def test_custom_planning_policy_is_operational_requirement_not_bp38(self) -> None:
        requirement = self.registry["operational_requirements"][
            "planning_decomposition_policy"
        ]
        self.assertEqual(requirement["default_mode"], "standard")
        self.assertEqual(requirement["custom_mode"], "custom")
        self.assertEqual(
            requirement["canonical_role"],
            "planning_policy",
        )
        principle_ids = {item["id"] for item in self.registry["principles"]}
        self.assertNotIn("BP-38", principle_ids)

    def test_governance_is_not_loaded_by_agent_manifests(self) -> None:
        paths = sorted((ROOT / "agent-bundles").glob("*/manifest.json"))
        paths.append(ROOT / "registry" / "applicability.json")
        for manifest_path in paths:
            text = manifest_path.read_text(encoding="utf-8")
            with self.subTest(manifest=manifest_path):
                self.assertNotIn("governance/", text)
                self.assertNotIn("../governance", text)


if __name__ == "__main__":
    unittest.main()
