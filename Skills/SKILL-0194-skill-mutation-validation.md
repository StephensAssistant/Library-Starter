---
id: SKILL-0194
type: skill
title: Skill Mutation Validation
status: current
created: 2026-09-20
updated: 2026-10-16
owner: Library owner

trigger_phrases: ["validate skill mutation", "held out skill test", "skill regression suite"]
links: [FLOW-0001, FLOW-0002, PLAY-0041, PLAY-0046, PLAY-0069]
tags: [skill, library-mechanics, learning, validation]
---

# Skill Mutation Validation

Tests a material Skill mutation against frozen and held-out cases.

## When to use

Use before accepting a change to a Skill trigger, action, boundary or stop condition.

## Method

1. Freeze representative positive, negative and boundary cases.
2. Keep held-out cases separate from examples that authored the change.
3. Apply one bounded mutation.
4. Compare target improvement and regressions in purpose, authority, evidence, safety and stopping. For material guidance acceptance, a non-author reviewer assesses the persisted change and evidence; record reviewer/pass identity and inspected sources. An author switching Hats is not independent review. Missing required independent evidence blocks acceptance.
5. Retain rejected wording with scores/reasons to prevent rediscovery.
6. Require stronger evidence for a larger rewrite.
7. When a trigger or routing companion is in scope, use the current registry builder and benchmark contract. Curated phrases may extend frontmatter phrases; equality of the two lists is not the contract. Check all-current fixture coverage with meaningful positive cases for current owners; an excluded ID alone is nominal coverage, not proof that its intended route works. Execute the preserved positive, negative and boundary assertions against source-derived routing. A prose benchmark section, a configured ID or a documentary review score does not prove the routing tests pass. Fix omitted coverage and diagnosed semantic routing defects without copying whole motivating utterances into triggers or weakening expected outcomes; correct a demonstrably stale expected owner only with cited current contract evidence, retain the original assertion and reason, preserve useful positive/negative coverage, and retain held-out checks with their limits.

## Benchmark case

A shorter trigger improves positive routing but activates a negative case; reject and retain the failure record.

## Anti-patterns

- Testing only the motivating example
- Discarding rejected variants
- Accepting improvement with safety regression

## Stop

Stop with the evidenced proposed acceptance/rejection and any independent-review blocker; the Library owner owns accepted policy. This assessment does not authorise candidate validation, Actions, deployment or merge.
