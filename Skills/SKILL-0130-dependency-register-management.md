---
id: SKILL-0130
type: skill
title: Dependency Register Management
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [project-management, dependencies, register]
trigger_phrases: ["record dependency", "dependency register", "update dependency state"]
---

# SKILL-0130 — Dependency Register Management

## Purpose

Maintain the lifecycle state of an evidenced dependency in the governing work record.

## Intent routing contract

Activate only for record dependency, dependency register, update dependency state or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Record the required upstream state and downstream acceptance outcome.
2. Capture evidence, owner or external party and current state: ready, waiting, blocked, satisfied or superseded.
3. Record any interim route and whether it permits progress only or final completion.
4. Set a review or closure trigger.
5. Update the parent and plan when the dependency materially changes.
6. Close only when evidence proves the required state or the dependency is formally superseded.

## Anti-patterns

- Removing a dependency because a bridge permits progress.
- Treating every wait as blocked.
- Letting the register contradict the governing parent.

## Decision and evidence details

Retain the upstream requirement, downstream acceptance condition, current evidence/date and the exact reason for a state transition. Distinguish an interim route that enables work from evidence that satisfies final acceptance.

Boundary design case: a bridge supplies build data but the required native source is still unverified. Record progress under the bridge while keeping the final-source dependency open; neither build completion nor silence from the owner proves satisfaction.

## Benchmark case

A native-source dependency remains open while a bridge permits build work, then closes only when the native source is validated for final acceptance.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop lifecycle changes when the upstream state or closure evidence is unresolved.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
