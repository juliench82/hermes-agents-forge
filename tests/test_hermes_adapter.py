"""Fixture-backed compatibility tests for the legacy Hermes adapter."""
import json
import tempfile
import unittest
from pathlib import Path

from compiler.hermes_adapter import CONTRACT_VERSION, LEGACY_PROFILES, STAGES, render_hermes
from compiler.planner import build_plan
from runtime.tenant_spec import validate_file

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "examples" / "solo-founder-app-builder.tenant-spec.json"
EXPECTED_STAGES = [stage for stage, _ in STAGES]

PROFILE_DATA = {
    "architect": ("""name: architect
purpose: Define constraints, interfaces, risks, and implementation plans
version: 1
inputs: [task_spec]
outputs: [plan, handoff]
allowed_tools: [filesystem.read, git.read]
requires_approval_for: []
skills: [architecture-plan]
""", "# Architect\n"),
    "builder": ("""name: builder
purpose: Implement approved changes and produce verification evidence
version: 1
inputs: [approved_task, implementation_plan]
outputs: [code_changes, handoff]
allowed_tools: [filesystem.read, filesystem.write, terminal.test, git.read]
requires_approval_for: [git.push, github.write]
skills: [implement-feature]
""", "# Builder\n"),
    "orchestrator": ("""name: orchestrator
purpose: Decompose work, assign profiles, and manage task state
version: 1
inputs: [objective]
outputs: [task_graph, handoff]
allowed_tools: [filesystem.read, task.create, task.transition, profile.delegate]
requires_approval_for: [profile.delegate.external]
skills: [coordinate-task]
""", "# Orchestrator\n"),
    "product-strategist": ("""name: product-strategist
purpose: Define user outcomes, scope, and testable acceptance criteria
version: 1
inputs: [user_intent]
outputs: [product_spec, handoff]
allowed_tools: [filesystem.read]
requires_approval_for: []
skills: [define-acceptance-criteria]
""", "# Product Strategist\n"),
    "quality-guardian": ("""name: quality-guardian
purpose: Independently verify scope, safety, tests, and acceptance criteria
version: 1
inputs: [task_spec, builder_handoff]
outputs: [review_decision, handoff]
allowed_tools: [filesystem.read, terminal.test, security.scan, git.diff]
requires_approval_for: []
skills: [verify-change]
""", "# Quality Guardian\n"),
    "self-improver": ("""name: self-improver
purpose: Draft reviewed improvements from recurring failures and reusable knowledge
version: 1
inputs: [completed_task, task_events]
outputs: [improvement_proposal, handoff]
allowed_tools: [filesystem.read, proposal.create]
requires_approval_for: [policy.write, profile.write]
skills: [propose-improvement]
""", "# Self Improver\n"),
}


def legacy_source_root(directory: Path) -> Path:
    source_root = directory / "legacy-source"
    for name, (profile, skill) in PROFILE_DATA.items():
        profile_root = source_root / "profiles" / name
        profile_root.mkdir(parents=True)
        (profile_root / "profile.yaml").write_text(profile)
        (profile_root / "skill.md").write_text(skill)
    return source_root


class HermesAdapterTests(unittest.TestCase):
    def render(self, tmp_path: Path):
        validate_file(SPEC)
        return render_hermes(build_plan(SPEC), tmp_path / "rendered", legacy_source_root(tmp_path))

    def test_compatibility_spec_validates_and_preserves_legacy_profiles(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source_root = legacy_source_root(tmp_path)
            root = render_hermes(build_plan(SPEC), tmp_path / "rendered", source_root)
            runtime = json.loads((root / "runtime.json").read_text())
            coordination = json.loads((root / "coordination.json").read_text())
            self.assertEqual(runtime["routingMode"], "skill-routed")
            self.assertEqual(runtime["rootAgent"], "orchestrator")
            self.assertEqual([stage["id"] for stage in coordination["stages"]], EXPECTED_STAGES)
            self.assertEqual([agent["legacyProfile"] for agent in runtime["agents"]], list(LEGACY_PROFILES))
            for name in LEGACY_PROFILES:
                self.assertEqual((source_root / "profiles" / name / "profile.yaml").read_text(), (root / "profiles" / name / "profile.yaml").read_text())
                self.assertEqual((source_root / "profiles" / name / "skill.md").read_text(), (root / "profiles" / name / "skill.md").read_text())
            runtime_text = (root / "runtime.json").read_text().lower()
            self.assertNotIn("password", runtime_text)
            self.assertNotIn('"token"', runtime_text)

    def test_render_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source_root = legacy_source_root(tmp_path)
            plan = build_plan(SPEC)
            first = render_hermes(plan, tmp_path / "first", source_root)
            second = render_hermes(plan, tmp_path / "second", source_root)
            self.assertEqual((first / "runtime.json").read_bytes(), (second / "runtime.json").read_bytes())
            self.assertEqual((first / "coordination.json").read_bytes(), (second / "coordination.json").read_bytes())
            self.assertEqual((first / "fingerprint.sha256").read_bytes(), (second / "fingerprint.sha256").read_bytes())

    def test_contract_version_and_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.render(Path(tmp))
            runtime = json.loads((root / "runtime.json").read_text())
            manifest = json.loads((root / "manifest.json").read_text())
            self.assertEqual(runtime["contractVersion"], CONTRACT_VERSION)
            self.assertEqual(runtime["contractStatus"], "compatibility")
            self.assertEqual(manifest["contractVersion"], CONTRACT_VERSION)
            self.assertIs(manifest["secretValuesIncluded"], False)

    def test_profile_identity_version_skills_io_routing_approval_namespace(self):
        with tempfile.TemporaryDirectory() as tmp:
            runtime = json.loads((self.render(Path(tmp)) / "runtime.json").read_text())
            by_profile = {agent["legacyProfile"]: agent for agent in runtime["agents"]}
            for name in LEGACY_PROFILES:
                with self.subTest(profile=name):
                    agent = by_profile[name]
                    self.assertEqual(agent["id"], name)
                    self.assertEqual(agent["legacyProfile"], name)
                    self.assertTrue(str(agent["profileVersion"]).strip())
                    self.assertIsInstance(agent["inputs"], list)
                    self.assertIsInstance(agent["outputs"], list)
                    self.assertIsInstance(agent["skills"], list)
                    self.assertTrue(isinstance(agent["requiresApprovalFor"], list) or agent["requiresApprovalFor"] in ([], "[]", ""))
                    self.assertTrue(str(agent["namespace"]).startswith("solo-founder."))
                    self.assertEqual(agent["profilePath"], f"profiles/{name}/profile.yaml")
                    self.assertEqual(agent["skillPath"], f"profiles/{name}/skill.md")
            self.assertEqual(runtime["routingMode"], "skill-routed")

    def test_delegation_and_handoff_structure(self):
        with tempfile.TemporaryDirectory() as tmp:
            coordination = json.loads((self.render(Path(tmp)) / "coordination.json").read_text())
            self.assertEqual(coordination["workflow"], "solo-founder-app-builder")
            self.assertEqual(coordination["handoffContract"], "shared/profile-contract.md")
            self.assertIn("shared/workflows.md", coordination["policyContracts"])
            self.assertIn("shared/safety-gates.md", coordination["policyContracts"])
            self.assertIn("shared/safety-enforcement.md", coordination["policyContracts"])
            self.assertIsInstance(coordination["delegation"], list)
            for edge in coordination["delegation"]:
                self.assertIn("from", edge)
                self.assertIn("to", edge)

    def test_stage_agent_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            coordination = json.loads((self.render(Path(tmp)) / "coordination.json").read_text())
            self.assertEqual([(stage["id"], stage["agent"]) for stage in coordination["stages"]], list(STAGES))


if __name__ == "__main__":
    unittest.main()
