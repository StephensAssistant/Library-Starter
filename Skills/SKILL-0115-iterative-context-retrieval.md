---
id: SKILL-0115
type: skill
title: Iterative Context Retrieval
status: current
created: 2026-09-20
updated: 2026-11-01
links: [HAT-0015, PLAY-0006, PLAY-0046, PLAY-0047, PLAY-0069]
tags: [ai, retrieval, context]
trigger_phrases: ["retrieve task context", "search distributed evidence", "refine context search", "assess existing product reuse", "find reusable work evidence"]
---

# SKILL-0115 — Iterative Context Retrieval

## Purpose

Retrieve the smallest sufficient evidence set from a distributed corpus through bounded refinement.

## Intent routing contract

Activate for retrieve task context, search distributed evidence, refine context search, find reusable work evidence, assess existing product reuse or equivalent intent. Owns evidence retrieval and an evidence-backed reuse-fit assessment for the current decision, including supporting and conflicting sources. It does not select product architecture, define acceptance for the Library owner, assemble a separate final work packet or execute the work. Hand intake/scoping to PLAY-0021 and consequential unresolved human decisions to SKILL-0318; use adjacent associated Skills for their own jobs.

## Input and outcome contract

Required inputs are the current authorised question/outcome, known target/work record and next decision or action; unavailable identity, sources/revisions, freshness or access are explicit Gaps to investigate, not inferred defaults. Retrieve only through available authorised surfaces. The output is a source-backed assessment sufficient for that next decision, with Known/Inferred/Gap, relevant alternatives, source/revision/date and applicability limits, useful rejected candidates, remaining uncertainty and next check/owner recorded in the canonical work record or used plan. A search hit is a candidate, never proof of identity, a confirmed link, permission or deployment state. This capability permits evidence retrieval/analysis only; it grants no product change, external send, status change or release authority.

## Method

1. Retrieve broadly once against the decision-changing questions.
2. Score candidates by authority, relevance, freshness and coverage.
3. Name uncovered gaps and refine terms, paths or record types.
4. Refine in bounded batches of up to three cycles, stopping earlier when material gaps are covered. At each batch boundary, assess remaining gaps: continue only with a new evidence-backed, authorised search/check that can change the decision; never repeat unchanged searches or proceed through a material gap.
5. Record why selected sources matter and why rejected candidates are insufficient.
6. Do not load additional discovery material once it cannot change the decision or verification. This sufficiency rule does not truncate AGENTS.md's mandatory confirmed association closure.
7. Before treating absent content as evidence, check the returned range, completeness and truncation. Retrieve omitted relevant spans or the tail before a whole-file absence conclusion. Reuse already-complete checked content; do not reread it merely because another display was partial.

## Evidence and existing-product reuse assessment

1. **Frame the discriminating question.** Separate the identity of an existing Ticket/Project from the app, tool, report, table or process affected. Classify the product as existing, new or unknown only from checked evidence. A new request or missing search match MUST NOT imply a new product.
2. **Search relevant kinds of evidence.** Within the existing bounded refinement method, search prior Tickets/Projects, Knowledge, Decisions, Skills/Playbooks, table/data definitions and existing app/tool/report records that could answer the question or satisfy the need. Search outside confirmed links when useful; retain a candidate as Inferred until its source is read and applicability assessed. Follow mandatory association closure independently of discovery sufficiency.
3. **Check the source before relying on it.** Compare authority, revision/date, environment, purpose and scope with the current need. Check source freshness under its owning contract and actual access when required. A prior design, proposal, prototype or test MUST NOT become evidence of current production capability without current deployed proof. Check contradictory evidence and chronology; unavailable, incomplete, stale or conflicting material evidence leaves a named Gap. A negative finding requires an appropriately targeted, complete search; denied access or truncation is not absence.
4. **Assess fit without forcing an outcome.** For credible candidates, compare reuse/extension of the existing product, adaptation of a component or technique, and a new build against the current requirements and constraints. Identify relevant fit, missing behaviour, compatibility/dependencies, actor/access/ownership constraints, change impact and a check capable of proving or rejecting the fit. Evidence may support reuse, justify new work or leave the choice unresolved. MUST NOT treat resemblance as compatibility, invent a confirmed relationship or silently choose an approach with a material gap.
5. **Stop at next-action sufficiency.** Complete retrieval when the selected evidence can support the next authorised prototype, review, diagnostic, implementation or test decision and its relevant limitations are visible. Evidence for every later phase is not required. If a material gap remains, refine only using a new discriminating authorised check under the existing batch limit; otherwise block that dependency and route the precise human decision through SKILL-0318. Reuse settled findings and reopen only the assessment affected by new facts.

## Anti-patterns

- Searching indefinitely because more related records exist.
- Using similarity as proof.
- Failing to state why a source was selected.

## Benchmark case

For an incident, a passing retrieval finds the current Ticket, authoritative script and recent evidence in two cycles and excludes older similar incidents that do not alter the diagnosis.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the evidence is sufficient or no new authorised discriminating search/check is available; surface the precise remaining decision-changing gap and block its dependent action. Use SKILL-0318 for the independent human decisions left after discoverable evidence checks.

## Retrieval lesson — 31 October 2026

During this review, an excerpt omitted SKILL-0287's later 22:56 recovery section. A whole-file absence claim was withdrawn after the omitted tail was checked. This is retrieval-error evidence, not new Sigma runtime proof.

Boundary design case: a displayed excerpt ends before a dated recovery section. Retrieve the relevant tail and reconcile chronology before declaring that recovery evidence absent. This case is unexecuted.


## Reuse-assessment design cases — 1 November 2026

Unexecuted cases for the technique extension; these are documentary expected outcomes, not runtime PASS evidence.

- Normal: an existing app plus a current prior Ticket and Decision cover the requested measure. Read the sources, distinguish current capability from the proposed extension, record fit/gaps and the smallest next proof for PLAY-0021; do not create a duplicate product.
- Boundary: a similar report uses incompatible grain or an obsolete source. Record why its evidence or component may still help but its whole-product reuse fails; do not force reuse or ignore the precedent.
- Failure/recovery: the source is truncated or access is denied. Check omitted relevant content when authorised; otherwise retain the precise Gap and blocked dependency. Never report “no existing app” from an incomplete search. Resume only the affected assessment when the evidence becomes available.
- Affected caller: a small defect with checked target, existing evidence and acceptance already has sufficient context. Return that assessment for the next fix/test without forcing broad product research or complete future-phase requirements.
- Near-miss: “build the report now” with a settled approach belongs to the authorised build capability; retrieval supplies only evidence needed for a material unresolved question and does not grant execution authority.

Source and verification limits: extends the existing bounded retrieval technique for the Ticket/Project intake requirement of 1 November 2026. Source inspection and written cases do not establish current app access, deployed capability, independent review, workflow admission or behavioural effectiveness.


## Contextual links

- `PLAY-0021` — `shared_method` — Retrieve the shared Ticket/Project intake and next-step readiness contract when reuse evidence must inform customer requirements; advisory, not a confirmed dependency or authority.
