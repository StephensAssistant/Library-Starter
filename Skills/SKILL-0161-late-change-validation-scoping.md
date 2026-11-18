---
id: SKILL-0161
type: skill
title: Late-change Validation Scoping
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, project-management, change-control, testing]
trigger_phrases: [retest late change, validation invalidated by change, late change regression]
---

# Late-change Validation Scoping

Determine which prior validation and acceptance evidence a late change invalidates.

## When to use

Use after a late authorised change modifies behaviour, data contracts, dependencies or customer-visible output.

## Method

1. Identify the changed surfaces and previously accepted evidence.
2. Trace which tests or acceptance claims depended on the former behaviour.
3. Mark only evidenced invalidation; retain unaffected proof.
4. Define focused validation plus the necessary regression boundary.
5. Record new evidence before restoring the affected acceptance claim.

## Decision and evidence details

Map each affected acceptance claim to the changed behaviour and its prior test evidence. For retained claims, explain why their inputs and conditions are unaffected. Unknown dependency reach is a validation-scope gap, not proof that the old result still applies.

Boundary design case: a changed filter may affect an uninspected downstream calculation. Hold the dependent acceptance until the path is traced; do not either discard unrelated proof or restore all acceptance from one local passing test.

## Benchmark case

A late join change alters one report metric. A passing application reruns the metric path and required regression while retaining unrelated visual acceptance evidence.

## Anti-patterns

- Reusing invalidated evidence.
- Rerunning everything without a reason.
- Rerunning only the edited line.

## Stop

Stop with a justified validation scope and restored evidence, or a named unresolved test gap.
