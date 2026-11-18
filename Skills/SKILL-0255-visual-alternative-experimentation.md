---
id: SKILL-0255
type: skill
title: Visual Alternative Experimentation
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0037]
tags: [skill, action-specific]
trigger_phrases: ["compare chart alternatives", "visual experiment", "bump chart test", "small multiples test"]
---

# Visual Alternative Experimentation

Reusable capability for testing alternative visual encodings against a defined analytical question.

## When to use

Use only when the requested action is testing alternative visual encodings against a defined analytical question. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the analytical question, audience, same underlying data/scope and comprehension criterion before building at least two encodings.
2. Create at least two options; compare what each reveals, hides and demands cognitively; keep novelty only when comprehension improves.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the alternatives, what each reveals/hides, comparison observations and selected option or unresolved choice; disclose when comprehension has not been tested.

## Benchmark case

A bump chart is discarded when value—not rank—is the question, and the lesson is retained.

Boundary design case: One chart shows ranks and the other values over different periods. Align the question and data scope before comparing; novelty alone does not demonstrate improved comprehension.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Sources

- storytelling with data, *how do I get better at data storytelling?*: https://www.storytellingwithdata.com/blog/how-do-i-get-better

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0255 | related_to | undirected | user_confirmed | supports
