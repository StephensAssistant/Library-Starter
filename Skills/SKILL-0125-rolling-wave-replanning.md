---
id: SKILL-0125
type: skill
title: Rolling-Wave Replanning
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [project-management, rolling-wave, replanning]
trigger_phrases: ["rolling-wave plan", "replan later work", "uncertain delivery phase"]
---

# SKILL-0125 — Rolling-Wave Replanning

## Purpose

Increase plan detail only as evidence makes future work executable, and replan from the earliest invalidated assumption.

## Intent routing contract

Activate only for rolling-wave plan, replan later work, uncertain delivery phase or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Keep near-term work executable when inputs, acceptance and authority are known.
2. Keep distant work coarse while architecture, source, dependency or customer decisions remain unproven.
3. Promote a later item only when blocking assumptions and contracts are sufficiently resolved.
4. When evidence changes, identify the earliest affected assumption or dependency.
5. Rebuild downstream sequence from that point instead of appending repairs to an obsolete plan.
6. Record what changed, why detail changed and the next decision-changing action.

## Anti-patterns

- Detailing speculative distant work as committed.
- Making a plan longer instead of more precise.
- Retaining obsolete sequence after a failed assumption.

## Decision and evidence details

For each promoted item, record the newly resolved input, acceptance condition or authority and its source. For a replanned segment, show the earliest invalidated assumption and the downstream sequence that changes; retain valid completed work and unresolved later items.

Boundary design case: an alternative source is suggested but not proven available. Keep dependent work coarse and name the source-verification action; a plausible alternative alone does not make the implementation executable.

## Benchmark case

When a source API proves unavailable, a passing replan revises the earliest source assumption, preserves valid completed work and leaves later implementation coarse until the alternative is proven.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop promotion to executable detail while a blocking assumption, contract or authority remains unknown.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
