---
id: SKILL-0249
type: skill
title: AI Storytelling Artifact Critique
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0038, SKILL-0039]
tags: [skill, action-specific]
trigger_phrases: ["AI critique chart", "AI critique dashboard", "improve AI story draft"]
---

# AI Storytelling Artifact Critique

Reusable capability for using AI to critique a supplied data-storytelling artifact without replacing validated work.

## When to use

Use only when the requested action is using AI to critique a supplied data-storytelling artifact without replacing validated work. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the actual artifact/version, intended audience, takeaway, source evidence and critique scope before judging clarity, comparison or sequence.
2. Ask what is unclear, misleading, cluttered, unsupported or weakly sequenced; preserve strengths and revise only evidenced weaknesses.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return specific findings tied to visible passages/elements, preserved strengths, proposed corrections and supporting evidence; separate an observed defect from a subjective preference.

## Benchmark case

A dashboard draft retains its proven layout while AI identifies one misleading comparison for correction.

Boundary design case: A dashboard screenshot omits the filter context needed to judge a comparison. Mark that limitation and request or inspect the context; do not replace its validated layout based on a guessed scope.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Sources

- storytelling with data, *AI for data storytelling*: https://www.storytellingwithdata.com/ai-data-storytelling

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0012--SKILL-0249 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0038--SKILL-0249 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0039--SKILL-0249 | related_to | undirected | user_confirmed | supports
