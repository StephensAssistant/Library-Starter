---
id: SKILL-0085
type: skill
title: Software Correctness Test Design
status: current
created: 2026-09-20
updated: 2026-10-12
links: [SKILL-0007]
tags: [testing, software-correctness]
trigger_phrases: ["design software correctness tests", "write boundary tests", "plan integration regression tests"]
---

# SKILL-0085 — Software Correctness Test Design

## Purpose

Design focused software tests that distinguish correct from incorrect behaviour across the affected code contracts.

## When to use

Use for: design software correctness tests; write boundary tests; plan integration regression tests.

## Method

1. State the observable behaviour and changed boundary.
2. Choose unit, integration, system, E2E or acceptance level according to where failure can occur.
3. Add the most material negative, boundary, equivalence, invariant and error-path cases.
4. Verify affected interfaces and proportionate neighbouring regression.
5. Define expected evidence before execution.

## Benchmark case

For a parser change, design focused valid, malformed, empty and boundary inputs plus the caller contract, without adding unrelated end-to-end cases.

## Anti-patterns

- Happy-path-only testing.
- Using a unit pass to excuse a broken integration.
- Writing tests that repeat implementation rather than behaviour.

## Stop

Stop with executable cases, expected results and mapped failure modes.

## Matt Pocock method extension — 2026-10-10

For material behavioural work, test the observable caller contract with independently derived expected results. Work in a small red–green slice: prove the test fails for the missing or wrong behaviour, implement the minimum coherent change, then improve structure while keeping evidence. Choose the test boundary before mocking; replace external I/O when necessary, not the internal implementation being assessed. Confirm that a plausible regression would fail the check. Avoid assertions that mirror the code or tests for trivial reversible edits. A complete batch of speculative failing tests is weaker than one verified slice; existing confirmed requirements settle behaviour without repeated approval.

## Source adaptation — 2026-10-10

[tdd](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/tdd/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.


## Temporary Git repository lifecycle — 12 October 2026

When a correctness test creates a temporary Git repository and commits into it, isolate automatic maintenance before the first mutation: set repository-local `maintenance.auto=false` and `gc.auto=0`. Git commits can return after launching detached housekeeping; successful synchronous command completion alone does not guarantee that no writer remains when TemporaryDirectory removes the repository. Keep cleanup strict and preserve the behavioural assertions; do not suppress directory-not-empty errors or weaken a historical-visibility guard. This configuration is local to the disposable fixture and does not alter production Git maintenance.

Evidence: candidate workflow 38240047930 failed at test_historical_snapshot_rejects_opening_id_leakage during `.git/objects` cleanup with OSError 39. A controlled host auto-maintenance configuration produced 24 detached maintenance launches over twelve original fixture runs. With local isolation, the same twelve runs passed with zero maintenance launches; the focused module passed three tests and skipped its unavailable full-corpus test. The original cleanup exception was not reproduced locally, so background maintenance is a supported race mechanism and prevention, not a proved exclusive cause of the original runner failure. Full candidate validation remains the release gate.
