---
id: SKILL-0132
type: skill
title: Workflow Bottleneck Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-17
links: []
tags: [project-management, flow, bottleneck]
trigger_phrases: ["blocked flow", "workflow bottleneck", "review queue"]
---

# SKILL-0132 — Workflow Bottleneck Diagnosis

## Purpose

Diagnose where work flow is constrained and select the smallest action that releases valuable completion.

## Intent routing contract

Activate only for blocked flow, workflow bottleneck, review queue or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Map active, waiting, review/validation and queued states.
2. Inspect queue growth, context switching, repeated displacement and incomplete outcomes.
3. Distinguish external waiting from an internal capacity or process bottleneck.
4. Identify the constraint by downstream completion effect, not local busyness.
5. Prefer smaller finishable slices only when dependencies, validation and ownership remain visible.
6. Record the unblock action and recheck flow after it completes.

## Anti-patterns

- Using completion counts while important outcomes remain unfinished.
- Calling all waiting work blocked.
- Splitting work so finely that acceptance becomes invisible.

## Benchmark case

When an observed BI-validation queue grows and accepted throughput is constrained there, a passing diagnosis uses queue/wait/acceptance evidence to identify that constraint and selects the smallest authorised remedy. Different build and validation durations alone do not establish a bottleneck.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when state data is insufficient to identify the constraint or the unblock authority is unknown.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.

## Outcome-based flow diagnosis — 17 October 2026

Before measuring, define accepted completion and the exact start/end events, population/window, units and source. Separate active execution, queue/wait time, repair and human intervention; do not infer efficiency from step count or tool activity. When relevant, calculate accepted completions per unit time, first-pass completions divided by eligible cases, end-to-end duration including waits, resource cost divided by accepted completions, and repeated/avoidable work. State the denominator and excluded cases. A zero accepted-completion denominator makes cost per accepted completion undefined, not zero. Choose only measures that answer the actual diagnosis; this is not a mandatory metrics dashboard.

Identify the constraint by its effect on accepted throughput. Change the smallest evidenced cause, retain authority/quality controls, then compare equivalent populations and conditions or disclose confounders. Mark proposed targets and design estimates separately from observations; do not claim causal improvement from an unmatched before/after anecdote.

Benchmark: a faster build increases the validation queue and leaves accepted completions unchanged. Do not claim delivery improvement; assess the queue and acceptance constraint before adding build capacity. Source: [Google SRE, Implementing SLOs](https://sre.google/workbook/implementing-slos/), inspected 17 October 2026; these workflow measures are a Library adaptation, not Google-prescribed targets.
