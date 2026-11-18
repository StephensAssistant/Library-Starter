---
id: SKILL-0133
type: skill
title: Data Presentation Rehearsal
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["rehearse a data presentation", "practice my data story", "timed presentation rehearsal"]
links: [SKILL-0037]
tags: [skill, action-specific]
---

# Data Presentation Rehearsal

Rehearse an existing, evidence-validated data story for clear spoken delivery.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use when the story and evidence already exist and the presenter needs message, visual, delivery or timed rehearsal. Route story invention to [[SKILL-0037]].

## Method

1. State the single audience takeaway and requested action.
2. Run message, visual and delivery passes aloud; add a timed pass when required.
3. Record awkward transitions, unsupported claims, attention drift and sections needing rework.
4. Score each pass using observable criteria: the takeaway is stated once and accurately; every visual is oriented by metric, period and comparison; claims remain evidence-supported; transitions are complete; the requested action is explicit; and elapsed time stays within the limit.
5. Use listener restatement, unanswered questions, visible navigation errors, filler/repetition counts and timing variance as feedback where available; do not substitute confidence or preference.
6. Repeat only changed sections, then confirm the complete delivery satisfies every observable criterion.

## Decision and evidence details

Retain the story/version, intended audience, time limit when applicable and observations from each rehearsal pass. If rehearsal exposes an unsupported core claim, return that claim for story/evidence correction before treating delivery practice as complete.

Boundary design case: a presenter can deliver within time but cannot support the asserted cause. Record the evidence gap; timing and listener confidence cannot validate the claim. These are design cases, not reported rehearsal results.

## Benchmark case

A sales-decline presentation is rehearsed aloud; a listener correctly restates the takeaway and requested decision, every chart is oriented without correction, unsupported causal language is removed and the final run fits the meeting limit.

## Anti-patterns

- Rehearsing silently
- Practising an unclear or unsupported story
- Measuring success by confidence alone
- Accepting vague feedback such as “felt good” without an observable delivery result

## Sources

- https://www.storytellingwithdata.com/

## Stop

Stop when the presenter can deliver the supported takeaway naturally, orient each visual efficiently and remain within the time limit.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0133 | related_to | undirected | inherited_from_source_split | supports
