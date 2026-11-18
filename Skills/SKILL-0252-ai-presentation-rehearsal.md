---
id: SKILL-0252
type: skill
title: AI Presentation Rehearsal
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0038, SKILL-0039]
tags: [skill, action-specific]
trigger_phrases: ["AI presentation rehearsal", "practice data presentation", "AI likely questions"]
---

# AI Presentation Rehearsal

Reusable capability for rehearsing a spoken data story and likely audience questions with AI.

## When to use

Use only when the requested action is rehearsing a spoken data story and likely audience questions with AI. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the speaker, audience, intended decision, current narrative/slides and available supporting evidence before rehearsing sequence and objections.
2. Test sequence, wording, objections and likely questions; retain the speaker's natural language and practise aloud.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return actionable rehearsal observations, proposed natural-language refinements and evidence-backed answers or explicit unanswered questions; distinguish AI review from actual aloud rehearsal.

## Benchmark case

A presenter rehearses the decision narrative and prepares evidence-backed answers to the three most likely objections.

Boundary design case: A likely question requires a number absent from the evidence. Prepare an honest uncertainty response and a source check; do not invent an answer for a smoother rehearsal.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Sources

- storytelling with data, *AI for data storytelling*: https://www.storytellingwithdata.com/ai-data-storytelling

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0012--SKILL-0252 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0038--SKILL-0252 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0039--SKILL-0252 | related_to | undirected | user_confirmed | supports
