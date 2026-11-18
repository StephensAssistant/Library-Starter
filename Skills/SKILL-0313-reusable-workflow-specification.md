---
id: SKILL-0313
type: skill
title: Reusable Workflow Specification
status: current
created: 2026-10-10
updated: 2026-11-09
links: [FLOW-0001, FLOW-0002, HAT-0023, PLAY-0069, SKILL-0320, SKILL-0321]
tags: [skill, ai, software-methods]
trigger_phrases: ["specify a repeatable agent workflow","capture a repeatable work loop","design process guardrails","strengthen playbook guardrails"]
---

# Reusable Workflow Specification

Extract an observed repeatable operation into an explicit invocation contract with inputs, state, completion and recovery.

## When to use and intent routing contract

Activate for specify a repeatable agent workflow, capture a repeatable work loop, design process guardrails, strengthen playbook guardrails or equivalent intent. Exclude schedule a workflow automatically, expand task authority with a prompt. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Start from observed successful work and its failures. Search for an existing capability owner; extend it when the job is the same rather than creating a duplicate workflow.
2. Specify trigger, inputs, prerequisites, current authority, required evidence, actions, expected outputs and persistence owner. Use a Skill for a distinct technique, a Playbook to combine Skills for one defined outcome, and a governed `Workflows/FLOW-<NNNN>-<slug>.md` record for orchestration across Playbooks or nested Workflows. Follow Workflows/README.md and its creation contract; reuse existing owners and do not migrate existing records automatically.
3. Require an existing governing Playbook for every workflow step/control state, including nested invocation and its exits; executable steps use that Playbook. Build complete requirement-to-step-to-Playbook-to-Skill coverage from current contracts with confirmed canonical supporting associations, executable dependencies and verification evidence. Missing or incomplete support blocks approval; search/reuse first, amend the same capability owner or create only a distinct carefully scoped missing capability under the current governed process. Resolve material ambiguity, test affected callers and obtain updated independent review before approval. For each material step, specify authorised scope and target/actor/access, evidence and prerequisites, allowed effects and limits, observable success check, failure/stop/recovery path and accountable owner. Reuse applicable shared controls; identify whether each is enforced by permissions/code or remains an instruction. An unimplemented control is a Gap, not proven protection. Apply AGENTS.md's 95 gate; unresolved gaps route to SKILL-0318's current domino-paced decision cadence before dependent execution.
4. Define bounded iterations, idempotency, internal attempt stop conditions, recovery and exactly two service outcomes: completed success or awaiting_steve. Keep transient run state separate from reusable instructions; point to canonical records instead of copying mutable state.
5. Hand below-gate findings to the responsible Hats with evidence, required correction, current authority and acceptance checks. Complete authorised repairs and recheck against the same rubric; keep authority and human-decision blockers explicit. A score cannot supply missing execution evidence or independent acceptance.
6. Test one normal, failure and out-of-scope invocation. Label a captured contract untested until those checks provide evidence; capture alone is not a completed tested workflow. If scheduling is later requested, use the automation owner with explicit future-work authority; capturing a loop does not create a recurring task.

## Anti-patterns

- A prompt that authorises new sends, deployments, spending or background activity.
- Unbounded recursion, hidden run state or a duplicate canonical document.

## Pilot-derived creation checks — 16 October 2026

Workflow admission requires these checks: verify the live allocator execution branch/config before reserving a newly registered prefix; compare actual Playbook outcomes before proposing a count of components; and distinguish full associated-contract loading from actual executable dependencies. An existing broad Playbook may govern several phases only when its own phase contract defines each entry/exit slice, shared state/effects, ordering, success/failure and re-entry; never invoke its full procedure repeatedly. Verify support links reciprocally and search existing Skill owners before creating a gap-filling technique. Test draft admission and the actual approval-denial path; local graph walks and instruction tests cannot substitute for real runtime-control evidence. Preserve a needs_review draft until the required evidence exists.

Check refusal/cancellation reporting independently against PLAY-0069 Two-outcome service contract. Exercise absent admission, authority/access, prior-phase or ledger evidence; assess the actual read-only packet against that owner rather than redefining its prerequisites here. During metadata edits, preserve instructional code examples and placeholders outside the actual frontmatter; a global substitution can silently corrupt a template.

## Benchmark cases

- Guardrail boundary: a proposed write with unknown target access or an absent required success check remains blocked, regardless of a claimed score above 95. Discoverable facts are investigated; human-owned gaps follow current SKILL-0318’s Method for the governed question cadence. Read-only fact discovery remains available within authority.

- Positive: Capture a repeatable read-only report check with bounded retries and an evidence output.
- Negative/boundary: A loop that asks to keep running until a future date needs separate scheduling authority.

- Component-support boundary: an existing Playbook with a missing/incomplete supporting Skill, including a transitive called Playbook, blocks workflow approval even at a claimed score of 100. Reuse/amend/create the canonical capability, verify affected normal/failure/boundary behaviour and obtain fresh independent review; named IDs alone are not evidence of complete coverage.

## Stop

Stop at a tested reusable contract with a named owner and explicit blockers. No installation or scheduling is implied.

## Maturity

Upstream marks this method beta/in progress. This is a bounded Library adaptation, not evidence of production tooling reliability. Verify it against the actual task before relying on it.


## Source adaptation — 2026-10-10

[loop-me](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/loop-me/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.


## Admission qualification lesson — 16 October 2026

During FLOW-0001's first requested live admission, two policy pins differed from canonical source solely because the local materialisation added a trailing newline. Calculate instruction/policy hashes from exact current canonical bytes; verify local materialisation byte agreement before hashing, including final newlines. Structural draft PASS does not verify approved pins. Exercise admission against the actual canonical baseline and retain any remaining approval/runtime gaps; a failed gate must not be relabelled as a completed live workflow run. Corrected pins do not by themselves approve the workflow.


## Workflow lifecycle and admission handoff — 16 October 2026

Use HAT-0023 for workflow lifecycle expertise and PLAY-0069 for external qualification/recovery. For each material event record its existing handler Playbook, supporting Skills, responsible expertise, observable recovery/acceptance checks, authority, bounded attempts and stop. The Director first investigates available Library knowledge, then gives Head Librarian the evidence-backed expertise/repair requirement; Head makes inter-Hat assignments. Unknown or unsupported routes block their dependent action until the component/control is supplied and reviewed. Do not invoke an unapproved workflow to authorise its own repair. Read-only refusal reporting must remain possible when successful action prerequisites, ledger or write access are absent. A new Hat provides ownership, not missing procedure, platform permission or self-approval.

## Avoid circular qualification and permission loops — 16 October 2026

Director review of FLOW-0001 found two design defects: every repairable failure ended at blocked without a concrete continuation decision, and the pilot's blanket unverified-runtime wording plus absent concrete operator procedure allowed a circular interpretation of first qualification. The governing guides already permitted manual controls and independent primitive qualification; they did not mandate a whole live run or installed executor. Keep target stop/admission intact; use the existing external PLAY-0069 controller to investigate, route canonical component repair through Head Librarian, qualify changed behaviour and return exact eligibility. Do not add another workflow or decision node when the external handler already owns that decision. Require specific tested controls; manual operator gates remain instruction and must define prospective ledger/counters/evidence checks. Qualify named primitives and operator decisions before first admission, then review exact sources independently. An admitted whole-workflow run is later integrated evidence, not automatically a prerequisite to its own initial approval. Generic conditional requirements still need representative evidence.


Before adding policy/resource pins, inspect the checker's accepted contract and test the approved-fixture path: the pilot's draft check accepted added context pins while its approval path still required exactly five policies. The bounded correction preserves mandatory policies and validates extra current canonical instruction bytes without declaring them executable. Source draft PASS is not evidence that an eventual approved definition is representable. Keep unbound native/control resources explicit until their required baseline or pin owner is independently verified.

The admission checker's direct parser/record-recognition imports are unconditional controls too: bind their exact bytes as mandatory policy pins. A hash of the top-level checker alone cannot detect changed helper behaviour. Representative approved fixtures must reject either changed helper; other conditional native resources still require explicit scoped baseline/freshness verification.

## Conditional resource freshness — 16 October 2026

Director qualification of FLOW-0001 found that pinned instruction IDs and a top-level checker hash did not bind all actual native helpers, schema/configuration and conditional control resources. Record their finite canonical union in .github/workflow-resources.json and exact bytes in the workflow's resource_pins; pin the registry as policy too. Qualify changed/omitted/extra resources, malformed registry and unsafe/mutable paths with actual approved fixtures. A changed registry/resource or definition invalidates old acceptance; do not refresh hashes and retain PASS. Keep mutable work/customer/ledger/native-output values as fresh run inputs, and immutable external source revision/hash checks as explicit evidence rather than invented repository paths. Independent semantic review owns completeness; no mechanism grants actions or automatically executes the workflow.

## Live owner/evidence alias defect — 16 October 2026

Keep editable checkpoint records separate from frozen qualification proofs. Verify the two can evolve without invalidating one another.

The same guard review exposed an ancestor-folder seam: exact file overlap alone could permit replacing a directory containing frozen files. Repository planned-write preflight supports file effects only and rejects existing directory targets and symlink/alias/escape paths; broad folder effects remain prohibited, not an unverified success case. The directory denial is included in the targeted regression.

## Workflow-entry authority

For a workflow that declares PLAY-0056, use AGENTS rule6 and SKILL-0188: an explicit request to run the already-approved workflow supplies its declared component scope once at entry, not repeated per-Playbook exception prompts. Keep construction, approval and invocation distinct. Declare permitted effects and exclusions, exact current admission, actor/access, original and proved current baseline, nested return handling and shared bounds. Never infer actions from navigation links or a read contract. A source-only child remains useful independently; compose a parent for a wider outcome rather than silently expanding all callers. Carry the cumulative candidate-repair cap across components and external recovery. Test inherited acceptance plus source-only/draft/stale/undeclared/expired/access/scope/integrity refusals, failed-child denial and no merge authority. A new workflow or policy never approves or invokes itself.

Native fixture control exception: resource-registry version2 may explicitly list canonical executable Artifact .js/.py sources in native_fixture_sources when a reviewed test harness uses that code. Each listed path must be an actual safe canonical file used by a workflow resource set, and that workflow still binds its exact resource hash and refuses planned writes to it. This is not an exemption for mutable work records, report/HTML/TXT outputs or arbitrary Artifact data. Existing version1 registries remain accepted without the exception. Dynamic candidate/test data and Artifact metadata are fresh verified run inputs, not frozen instruction resources; record their exact named baseline and actual helper results at invocation.

Qualification must include normal legitimate source progression, not only initial green admission: mutable routing and benchmark datasets belong to exact original/proposed candidate inputs with preserved assertions, validators and independent mutation acceptance. Pin the code that validates those inputs; do not freeze the editable data and then reject every normal caller update. Whole-workflow planned-write checks still refuse any real frozen instruction/control or proof overlap.

## External execution-route qualification — 16 October 2026

For each required external effect, record effect, exact trigger/ref/SHA and author-boundary inputs, actual callable tool/UI/worker, authenticated actor/access evidence, permitted effects, readable run/status/artifact channel, supported alternatives, failure owner and shared limits. Check callable availability separately from permission: tool absent, observed permission denial and a skipped trigger are distinct diagnoses. Repository push permission is not dispatch proof. Keep current per-run values in the owning ledger; reusable instructions declare the procedure only.

Before effects, qualify a concrete route for every indispensable external dependency. Inspect the native trigger/input/status producer and current capability inventory; exercise relevant operator decisions with raw cases and actual available primitives. Source admission, mocked pipeline tests, source push/readback and a safe refusal do not prove external triggering or complete recovery. Keep source-qualified design, current-environment eligibility and actual end-to-end success as separate evidenced claims. An unresolved critical route blocks its dependent effects and any operational-feasibility PASS; a score or disclaimer cannot waive it. First source qualification need not run an unapproved whole workflow, but must define and test its actual route, pre-effect gate, permitted first-use proof and truthful failure path. A first authorised live operation must verify the observed exact event/head, non-skipped execution and required result; until then no platform success is claimed.

Head Librarian records the required specialist contributions, identity, inspected source/evidence, finding, correction and verdict. Guardrail Designer reviews branch/stop/handoff coverage; Reliability reviews external triggering, observability and recovery; Security reviews material identity/access/integration boundaries; Tester exercises behaviour; a separate non-author Validator assesses exact acceptance. Record a source-backed reason when a specialist trigger does not apply. A linked/pinned Hat, role switch or catalogue checklist is not evidence its review occurred.


## Service-failure qualification

For every indispensable external read, qualify whether and how transient transport can recover before its step returns: precise retryable class, exact request scope, total/per-request deadlines, attempt/page budgets, backoff, cancellation and exhausted outcome. Test the actual request/retry logic with transient-then-success, permanent failure, partial pagination, timeout and exhaustion. A successful-response mock alone leaves this path unqualified. Require complete trustworthy evidence before negative/absence results. Distinguish bounded read transport inside one step from replaying failed deterministic validation; never retry writes with uncertain effects or invent source changes to clear a transient request. Keep request attempts separate from candidate/source repair caps and preserve terminal expiry.

## Qualify the complete failure feedback loop

Apply PLAY-0069 Mandatory tracked repair and execution handback, Two-outcome service contract and Active-phase continuation versus re-entry through Workflows/README.md Single-owner rule bindings. Identify the local executing AI, canonical defect/work owner, evidence and affected return. Qualify duplicate observations, same-defect recurrence, distinct defects, missing allocator/tracker or unreachable executing AI, repair-only versus live acceptance, and eligible versus refused return. This technique supplies qualification cases; the operational controller stays in PLAY-0069.

## Canonical raw-byte qualification before admission

Before pinning or admitting a workflow from a local materialisation, verify every definition, executable component, policy, resource and existing qualification-evidence file against the same freshly resolved canonical Git tree. Recompute each Git blob SHA from the actual UTF-8 bytes (including every final newline) and compare with the canonical tree object; a self-consistent local checker is insufficient. Refuse incomplete/truncated trees, absent paths and mismatches. Recover exact bytes from the canonical object, never normalise whitespace or rewrite a canonical source to match a bad cache. Track intentionally proposed overlays separately, review their actual delta against that verified baseline, renew affected child before parent approval, and reverify exact saved bytes after guarded publication.


## Existing native control transport is distinct from source work

Qualify an indispensable operation against actual non-browser capabilities before treating missing dispatch API/browser as a universal execution blocker. Where PLAY-0056's explicitly declared validation-request route fits, distinguish already-staged relevant corrected source from the same-tree operational request commit. Test unchanged-failed-tree/SHA-only laundering, once-only request/history, completed-child/current authority, exact tree/sole parent/message/boundary, original learning receipt/full authored range, uncertain write and actual result requirements. Preserve substantive_source behavior and all existing budgets. Do not fabricate a new file edit to satisfy a transport assumption; amend and independently qualify an unnecessarily restrictive source/transport contract before using a new mode. Actual platform execution remains separate from source qualification.


## Capability-based implementation routes

the Library owner clarified on16October2026 at18:47BST that the same workflow can need different execution methods in Codex and another assistant. Select and qualify transports from the current operator's actual tools, authenticated identity, access and observable outputs; never hard-code product names as capability or make one assistant's browser/CLI a universal prerequisite. PLAY-0056 owns the shared route matrix. Keep a single outcome/guardrail contract with explicit qualified implementation branches, rechecked per invocation and environment. The existing assessor selects callable dispatch before qualified push; it does not infer capability from model identity.


## Two-outcome service contract — 16 October 2026

the Library owner's 16 October correction removed the former required blocked terminal; preserve historical failed/cancelled/blocked evidence under its original scope. Current service and handoff behaviour is owned by PLAY-0069 Two-outcome service contract, recovery by Mandatory tracked repair and execution handback, and continuation by Active-phase continuation versus re-entry. Apply Workflows/README.md Single-owner rule bindings to the schema/checker's required fields instead of copying that policy.

Qualify direct error recovery and verified handback, recurring/distinct defects, child noncompletion, missing tracker/access/ledger, no permitted retry, budget exhaustion, source movement, genuine-question escalation and immediate cancellation. Assess actual decisions and outputs; source review is not a live result.

## Exact contract-derived workflow visual — 16 October 2026

the Library owner required every built or edited FLOW to maintain a visual that represents its actual declared flow, rather than an inferred illustration. Maintain one workflow-json source of truth and derive the embedded Mermaid visual through the canonical deterministic renderer. Show every state and labelled branch, failure edges after the shared handler, nested calls, waits, the existing shared repair/verified executing-AI handback loop and the two service outcomes. Derive the shared protocol before each failure destination from failure_handling, including its conditional failed-step continuation and immediate cancellation acknowledgement bypass. Missing information goes to the actual awaiting_steve handoff; do not depict a fictional completed repair or executing-AI handback when its required input is absent. Depict cancellation according to PLAY-0069 Two-outcome service contract. Do not author a second independent diagram graph, guess missing paths or add business phases simply to make the picture work.

Regenerate after executable-contract changes; the source checker must reject absent, stale or duplicate generated visuals by exact renderer comparison. “100%” denotes exact checked structural parity with the declared graph, not a probabilistic score, model assurance or perfect runtime correctness. An actual independent reviewer still checks semantic completeness against Playbook/Skill/recovery contracts and observed evidence: exact rendering cannot repair an omitted decision, prove access or certify runtime success. Keep the fewest operational steps consistent with required controls, and preserve historical visual/evidence claims under their original scope.
 
## Minimum necessary workflow execution — 17 October 2026

Apply Workflows/README.md, Mandatory operating briefings and Single-owner rule bindings, to each declared step and its qualification cases.


Apply Workflows/README.md, Minimum necessary execution contract, including its author/reviewer gate; Workflows/_HOW-TO-CREATE.md binds that contract during authoring. Keep only the workflow-local operation/evidence/return and actual qualification results here.

Source: the Library owner's17October reflection on excess Commit Ready work and explicit instruction to tighten the four rules and future workflow template. Observed excess included overlapping test execution, oversized context output, repeated narrative/status probes and an avoidable interactive metadata route. The correction is narrower operator/author contracts, not fewer required checks or more automatic authority. Qualify both justified/unjustified repeats and expansions, unchanged-evidence reuse, immediate normal exit and a genuine human-owned blocker. These are manual instructions; source-check/wording review alone is not installed runtime enforcement.

## Five-part design framework — 17 October 2026

Apply Workflows/README.md, "Outcome, necessary work, decisions, recovery and proof" as the single governing definition. Before graph composition: define beneficiary, observable final state, exact population/targets, authority and per-requirement acceptance predicates; map every retained operation to a requirement, required dependency or named material-risk control; apply SKILL-0320 to decision rules and SKILL-0321 to semantic state assessment; define effect-safe bounded recovery; and specify the evidence oracle and owner before execution. Populate the existing schema fields and template sections. Do not add a phase, approval ceremony or evidence ledger for each heading.

Use MUST/MUST NOT/MAY ONLY with stated conditions. A missing value, contradictory source, vague predicate or unevaluated condition is a gap, not a permitted assumption/default. Locate accessible evidence; otherwise stop its dependent action and follow the existing owner/decision route. An explicitly authorised default needs its trigger and exact value. Approval requires the framework rejection rule and existing qualification gates. Changing dependent guidance invalidates exact acceptance; mark affected FLOWs needs_review, preserve historical proof and do not refresh pins or claim current approval without new qualification.

Benchmark: a "successful export" requirement with no target population, freshness or destination oracle fails design review. A representative normal case names the exact scope, output identity and independent predicate; the scenario must demonstrate the result, not merely contain those words. A matching Mermaid diagram cannot establish semantic or runtime correctness.

Source: the Library owner's explicit framework/wording instruction, 17 October 2026; the primary-source research in Reference/workflow-quality-research-20261017-v1.md. These are manual design/review requirements; no new runtime enforcement is installed.
