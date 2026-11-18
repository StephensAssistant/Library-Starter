---
id: SKILL-0251
type: skill
title: AI Story Delivery-Mode Adaptation
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0038, SKILL-0039]
tags: [skill, action-specific]
trigger_phrases: ["adapt dashboard to presentation", "AI pre-read adaptation", "story delivery mode"]
---

# AI Story Delivery-Mode Adaptation

Reusable capability for adapting one verified data story to a specified delivery medium.

## When to use

Use only when the requested action is adapting one verified data story to a specified delivery medium. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the verified source story, audience, requested medium, intended decision and applicable delivery constraints.
2. Preserve evidence and decision while changing density, sequencing and annotation for dashboard, live presentation, pre-read or reference use.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the adapted story with source claims/metrics preserved and material changes to density, sequence and annotation explained; identify any medium-dependent context that remains unavailable.

## Benchmark case

A dense dashboard becomes a focused live narrative without changing its metrics or claims.

Boundary design case: A live presentation needs a shorter narrative but removing a scope qualification would change the claim. Preserve that qualification and adapt the presentation around it rather than strengthening the conclusion.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Sources

- storytelling with data, *AI for data storytelling*: https://www.storytellingwithdata.com/ai-data-storytelling

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0012--SKILL-0251 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0038--SKILL-0251 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0039--SKILL-0251 | related_to | undirected | user_confirmed | supports
