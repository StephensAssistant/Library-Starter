---
id: SKILL-0250
type: skill
title: AI Interpretation Pressure Testing
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0038, SKILL-0039]
tags: [skill, action-specific]
trigger_phrases: ["challenge data takeaway", "AI alternative explanation", "pressure test narrative"]
---

# AI Interpretation Pressure Testing

Reusable capability for using AI to surface alternative explanations and evidential weaknesses in a data story.

## When to use

Use only when the requested action is using AI to surface alternative explanations and evidential weaknesses in a data story. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the current takeaway, underlying evidence, comparison population, scope and audience before proposing alternative explanations or objections.
2. Ask which comparison, scope issue, assumption or audience objection could change the takeaway; verify material challenges against source data.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return each material challenge, the source check capable of resolving it, observed evidence and its effect on the takeaway; retain unresolved alternatives as hypotheses.

## Benchmark case

AI suggests seasonality as an alternative explanation; the claim is checked before the narrative is changed.

Boundary design case: AI proposes seasonality but the required comparison periods are unavailable. Preserve it as an unverified alternative, not a proven correction or a causal explanation.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Sources

- storytelling with data, *AI for data storytelling*: https://www.storytellingwithdata.com/ai-data-storytelling

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0012--SKILL-0250 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0038--SKILL-0250 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0039--SKILL-0250 | related_to | undirected | user_confirmed | supports
