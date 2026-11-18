---
id: SKILL-0256
type: skill
title: Team Data-Story Critique Facilitation
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0037]
tags: [skill, action-specific]
trigger_phrases: ["run dashboard critique", "team chart review", "peer storytelling session"]
---

# Team Data-Story Critique Facilitation

Reusable capability for facilitating a structured team critique session for a data artifact.

## When to use

Use only when the requested action is facilitating a structured team critique session for a data artifact. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the artifact/version, intended audience/takeaway, participants and the comparison criterion. Select the single revision to test only after collecting observations and comparing interpretation with intent.
2. State audience and intended takeaway; collect silent observations; compare observed interpretation with intent; test one change; record the learning.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return recorded observations, differences from intended interpretation, the tested revision and reusable learning; a planned session or AI-simulated response is not participant feedback.

## Benchmark case

A 25-minute review shows reviewers missed the intended comparison, tests one revision and captures the reusable result.

Boundary design case: Reviewers have not seen the artifact. Prepare the session but do not invent silent observations or claim they understood the intended comparison; preserve the missing feedback.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Sources

- storytelling with data, *how do I get better at data storytelling?*: https://www.storytellingwithdata.com/blog/how-do-i-get-better

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0256 | related_to | undirected | user_confirmed | supports
