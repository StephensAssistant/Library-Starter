---
id: PLAY-0021
type: playbook
title: Work Intake & Scoping — Tickets and Projects
status: current
created: 2026-08-15
updated: 2026-11-05
owner: the Library owner
links: [PLAY-0006, PLAY-0007, PLAY-0008, SKILL-0318, PLAY-0030]
tags: [playbook, project-intake, scoping, feasibility, new-work]
trigger_phrases: ["project intake", "ticket intake", "scope new project", "scope a ticket", "scope existing app change", "turn request into project"]
migrated_from: PLAY-0021-old-library
---
# Work Intake & Scoping — Tickets and Projects

## Trigger

A new or resumed Ticket or Project needs enough shared understanding to take its next authorised step, including a change to an existing app, tool or report.

## Intent routing contract

Owns shared work intake and scoping for Tickets and Projects, whether the affected product is existing, new or not yet resolved. A request for a new feature does not establish that a new product or work record is needed. PLAY-0006 owns initial routing; PLAY-0007 handles material ambiguity; SKILL-0318 owns decision alignment through its exact upstream pair and governed clarification cadence. PLAY-0049 owns usable plan/decomposition. This Playbook produces or updates the requirements packet; it does not execute a delivery workflow, create external work or grant implementation/release authority.

## Method

1. **Resolve the work and affected product.** After required intake routing, open the selected canonical Ticket/Project and used plan when present. Distinguish the work record from the app, tool, report or process being changed. Determine whether the product is existing, genuinely new, or unknown from evidence; record exact identity/environment when known. Search before creating either a work record or a product. An ambiguous match remains unknown; similarity is not identity or a confirmed relationship.
2. **Discover before interviewing or designing.** Use SKILL-0115 to search relevant prior Tickets/Projects, Knowledge, Decisions, Skills, Playbooks, tables/data definitions and existing apps/tools/reports for reusable evidence and products that could be extended. Read relevant sources, including conflicting evidence; assess authority, currency, scope, access and applicability. Separate Known, Inferred and Gap. Reuse already-assessed evidence unless a change justifies another check. A blocked or incomplete search is not evidence that nothing exists.
3. **Bound the next decision.** Restate the problem/outcome, affected users, in/out scope and observable acceptance using the existing record and settled answers. Use the internal conditional prompts below only where their answer can change the next authorised prototype, review, diagnostic, implementation or test step. Resolve discoverable facts first. Use SKILL-0318 to ask the necessary remaining material questions, grouping independent questions when useful and deferring dependent questions until their prerequisites are known; then recompute the remaining branches. Ask priority only when the current record/conversation does not state it, as AGENTS.md requires. Do not collect perfect requirements for all future phases before a bounded useful step.
4. **Assess the approach.** Compare extending/reusing a suitable existing product, adapting a relevant component/pattern and building new only to the depth needed for the next decision. Use evidence of requirement fit, constraints, access, compatibility, ownership, verification and change impact. Prefer suitable reuse; do not force reuse when it fails the accepted outcome or creates unjustified risk. Record the chosen approach and the material reason alternatives do not fit; an unresolved material fit question becomes a bounded check or SKILL-0318 decision, not an assumed new build.
5. **Keep one canonical packet.** Put the problem/outcome, users, scope/non-goals, constraints, evidence/reuse assessment, assumptions/gaps, acceptance and agreed next action in the owning Ticket/Project's existing sections and used plan. Preserve history and existing parent/plan pointers; do not create a second undocumented brief or duplicate fields. Small work needs only proportionate inline content and a Work plan checklist; use PLAY-0049 for substantial sequencing or a linked plan. Use the selected folder's current creation guide only when a distinct new record is actually needed. Use PLAY-0030 only for real competing capacity.
6. **Advance iteratively.** Make the next phase, expected proof and unresolved dependency clear in that same packet using the phase guidance below. Proceed only within the request's authority and verified actor/access. At each useful result, verify what it proves, update evidence and next action, reassess applicable capabilities and return only to the affected phase when new facts change a decision. Do not restart settled intake or pursue invalidated branches.

### Internal conditional prompts

These are reasoning prompts, not a mandatory customer questionnaire or new schema. Omit a prompt when evidence already answers it or its answer cannot change the next step.

- If the target is unclear: which existing product/record and environment is affected; what evidence distinguishes it from similar candidates?
- If the need is unclear or solution-led: who needs what behaviour, what happens now, and which concrete example shows the problem or desired result?
- If scope/acceptance is unresolved: what is the smallest useful outcome, what is excluded, and what observable result would the Library owner or the evidenced acceptance authority accept?
- If reuse may fit: what existing product, table, definition, decision or technique covers the need; what must change, and what evidence could reject that fit?
- If data/integration affects the step: what authoritative source, definitions, keys, grain, freshness and interface are required; which remain unverified?
- If feasibility or effects matter: which systems, actors, access, constraints, dependencies and affected consumers must be checked before this step; is the proposed effect authorised?
- If a visible or uncertain interaction needs agreement: what smallest sketch, prototype, sample or rendered review would resolve it? A clear tiny defect may go directly to a focused fix and test; intake does not require a mockup for every Ticket.
- If delivery/acceptance is approaching: what test proves this increment, what regression or independent review applies, and what remains before acceptance, release or closure? Apply actual owner contracts rather than inventing sign-off roles or a universal UAT gate.

### Next-step readiness

| Proposed next step | Evidence needed for this step | If something is missing |
|---|---|---|
| Reviewable example or prototype | Identified audience, intended behaviour/output, bounded scope and the specific question the example will answer. Use verified data or label illustrative data and unverified assumptions explicitly. | Resolve only a gap that changes the example; keep later implementation dependencies visible. Feedback proves the reviewed requirement/design, not live correctness. |
| Real increment in a suitable test space | Sufficient agreed requirements and observable acceptance for this increment; verified target/environment, actor/access, source/interface definitions and applicable controls for the actual change. | Block the dependent build/test action; continue an independently useful authorised example or evidence check. Do not substitute a mockup for runtime proof. |
| Live promotion | The actual release owner's required implementation, test, independent review, acceptance and operational evidence for the exact candidate, plus live-action authority. | Retain the named missing proof/authority and test-space state. No prototype, phase label or customer comment authorises promotion; apply existing release/hypercare controls. |

Use an example when it can settle a material uncertainty; do not insert one into a fully specified small fix merely to fill a phase. Record which feedback or observation moves the next step forward and which questions remain open.

### Phase guidance in the existing work plan

Use requirements → discovery → approach → delivery → verification → acceptance/closure as explicit progression, scaled to the work. These are planning phases, not new status values or an approved Workflow. Record one current phase per work item; put concurrent activities, blocked discovery and later-phase gaps in evidence/next-action notes rather than combining phase labels. A small Ticket may express the phases in a few inline steps; a Project and its child Tickets may be at different phases, and each child's evidence/acceptance remains distinct.

- **Requirements:** enough agreed outcome, scope and acceptance to investigate the next uncertainty; record remaining gaps rather than guessing.
- **Discovery:** relevant evidence and existing-product fit assessed, or a precise search/access blocker and its dependent action identified. Discovery can refine requirements.
- **Approach:** an evidence-backed reuse/adapt/new choice, constraints and smallest next increment are agreed to the extent needed for its authorised action.
- **Delivery:** the authorised increment is produced against that scope. A proposal, mockup or development/test result is labelled as such; it is not production delivery.
- **Verification:** compare actual results with acceptance and applicable regression/review controls; retain source/revision/environment, outcome and limits. Failed or missing proof reopens the affected decision or delivery step rather than implying acceptance.
- **Acceptance/closure:** obtain the acceptance required by the actual owning contract and follow the folder closure guide before changing status. Implementation, test success, release and closure are distinct facts; never infer one from another. If incomplete, retain the remaining gap and next action.

## Benchmark cases

Unexecuted design cases for the proposed procedure:

- Existing report feature: prior Ticket/Decision and current app show a suitable extension; update the existing work packet, resolve only the missing behaviour/acceptance choice and plan the smallest development increment rather than starting another app.
- Small clear defect: target, priority, reproduction and acceptance are recorded; reuse known evidence and proceed to the authorised focused fix/test without a questionnaire, separate plan or mandatory mockup.
- Unclear product/access: two similar apps exist and the authoritative source cannot be read; retain unknown identity/access Gap, distinguish candidate evidence and resolve the blocking fact before dependent change. Do not claim a negative search or choose by title resemblance.
- Changed requirement during verification: return to the affected requirement/approach and update dependent proof; preserve settled decisions and history. A child Ticket may need discovery while its parent remains in delivery.
- Near-miss: a factual lookup or a request only to save a settled record uses its owning capability; this Playbook does not manufacture intake or authorise executing the newly recorded work.

## Stop

Stop intake when the canonical packet supports the next authorised action with its observable check, or records a precise decision/evidence/access blocker or defer/decline decision. Continue delivery only when separately in the authorised scope. No Mission Control ladder, SQUEEZE cycle or repeated interview.

AGENTS.md owns shared authority, evidence reuse and task boundaries. Written phase guidance and cases do not prove workflow admission, runtime execution, acceptance or filing.

## Contextual links

- `SKILL-0115` — `shared_method` — Retrieve bounded evidence discovery and existing-product reuse assessment for the next intake decision; advisory, not a confirmed dependency or authority.
