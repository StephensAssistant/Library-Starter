---
id: SKILL-0081
type: skill
title: Evidence-First Code Debugging
status: current
created: 2026-09-20
updated: 2026-10-10
links: [SKILL-0008]
tags: [coding, evidence-first]
trigger_phrases: ["debug this code defect", "find the earliest divergence", "test a bug hypothesis"]
---

# SKILL-0081 — Evidence-First Code Debugging

## Purpose

Isolate and repair the earliest correctable mechanism that explains an observed software defect.

## When to use

Use for: debug this code defect; find the earliest divergence; test a bug hypothesis.

## Method

1. Capture the exact symptom and expected contract.
2. Trace backwards to the earliest actual-versus-expected divergence.
3. Form the smallest falsifiable mechanism.
4. Run one discriminating check.
5. Apply the minimal repair only if evidence supports it.
6. Prove the repaired case and neighbouring behaviour.

## Benchmark case

For a one-sided trading execution defect, trace signal, request and fill evidence to find the first missing short-side event before changing strategy logic.

## Anti-patterns

- Random rewrites.
- Repeating a failed fix without new evidence.
- Repairing downstream symptoms.
- Rationalising defects as expected behaviour.

## Stop

Stop with a proven cause and repair evidence, or the next discriminating check.

## Matt Pocock method extension — 2026-10-10

Before changing code, establish a precise symptom and a repeatable failing observation where feasible: input, expected output, actual output and relevant environment. If an executable reproduction is unavailable, collect bounded read-only evidence and name that limitation. Maintain a short ranked set of falsifiable hypotheses, each with the cheapest discriminating observation. Change one variable at a time, record what the result rules out and update ranking. Implement the smallest causal fix, show the original failure is resolved, add a meaningful regression check when warranted, and remove temporary instrumentation. Do not turn speculative theories into wide rewrites or require the user to operate a manual debugger when supported tools suffice.

## Source adaptation — 2026-10-10

[diagnosing-bugs](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/diagnosing-bugs/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.
