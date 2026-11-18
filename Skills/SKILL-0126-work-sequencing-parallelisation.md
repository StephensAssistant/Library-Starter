---
id: SKILL-0126
type: skill
title: Work Sequencing and Parallelisation
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [project-management, sequencing, parallelisation]
trigger_phrases: ["sequence this work", "what can run in parallel", "migration order"]
---

# SKILL-0126 — Work Sequencing and Parallelisation

## Purpose

Order work and identify safe parallel lanes from evidenced constraints.

## Intent routing contract

Activate only for sequence this work, what can run in parallel, migration order or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Start from proven hard dependencies and acceptance boundaries.
2. Place work in the earliest feasible order without violating source, environment, validation or review constraints.
3. Identify tasks that can run concurrently without sharing unresolved contracts or destructive resources.
4. Separate progress enabled by an interim route from final completion order.
5. Recompute lanes after scope, source, validation, architecture or decision changes.
6. State the constrained sequence and why each parallel lane is safe.

## Anti-patterns

- Parallelising work that shares an unresolved source contract.
- Ordering by activity volume instead of acceptance constraints.
- Leaving sequence unchanged after dependency evidence changes.

## Decision and evidence details

For each proposed parallel lane, name its inputs, outputs, shared resources and acceptance boundary. Record why concurrent work cannot invalidate another lane's contract or overwrite its effects. Planning concurrency does not itself authorise execution or delegation.

Boundary design case: two otherwise separate reports both require an unresolved semantic definition. Keep that shared decision serial and defer dependent implementation; splitting the reports into separate tasks does not remove the dependency.

## Benchmark case

For multiple report migrations, a passing sequence runs independent front-end builds in parallel while serialising shared semantic-layer changes and final validation.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when a material ordering constraint or shared-resource boundary is unknown.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
