---
id: SKILL-0186
type: skill
title: Staging Reconciliation Handoff
status: current
created: 2026-09-20
updated: 2026-10-18
owner: Library owner

trigger_phrases: ["handoff to staging reconciler", "generated output reconciliation", "candidate ready sequence"]
links: [FLOW-0001, FLOW-0002, PLAY-0046, PLAY-0056, PLAY-0059]
tags: [skill, library-mechanics, reconciliation, workflow]
---

# Staging Reconciliation Handoff

Hands complete canonical source to the governed staging reconciler.

## When to use

Use after related source and mandatory companion changes are complete.

## Method

1. Confirm the final authored source state is complete.
2. Do not hand-edit generated views.
3. Enter workflow reconciliation only under AGENTS.md Library rule 6 and PLAY-0056 authority under AGENTS rule6 (declared approved-workflow entry grant, approved daily schedule, or standalone named one-off exception); a source save or mechanical commit does not authorise candidate validation or Actions. Otherwise hand off the complete source and pending validation without invoking the workflow.
4. Follow a reconciled head only when exact workflow evidence binds it to the pinned source, proves descendant ancestry and a generated-only diff; preserve an unrelated advance and stop.
5. Accept only `candidate-ready` on the exact final staging head. Preserve its evidence and verify current main remains the admitted base.
6. When the authorised PLAY-0056 handoff requires a draft PR, inspect the existing staging-to-main PRs before creating one. Reuse one matching draft or create exactly one draft under the current invocation; verify repository, head branch staging, base main, draft state, current head SHA equal to the final validated staging SHA and current base SHA equal to the admitted main. Re-read refs before the API effect; reject unexpected movement, duplicate/ambiguous PR state or missing draft/status visibility. Do not request review, mark ready or merge. Record the actual PR URL/head/base and readback; API success alone is not acceptance. Missing capability leaves a precise handoff blocker, not candidate completion.

## Benchmark case

A source update changes an index input; the author stops editing generated indexes and follows the workflow-created reconciliation head.

## Anti-patterns

- Authoring generated Board changes
- Accepting candidate-ready for an older head
- Treating an intermediate commit as final

## Stop

Stop at source hand-off with validation explicitly pending when no run is authorised; otherwise stop at the exact authorised candidate/draft-PR handoff acceptance or the precise terminal failure. Authority ends on completion, failure or stop; a repair does not grant another run.



## Candidate-to-draft handoff cases

Normal: exact-head candidate-ready plus unchanged main and a matching existing draft PR permits verified reuse. Creation is conditional on no matching PR and current authorised scope. Negative: stale status, wrong branch/head/base, non-draft or ambiguous PR state, unexpected ref movement or missing status/draft visibility blocks acceptance. Boundary: source-only handoff remains pending validation; an explicit approved-parent invocation may supply PLAY-0056 entry authority, but never merge authority. This extends the existing staging reconciliation handoff, not a new independent outcome or runtime executor.

## Trigger-to-result handoff

Apply PLAY-0056 Candidate trigger selection and recovery. At parent entry verify a callable candidate trigger and readable run/status/artifact/PR channels before child effects; record the route and exact input/boundary obligations, then resolve actual candidate values at validation entry. Ordinary source pushes can produce a skipped job; neither the skipped run nor source readback is candidate acceptance. Dispatch inputs and a marked push's event.before are not interchangeable without boundary proof. Verify exact observed event/source SHA, executed candidate job and final status/artifact before the draft-PR handoff. Missing tool, permission denial and skipped trigger have distinct diagnoses; invoke the Director-to-Head recovery investigation before declaring supported alternatives exhausted, preserving terminal stops and authority.

## Read-only entry assessor and boundary resolution

First apply PLAY-0056 “Required route assessment before a blocker or permission question”, including its canonical-file input route. “Run locally” does not mean “create a checkout”. A missing dispatch tool or checkout MUST NOT be reported as universal route exhaustion. The assessor checks supplied evidence structure and native route wiring; it does not authenticate anchors, execute the workflow or enforce what the operator tells the Library owner.

Run `python3 .github/scripts/candidate_entry.py --input <operator-evidence.json>` against the exact current source before parent effects (phase entry) and again before candidate publication/dispatch (phase validate). This is a pure route assessor, not authentication or an executor. Supply terminal=false, phase, and checks mapping each required gate to {verified:true,evidence:<actual anchor>}: current_authority, current_admission, actor_access, main_unchanged, expected_staging, scope_preserved, shared_bounds, guarded_source_write, source_readback, runs_read, artifacts_read, statuses_read and draft_pr_read. Unknown, false, malformed or unanchored gates block. Do not invent a verification value to obtain green output.

Supply dispatch/push route objects with actual callable boolean, access verified/unknown/denied, evidence anchor and the independently evidenced nonzero required_author_base for either route. The default substantive_source push mode additionally requires trigger_observed, meaningful_source and post_child_only true, independently evidenced required_author_base, and either exact expected_parent or (entry only) expected_parent=null plus parent_from_verified_child=true and explicit_author_base=true. That defers only future own-child parent binding, never the required author boundary or authority. Include explicit_author_base=true when a canonical Candidate-Author-Base trailer will represent a boundary different from the push parent. All source/actor/input evidence remains subject to review; the helper cannot verify the truth of supplied anchors.

Entry returns qualified_route_plan, never permission to dispatch or candidate success. At validate require child_completed=true and observed current staging_sha. Dispatch candidate_sha must equal that current head. Push candidate_sha is the prepared new commit: require planned_commit_verified=true, planned_commit_parent=expected_parent=current staging, a distinct candidate SHA and the exact verified required boundary/trailer; supply the actual prepared candidate_message, which the assessor checks for trigger eligibility and the exact resolved author base; inspect its actual sole parent, full proposed tree and message before moving staging. Native boundary resolution checks the strict trailer/dispatch/legacy-before input and proper ancestry again. A marked source push and its intended candidate trigger are one operational effect under the existing grant, after child completion; no source-only save is marked.

eligible_for_authorised_attempt means only that the explicit evidence and native route wiring passed this read-only check. Recheck current refs/targets immediately before the guarded effect; afterwards verify the actual event/source, executed job, diagnostics, exact final candidate-ready and draft PR. Missing result or mismatched/unknown effects follow PLAY-0056 recovery; never report a local assessor output as actual platform acceptance.

## Read transport is not a candidate verdict

Apply PLAY-0056 Transient read recovery inside the learning gate. A scoped GET may recover within its finite request/deadline budget before producing a result; it is not a replay of failed candidate validation. Read failure, partial pagination and successful later retrieval checks do not establish no prior failure or candidate-ready. Record actual run/attempt, failed gate, HTTP status, request scope, effects, recovery count/deadline and authoritative result. Unknown write outcomes never use blind transport retries. Preserve terminated runs and the separate changed-input candidate-repair cap; capture a diagnosed authored repair with the mandatory learning receipt.

## Explicit validation-request assessment

Apply PLAY-0056 Validation-request commit for already-staged corrected source. Select push.mode=validation_request rather than falsely setting meaningful_source for an empty commit. This existing push route uses the same guarded create_commit/update_ref capabilities after child completion; it adds no browser requirement or new permission.

Supply exact data.staging_sha/main_sha and push.request with source_sha, source_tree, base_tree, repair_commit_sha, main_sha, failed_trees and prior_requests. SHA fields are nonzero40lowercasehex; source/main must match current observed values, source tree differs from base and every unresolved failed tree, and prior_requests is a completely verified empty list for the same tree/boundary/main. Supply exactly six anchored request_checks: source_changed_since_base, relevant_correction, author_base_provenance, first_request_for_source, failed_tree_excluded and receipt_provenance. These proofs require actual current API/Git objects, diagnosed authorised correction and independent acceptance; booleans do not authenticate them.

At validation also supply verified planned_commit_tree equal to request.source_tree and the existing exact sole parent/current head/new candidate/message proofs. The actual message has one canonical Candidate-Validation-Request: source_sha trailer and one explicit Candidate-Author-Base trailer; native boundary resolution remains strict. Preserve the actual original repair receipt with an honest already-covered request disposition, not a fictitious captured control-commit edit. Unknown/prior request or write effects stop for object reconciliation. The helper distinguishes this route and leaves legacy substantive_source checks intact; eligible output still is not execution or candidate acceptance.

## Reusing an exact-current accepted handoff — 17 October 2026

Apply PLAY-0056 Exact-current accepted-result reuse before requesting another validation. Verify the current scoped source inventory, exact staging/main, current approved admission/definition/dependency baseline, all required receipt validity, exact executed successful candidate/artifact/status and matching open draft PR. The Playbook owns the full predicate; do not create a competing abbreviated acceptance rule.

Return a fresh verification packet with result_origin=reused and original acceptance pointers only when every required predicate passes. Do not claim a child, commit or candidate execution occurred in this invocation. A known required source change or invalidated acceptance follows the existing qualified new-validation path. An unreadable/unknown/contradictory assessment fails to shared recovery; it is not a no-prior-request verdict. Apply mandatory live checks and existing freshness contracts; no arbitrary TTL or permission to reuse expired proof.

Benchmark: unchanged exact candidate/base/instruction baseline and valid receipts plus current matching draft PR -> verified reuse without a commit/run. Changed main or instruction baseline -> no reuse. Missing history or status -> failure/recovery, not a fresh trigger. Pending same-tree request -> reconcile; no duplicate. These are operator rules; qualify actual cases and independent acceptance before FLOW approval.
