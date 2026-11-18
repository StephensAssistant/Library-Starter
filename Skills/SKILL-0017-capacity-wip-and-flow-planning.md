---
id: SKILL-0017
type: skill
title: Capacity-Based Work Selection
status: current
created: 2026-08-29
updated: 2026-09-20
links: []
tags: [project-management, capacity, work-selection]
trigger_phrases: ["what can fit", "capacity planning", "workload selection"]
---

# SKILL-0017 — Capacity-Based Work Selection

## Purpose

Select work that can credibly fit evidenced capacity without fabricating commitments.

## Intent routing contract

Activate only for what can fit, capacity planning, workload selection or equivalent intent. Use associated records for their own jobs; this Skill does not silently expand into adjacent work.

## Method

1. Classify current work as active execution, waiting/external, review/validation or queued.
2. Use stated or evidenced capacity for commitments; treat percentages and WIP limits as context-specific heuristics.
3. Reserve slack for interruption, incidents, review and uncertainty when volatility is evidenced.
4. Distinguish open work from attention-demanding work.
5. When capacity is unknown, return a constrained order and name the evidence required for scheduling.
6. Do not override explicit priority or due commitments.

## Anti-patterns

- Treating every open Ticket as equal capacity consumption.
- Inventing dates, availability or utilisation percentages.
- Starting all important work simultaneously.

## Benchmark case

Given two active builds, one external wait and unknown future availability, a passing result distinguishes attention demand, identifies the feasible next item and refuses a dated commitment without capacity evidence.

## Output and evidence

Record the inputs, decisions, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when a commitment is requested but capacity, fixed commitments or authority are unresolved.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; former combined responsibilities moved to independent Skills while preserving existing links.
