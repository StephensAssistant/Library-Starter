---
id: PLAY-0024
type: playbook
title: Code & Skill Review Cycle — Catch Drift Before It Compounds
status: current
created: 2026-08-17
updated: 2026-11-09
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0004, HAT-0011, HAT-0015, PLAY-0006, PLAY-0015, PLAY-0019, PLAY-0028, PLAY-0033, PLAY-0046, PLAY-0069, SKILL-0117, SKILL-0318]
tags: [playbook, skill-review, ecosystem-health, drift, cross-referencing]
migrated_from: PLAY-0024-old-library
---
# Code & Skill Review Cycle — Catch Drift Before It Compounds

## Trigger

the Library owner requests or schedules a bounded code/Skill/Playbook audit; or a material mistake, failed validation, verified behavioural mismatch, or major architectural change creates a credible risk that affected records have drifted.

## Method

Inspect the named code, Skill or Playbook and every directly linked dependency and dependant for factual drift, duplicated or conflicting rules, broken relationships and obsolete behaviour. Compare shared claims across those records rather than assessing the named file in isolation. When a direct link exposes a contradiction farther downstream, follow only that evidenced conflict chain until it is resolved or precisely blocked; record every additional file brought into scope and do not expand through unrelated links. Return evidence-backed keep/change/remove recommendations, identifying the authoritative source for each conflict. When the review is triggered while an item is already being changed, surface the finding during that active work and resolve it before declaring the current update complete; do not defer a known inconsistency to an unspecified later review. Where authority or intended behaviour is materially ambiguous, present the evidence and follow current SKILL-0318’s Method for the governed question cadence; block only dependent changes. Present the concrete correction and obtain the Library owner's explicit confirmation when existing authority does not cover it or the applicable domain contract requires that approval. Complete corrections already authorised by the Library owner or standing instruction without a repeated permission ceremony. Within that authority, update every affected confirmed reciprocal relationship, verify the persisted changes and return findings to an actual non-author reviewer when independent acceptance is required. Neither the review nor source staging grants validation, release or merge authority.

For authored code or configuration, record the current non-author HAT-0015 PASS using HAT-0015's exact-diff receipt. The candidate pipeline rejects missing, duplicated, declared self-review, non-PASS and stale-digest receipts before preparation continues. A routing message, green automated test or author self-check cannot substitute for that receipt.

## Conflict-resolution acceptance

For each evidenced contradiction, identify the authoritative canonical owner under AGENTS priority and align every affected active instruction and executable control in the same repair. Mark retained historical guidance superseded without deleting provenance. Verify normal, boundary and failure cases lead to one consistent action, obtain required non-author review and record any remaining authority/decision blocker. No conflict is resolved merely by choosing one instruction in chat.

## Stop

Requested or event-triggered assessment and any authorised fixes are complete, with the affected surface and all direct links checked and every unresolved conflict assigned an authority or owner. Event triggers do not authorise unrelated estate-wide audits, automatic recurring reviews or unrelated new capability.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Matt Pocock method extension — 2026-10-10

Review separately for specification conformance and engineering standards: correct behaviour is not proof of maintainability, and tidy code is not proof of correctness. Use exact diff/source references and reproduce material claims where feasible. Correct authorised defects and re-check affected evidence until the bounded result is stable; do not keep cycling on subjective preferences. Independent review requires an actual separate reviewer, not the author relabelling a second pass. For a PR draft, lead with the concrete problem and resulting behaviour, add relevant validation and residual limits, and use a compact visual only if it clarifies the change. No branch commit, PR publication or message sending is implied. The upstream PR visual menu credits Dex Horthy/HumanLayer; this adaptation paraphrases the documentation method rather than copying its template.

## Source adaptation — 2026-10-10

[code-review](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/code-review/SKILL.md), [pr](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/pr/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.


## Explicit workflow support

For the current authored change review, use SKILL-0117 to evaluate evidence and SKILL-0318 for consequential unresolved review decisions. Preserve genuine reviewer independence and exact acceptance; reading a linked contract does not invoke its operational actions.



## Addy Osmani reference-method extension — 2026-11-01

Within the existing review scope, assess correctness, readability, architecture, security and performance separately; support material findings with the relevant artifact and contract evidence. Prefer a structural remedy that removes unnecessary concepts over one that only relocates complexity. Treat size thresholds as inspection signals, not acceptance rules.

For a consequential uncertain claim, isolate the smallest relevant artifact and its contract, including necessary callers, guards or evidence; omit the author's conclusion and reasoning. Where an independent reviewer is already authorised and available, ask for counterexamples and contract violations rather than validation. Reconcile each finding against the actual artifact as a contract misunderstanding, actionable defect, accepted trade-off or unsupported finding. Stop when no new material finding remains or after three cycles; record any unresolved issue without claiming acceptance. A self-check is not independent review and does not satisfy the existing non-author receipt requirement. This technique adds no reviewer invocation, external-model disclosure or acceptance authority.

Source adaptation: Reference/addyosmani-agent-skills-8bfcc1f/skills/code-review-and-quality/SKILL.md; Reference/addyosmani-agent-skills-8bfcc1f/skills/doubt-driven-development/SKILL.md. Pinned revision: `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`. Paraphrased reference techniques within this existing owner; the Library contract and current task authority govern use. No upstream workflow, trigger, link relationship, installer, agent configuration or operational authority is imported.
