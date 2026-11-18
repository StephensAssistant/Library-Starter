"""Synthetic workflow fixtures, never governed/allocated Library records."""
import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import check_workflows as wf


@contextmanager
def symlink_boundary(link, target, target_is_directory=False):
    """Use a real symlink when permitted, otherwise emulate its boundary."""
    try:
        link.symlink_to(target, target_is_directory=target_is_directory)
    except (NotImplementedError, OSError):
        if target_is_directory:
            link.mkdir()
            for source in target.iterdir():
                if source.is_file():
                    (link / source.name).write_bytes(source.read_bytes())
        else:
            link.write_bytes(target.read_bytes())
        original = Path.is_symlink
        with mock.patch.object(
            Path,
            "is_symlink",
            autospec=True,
            side_effect=lambda candidate: candidate == link or original(candidate),
        ):
            yield
    else:
        yield


def state(key, kind):
    return dict(id=key, kind=kind, playbook="PLAY-0001", owner="HAT-0001", actor_access="Verify operator grants at invocation",
                scope="Read the agreed source only", prerequisites=["Source available"], inputs=["Source"],
                outputs=["Recorded evidence"], allowed_effects=["Read only"], success_check="Compare evidence",
                recovery="Preserve evidence and block dependent action", max_attempts=1,
                controls=[dict(requirement="Read authority", mode="instruction", evidence="Owning ticket", critical=True)])


def handoff():
    return dict(question="State the precise missing input that Library owner must provide after internal investigation",
                why_needed="Explain the unresolved dependency and why internal recovery cannot supply it",
                investigated_options="Record the evidence and recovery options actually investigated",
                recommendation="Give the evidence-supported option and its consequences",
                owner="Library owner", preserved_effects="List completed effects and reconcile uncertain effects",
                remaining_limits="Carry forward consumed attempts and remaining bounds without reset",
                next_entry="Identify the safe continuation or fresh admission checks after Library owner answers",
                cancellation="If Library owner cancelled, preserve that instruction and ask what is needed to resume; do not retry")


def failure_handling():
    return dict(playbook="PLAY-0069", director="HAT-0023", coordinator="HAT-0001", continuation_target="failed_step_continuation", cancellation_policy="immediate_stop_acknowledgement",
                error_tracking="Record each observed error and its evidence in the owning issue",
                repair_loop="Invoke the Director and Head before following any failure edge; investigate, assign, repair, test and review",
                handback="Return the verified repair and evidence to the executing AI for an observed attempt",
                continuation="Continue only after effect reconciliation and valid entry checks",
                child_return="Only completed child returns success; all other child results invoke this handler",
                limits="Share consumed repair and transition budgets; never reset limits on child return or fresh entry",
                awaiting_steve="After internal recovery, ask Library owner a precise question with investigated options and preserved effects")


def contract():
    return dict(schema_version=1, purpose="Reconcile a supplied result", trigger="Explicit review request",
                scope="Read only", non_goals=["No sends or production writes"], inputs=["Supplied result"],
                outputs=["Evidence"], authority="Current request permits read-only assessment",
                completion="Comparison evidence accepted", persistence="Owning ticket",
                risks=["Source may be stale"], grill_me="SKILL-0318", entry="read", max_transitions=10, failure_handling=failure_handling(),
                steps=[dict(state("read", "playbook"), uses="PLAY-0001", capabilities=[], next="done", failure="blocked"),
                       dict(state("done", "terminal"), outcome="completed"),
                       dict(state("blocked", "terminal"), outcome="awaiting_steve", handoff=handoff())],
                coverage={}, dependencies={"SKILL-0318": [], "HAT-0001": [], "PLAY-0001": ["SKILL-0318"], "HAT-0023": [], "PLAY-0069": ["SKILL-0313"], "SKILL-0313": []}, pins={}, policy_pins={}, resource_pins={}, tests=[], gaps=[], review={})


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.spec = contract()
        self.approved = False
        for folder, prefix in (("AIHats", "HAT"), ("Skills", "SKILL"), ("Playbooks", "PLAY"), ("Workflows", "FLOW")):
            (self.root / folder).mkdir()
        config = {"folders": {"AIHats": "HAT", "Skills": "SKILL", "Playbooks": "PLAY", "Workflows": "FLOW"}}
        (self.root / ".github").mkdir()
        (self.root / ".github/type-prefixes.json").write_text(json.dumps(config))
        for folder, key, kind in (("AIHats", "HAT-0001", "aihat"), ("Skills", "SKILL-0318", "skill"), ("Playbooks", "PLAY-0001", "playbook"), ("AIHats", "HAT-0023", "aihat"), ("Playbooks", "PLAY-0069", "playbook"), ("Skills", "SKILL-0313", "skill")):
            links = ("[SKILL-0313]" if key == "PLAY-0069" else "[PLAY-0069]" if key == "SKILL-0313"
                     else "[SKILL-0318]" if kind == "playbook" else "[PLAY-0001]" if kind == "skill" else "[]")
            (self.root / folder / (key + "-fixture.md")).write_text(
                f"---\nid: {key}\ntype: {kind}\nstatus: current\nlinks: {links}\n---\nFixture instruction.\n")
        for path in wf.POLICIES:
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("Fixture policy\n")
        (self.root / ".github/workflow-resources.json").write_text(json.dumps(
            {"schema_version": 1, "workflows": {"FLOW-0001": []}}))
        self.report = self.root / "evidence.txt"
        self.report.write_text("Non-author fixture test/review evidence\n")
        self.path = self.root / "Workflows/FLOW-0001-fixture.md"

    def render(self, spec=None, identity="FLOW-0001"):
        spec = self.spec if spec is None else spec
        return (f"---\nid: {identity}\ntype: workflow\ntitle: Synthetic fixture\nstatus: current\n"
                f"owner: Library owner\nauthor: fixture-author\nreview_status: {'approved' if self.approved else 'draft'}\n"
                "trigger_phrases: [review fixture]\nlinks: [HAT-0001, PLAY-0001, SKILL-0318, HAT-0023, PLAY-0069, SKILL-0313]\n---\n"
                "# Fixture\n```workflow-json\n" + json.dumps(spec, indent=2) + "\n```\n" + wf.render_visual(spec) + "\n")

    def errors(self, required=False):
        self.path.write_text(self.render())
        return wf.validate(self.path, wf.collect(self.root), self.root, required)

    def approve(self):
        self.approved = True
        entries = wf.collect(self.root)
        closure = wf.instruction_closure({"SKILL-0318", "HAT-0001", "PLAY-0001", "HAT-0023", "PLAY-0069"}, entries, self.spec["dependencies"])
        self.spec["pins"] = {key: wf.digest(entries[key]["path"].read_bytes()) for key in closure}
        self.spec["policy_pins"] = {path: wf.digest((self.root / path).read_bytes()) for path in wf.POLICIES}
        registry = json.loads((self.root / ".github/workflow-resources.json").read_text())
        self.spec["resource_pins"] = {key: wf.digest((self.root / key).read_bytes())
                                      for key in registry["workflows"]["FLOW-0001"]}
        proof = dict(path="evidence.txt", sha256=wf.digest(self.report.read_bytes()), result="PASS")
        self.spec["coverage"] = {"PLAY-0001": [dict(requirement="Read-only comparison and controlled exit", steps=[s["id"] for s in self.spec["steps"]], skills=["SKILL-0318"], status="verified", evidence=proof)]}
        self.spec["coverage"]["PLAY-0069"] = [dict(requirement="Shared recovery, verified handback and bounded Library owner escalation", steps=[s["id"] for s in self.spec["steps"]], skills=["SKILL-0313"], status="verified", evidence=proof)]
        self.spec["tests"] = [dict(proof, kind=kind) for kind in ("normal", "failure", "boundary")]
        self.spec["review"] = dict(reviewer="fixture-independent-reviewer", verdict="PASS", definition_sha256="pending",
                                   scores=dict(requirements=30, evidence=30, feasibility=20, verification=20), evidence=proof)
        self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)

    def immutable_proof(self):
        self.approve()
        path = self.root / "Reference/qualification-v1.txt"
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(self.report.read_bytes())
        proof = dict(path=path.relative_to(self.root).as_posix(), sha256=wf.digest(path.read_bytes()), result="PASS")
        self.spec["tests"] = [dict(proof, kind=kind) for kind in ("normal", "failure", "boundary")]
        for rows in self.spec["coverage"].values():
            for row in rows:
                row["evidence"] = proof
        self.spec["review"]["evidence"] = proof
        self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
        return path

    def test_mutable_owner_cannot_be_qualification_proof(self):
        self.approve()
        path = self.root / "Tickets/TICK-0001-live.md"
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(self.report.read_bytes())
        proof = dict(path=path.relative_to(self.root).as_posix(), sha256=wf.digest(path.read_bytes()), result="PASS")
        self.spec["tests"] = [dict(proof, kind=kind) for kind in ("normal", "failure", "boundary")]
        for rows in self.spec["coverage"].values():
            for row in rows:
                row["evidence"] = proof
        self.spec["review"]["evidence"] = proof
        self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
        self.assertTrue(any("evidence" in error for error in self.errors(True)))

    def test_immutable_proof_allows_normal_owner_checkpoint(self):
        self.immutable_proof()
        path = self.root / "Tickets/TICK-0001-live.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text("Original run owner\n")
        self.assertEqual([], self.errors(True))
        path.write_text("Meaningful pilot checkpoint\n")
        self.assertEqual([], self.errors(True))
        self.assertEqual([], wf.check_repository(self.root, "FLOW-0001", [path.relative_to(self.root).as_posix()]))

    def test_changed_or_missing_immutable_proof_refuses_admission(self):
        path = self.immutable_proof()
        self.assertEqual([], self.errors(True))
        path.write_text("Changed proof\n")
        self.assertTrue(any("evidence" in error for error in self.errors(True)))
        path.unlink()
        self.assertTrue(any("evidence" in error for error in self.errors(True)))

    def test_planned_writes_cannot_overlap_any_frozen_readset(self):
        proof = self.immutable_proof()
        self.assertEqual([], self.errors(True))
        for path in (proof.relative_to(self.root).as_posix(), "AGENTS.md", "Playbooks/PLAY-0001-fixture.md", self.path.relative_to(self.root).as_posix()):
            self.assertTrue(any("overlaps frozen" in error for error in wf.check_repository(self.root, "FLOW-0001", [path])), path)

    def test_planned_writes_require_identity_and_canonical_safe_path(self):
        self.immutable_proof()
        self.errors(True)
        self.assertTrue(wf.check_repository(self.root, None, ["new.txt"]))
        for path in ("../outside", str(self.report), "a/../b", "./new.txt", "a//b", "C:/outside", "C:outside", "a\\b", ".github"):
            self.assertTrue(any("unsafe planned" in error for error in wf.check_repository(self.root, "FLOW-0001", [path])))

    def test_draft_is_valid_but_not_invocable(self):
        self.assertEqual([], self.errors())
        self.assertIn("workflow is not current and approved", self.errors(True))

    def test_exact_approved_definition_passes(self):
        self.approve()
        self.assertEqual([], self.errors(True))

    def test_missing_control_blocks_even_at_100(self):
        self.approve()
        self.spec["steps"][0]["controls"] = []
        self.assertTrue(any("controls required" in e for e in self.errors()))

    def test_unverified_critical_control_blocks(self):
        self.approve()
        self.spec["steps"][0]["controls"][0]["mode"] = "unverified"
        self.assertTrue(any("critical control" in e for e in self.errors()))

    def test_self_approval_rejected(self):
        self.approve()
        self.spec["review"]["reviewer"] = " Fixture-Author "
        self.assertTrue(any("independent reviewer" in e for e in self.errors()))

    def test_definition_and_prose_edits_invalidate_review(self):
        self.approve()
        self.spec["scope"] += " plus writes"
        self.assertTrue(any("exact current definition" in e for e in self.errors()))
        self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
        self.path.write_text(self.render() + "Changed boundary\n")
        self.assertTrue(any("exact current definition" in e for e in wf.validate(self.path, wf.collect(self.root), self.root)))

    def test_direct_and_transitive_dependencies_are_pinned(self):
        skill = self.root / "Skills/SKILL-0318-fixture.md"
        skill.write_text(skill.read_text().replace("links: [PLAY-0001]", "links: [PLAY-0001, HAT-0001]"))
        self.spec["dependencies"]["SKILL-0318"] = ["HAT-0001"]
        self.approve()
        skill.write_text(skill.read_text() + "Changed rule\n")
        self.assertTrue(any("stale dependency" in e for e in self.errors()))

    def test_new_transitive_dependency_invalidates_approval(self):
        self.approve()
        play = self.root / "Playbooks/PLAY-0001-fixture.md"
        play.write_text(play.read_text().replace("links: [SKILL-0318]", "links: [SKILL-0318, SKILL-0002]"))
        (self.root / "Skills/SKILL-0002-fixture.md").write_text("---\nid: SKILL-0002\ntype: skill\nstatus: current\nlinks: []\n---\n")
        self.spec["dependencies"]["PLAY-0001"].append("SKILL-0002")
        self.spec["dependencies"]["SKILL-0002"] = []
        self.assertTrue(any("transitive" in e or "exact current definition" in e for e in self.errors()))

    def test_superseded_dependency_rejected(self):
        self.approve()
        p = self.root / "Playbooks/PLAY-0001-fixture.md"
        p.write_text(p.read_text().replace("status: current", "status: superseded"))
        self.assertTrue(any("superseded" in e for e in self.errors()))

    def test_stale_policy_rejected(self):
        self.approve()
        (self.root / "AGENTS.md").write_text("Changed authority\n")
        self.assertTrue(any("stale or absent policy pin" in e for e in self.errors()))

    def add_policy_context(self):
        path = self.root / "AIHats/HAT-0002-policy-context.md"
        path.write_text("---\nid: HAT-0002\ntype: aihat\nstatus: current\nlinks: []\n---\nExternal context, not a call.\n")
        self.approve()
        key = path.relative_to(self.root).as_posix()
        self.spec["policy_pins"][key] = wf.digest(path.read_bytes())
        self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
        return key, path

    def register_resource(self):
        key = ".github/scripts/fixture-control.py"
        path = self.root / key
        path.write_text("Fixture resource control\n")
        registry = {"schema_version": 1, "workflows": {"FLOW-0001": [key]}}
        (self.root / ".github/workflow-resources.json").write_text(json.dumps(registry))
        self.approve()
        return key, path

    def test_authoring_support_controls_are_resources_not_work_inputs(self):
        for key, content in (("Planning/README.md", "Planning guide\n"),
                             ("Tickets/_TEMPLATE.md", "---\nid: TICK-<NNNN>\ntype: ticket\n---\nTemplate\n")):
            path = self.root / key
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            registry = self.root / ".github/workflow-resources.json"
            registry.write_text(json.dumps({"schema_version": 1, "workflows": {"FLOW-0001": [key]}}))
            self.approve()
            self.assertEqual([], self.errors(True))
        path.write_text("---\nid: TICK-9999\ntype: ticket\n---\nActual record in disguise\n")
        self.spec["resource_pins"][key] = wf.digest(path.read_bytes())
        self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
        self.assertTrue(any("canonical immutable control" in e for e in self.errors(True)))

    def test_registered_resources_pass_and_changes_block_admission(self):
        key, path = self.register_resource()
        self.assertEqual([], self.errors(True))
        path.write_text(path.read_text() + "Changed control\n")
        self.assertTrue(any("stale resource pin" in e for e in self.errors(True)))
        self.spec["resource_pins"][key] = wf.digest(path.read_bytes())
        self.assertTrue(any("exact current definition" in e for e in self.errors(True)))

    def test_resource_set_cannot_omit_or_add_paths(self):
        key, _ = self.register_resource()
        for replacement in ({}, {key: self.spec["resource_pins"][key], "evidence.txt": "fake"}):
            self.spec["resource_pins"] = replacement
            self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
            self.assertTrue(any("exactly cover" in e for e in self.errors(True)))

    def test_registry_changes_invalidate_policy_and_review(self):
        self.register_resource()
        registry = self.root / ".github/workflow-resources.json"
        registry.write_text(json.dumps({"schema_version": 1, "workflows": {"FLOW-0001": []}}))
        self.assertTrue(any("stale or absent policy pin" in e for e in self.errors(True)))

    def test_malformed_or_missing_resource_registry_is_denied(self):
        self.approve()
        path = self.root / ".github/workflow-resources.json"
        for payload in ("not json", '{"schema_version":1,"schema_version":1,"workflows":{}}',
                        '{"schema_version":true,"workflows":{}}',
                        '{"schema_version":1,"workflows":{}}',
                        '{"schema_version":1,"workflows":{"FLOW-0001":[1]}}',
                        '{"schema_version":1,"workflows":{"FLOW-0001":["x","x"]}}'):
            path.write_text(payload)
            self.assertTrue(any("resource registry" in e for e in self.errors(True)), payload)
        path.unlink()
        self.assertTrue(any("resource registry" in e for e in self.errors(True)))

    def test_resources_reject_mutable_inputs_aliases_and_symlink_parents(self):
        self.approve()
        alias = self.root / "alias"
        (self.root / ".github/scripts/control.py").write_text("Control\n")
        with symlink_boundary(alias, self.root / ".github/scripts", target_is_directory=True):
            for key in ("evidence.txt/../evidence.txt", "alias/control.py", "../outside", str(self.report),
                        "Tickets/TICK-9999-run.md", ".github/id-reservations.json", "AGENTS.md"):
                if key in {"Tickets/TICK-9999-run.md", ".github/id-reservations.json"}:
                    target = self.root / key
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text("Mutable run input\n")
                registry = self.root / ".github/workflow-resources.json"
                registry.write_text(json.dumps({"schema_version": 1, "workflows": {"FLOW-0001": [key]}}))
                self.spec["resource_pins"] = {key: "fake"}
                self.assertTrue(any("canonical immutable control" in e for e in self.errors(True)), key)

    def test_external_policy_context_is_pinned_without_execution(self):
        key, _ = self.add_policy_context()
        self.assertEqual([], self.errors(True))
        self.assertNotIn("HAT-0002", self.spec["dependencies"])
        self.assertNotIn("HAT-0002", self.spec["pins"])

    def test_admission_helper_changes_invalidate_approval(self):
        for key in (".github/scripts/frontmatter_utils.py", ".github/scripts/record_paths.py"):
            self.approve()
            path = self.root / key
            path.write_text(path.read_text() + "Changed admission helper\n")
            self.assertTrue(any("stale or absent policy pin: " + key in e for e in self.errors(True)))

    def test_external_policy_change_requires_fresh_evidence(self):
        key, path = self.add_policy_context()
        path.write_text(path.read_text() + "Changed control\n")
        self.assertTrue(any("stale or absent policy pin" in e for e in self.errors(True)))
        self.spec["policy_pins"][key] = wf.digest(path.read_bytes())
        self.assertTrue(any("exact current definition" in e for e in self.errors(True)))

    def test_required_policy_cannot_be_replaced_by_extra_context(self):
        self.add_policy_context()
        self.spec["policy_pins"].pop("AGENTS.md")
        self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
        self.assertTrue(any("required policy/checker" in e for e in self.errors(True)))

    def test_external_policy_must_be_current_canonical_instruction(self):
        key, path = self.add_policy_context()
        original = path.read_text()
        for status in ("superseded", "draft"):
            path.write_text(original.replace("status: current", "status: " + status))
            self.spec["policy_pins"][key] = wf.digest(path.read_bytes())
            self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
            self.assertTrue(any("current canonical" in e for e in self.errors(True)))
        path.unlink()
        self.assertTrue(any("current canonical" in e for e in self.errors(True)))

    def test_extra_policy_rejects_forged_id_name_and_folder(self):
        self.approve()
        for key, identity in (("Skills/arbitrary-not-governed.md", "NONCANONICAL"),
                              ("Skills/SKILL-9998-wrong-id.md", "SKILL-9997"),
                              ("AIHats/SKILL-9996-wrong-folder.md", "SKILL-9996")):
            path = self.root / key
            path.write_text(f"---\nid: {identity}\ntype: skill\nstatus: current\nlinks: []\n---\nForged fixture.\n")
            self.spec["policy_pins"][key] = wf.digest(path.read_bytes())
            self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
            self.assertTrue(any("current canonical" in e for e in self.errors(True)), key)
            self.spec["policy_pins"].pop(key)
            path.unlink()

    def test_extra_policy_rejects_arbitrary_file_alias_traversal_and_link(self):
        self.approve()
        link = self.root / "external-policy.md"
        with symlink_boundary(link, self.report):
            for key in ("evidence.txt", "external-policy.md", "../outside", str(self.report),
                        "AIHats/./HAT-0001-fixture.md", "AIHats/HAT-9999-missing.md"):
                self.spec["policy_pins"][key] = wf.digest(self.report.read_bytes())
                self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
                self.assertTrue(any("current canonical" in e for e in self.errors(True)), key)
                self.spec["policy_pins"].pop(key)

    def test_missing_and_changed_test_evidence_rejected(self):
        self.approve()
        self.report.write_text("Changed report\n")
        self.assertTrue(any("test evidence" in e or "hashed evidence" in e for e in self.errors()))
        self.report.unlink()
        self.assertTrue(any("test evidence" in e or "hashed evidence" in e for e in self.errors()))

    def test_missing_boundary_test_rejected(self):
        self.approve()
        self.spec["tests"].pop()
        self.assertTrue(any("boundary test evidence" in e for e in self.errors()))

    def test_rubric_threshold_and_boolean_scores_rejected(self):
        self.approve()
        self.spec["review"]["scores"]["requirements"] = 24
        self.assertTrue(any("rubric" in e for e in self.errors()))
        self.spec["review"]["scores"]["requirements"] = True
        self.assertTrue(any("rubric" in e for e in self.errors()))

    def test_dangling_unreachable_and_closed_loop_rejected(self):
        self.spec["steps"][0]["next"] = "missing"
        self.assertTrue(any("dangling" in e for e in self.errors()))
        self.spec = contract()
        self.spec["steps"].append(dict(state("orphan", "terminal"), outcome="awaiting_steve", handoff=handoff()))
        self.assertTrue(any("unreachable" in e for e in self.errors()))
        self.spec = contract()
        self.spec["steps"][0].update(next="read", failure="read")
        self.assertTrue(any("no terminal path" in e for e in self.errors()))

    def test_retry_and_run_bounds_rejected(self):
        self.spec["steps"][0]["max_attempts"] = 4
        self.assertTrue(any("max_attempts" in e for e in self.errors()))
        self.spec = contract()
        self.spec["max_transitions"] = 0
        self.assertTrue(any("max_transitions" in e for e in self.errors()))

    def test_decision_requires_otherwise_and_failure(self):
        self.spec["steps"][0] = dict(state("read", "decision"), branches=[dict(when="matched", to="done"), dict(when="unknown", to="blocked")], failure="blocked")
        self.assertTrue(any("otherwise" in e for e in self.errors()))
        self.spec["steps"][0]["branches"][1]["when"] = "otherwise"
        self.assertEqual([], self.errors())

    def test_wait_has_timeout_and_resume(self):
        self.spec["steps"][0] = dict(state("read", "wait"), resume_when="Supplier evidence received", timeout="Review after two days; then block", next="done", failure="blocked")
        self.assertEqual([], self.errors())
        self.spec["steps"][0]["timeout"] = ""
        self.assertTrue(any("timeout" in e for e in self.errors()))

    def test_recursive_subworkflow_rejected(self):
        self.spec["steps"][0].update(kind="workflow", uses="FLOW-0001", return_policy="completed_only", budget_policy="shared")
        self.path.write_text(self.render().replace("links: [HAT-0001,", "links: [FLOW-0001, HAT-0001,"))
        self.assertTrue(any("recursive workflow" in e for e in wf.check_repository(self.root)))

    def test_bad_json_duplicate_and_unknown_keys_fail_closed(self):
        with self.assertRaises(ValueError):
            wf.load_contract('```workflow-json\n{"x":1,"x":2}\n```\n')
        self.spec["unrecognised"] = True
        self.assertTrue(any("contract keys" in e for e in self.errors()))

    def test_paths_reject_traversal_and_symlink(self):
        for value in ("../outside", str(self.report), "a/../b", "./evidence.txt", "a//b", "C:/outside", "C:outside", "a\\b"):
            self.assertIsNone(wf.safe_file(self.root, value), value)
            self.assertIsNone(wf.canonical_repo_parts(value), value)
        link = self.root / "link.txt"
        with symlink_boundary(link, self.report):
            self.assertIsNone(wf.safe_file(self.root, "link.txt"))

    def test_missing_required_id_fails(self):
        self.assertTrue(any("not found" in e for e in wf.check_repository(self.root, "FLOW-9999")))

    def test_terminal_has_no_hidden_transition(self):
        self.spec["steps"][1]["next"] = "read"
        self.assertTrue(any("unknown step fields" in e for e in self.errors()))

    def test_direct_reference_must_be_linked(self):
        self.path.write_text(self.render().replace("PLAY-0001, ", ""))
        self.assertTrue(any("frontmatter links" in e for e in wf.validate(self.path, wf.collect(self.root), self.root)))

    def test_malformed_approved_pin_containers_report_errors(self):
        self.approve()
        self.spec["pins"] = []
        self.assertTrue(any("pins must be a hash map" in e for e in self.errors()))
        self.spec["policy_pins"] = []
        self.assertTrue(any("policy_pins must be a hash map" in e for e in self.errors()))

    def test_context_links_do_not_imply_execution_dependencies(self):
        play = self.root / "Playbooks/PLAY-0001-fixture.md"
        play.write_text(play.read_text().replace("links: [SKILL-0318]", "links: [SKILL-0318, PLAY-0002]"))
        self.approve()
        self.assertEqual([], self.errors(True))

    def test_dependency_manifest_requires_complete_reachable_keys(self):
        self.spec["dependencies"].pop("HAT-0001")
        self.assertTrue(any("missing dependency declaration" in e for e in self.errors()))
        self.spec = contract()
        self.spec["dependencies"]["SKILL-0002"] = []
        self.assertTrue(any("exactly cover" in e for e in self.errors()))

    def test_new_prefix_uses_existing_serialised_allocator(self):
        import allocate_ids
        import parse_id_reservation_request
        (self.root / ".github/id-reservations.json").write_text('{"reservations": []}')
        request = parse_id_reservation_request.parse_request("[ID-RESERVE] FLOW 1", {"FLOW"})
        self.assertEqual([{"prefix": "FLOW", "count": 1}], request["requests"])
        values = allocate_ids.allocate_batch(self.root, request["requests"], "fixture")
        self.assertEqual(["FLOW-0001"], values)
        values = allocate_ids.allocate_batch(self.root, request["requests"], "fixture")
        self.assertEqual(["FLOW-0002"], values)

    def test_workflow_identity_is_not_hidden_as_support(self):
        import check_ids
        self.path.write_text(self.render())
        found, errors = check_ids.scan_tree(self.root, {"Workflows": "FLOW"})
        self.assertEqual([], errors)
        self.assertIn("FLOW-0001", found)
        from schema_rules import load_rules, validate_entry_frontmatter
        rules = load_rules("workflow.json")
        metadata = wf.parse_frontmatter(self.render())
        metadata.update(created="2026-10-16", updated="2026-10-16", tags=["workflow"])
        self.assertEqual([], validate_entry_frontmatter(metadata, rules))

    def test_absolute_validator_failure_exits_nonzero(self):
        import ast
        from unittest.mock import patch
        source = ast.parse((SCRIPTS / "validate_repo_state.py").read_text())
        main = next(n for n in source.body if isinstance(n, ast.FunctionDef) and n.name == "main")
        # Exercise the actual admission hook without invoking repository-wide candidate checks.
        main.body = main.body[:3]
        code = compile(ast.fix_missing_locations(ast.Module(body=[main], type_ignores=[])), "admission_hook", "exec")
        scope = {"REPO_ROOT": self.root, "sys": sys}
        exec(code, scope)
        with patch.object(wf, "check_repository", return_value=["invalid workflow"]):
            with self.assertRaises(SystemExit) as raised:
                scope["main"]()
        self.assertEqual(1, raised.exception.code)

    def test_every_step_needs_available_governing_playbook(self):
        self.spec["steps"][1].pop("playbook")
        self.assertTrue(any("governing Playbook" in e for e in self.errors()))
        self.spec = contract()
        self.spec["steps"][2]["playbook"] = "PLAY-9999"
        self.assertTrue(any("Playbook unavailable" in e for e in self.errors()))

    def test_executable_step_cannot_bypass_bound_playbook(self):
        self.spec["steps"][0]["uses"] = "PLAY-0002"
        self.assertTrue(any("must use its governing Playbook" in e for e in self.errors()))

    def test_approval_rejects_missing_or_gap_skill_coverage(self):
        self.approve()
        self.spec["coverage"] = {}
        self.assertTrue(any("Playbook coverage" in e for e in self.errors()))
        self.approve()
        self.spec["coverage"]["PLAY-0001"][0]["status"] = "gap"
        self.assertTrue(any("supporting Skills incomplete" in e for e in self.errors()))

    def test_every_control_state_needs_skill_coverage(self):
        self.approve()
        self.spec["coverage"]["PLAY-0001"][0]["steps"] = ["read", "done"]
        self.assertTrue(any("every step/control state" in e for e in self.errors()))

    def test_empty_wrong_type_or_undeclared_support_rejected(self):
        self.approve()
        self.spec["coverage"]["PLAY-0001"][0]["skills"] = []
        self.assertTrue(any("requires Skills" in e for e in self.errors()))
        self.approve()
        self.spec["dependencies"]["PLAY-0001"] = []
        self.assertTrue(any("declared Playbook dependencies" in e for e in self.errors()))
        self.spec["dependencies"]["PLAY-0001"] = ["SKILL-0318"]
        p = self.root / "Skills/SKILL-0318-fixture.md"
        p.write_text(p.read_text().replace("type: skill", "type: playbook"))
        self.assertTrue(any("Skill unavailable or wrong type" in e for e in self.errors()))

    def test_supporting_association_must_be_canonical_and_reciprocal(self):
        self.approve()
        p = self.root / "Skills/SKILL-0318-fixture.md"
        p.write_text(p.read_text().replace("links: [PLAY-0001]", "links: []"))
        self.assertTrue(any("canonical and reciprocal" in e for e in self.errors()))

    def test_coverage_evidence_freshness_and_requirement_changes_invalidate(self):
        self.approve()
        self.spec["coverage"]["PLAY-0001"][0]["requirement"] += " and a write"
        self.assertTrue(any("exact current definition" in e for e in self.errors()))
        self.approve()
        self.spec["coverage"]["PLAY-0001"][0]["evidence"]["sha256"] = "wrong"
        self.assertTrue(any("hashed evidence" in e for e in self.errors()))

    def test_draft_can_record_explicit_unfinished_coverage(self):
        self.spec["coverage"] = {"PLAY-0001": [dict(requirement="Unsettled technique", steps=["read"], skills=[], status="gap", evidence={})]}
        self.spec["gaps"] = ["Find or improve the supporting Skill before approval"]
        self.assertEqual([], self.errors())
        self.assertTrue(any("not current and approved" in e for e in self.errors(True)))

    def test_transitive_playbook_without_skills_cannot_be_approved(self):
        p = self.root / "Playbooks/PLAY-0002-fixture.md"
        p.write_text("---\nid: PLAY-0002\ntype: playbook\nstatus: current\nlinks: []\n---\nIndirect operation\n")
        self.spec["dependencies"]["PLAY-0001"].append("PLAY-0002")
        self.spec["dependencies"]["PLAY-0002"] = []
        self.approve()
        self.assertTrue(any("transitively executed Playbook" in e for e in self.errors()))

    def test_transitive_playbook_can_have_verified_caller_scoped_support(self):
        p = self.root / "Playbooks/PLAY-0002-fixture.md"
        p.write_text("---\nid: PLAY-0002\ntype: playbook\nstatus: current\nlinks: [SKILL-0318]\n---\nIndirect operation\n")
        p = self.root / "Skills/SKILL-0318-fixture.md"
        p.write_text(p.read_text().replace("links: [PLAY-0001]", "links: [PLAY-0001, PLAY-0002]"))
        self.spec["dependencies"]["PLAY-0001"].append("PLAY-0002")
        self.spec["dependencies"]["PLAY-0002"] = ["SKILL-0318"]
        self.approve()
        proof = dict(path="evidence.txt", sha256=wf.digest(self.report.read_bytes()), result="PASS")
        self.spec["coverage"]["PLAY-0002"] = [dict(requirement="Indirect operation supported", steps=["read"], skills=["SKILL-0318"], status="verified", evidence=proof)]
        self.spec["review"]["definition_sha256"] = wf.fingerprint(self.render(), self.spec)
        self.assertEqual([], self.errors(True))


    def test_two_outcome_contract_success_and_recovery_handoff_pass(self):
        self.approve()
        self.assertEqual([], self.errors(True))
        self.assertEqual({"completed", "awaiting_steve"}, {s["outcome"] for s in self.spec["steps"] if s["kind"] == "terminal"})

    def test_third_or_duplicate_terminal_rejected(self):
        self.spec["steps"][0].update(kind="decision", branches=[dict(when="matched", to="done"), dict(when="otherwise", to="extra")])
        for field in ("uses", "capabilities", "next"):
            self.spec["steps"][0].pop(field)
        self.spec["steps"].append(dict(state("extra", "terminal"), outcome="completed"))
        self.assertTrue(any("exactly two terminal" in e for e in self.errors()))

    def test_blocked_and_cancelled_are_not_service_outcomes(self):
        for outcome in ("blocked", "cancelled"):
            with self.subTest(outcome=outcome):
                self.spec = contract()
                self.spec["steps"][2].pop("handoff")
                self.spec["steps"][2]["outcome"] = outcome
                self.assertTrue(any("invalid terminal outcome" in e for e in self.errors()))

    def test_failure_cannot_be_reported_as_success(self):
        self.spec["steps"][0]["failure"] = "done"
        self.assertTrue(any("failure cannot transition directly to completed" in e for e in self.errors()))

    def test_missing_or_forged_shared_recovery_hook_rejected(self):
        for field in failure_handling():
            with self.subTest(field=field):
                self.spec = contract()
                self.spec["failure_handling"].pop(field)
                self.assertTrue(any("failure_handling" in e for e in self.errors()))
        self.spec = contract()
        self.spec["failure_handling"]["director"] = "HAT-9999"
        self.assertTrue(any("failure_handling" in e for e in self.errors()))

    def test_empty_or_incomplete_steve_handoff_rejected(self):
        for field in handoff():
            with self.subTest(field=field):
                self.spec = contract()
                self.spec["steps"][2]["handoff"][field] = " "
                self.assertTrue(any("actionable Library owner-owned handoff" in e for e in self.errors()))
        self.spec = contract()
        self.spec["steps"][2]["handoff"]["owner"] = "AI"
        self.assertTrue(any("Library owner-owned" in e for e in self.errors()))

    def test_noncompleted_child_cannot_return_success_or_reset_budget(self):
        for field, value in (("return_policy", "any_result"), ("budget_policy", "reset")):
            with self.subTest(field=field):
                self.spec = contract()
                self.spec["steps"][0].update(kind="workflow", uses="FLOW-0002", return_policy="completed_only", budget_policy="shared")
                self.spec["steps"][0][field] = value
                self.assertTrue(any("completed_only with shared budgets" in e for e in self.errors()))

    def test_recovery_hooks_must_be_declared_and_pinned(self):
        self.spec["dependencies"].pop("PLAY-0069")
        self.assertTrue(any("missing dependency declaration" in e for e in self.errors()))
        self.spec = contract()
        self.approve()
        p = self.root / "AIHats/HAT-0023-fixture.md"
        p.write_text(p.read_text() + "Changed recovery ownership\n")
        self.assertTrue(any("stale dependency pin: HAT-0023" in e for e in self.errors()))


    def test_visual_is_required_once_and_cannot_be_tampered(self):
        text = self.render()
        for changed in (text.replace(wf.render_visual(self.spec), ""),
                        text + wf.render_visual(self.spec) + "\n",
                        text + "\n```mermaid\nflowchart TD\nX --> Y\n```\n",
                        text.replace('Success', 'Invented success', 1)):
            with self.subTest(text=changed[-120:]):
                self.path.write_text(changed)
                self.assertTrue(any("visual" in e for e in wf.validate(self.path, wf.collect(self.root), self.root)))

    def test_visual_derives_every_decision_branch_and_wait_edge(self):
        self.spec["steps"][0] = dict(state("read", "decision"), branches=[dict(when="matched", to="done"), dict(when="otherwise", to="blocked")], failure="blocked")
        visual = wf.render_visual(self.spec)
        self.assertIn('S_read -->|"matched"| S_done', visual)
        self.assertIn('S_read -->|"otherwise"| S_blocked', visual)
        self.assertEqual([], self.errors())
        self.path.write_text(self.render().replace('    S_read -->|"otherwise"| S_blocked\n', ""))
        self.assertTrue(any("visual is stale" in e for e in wf.validate(self.path, wf.collect(self.root), self.root)))
        self.spec["steps"][0] = dict(state("read", "wait"), resume_when="Verified supplier result", timeout="One bounded observation", next="done", failure="blocked")
        self.assertIn('S_read -->|"Resume condition met"| S_done', wf.render_visual(self.spec))

    def test_visual_nested_call_and_shared_error_handback_are_explicit(self):
        self.spec["steps"][0].update(kind="workflow", uses="FLOW-0002", return_policy="completed_only", budget_policy="shared")
        visual = wf.render_visual(self.spec)
        for fragment in ('FLOW-0002', 'completed child only; shared budgets',
                         'S_read -->|"Completed child"| S_done',
                         'S_read -->|"Failure or noncompleted child; shared recovery first"| R_issue',
                         'R_issue --> R_director', 'R_director --> R_head',
                         'R_repair -->|"Repair independently qualified"| R_handback', 'R_handback --> R_gate',
                         'Origin read: verified qualified handback; same active component; only within existing authority and remaining bounds',
                         'Unresolved read: declared failure route after investigation'):
            self.assertIn(fragment, visual)

    def test_visual_recovery_returns_to_origin_without_reset_or_entry_replay(self):
        self.spec["steps"][0]["next"] = "second"
        self.spec["steps"].insert(1, dict(state("second", "playbook"), uses="PLAY-0001", capabilities=[], next="done", failure="blocked"))
        visual = wf.render_visual(self.spec)
        for origin in ("read", "second"):
            self.assertIn('R_gate -->|"Origin ' + origin + ': verified qualified handback; same active component; only within existing authority and remaining bounds"| S_' + origin, visual)
            self.assertIn('S_' + origin + ' -->|"Failure; shared recovery first"| R_issue', visual)
        self.assertNotIn('workflow entry', visual)
        self.assertEqual([], self.errors())
        self.spec["failure_handling"]["continuation_target"] = "restart_entry_and_reset"
        self.assertTrue(any("failure_handling" in e for e in self.errors()))

    def test_visual_excludes_receipt_metadata_but_review_binds_visual(self):
        original = wf.render_visual(self.spec)
        self.spec["pins"] = {"unused": "another hash"}
        self.spec["review"] = {"verdict": "PASS", "definition_sha256": "another value"}
        self.assertEqual(original, wf.render_visual(self.spec))
        self.spec = contract()
        self.approve()
        text = self.render()
        changed = text.replace('R_issue --> R_director', 'R_issue --> R_head')
        self.assertNotEqual(wf.fingerprint(text, self.spec), wf.fingerprint(changed, self.spec))

    def test_visual_is_not_a_semantic_or_runtime_guarantee(self):
        # Exact generated graphics cannot certify the factual truth of prose.
        self.spec["failure_handling"]["repair_loop"] = "The operator must verify the actual investigation and repair evidence"
        self.assertEqual([], self.errors())
        self.spec["steps"][0]["max_attempts"] = 4
        self.assertTrue(any("max_attempts" in e for e in self.errors()))

    def test_visual_entry_and_attempt_bounds_are_derived(self):
        before = wf.render_visual(self.spec)
        self.assertIn('E_start --> S_read', before)
        self.assertIn('global max_transitions: 10', before)
        self.assertIn('read · playbook · max_attempts: 1', before)
        self.assertIn('done · completed · max_attempts: 1', before)
        self.assertIn('blocked · awaiting_steve · max_attempts: 1', before)
        self.spec["entry"] = "done"
        self.assertIn('E_start --> S_done', wf.render_visual(self.spec))
        self.assertNotEqual(before, wf.render_visual(self.spec))
        self.spec = contract()
        self.spec["steps"][0]["max_attempts"] = 2
        self.spec["max_transitions"] = 20
        self.assertIn('global max_transitions: 20', wf.render_visual(self.spec))
        self.assertIn('read · playbook · max_attempts: 2', wf.render_visual(self.spec))

    def test_visual_cancellation_bypasses_repair_and_requires_policy(self):
        visual = wf.render_visual(self.spec)
        self.assertIn('Global interrupt · Library owner cancels during any active state or recovery', visual)
        self.assertIn('C_cancel --> C_ack', visual)
        self.assertIn('C_ack -->|"Library owner owns the next decision; preserve cancellation instruction"| S_blocked', visual)
        self.assertNotIn('C_cancel --> R_', visual)
        self.assertNotIn('C_ack --> R_', visual)
        self.spec["failure_handling"]["cancellation_policy"] = "repair_then_cancel"
        self.assertTrue(any("failure_handling" in e for e in self.errors()))

    def test_visual_unavailable_repair_does_not_invent_successful_handback(self):
        visual = wf.render_visual(self.spec)
        self.assertIn('R_head -->|"Investigated; no permitted repair, access, input or remaining limit"| R_gate', visual)
        self.assertIn('R_repair -->|"Unqualified; no further permitted repair or investigation"| R_gate', visual)
        self.assertIn('R_repair -->|"Repair independently qualified"| R_handback', visual)
        self.assertNotIn('R_repair --> R_handback', visual)
        self.assertIn('Origin read: verified qualified handback;', visual)

    def test_foundation_registers_control_surface_and_allocator(self):
        root = SCRIPTS.parents[1]
        config = json.loads((root / ".github/type-prefixes.json").read_text())
        self.assertEqual("FLOW", config["folders"]["Workflows"])
        self.assertIn("Workflows", json.loads((root / ".github/allowed-top-level-folders.json").read_text())["folders"])
        import validation_scope
        self.assertEqual("full", validation_scope.classify(["Workflows/FLOW-0001-fixture.md"])["mode"])
        import final_candidate_checks
        rows, _, _ = final_candidate_checks.generation_plan(["Workflows/FLOW-0001-fixture.md"])
        self.assertIn(("build_folder_indexes.py", ()), rows)
        self.assertIn(("build_library_graph.py", ()), rows)


if __name__ == "__main__":
    unittest.main()
