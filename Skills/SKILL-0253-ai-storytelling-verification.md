---
id: SKILL-0253
type: skill
title: AI Storytelling Verification
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0038, SKILL-0039]
tags: [skill, action-specific]
trigger_phrases: ["verify AI data story", "validate AI narrative", "AI artifact fact check"]
---

# AI Storytelling Verification

Reusable capability for independently validating a final AI-assisted data-storytelling artifact.

## When to use

Use only when the requested action is independently validating a final AI-assisted data-storytelling artifact. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the final artifact/version, intended audience/action and authoritative data/definition sources before checking its claims and presentation.
2. Check numbers, definitions, scope, causal language, accessibility, chart suitability, labels and requested action against authoritative sources.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return claim/element-level findings with evidence, corrections needed and unverified portions; a polished artifact or AI agreement is not independent source validation.

## Benchmark case

Every AI-suggested claim in a sales story traces to verified data before delivery.

Boundary design case: The final chart has numbers that cannot be traced to the supplied source. Mark those claims unverified and withhold a complete validation claim; do not infer correctness from the narrative consistency.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Sources

- storytelling with data, *AI for data storytelling*: https://www.storytellingwithdata.com/ai-data-storytelling

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0012--SKILL-0253 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0038--SKILL-0253 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0039--SKILL-0253 | related_to | undirected | user_confirmed | supports
