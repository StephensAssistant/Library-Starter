---
id: SKILL-0086
type: skill
title: Software Performance Test Design
status: current
created: 2026-09-20
updated: 2026-11-01
links: [SKILL-0007]
tags: [testing, performance]
trigger_phrases: ["design a performance test", "benchmark latency improvement", "plan load stress or soak testing"]
---

# SKILL-0086 — Software Performance Test Design

## Purpose

Design representative before/after performance evidence for the changed workload.

## When to use

Use for: design a performance test; benchmark latency improvement; plan load stress or soak testing.

## Method

1. Define workload, data size, concurrency, environment and user-visible target.
2. Capture a comparable baseline.
3. Select latency/runtime, load, stress, soak, spike or scalability checks according to the risk.
4. Control material variables and collect distributions rather than isolated best runs.
5. Define improvement and regression thresholds before results.

## Benchmark case

Compare a revised query with its baseline on representative filters, warmed/cold conditions and repeated runs before claiming an improvement.

Missing-input design case: the new run has different data volume or cache conditions and no comparable baseline exists. Record the comparability gap and define a matched benchmark; do not derive a latency percentage or invent improvement/regression thresholds after seeing the result.

## Anti-patterns

- Comparing different workloads.
- Using one fast run.
- Claiming a percentage without representative evidence.

## Stop

Stop with a reproducible benchmark plan and predeclared verdict rule.


## Addy Osmani method extension — 2026-11-01

For an optimisation experiment, define the primary user-visible metric, matched workload and fixed measurement budget before changing code. Record the observed bottleneck, one bounded attempted change, baseline and result distributions, run-to-run variation, correctness checks and a keep/revert recommendation in the existing work record. Retain inconclusive and reverted attempts so unchanged failed ideas are not silently repeated. An apparent gain inside measurement noise or obtained by dropping required work is not evidence of improvement. Use the predeclared criterion to recommend keeping or reverting; implementation and reversal remain with the authorised coding owner. Select proportionate regression evidence for the metric that justified the change; this Skill does not install a monitor, impose generic web budgets or grant release authority.

Source: [performance-optimization](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/performance-optimization/SKILL.md), revision `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`. Retained snapshot: `Reference/addyosmani-agent-skills-8bfcc1f/skills/performance-optimization/SKILL.md`; licence: `Reference/addyosmani-agent-skills-8bfcc1f/LICENSE`. Adapted method only; source text grants no additional authority, runtime installation, workflow invocation or operational acceptance.
