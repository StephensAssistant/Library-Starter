---
id: PLAY-0059
type: playbook
title: Prepare Library Source
status: current
created: 2026-09-11
updated: 2026-11-15
owner: the Library owner
trigger_phrases: ["prepare library source", "run PLAY-0059", "upload to library staging", "file this chat", "upload everything we discussed"]
links: [FLOW-0001, FLOW-0002, PLAY-0075, PLAY-0029, PLAY-0046, PLAY-0055, PLAY-0056, SKILL-0012, SKILL-0023, SKILL-0024, SKILL-0025, SKILL-0026, SKILL-0113, SKILL-0114, SKILL-0183, SKILL-0184, SKILL-0185, SKILL-0186, SKILL-0187, SKILL-0188, SKILL-0319]
tags: [playbook, commit-ready, staging, filing]
---

# Prepare Library Source

## Trigger

the Library owner wants the current conversation’s Library work written to `staging` so PLAY-0056 can run without an authoring bounce, or the Library owner's enabled daily schedule explicitly authorises PLAY-0059 and PLAY-0056 for the resolved staging batch.

## Intent routing

Say **Prepare Library Source** or **run PLAY-0059** for this source-only Playbook. **Run Commit Ready** names the governing FLOW-0002 workflow; the former bare Commit Ready alias must not select this Playbook. A workflow calling PLAY-0059 by ID continues to use the same source-preparation phase contract.

This Playbook files and checks **source**. PLAY-0056 validates the candidate. PLAY-0055 merges.

A save / stage / upload request authorises only the source write. It does not run PLAY-0056 or PLAY-0055.

## Deferred scratch mode for Cleanup — 15 November 2026

An admitted FLOW-0002 Cleanup invocation passes `scratch_mode=defer_until_validated` through FLOW-0001. This mode is fixed at entry and cannot be selected from a filename, a missing validation result, or an operator preference. Ordinary source preparation uses `scratch_mode=source_closeout`. Missing, unknown or contradictory mode evidence blocks the affected phase.

In deferred mode, every instruction in this Playbook to delete scratch (including Method 3, 5 and 8, Scratch close-out and the unchanged-source return) is deferred. Perform the same inventory, capture, source readiness and exact readback; perform **no scratch deletion**. Return a verified disposition packet containing each exact task-owned path, ownership evidence, file identity, preserved destination/readback or no-durable-value reason, active-use/retention reason, and required deletion trigger. Mark `scratch_result=deferred`; never mark proposed removals performed. Include newly created preparation files. This is successful source preparation only, not completed Cleanup.

FLOW-0002 owns validation and only then invokes PLAY-0075 for the exact-candidate deletion gate and close-out. A failed, cancelled, unapproved or incomplete parent leaves all deferred files intact. The child never invokes validation, grants operational authority, or silently falls back to ordinary close-out. Ordinary `source_closeout` behavior remains governed by the existing method below. This change invalidates affected FLOW approval until exact requalification; a written definition is not invocation authority.

## Method

1. Read `AGENTS.md`. Load the changed type’s folder guide and the complete required association closure under AGENTS.md, including SKILL-0023, SKILL-0024, SKILL-0025 and SKILL-0026.
2. Stabilise the runtime batch before resolving its head. Read `main`, `staging`, and any active authorised `candidate-ready` or reconciler run. If a run is still in flight, wait for it to finish, then read both heads again. Adopt a staging advance only when exact workflow evidence proves it is the deterministic generated-output reconciliation for the pinned source SHA and it changes only reconciler-owned outputs. Resolve the initial batch from the verified current heads before effects. Once that baseline is recorded, unrelated or unproved staging movement stops this invocation on the first observation, even when the advance is a descendant and its paths do not overlap this pack. Preserve the advance and pending source; do not re-inventory onto it, change the proposal's expected head or restart readiness within this invocation. Changed `main`, overlap and non-descendant movement also stop. Only this run's exact verified source save, its matching ledger-only allocator receipt under Method4, or an explicitly permitted workflow-proven generated-only reconciliation may advance its expected head; record old/new heads and parent/diff/readback evidence without changing the frozen admission baseline. A separately valid fresh source request follows AGENTS.md and SKILL-0188; it does not resume or reset this stopped invocation.
3. Inventory this conversation only for an interactive run. For an authorised daily run, inventory the resolved staging batch's changed work records and retained Chat provenance under the scheduled learning review below. Each durable item is create, update, Artifact pair, Chat provenance, confirmed link, or explicit non-file. An AI-local scratch file is durable only when it is relevant to authoritative work and the Library owner has confirmed it fully functioning or explicitly accepted it. One-off tests and diagnostics are not Artifacts; capture material evidence in the owner, then delete the scratch copies. Search `staging` before create. Other chats and other AI sessions are out of scope unless the Library owner supplies or names their governed Library records.
4. For each known durable item that needs a new ID, reserve the required ID or IDs through SKILL-0024. Wait for the receipt, then continue. Never guess. Allocation is the permitted existing serialized reservation route, not candidate validation. Before proceeding after its own receipt commit, verify returned IDs, unchanged main, ancestor continuity and the exact ledger-only diff matching this request; record the old/new expected staging head and receipt provenance. Unrelated or unproved movement still stops. Never hand-edit the ledger or adopt a concurrent author update.
5. Assemble source from the live template. Update the existing owner when one exists. Apply SKILL-0026 companions and SKILL-0025 reciprocal links. Chat is daily-file, no frontmatter, outbound only. Do not hand-edit generated views or `.github/id-reservations.json`. When the Library owner confirms a relevant reusable scratch file is fully functioning or otherwise explicitly accepts it, file it in the Library: update the existing record, or file it as new work. Delete the local scratch copy when it is no longer needed. Do not file unconfirmed, partial, superseded, test-only or diagnostic scratch files.
6. Complete the learning review below for an authorised daily run, include any bounded Skill capture in the same source pack, then run the readiness gate below. Fix or name Gaps. Do not write a pack that the source checks will reject.
7. After the complete delta comparison below, write to named `staging` only when a nonempty required authored delta exists; an unchanged result skips this write and uses the verified unchanged-source return. Re-read the head and targets immediately before each write. If staging moved, preserve it and stop. Point at paths and SHAs.
8. After changed-source readback or verified unchanged-source return, complete the Scratch close-out below for this session's task-owned files. Do not retain residue merely because it might be useful; every retained file needs a named current purpose and deletion trigger.
9. Apply SKILL-0012. A nested call returns its compact source/result/evidence/effects/scratch/remaining-limits packet directly to its parent without a user pause; a standalone call returns a short completion summary. Produce a copy-ready continuation prompt ONLY when the Library owner explicitly requests one; completion, closure and a possible future session are not a request. If explicitly requested, produce one prompt. Its first instruction must direct the AI to `the configured Library repository` on `staging` and require a fresh read of `AGENTS.md`; then state the confirmed work record or subject, staged paths, current evidence/state, precise next action, explicit boundaries, and any intentionally retained scratch file with its purpose. Do not claim PLAY-0056 or PLAY-0055 ran unless they were authorised and completed.

## Scheduled learning review

Run once during the authorised daily Commit Ready pass, before candidate validation. This is a review of the resolved batch, not a nightly audit of the entire Library.

1. Record the stable batch revision and assessed paths. Use the previous successful daily run's evidenced boundary when available; otherwise inventory pending staging changes against the verified base and state that the daily boundary is unknown. Read changed Tickets, Projects, used plans, retained discussion/Chat provenance, accepted results, corrections, workarounds, and existing learning dispositions relevant to that batch.
2. Look for missing methods, repeated manual work, ineffective guidance, and verified improvements from successful work as well as failures. Compare candidates with the current complete Skill catalogue and read plausible owners before deciding. Read only the historical cases needed to establish repetition or non-duplication. Repetition is a discovery signal; planned, cancelled, unaccepted, or test-only work is not proof of a successful method.
3. Apply PLAY-0041 and the existing learning-classification, common-owner, and mutation-validation Skills. Keep adequate guidance; extend its existing owner when incomplete. Create only a verified, distinct, reusable uncovered method through the serialized reservation and current Skills folder contract. Preserve purpose, authority, source/date, failure constraints, stop conditions, and representative positive, negative, and boundary cases. One-off facts stay in their work owner; Skills combined for one outcome remain Playbooks, while orchestration across Playbooks or nested Workflows belongs in governed Workflows/FLOW records. Do not automatically migrate existing records.
4. Reuse earlier capture in the batch. Deduplicate evidence by occurrence and method; do not count repeated fields or repeated receipts as independent work. Include authorised bounded Skill source changes before freezing the validation candidate. New Skill creation remains blocked until allocation succeeds; do not invent IDs or relationships.
5. Record a concise assessment in the existing run evidence/output: assessed revision/boundary and paths; kept, updated, created, or deferred owners with source anchors; exact blocked or unverified capture. A no-change result is valid. Do not create an empty Skill, standalone review Ticket, or receipt-only commit to prove that the review happened.
6. Verify the source delta preserves identity, confirmed links, original purpose, and authority. Independent acceptance and exact candidate validation remain separate. If a material verified capture cannot be completed safely, report the blocker rather than claim the batch is learning-complete.

Only persisted or explicitly supplied discussions are accessible evidence. Never claim to have reviewed every chat or another AI's scratch. Report missing coverage precisely; unrelated unavailable history does not justify an estate-wide search. Do not add paid calls, new schedules, background workers, or another commit run. This checkpoint supplements automatic learning during work; it does not defer that capture until night.

## Scratch close-out

Apply SKILL-0319 after the authorised source has been written and read back, and before the final handoff. Scope is only exact files created or controlled by this AI in the active session; never infer ownership of user files or another session's scratch.

1. Inventory the task-owned local files and classify each one:
   - **File, verify, then delete local duplicate:** accepted reusable output that belongs in the Library. Complete its governed filing, verify the staged path/content, and delete the local duplicate unless it remains the named active working copy.
   - **Capture, then delete:** diagnostic, test, query result or failed iteration whose material evidence or reusable learning belongs in an existing owner. Preserve that evidence first, verify the owner update, then delete the local file.
   - **Retain temporarily:** an active input, unfinished deliverable, sole unreproduced evidence, or exact file required for the named next action. Record its exact path, purpose and deletion trigger in the handoff. “Might be useful” is not a retention reason.
   - **Delete:** superseded drafts, redundant copies, transient downloads, rendered previews, caches, test-only files and other residue with no remaining delivery, evidence, learning or recovery value.
2. Before deletion, prove the exact resolved paths stay inside the task-owned scratch/output boundary. Prefer recoverable deletion when practical; never use a broad recursive delete, unresolved variable, wildcard across mixed ownership, repository root, home directory or shared folder.
3. Do not delete a file merely because a summary exists. Retain it when the summary cannot reproduce evidence needed for an unresolved validation, investigation, audit or recovery step.
4. Read back the remaining inventory. Report what was deleted, what was retained and why, and any permission or ownership blocker. A blocked cleanup is a named Gap, not permission to widen scope or claim completion.

## Readiness gate

These are the source checks PLAY-0056 runs before generated views exist. The pack must already satisfy them.

Always:
- Pre-write readiness checks only this session’s exact task-owned scratch disposition/capture plan: accepted outputs to file, evidence to capture, exact proposed deletions and retained files with purpose/deletion trigger. Preserve required unsaved source and sole evidence. This plan is not proof of completed filing/readback/deletion. Actual source verification precedes cleanup; actual remaining inventory is accepted after changed-source readback or verified unchanged-source return. Unknown ownership/evidence is retained and reported. Never assume another session’s access.
- Frontmatter matches `.github/frontmatter-rules/` (SKILL-0023)
- IDs reserved, contiguous, consumed; filename = frontmatter `id` (SKILL-0024)
- Chat IDs reserved and consumed when a Chat entry is added
- Reciprocal `links` on both live endpoints; Chat outbound only (SKILL-0025)
- No secrets; no `main`; no guessed IDs or invented due/evidence
- Unrelated staged work and admitted `Reference/` blobs unchanged
- Full-file rewrites copy unread lines verbatim (SKILL-0026)

If the pack includes that type:
- Ticket / Project / Planning: planning companion, `Live plan:` pointer, operating fields
- Artifact: native + companion + valid `stored_at` + two consumed ART IDs
- Playbook / Skill: `trigger_phrases`, `.github/intent-routing.json` entry, benchmark case
- Knowledge: reusable and source-backed; otherwise keep it in the work record
- Reference: immutable after admission
- `.github/`, Workflows, Playbooks, Skills, AIHats or `AGENTS.md`: this is full-scope; do not treat it as an ordinary record edit

Leave generated Catalog/index/graph files to the reconciler.

## Checks and branches

- Missing fact that changes type, ID or a confirmed link: research source evidence first; ask the single highest-leverage remaining material question under SKILL-0318 and recompute after its answer and hold affected writes.
- Reservation unavailable: stop.
- Head movement after the invocation's initial baseline is recorded: continue only for the explicitly permitted proved own source-save/allocator effects or exact generated-only reconciler continuation. The first unrelated or unproved staging advance, or changed `main`, stops the stale invocation regardless of path overlap. Preserve it; do not restart readiness, retarget the proposal or absorb a different batch. A separate valid future source request requires fresh construction under SKILL-0188 and never revives this invocation.
- Head or target movement at the final immediate pre-write check: preserve it and stop; the next authorised run must stabilise and re-inventory it.
- Another AI or session owns required scratch-only material: stop and ask the Library owner to supply it or file an accepted checkpoint; never infer access.
- the Library owner also says “run commit playbook”: finish this Playbook first; enter PLAY-0056 only under its separate AGENTS.md Library rule 6 authority. A standalone unscheduled request must explicitly name a single-use one-off exception; an already-approved parent workflow may instead supply the declared inherited entry grant under AGENTS rule6. This source-only Playbook never starts PLAY-0056 by itself.

## Benchmark case

**Normal case:** this session contains a fully functioning reusable replacement, its completed diagnostic script, two superseded render/test files and an unfinished input. Expected result: file and read back the accepted replacement before deleting its redundant local copy; preserve the diagnostic's material result in the owner and delete the diagnostic; delete both superseded files; retain the unfinished input with its exact path, purpose and deletion trigger. PLAY-0056 is not run. Without an explicit prompt request, return the concise result/parent packet. If the Library owner explicitly requests a continuation prompt, it directs the next AI to `the configured Library repository` on `staging`, requires a fresh read of `AGENTS.md`, and names only the intentionally retained scratch.

**Cleanup boundary case:** a local file's ownership is ambiguous or it is the sole unreproduced evidence for an unresolved validation. Expected result: retain it, name the ownership/evidence Gap and stop cleanup for that file; never broaden deletion scope or treat a summary as equivalent evidence.

**Reservation case:** a new record is required and no reservation receipt exists. Expected result: request the required reservation, wait for the receipt, then file it; stop only if reservation is unavailable or fails.

**Reconciler case:** the run begins while `candidate-ready` is persisting deterministic generated outputs for the same pinned source. Expected result: wait for the run, verify the artifact, source SHA, ancestry and generated-only diff, adopt the reconciled head, then resolve the batch and continue. Do not pause the schedule merely because that verified reconciliation advanced staging.

**Concurrent source case:** after the initial baseline is recorded and before the first authored write, staging advances by an unrelated descendant commit touching no target in this pack. Expected result: preserve that advance and pending source, stop this invocation on the first observation, and perform no write, readiness restart, proposal retarget or batch adoption. Path non-overlap does not grant continuation. A separately valid fresh source request is a different entry under SKILL-0188, with no inherited counter/authority reset for the stopped invocation.

## Scheduled learning benchmark cases

- Successful repeated method with no owner: prove its distinct boundary, reserve its Skill ID, and include the sourced method and representative cases before candidate freeze.
- Existing method with a diagnosed gap: extend one owner; preserve accepted guidance and reject a duplicate Skill.
- Learning already captured earlier in the batch: retain it once and reuse its evidence; do not perform a second rewrite.
- Planned solution, cancelled execution, or one-off domain fact: defer unverified learning or retain the fact in its work owner.
- Missing Chat provenance or allocation failure: state the exact coverage/capture gap; do not invent access, an ID, or completion.
- Concurrent staging advance during capture: apply the existing stabilisation/stop rules; never absorb unrelated work.

## Stop

Source-readiness success requires durable work from this conversation on `staging` in folder-schema form; a named unresolved Gap is an internal noncompletion packet for recovery, not success. Task-owned scratch has a verified close-out disposition: unnecessary residue is deleted, and each retained file has a named purpose and deletion trigger. The readiness gate is explicit. Return source-readiness to an admitted approved parent when called as a child; that parent may proceed to PLAY-0056 only under its declared inherited workflow-entry grant. Otherwise stop before PLAY-0056 unless its AGENTS.md Library rule6 approved schedule or named one-off exception applies. A source save does not invoke candidate validation or Actions.


<!-- RELATIONSHIP-EVIDENCE: PLAY-0029--PLAY-0059 | related_to | undirected | authoritative_record | governs authorised recovery validation -->



## Workflow pilot phase contract — 16 October 2026

FLOW-0001 invokes named phases of this Playbook, not the whole Playbook repeatedly. Each phase is an entry/exit slice of the method: stabilise (2); inventory (1/3); assemble (4/5); readiness (6 plus Readiness gate); save (7, nonempty delta only); verify (changed-source readback or exact unchanged-source comparison); scratch close-out (8); result handoff (9; continuation prompt only on explicit request). Control and terminal states apply Checks and branches. Carry one run identity, stable source baseline and cumulative effects across slices; do not reset scope/authority or repeat previous writes. The daily learning phase delegates only the bounded resolved-batch review to PLAY-0041 under its existing guards, then returns to assembly. Interactive runs retain automatic task learning without claiming the scheduled batch review.

Readiness pre-write checks the declared close-out dispositions and prerequisite capture/readback plan; actual cleanup follows source readback. Completion requires verified remaining inventory and handoff. Failed or partial source writes MUST stop dependent writes and preserve exact saved paths/SHAs plus uncertain effects. Reconcile those effects through PLAY-0069. Apply the Manual FLOW operator gate to the exact phase/effect evidence before any continuation; use PLAY-0069 Active-phase continuation versus re-entry for the return decision. Source-readiness defects may be corrected only within established source-write authority; candidate validation never occurs here.

Confirmed support is recorded reciprocally below. These are actual explicit method requirements or phase-specific techniques, not topic associations. A Workflow reference or reading Commit/Merge contracts does not invoke them.

## Manual FLOW operator gate — 16 October 2026

Apply Workflows/README.md, Mandatory operating briefings, at this gate's initial entry, each declared phase and eligible continuation. This gate owns Commit Ready phase mechanics; PLAY-0069 Active-phase continuation versus re-entry owns generic return eligibility, and its Two-outcome service contract owns cancellation and truthful handoff.


For an admitted FLOW-0001 invocation, Head Librarian/operator maintains one prospective run ledger owned by its canonical work record, initially in this AI's exact task-owned working state: run identity, original request/authority source, exact definition/dependency/policy baseline, actor/access evidence, stable main/staging, current state, phase-attempt counts initially zero, transitions initially zero, known effects and current stop reason. Persist that ledger only at an already-authorised guarded source-save/checkpoint; logging grants no pre-readiness write and requires no remote commit per transition. Apply PLAY-0069 Two-outcome service contract when this ledger is incomplete or cannot be persisted for reporting. Preparing this gate or testing individual primitives outside the FLOW does not invoke it.

Before FIRST ENTRY to a nonterminal phase, verify current approval/admission and baseline, scope/authority/access, successful prerequisites, expected state, remaining global transitions and an unused phase attempt. Entry accepts the declared initial state with no predecessor; other phases require their applicable successful predecessor. Consume its single attempt before effects and record phase_status=active plus the exact incomplete operation. A recoverable subcheck/request failure does not itself terminate the phase. After handback qualifies under PLAY-0069 Active-phase continuation versus re-entry, resume the recorded incomplete operation only with phase_status=active and the same consumed single phase-attempt identity. Do not rerun the unused-attempt first-entry test. Count each eligible handback-to-origin continuation as one additional workflow transition; controller/request accounting remains separate under its governing owner. Returned phase_status=failed cannot satisfy this gate. Select one declared decision edge only from complete verified evidence. Use otherwise only for a complete authoritative no-match; missing, stale, contradictory or unreadable evidence follows failure/shared recovery, never otherwise; count every followed edge toward the declared global limit. Recheck head/targets immediately before source effects; use the actual guarded primitive, preserve exact saved paths/SHAs and verify results. A missing/contradictory check denies the dependent effect. The operator records checks and effects as they occur, not by reconstructing a successful trace afterwards.

Keep the initially resolved batch SHA as provenance and a separate current expected staging head. Advance that expected head only after this run's own exact verified source-save child, its matching ledger-only allocator receipt, or another explicitly permitted workflow-proven continuation under Method2/4. Record old/new heads, parent/diff and exact readback/receipt evidence. Unrelated or unproved movement stops the stale proposal/run under existing rules. This bookkeeping does not refresh the reviewed definition/dependency/policy baseline or retain invalidated admission.

An ineligible continuation follows the declared attempt-stop destination using PLAY-0069 Two-outcome service contract; admission refusal or exhausted bounds may return its read-only diagnostic without consuming further operational transitions. Head routes repairable source/procedure defects through PLAY-0069 outside the stopped invocation. For a separately valid fresh entry under that controller's Method 8, re-inventory and verify exact prior effects/idempotency before starting this gate.

Update that same operational run packet at every phase boundary, before handoff or interruption, and after reconciling an uncertain effect. Record the last verified operation and evidence, current phase/status and exact incomplete operation, confirmed and uncertain effects, retained file paths/purposes, remaining bounds, and the exact next permitted action or blocker. Keep the current summary consistent with its preserved history; never leave a pre-validation summary presented as current after validation has been verified. This is local operational evidence, not a receipt-only repository commit. Preserve terminal attempts as terminal and identify any separately admitted fresh run; never backfill successful transitions, revive an expired run or reset counters to make the packet appear complete.

This gate is an operator procedure (instruction), not automatically enforced software. Qualify its denial, counters, partial-effect preservation and branch decisions with representative observed operator cases and real effect-boundary primitives before approval. First approval does not require first running the unapproved whole FLOW. Do not claim installed runtime enforcement from a ledger, local graph walk or reviewer score.

## Qualification evidence and planned-write preflight — 16 October 2026

Keep immutable qualification proof separate from the editable work owner/run ledger. At inventory and again before effects, establish the exact planned source/companion/cleanup write footprint and compare it with the complete frozen read set: definition, executable components, policies, resources and every test/coverage/review evidence file, including called workflows. Use check_workflows.py --require-approved FLOW-ID with one --planned-write canonical/path per proposed source path; this read-only check supplies no write authority. Apply the same comparison to other planned effects in the manual gate. A normal owner/plan checkpoint must preserve admission. An overlap stops that dependent write and routes to external PLAY-0069 for an independently reviewed evidence/control correction; never refresh proof hashes, write into qualification evidence or reset a failed run. Keep the failed run terminal; any new admitted run needs a fresh identity and still-current request/scope/access.

## Approved parent invocation and return

An explicit request to run an already-approved parent may cover this source-preparation child and a separately declared PLAY-0056 step under AGENTS rule6. Parent and child record the same originating request, permitted effects and exact admission; child completion returns only source-readiness, not candidate acceptance or authority for another run. Use the governing Playbook phase contracts and shared prospective ledger/transition allowance; child edges count against the parent's remaining cap, attempts remain per declared phase, and the parent retains the cumulative candidate-repair counter. Save/readback/cleanup/handoff remain required. At parent-to-child return carry original and current expected staging heads, exact own-save/allocator ancestry/diffs/readbacks and partial effects. Unknown/unrelated movement stops; no silent authority, baseline or budget refresh. A failed/cancelled/admission-refused or awaiting_steve child returns its evidence/remaining-limits packet through the parent's shared recovery route, never its PLAY-0056 step. Apply PLAY-0069 Two-outcome service contract to the resulting child packet and root handoff.


## Two-outcome source return — 16 October 2026

Apply PLAY-0069 Two-outcome service contract to this source-only component. Return source evidence, effects, scratch dispositions and limits to its parent; source completion is not candidate acceptance. Use Approved parent invocation and return for the parent binding. Preserve the historical correction of the former third-terminal design; it is not evidence of a live result.

## Empty authored-delta source return — 17 October 2026

After inventory, assembly and source readiness, classify the exact authorised authored delta against the current expected head. A complete comparison yielding an empty delta must not create an empty source commit, allocate an unnecessary ID or fabricate an edit. Verify that every required scoped durable item and companion is already present with applicable source evidence; record source_result=unchanged, current head and exact paths/identities, then proceed through read-only verification, required scratch close-out and handoff. Unknown/missing target content is comparison failure, not an empty delta.

A nonempty accepted delta uses the existing guarded save/readback procedure. A changed/missing head or frozen instruction overlap still stops its dependent action; no no-op shortcut bypasses authority/admission/source-readiness or cleanup safeguards. An unchanged child return proves source readiness only; the parent separately assesses candidate evidence under PLAY-0056. Never relabel a new source change as unchanged to reuse an earlier candidate.

The source save phase is conditional: no-op entry is skipped, not a completed write. Verification accepts either an actual guarded-save receipt with exact new-source readback or an unchanged-source comparison receipt with current canonical identities. Preserve distinct actual effects in the return packet.

## Invocation decision and result return — 17 October 2026

Apply PLAY-0069 Two-outcome service contract for cancellation at the mode-selection boundary. For an eligible continuing operation, use complete verified run-source evidence: an actual enabled approved scheduled invocation selects daily learning; a current authorised interactive invocation that is not that scheduled run selects assembly. These normal predicates are mutually exclusive. A complete authoritative assessment proving neither mode selects the declared no-match handoff only after shared investigation identifies a genuine owner decision; never manufacture a question. Missing/stale/contradictory/unreadable evidence or evaluation failure takes failure/shared recovery, not otherwise.

Use the Manual FLOW operator gate's phase state and accounting. The result packet carries actual source_result/head/evidence/effects, scratch dispositions and remaining shared bounds. A continuation prompt exists only on explicit request, is never another completion gate and grants no Ticket closure action. Manual instructions are not installed runtime enforcement.
