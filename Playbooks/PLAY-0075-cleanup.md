---
id: PLAY-0075
type: playbook
title: Cleanup
status: current
created: 2026-11-15
updated: 2026-11-15
owner: the Library owner
trigger_phrases: ["run cleanup", "run the cleanup playbook", "clean up this chat"]
links: [FLOW-0002, PLAY-0056, PLAY-0059, PLAY-0071, SKILL-0319]
tags: [playbook, library-mechanics, cleanup, continuity]
verification_state: documentary-reviewed
---

# Cleanup

## Trigger

the Library owner requests Cleanup for the current chat. This means the whole ordered operation: **fresh AGENTS read → source preparation → final-candidate validation → scratch deletion → verification and report**. It does not mean a whole-machine sweep, repository cleanup, canonical deletion, merge, application removal, or other-session cleanup.

Creating, reviewing or saving this definition does not invoke Cleanup. The workflow entry and component boundaries below are mandatory; reading a dependency grants no execution authority.

## Method

1. **Read the current AGENTS.md in full first.** At each Cleanup invocation, the executing AI MUST reread the live Library constitution before inventory, writes, validation or deletion, even if it read it earlier in this chat. Record its exact revision and read receipt in the invocation evidence. This specific reread was explicitly required by the Library owner on 15 November 2026. Failed/incomplete access blocks effects; a cached excerpt is not a substitute. Then load this current Playbook and the required capability contracts under AGENTS.
2. **Establish the operation.** Head Librarian owns the run; the executing AI remains accountable for every step. Record the request, accessible conversation scope, actors/access, task-owned scratch boundaries, current main/staging and any prior partial effects. For a top-level Cleanup request, enter the Cleanup mode of FLOW-0002 once, only after its current approved admission proves that mode, its dependencies and the deferred-deletion source path. When called as a component by that parent, verify the same admitted parent/run identity; MUST NOT invoke, re-enter or recurse into FLOW-0002. That admitted entry owns preparation/validation orchestration and inherited authority under AGENTS Library rule 6. Missing validation MUST enter the existing authorised procedure, not become an optional skipped step. This Playbook MUST NOT invent approval, launch an unapproved mode, or silently fall back to ordinary Commit Ready. Establish exact-current result reuse only through PLAY-0056's existing contract.
3. **Account for this chat's content.** Before source preparation, inventory all accessible messages, attachments, tool/agent outputs and task-created files. Include accepted documents/scripts/assets; facts and sources; user-proposed ideas; accepted and rejected decisions; corrections, reusable lessons, tests and diagnostic evidence; constraints, pending questions and unfinished work. Search canonical owners before creating records. Record unavailable or compacted content as a coverage gap; never claim access to another device or session. Await or safely coordinate active task producers before final inventory; do not terminate unrelated processes.
4. **Assign and prove dispositions.** Each relevant item MUST have exactly one current disposition: preserve/update at an identified canonical destination; already preserved with exact readback; retain temporarily with path, purpose, owner, next action and deletion trigger; or disposable with an evidence-based reason. Preserve proposals as attributed proposals and hypotheses as provisional. Cleanup is not acceptance of an unfinished script. Preserve its checkpoint and retain its actual file when current filing rules do not permit canonical capture. A summary MUST NOT replace a native deliverable or sole evidence needed for reproduction, validation, investigation or recovery. Retention/legal/security obligations remain binding; secrets are not copied into the Library.
5. **Prepare source with deletion deferred.** Use PLAY-0059's declared deferred-deletion path through the admitted parent. Apply current folder guides/templates, serialized reservations, frontmatter/native-companion rules, source provenance and existing work checkpoints. Apply PLAY-0071 in its confirmed-then-contextual order, with reciprocal endpoints and recorded outcomes. Use canonical owners rather than duplicate summaries; leave generated outputs to their owner. Capture authorised durable content and reusable learning before candidate freeze. No nested helper or source-preparation phase may delete task scratch in this mode. Return exact content/disposition evidence to the parent; source-readiness is not filing validation.
6. **Verify source and validate the final candidate.** Read back every required changed destination and companion. Match native files by exact bytes/hash and compare preserved knowledge, decision status and provenance with the inventory. The parent then invokes PLAY-0056 under its admitted authority or verifies qualifying exact-current acceptance. Require its authoritative successful final-candidate result, including required review, generated reconciliation and draft-PR evidence under that contract. Queued, running, cancelled, failed, stale, inaccessible or uncertain results do not permit deletion. Trigger success is not validation success. Preserve scratch while the existing bounded diagnosis, changed-input repair and revalidation procedure runs.
7. **Reconcile the final deletion gate.** When the admitted parent calls deletion_gate_and_closeout with verified successful validation evidence, recheck current candidate/base and the preservation mapping. Any source change affecting that candidate or mapping makes the earlier result inapplicable; satisfy the governing exact-candidate gate again only within still-valid authority and shared limits. Unrelated head movement, cancellation and terminal expiry follow the existing stop rules, never a silent new batch. Inventory newly created validation/cleanup files and active consumers. Every required capture/link/companion must be verified before any removal. Return any newly discovered durable item and preserved effects to the parent's declared recovery path. MUST NOT jump backwards, replay a completed component, reset attempts or renew expired authority. Preparation and validation may continue only through an eligible path under the same applicable authority and cumulative limits; otherwise retain the files and return the precise blocker. Never discard content to preserve a green result.
8. **Delete an exact allowlist only.** Apply SKILL-0319. Each entry binds its exact resolved path, session ownership evidence, file identity/hash, disposition and preserved destination/evidence or no-durable-value reason. Immediately before removal, prove the file is unchanged and no longer being written or consumed. Exclude user originals, pre-existing files, canonical Library/repository/application files, another session's files, active copies, unfinished deliverables, unique evidence and unknown ownership. Reject symlinks, junctions and escaping paths. Never recursively delete directories, use mixed-ownership wildcards, or expand the allowlist after a failure. Prefer recoverable deletion when available and state whether a file was moved to recovery or actually removed. A changed file needs reassessment, not deletion under its old receipt.
9. **Verify and report actual effects.** Compare the remaining task-owned inventory against the allowlist and retentions. Reconcile uncertain deletion outcomes before retrying; do not infer absence from a successful call or claim deletion on an inaccessible device. Report preserved canonical locations, final validation evidence, actual removals/recoverable moves, retained files with purposes/triggers, inaccessible items and the precise next action. Keep the disposition/step evidence in the existing operational handoff; do not create a receipt-only Library commit after validation. Substantive newly discovered content follows step 7.

## Component entry and evidence

FLOW-0002 owns the ordered graph and recovery; this Playbook owns Cleanup-specific gates and close-out. The parent may call:

- **inventory_gate:** steps 1–4; returns policy revision/receipt, scope/access, coverage inventory, disposition packet and exact unresolved gaps. No deletion.
- **deletion_gate_and_closeout:** steps 7–9; requires the same run identity, successful source evidence, final-candidate validation evidence and remaining shared limits. No preparation or validation replay is implied.

PLAY-0059 owns source mechanics, PLAY-0056 owns validation/accepted-result reuse, PLAY-0071 owns link review, and SKILL-0319 owns exact-file deletion mechanics. Their current required support remains mandatory; this Playbook does not replace their policies.

For each step record its actual state and evidence in the existing run packet: not started, active, verified, blocked, or not applicable with a specific reason. A prose claim, reviewer verdict or self-score does not prove execution. Cancellation ends effects immediately. Diagnose failures from observed evidence; do not assume a failure was deliberate AI choice.

Apply PLAY-0059 Manual FLOW operator gate for packet freshness and handoff. If the PR-description transport fails after validation, apply PLAY-0056 PR-description transport recovery; this does not restart validation or permit early deletion.

## Stop

Completion requires all scoped durable content captured and read back, the required final-candidate pass verified, every eligible file removed or recoverably moved as reported, and the remaining inventory matching only justified retentions. An unresolved capture, validation, ownership, access or deletion gap MUST NOT be reported as complete. Valid intentional retentions are reported, never hidden. Zero eligible files is a verified no-op, not a reason to fabricate a write or rerun validation.

Use the governing recovery procedure for missing prerequisites and permitted repairs; continue unaffected authorised work. Preserve partial effects and remaining limits. Do not ask the Library owner again for already-granted authority. Ask only for an evidenced user-owned fact, access or decision after permitted investigation; do not bypass the gate, reset budgets or revive a terminal run.

## Benchmark cases

These are acceptance specifications, not claims of executed tests.

| Case | Required result |
|---|---|
| Accepted output, idea, failed diagnostic, obsolete preview and unfinished script | Preserve each item's actual status/evidence; validate final source; remove only eligible residue; retain unfinished source with its next action. |
| No validation, or old pass followed by a source edit | Enter authorised final-candidate validation; delete nothing on the old pass. |
| Trigger accepted but run pending/failed/uncertain | Preserve files; verify actual result or use bounded recovery. |
| Candidate validation succeeds but the PR form is not observed | Keep the verified candidate evidence and record the PR write as unconfirmed. Reconcile the current description through PLAY-0056; use only a permitted alternate route with required approvals intact, then verify the saved description and open/draft head/base. No duplicate validation, premature deletion or false completion. |
| Exact-current accepted result with no new source | Reuse only if PLAY-0056's full predicate holds; still perform final coverage and file identity checks. |
| Partial save or missing companion/link | Preserve affected source and all scratch; repair/read back/validate before deletion. |
| New file or content edit after inventory; active producer/consumer | Reclassify and preserve; never delete from stale evidence. |
| Unknown ownership, symlink/junction, other session or inaccessible device | Exclude and report the exact gap; no widened sweep. |
| Partial deletion or uncertain response | Verify individual paths and report actual effects; no blanket success or blind retry. |
| Empty chat/no eligible files | Verified no-op with applicable evidence; no invented commit, reservation or validation replay. |
| Compacted history or unique unfinished evidence | State coverage limits and retain necessary evidence; no exhaustive claim. |
| Cancellation, changed main, unrelated staging movement, exhausted budget | Stop dependent effects under the governing contract; preserve evidence; no terminal restart. |
| Cleanup source-preparation caller | Zero deletions before final validation; ordinary Commit Ready behaviour remains under its own admitted contract. |

## Link review — 15 November 2026

Confirmed result: links_created. the Library owner approved the source-preparation → validation → scratch-deletion design and requested its creation with two independent reviews. The concrete direct supporting contracts are FLOW-0002, PLAY-0059, PLAY-0056, PLAY-0071 and SKILL-0319; reciprocal integration changes belong in the same final candidate.

Contextual result: no_contextual_links. Inspected the current Playbooks catalogue, Skills catalogue, PLAY-0009/0033 continuity contracts and PLAY-0037/SKILL-0319 cleanup scope. The direct support above supplies the useful retrieval paths; a broad estate-hygiene relationship would misstate this chat-only scope. No unrelated Project, Ticket or application relationship is asserted.

## Creation evidence and qualification limits

Reserved by issue 516: PLAY-0075, allocator commit 7fe943cfd97691f7c7e75ed2ada0257ae129e102. User-approved sequence and the two earlier conceptual reviews were assessed on 15 November 2026. Those earlier conceptual reviews did not approve saved source or integration.

Creation and independent source reviews do not constitute candidate validation or workflow qualification. Until the Cleanup parent mode, source deferral, affected tests, dependency pins and independent admission evidence are complete, end-to-end invocation is not qualified. This explicit gate must be cleared through the existing qualification process, never hidden by a current status field.

## Independent saved-source review — 15 November 2026

Two separate non-author agents, cleanup_completeness and cleanup_controls, reread AGENTS first and independently reviewed the saved PLAY-0075 at commit 62933d6b8c1836e68935b8f8893b0a423170beb4. Both returned documentary PASS after correcting recursive parent invocation, parent/child handoff wording and newly discovered-content recovery. Saved source blob: 28d74ed33030585016cd877d9b2c3859402b936e. Their instruction walkthroughs covered mixed accepted/unfinished content, incomplete history, partial capture/deletion, stale/pending validation, changed files, active consumers, path ownership, cancellation and exhausted authority. No runtime cleanup or candidate pass was claimed.

The separate integration review identified excessive unused write/trigger access on reuse states and a conflicting first-action briefing. Both were corrected in commit 68d3105278121e6681d94d53c374ff80e18b5ba5 and independently rechecked by both reviewers. Current exact-definition qualification and admission evidence belongs to FLOW-0001, FLOW-0002 and Reference/FLOW-cleanup-qualification-20261115-v1.md; this documentary review does not substitute for those gates or for per-invocation candidate validation.
