---
id: SKILL-0083
type: skill
title: Code Change Outcome Verification
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0008]
tags: [coding, evidence-first]
trigger_phrases: ["verify a code change", "prove this implementation works", "check the acceptance criterion"]
---

# SKILL-0083 — Code Change Outcome Verification

## Purpose

Prove that a code change meets its user-, system- or data-visible success criterion.

## When to use

Use for: verify a code change; prove this implementation works; check the acceptance criterion.

## Method

1. State the observable criterion before interpreting test results.
2. Establish a baseline or reproduce the failure where practical.
3. Run the narrowest discriminating check against the changed behaviour.
4. Expand to proportionate regression checks.
5. Record actual versus expected evidence and residual risk.

## Benchmark case

After a stored-procedure fix executes successfully, verify the intended row population and key measure rather than treating execution as acceptance.

Missing-input design case: the command completes but the target output cannot be inspected or the expected criterion remains undefined. Return INCONCLUSIVE with the exact oracle gap; tool exit status alone cannot produce PASS or prove the changed population is correct.

## Anti-patterns

- Reporting tool success as outcome proof.
- Testing only compilation.
- Running broad tests without the changed criterion.

## Stop

Stop with a PASS/FAIL/INCONCLUSIVE verdict tied to direct evidence.
