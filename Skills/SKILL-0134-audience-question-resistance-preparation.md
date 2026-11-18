---
id: SKILL-0134
type: skill
title: Audience Question and Resistance Preparation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["prepare for presentation questions", "anticipate audience resistance", "rehearse stakeholder challenges"]
links: [SKILL-0037]
tags: [skill, action-specific]
---

# Audience Question and Resistance Preparation

Prepare evidence-grounded answers for likely audience questions and resistance to an existing data story.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use after the story is validated, when definitions, assumptions, causality, scope or action may be challenged.

## Method

1. List likely challenges by audience and decision.
2. Match each challenge to evidence, a qualified answer or an explicit unknown.
3. Prepare concise responses and the evidence location; never script false certainty.
4. Escalate any challenge that exposes an unsupported core claim back to [[SKILL-0037]].

## Decision and evidence details

Deliver a question/response record containing the audience concern, supported answer or qualification, exact evidence location and named follow-up for an unknown. Keep a challenge to a core claim separate from a request for extra detail; the former returns to story validation.

Boundary design case: no evidence distinguishes correlation from cause. Prepare a limited answer that preserves that uncertainty; do not invent a causal explanation to make the response sound decisive.

## Benchmark case

Senior stakeholders may challenge the comparison period and causality; the presenter prepares the verified period rationale and explicitly limits the causal claim.

## Anti-patterns

- Inventing certainty
- Preparing generic questions unrelated to the audience
- Treating resistance as a delivery failure

## Sources

- https://www.storytellingwithdata.com/

## Stop

Stop when material challenges have an evidence-backed answer, a stated limitation or a named follow-up.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0134 | related_to | undirected | inherited_from_source_split | supports
