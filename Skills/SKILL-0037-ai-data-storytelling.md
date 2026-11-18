---
id: SKILL-0037
type: skill
title: AI-Assisted Data-Story Angle Generation
status: current
created: 2026-09-17
updated: 2026-10-31
links: [SKILL-0038, SKILL-0039, SKILL-0133, SKILL-0134, SKILL-0135, SKILL-0254, SKILL-0255, SKILL-0256]
tags: [skill, data-storytelling, ai, narrative]
trigger_phrases: ["AI story angles", "AI narrative options", "find data story options", "AI storytelling context"]
---

# AI-Assisted Data-Story Angle Generation

Reusable capability for generating candidate story angles from verified evidence with AI.

## When to use

Use only when the requested action is generating candidate story angles from verified evidence with AI. Use the independent action-specific Skills for adjacent validation, recovery, testing, performance, rehearsal or delivery work.

## Intent-routing contract

This Skill owns this one action from authoritative inputs to its evidenced result. It does not absorb adjacent jobs merely because they use the same platform or subject.

## Method

1. Confirm authoritative inputs, scope and success condition.
2. Supply audience, decision, verified evidence, constraints and uncertainty. Ask for multiple plausible structures, separate facts from interpretation, and reject any angle requiring unsupported evidence.
3. Preserve evidence, assumptions, result and any unresolved material gap.


### Application checks

Return candidate angles as a supported takeaway, proposed narrative sequence and the evidence for each material claim. Label interpretations and unresolved questions separately from observed facts. Discard an angle when its causal claim or requested decision requires unsupported evidence; retain uncertainty rather than asking AI to fill it. The output is a set of evidence-compatible options for selection, not validated causation or permission to publish.

## Evidence expected

Retain the inputs, checks, chosen result, source/date context and any condition that requires reassessment.

## Benchmark case

For a validated department decline, AI proposes several evidence-compatible story structures without inventing a cause or recommendation.

Boundary design case: the evidence proves a decline but supplies no causal analysis. Return angles framed around the observed comparison and uncertainty; reject a supplier-failure explanation or recovery recommendation that needs evidence absent from the supplied packet.

## Anti-patterns

- Expanding this Skill into another action because the subject is similar.
- Treating tool success or polished output as verified evidence.
- Proceeding through an unresolved material input or authority gap.

## Stop

Stop when the authoritative input or success condition is unknown. Route the next distinct action to its own Skill.

## Sources

- storytelling with data, *AI for data storytelling*: https://www.storytellingwithdata.com/ai-data-storytelling

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0133 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0134 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0135 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: PLAY-0012--SKILL-0037 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0038 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0039 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0254 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0255 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0256 | related_to | undirected | user_confirmed | supports
