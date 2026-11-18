---
id: PLAY-0041
type: playbook
title: Continuous Learning, Repair & Feedback Loop
status: current
created: 2026-08-19
updated: 2026-11-05
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [FLOW-0001, HAT-0001, PLAY-0006, PLAY-0037, PLAY-0044, PLAY-0046, PLAY-0055, PLAY-0056, PLAY-0069, SKILL-0030, SKILL-0113, SKILL-0117, SKILL-0118, SKILL-0193, SKILL-0194, SKILL-0196, SKILL-0197]
tags: [playbook, gap-capture, lessons-learned, feedback-loop, cross-cutting]
migrated_from: PLAY-0041-old-library
---
# Continuous Learning, Repair & Feedback Loop

## Trigger

Run at task routing, every correction or contradiction, and task completion. A required Library layer may be missing, or a canonical asset may have helped, been missed, failed or conflicted.

## Method

1. Route through the Library: search current indexes, triggers, purposes and confirmed links; compare candidate boundaries; choose one clean match, stop on unresolved multiple matches, and declare a missing asset only after a zero-match search. Decompose mixed work, choose the smallest complete Hat sequence, switch at responsibility boundaries, then select every relevant Skill—no irrelevant Hats or Skills.
2. Apply SKILL-0030's selection rules: proven guidance survives; verified reusable patterns pass through their canonical owner to relevant Hats, Playbooks and Skills; small evidence-led mutations are proposed only when needed and retained only after equal-or-stronger results preserve the original purpose.
3. At task routing, any correction/contradiction and task completion, select exactly one event type from the total mapping below. Record the occurrence ID so one underlying outcome cannot count twice.
4. Search relevant signals and canonical assets for the same behaviour. Resemblance is not a confirmed link.
5. For an amendment apply the original-purpose invariant; for a new asset apply the new-asset invariant.
6. Every proposal states occurrence/evidence, diagnosed cause or gap, smallest delta, intended action, observable expected outcome, learning/facts/teamwork guardrails, check method, rollback/rejection condition and owner. New assets also require search-before-create/non-duplication evidence, one distinct boundary and a representative test.
7. Prefer the shortest wording that passes the same named frozen case/output criteria with equal or stronger action. Uncertainty retains the proven wording.
8. If purpose changes, route it as a separately governed replacement/new asset.
9. Verify facts through PLAY-0042. A material proposal changes a trigger, action, routing, ownership, authority, evidence/safety boundary, stop, shared rule or canonical asset contract. HAT-0007 runs a distinct pass: the reviewer did not author/edit, starts from the persisted evidence manifest, directly re-fetches named sources and records reviewer/pass identity plus hashes. A separate agent/session is optional isolation; a Hat switch inside the authoring pass is insufficient.
   `guidance-conflict` and `integrity-failure` always receive that distinct pass before resolution; `routing-ambiguous` receives it when material.
10. Apply the Library owner's current and standing authority before deciding to stop at a proposal. His 4 October 2026 instruction requires automatic same-session staging of bounded, verified, reusable Skill improvements and creation. Search first, preserve the existing purpose and authority boundaries, reserve new IDs through the serialized workflow and use the current folder contract. Other asset creation, purpose changes and consequential external action still require their own authority. Required independent validation/acceptance remains separate from the source write.
11. Recurrence reopens the previous adjustment and marks its control ineffective.
12. A retry after a failed `candidate-ready` run is incomplete until the newest repair commit carries SKILL-0030's exact repair receipt. `captured` must name a canonical owner changed by that authored repair; every no-change disposition needs a specific reason. The workflow fails closed on a missing or invalid receipt.

## Total event mapping

| Event type | Action | Receipt when mandatory |
|---|---|---|
| `guidance-success` | `keep` | `already-covered` |
| `guidance-missed` or `guidance-failed` | `propose-adjustment` | `n/a` pending; `captured` only after approved staged change |
| `guidance-conflict`, `integrity-failure` or `routing-ambiguous` | `stop-and-review` | `n/a` with pending reference |
| `cross-context-pattern` | common-owner analysis, then `propose-shared-rule` | `n/a` pending; then `captured` only after approved staged change |
| `hat-boundary-crossed` | `switch-hat` | `already-covered`, or missing-Hat row |
| `hat-missing-from-library` | `propose-new-hat` | `n/a` pending; then `captured` only after approved staged creation |
| `playbook-missing-from-library` | `propose-new-playbook` | `n/a` pending; then `captured` only after approved staged creation |
| `skill-missing-from-library` | `create-verified-skill-on-staging` under standing authority | `n/a` while evidence/allocation/write is blocked; `captured` only after the canonical Skill is staged |
| `task-local` | `no-change` | `task-local` with reason |
| `insufficient-evidence` | `no-change` | `n/a` with reason |
| `no-signal` | `no-change`; no standalone signal | `n/a` with reason |

`cross-context-pattern` requires two independent evidence-backed occurrences in different canonical assets or materially different work contexts, distinct occurrence IDs and common-owner analysis; never automatic link creation.

Primary-event precedence is: integrity → conflict → routing ambiguity → missing layer → failed → missed → Hat boundary → success → task-local → insufficient evidence → no-signal. Emit one primary; a later derived pattern may reference distinct prior occurrence IDs without replacing them.

## Lightweight boundary

Use existing work records, learning receipts and canonical assets. Do not create a record for routine keepers, launch background analysis, require a standing agent team or incur billed GitHub Actions minutes. Automatic bounded Skill capture is mandatory under the Library owner's standing instruction; it grants source writes to staging only and does not invoke PLAY-0059, PLAY-0056, PLAY-0055, candidate validation, Actions, paid services or schedules. Existing required validation runs only after zero incremental cost is verified. One on-use analysis pass is enough unless evidence or proposal changes.

For mixed work, a short `HAT-ROUTE` may name the sequence. Do not force email writing, documentation, scripting, testing and validation under one Hat; do not add a Hat that has no relevant work.

## Output

```text
LEARNING-SIGNAL: <occurrence ID> | <asset ID or missing layer> | <event type>
OUTCOME-EVIDENCE: <short observable result or source>
ACTION: <mapped action>
VALIDATION: <not-required|PASS|REVISE|REPLACEMENT-REQUIRED>
```

The total mapping is authoritative. `captured` is impossible until the the Library owner-approved canonical change is staged. For a failed-candidate repair, the normal output does not replace SKILL-0030's commit-message receipt.

## Check whether the improvement worked

Before changing guidance, freeze a representative trigger, expected observable action, critical prohibited action and baseline evidence in the existing owner. After the change, repeat that case and an independently chosen variation; include a missing-source or contradictory-evidence case and the affected caller. Retain source revisions, actual outputs, reviewer identity and unexecuted checks. Judge retrieval, correct evidence use and authority compliance separately; a critical boundary failure cannot be averaged away.

For shared-assistant changes, compare fresh ChatGPT and Codex sessions against the same saved work state: correct subject, evidence used before recommendation, preserved decisions, one next domino, and truthful handling of missing access. Include an interrupted-session resume and a correction repeated in a different context. Treat unread instructions, incorrect application and defective guidance as different causes; amend only the evidenced owner. Repository tests alone do not establish cross-assistant behaviour. Record measured effort or repeated clarification counts when available; do not manufacture time savings or a reliability percentage.

## Stop

Stop after the keeper is identified, the authorized bounded Skill capture is staged, or the applicable proposal/validation has reached its permitted boundary. State pending validation truthfully. Do not implement a proposal outside current/standing authority, create links from resemblance, or expand the current task beyond the Library owner's authority.

AGENTS.md owns shared authority, evidence reuse and task boundaries. SKILL-0030 owns learning classification and receipts.

## Workflow failures must return to execution

For an unhandled/unrecovered workflow failure, PLAY-0069 owns the mandatory tracked defect, Director-to-Head specialist assignment, evidenced repair, canonical lesson capture and executing-AI handback loop. Reuse the existing owner and one primary occurrence signal; do not create a duplicate Ticket for every read or repaired revision. A new defect uses the governed Ticket/allocator route only when no owner fits. Recovery inside an existing tested transient handler is not a separate failed outcome.

Learning completion requires the exact canonical prevention change or evidenced no-change disposition and its representative check. Record who verified it, the repair's real acceptance boundary and the remaining original outcome. This Playbook's learning stop does not end the outer workflow/recovery controller: return to PLAY-0069 for the permitted handback and observe the executing AI's result. Recurrence reopens the same ineffective adjustment under step11. A closed source repair is not proof of live success, and a lesson grants no new invocation authority or retry budget.
