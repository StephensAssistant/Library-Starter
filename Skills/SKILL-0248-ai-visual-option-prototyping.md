---
id: SKILL-0248
type: skill
title: AI Visual Option Prototyping
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0038, SKILL-0039]
tags: [skill, action-specific]
trigger_phrases: ["AI chart alternatives", "AI visual prototype", "AI chart ideas"]
---

# AI Visual Option Prototyping

Reusable capability for using AI to generate and compare evidence-compatible visual options.

## When to use

Use only when the requested action is using AI to generate and compare evidence-compatible visual options. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the audience, analytical question, verified evidence, platform constraints and required comparison before requesting visual alternatives.
2. Supply audience, task, verified evidence and platform constraints; request multiple conventional choices and compare comprehension trade-offs; keep human control of emphasis.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return comparable visual options with the evidence each uses, comprehension trade-offs and a justified recommendation; leave emphasis selection with the human and label untested comprehension claims.

## Benchmark case

AI proposes three charts for a validated decline; the option making the required comparison clearest is selected.

Boundary design case: The supplied decline is unverified. Do not fabricate data or present a visual option as evidence that the decline occurred; identify the missing source verification before relying on that claim.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Sources

- storytelling with data, *AI for data storytelling*: https://www.storytellingwithdata.com/ai-data-storytelling

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0012--SKILL-0248 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0038--SKILL-0248 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0039--SKILL-0248 | related_to | undirected | user_confirmed | supports
