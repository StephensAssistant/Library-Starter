---
id: SKILL-0008
type: skill
title: Risk-Based Test Selection
status: current
created: 2026-08-22
updated: 2026-10-31
links: [SKILL-0007, SKILL-0081, SKILL-0082, SKILL-0083, SKILL-0084, PLAY-0015, PLAY-0019, PLAY-0056]
tags: [testing, test-selection, risk]
trigger_phrases: ["choose the right tests", "select a test set", "what testing is needed", "is this sufficiently tested", "create a risk-based test plan"]
source_skill: testing-taxonomy
migrated_from: SKILL-0008-old-library
---

# SKILL-0008 — Risk-Based Test Selection

## Purpose

Choose the smallest set of tests that gives credible evidence for the actual change, material failure modes and affected contracts.

## When to use

Use before testing when the appropriate test types and depth must be selected. Route execution design to the applicable action-specific testing Skill.

## Method

1. State what changed, the observed defect or acceptance criterion, stable contracts and affected consumers.
2. Identify likely failure modes, consequence if wrong, persistence, data/time population and available baseline evidence.
3. Select a progression proportionate to risk: baseline/reproduction, focused correctness, negative/boundary, integration/contract, regression, recovery and acceptance.
4. Assign each selected check to a stated failure mode or contract.
5. Remove taxonomy items that do not discriminate this change.
6. Record residual untested risk explicitly.

## Test sufficiency

A set is sufficient when it directly checks the criterion, covers material negative/boundary cases, verifies affected contracts, applies proportionate regression and recovery, and exposes remaining risk.

## Benchmark case

For a narrow data-transformation defect, select reproduction, focused logic, join-cardinality, downstream contract and replay checks while excluding unrelated load, UI and security tests with reasons.

Missing-input design case: a requested change has no observable acceptance criterion. Inspect the available requirement and affected contracts, then name the unresolved criterion; a list of test types alone cannot establish sufficiency or justify an acceptance verdict.

## Anti-patterns

- Running a generic checklist unrelated to the change.
- Calling every possible test type mandatory.
- Treating successful execution as acceptance.
- Claiming complete coverage while material risks remain untested.

## Stop

Stop with a mapped test set, expected evidence and residual risk, or identify the missing requirement that prevents selection.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0008 | related_to | undirected | authoritative_record | supports
