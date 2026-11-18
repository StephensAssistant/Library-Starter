---
id: SKILL-0127
type: skill
title: Critical-Path and Slack Analysis
status: current
created: 2026-09-20
updated: 2026-09-20
links: []
tags: [project-management, critical-path, slack]
trigger_phrases: ["critical path", "schedule sensitivity", "calculate slack"]
---

# SKILL-0127 — Critical-Path and Slack Analysis

## Purpose

Identify schedule-critical work and slack only when credible durations and calendars support the calculation.

## Intent routing contract

Activate only for critical path, schedule sensitivity, calculate slack or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Confirm task network, durations, calendars and completion dependencies are credible.
2. Calculate earliest and latest dates and total/free slack when the evidence supports mathematics.
3. Identify the path whose delay changes the accepted completion date.
4. If durations or calendars are not credible, return a qualitative constrained sequence instead.
5. Explain sensitivity to uncertain estimates and the acceptance impact of the bottleneck.
6. Recompute after material estimate, scope or dependency change.

## Anti-patterns

- Publishing exact dates from guessed durations.
- Calling the item with most subtasks critical.
- Confusing business priority with schedule criticality.

## Benchmark case

With evidenced task durations and dependencies, a passing analysis calculates the zero-slack path and shows which one-day delay moves final acceptance; without them it declines false precision.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop mathematical analysis when durations, calendars or dependency edges are not credible.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
