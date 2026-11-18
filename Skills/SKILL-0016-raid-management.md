---
id: SKILL-0016
type: skill
title: Risk Management
status: current
created: 2026-08-29
updated: 2026-10-31
links: []
tags: [project-management, risk, mitigation]
trigger_phrases: ["delivery risk", "risk register", "risk response"]
---

# SKILL-0016 — Risk Management

## Purpose

Manage uncertain future events or conditions that could materially affect delivery, acceptance or customer outcomes.

## Intent routing contract

Activate only for delivery risk, risk register, risk response or equivalent intent. Use associated records for their own jobs; this Skill does not silently expand into adjacent work.

## Method

1. State the uncertain condition, cause, affected acceptance outcome and dated evidence.
2. Record owner or decision authority where known.
3. Choose a response: avoid, reduce, transfer/escalate, accept with authority, monitor or contingency.
4. Set an evidence- or state-based review trigger.
5. Reclassify the item when it occurs, is disproven, is accepted or no longer threatens the outcome.
6. Synchronise material status changes to the governing parent or plan.

## Anti-patterns

- Calling an existing defect a risk.
- Recording a risk without a response or review trigger.
- Inventing probability, impact scores, owners or acceptance.

## Benchmark case

For an API whose future delivery may miss cutover, a passing risk records the uncertain event, completion impact, owner, contingency, review trigger and conversion to an issue if the deadline is missed.

Near-miss design case: the supplier delivery has already failed. Preserve the dated failure evidence and route the occurred condition as an issue; do not leave it represented only as an uncertain future risk or invent a probability score.

## Output and evidence

Record the inputs, decisions, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the affected outcome, evidence or response authority is unknown and materially changes treatment.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; former combined responsibilities moved to independent Skills while preserving existing links.
