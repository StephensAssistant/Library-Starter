---
id: SKILL-0091
type: skill
title: Semantic-Model Correctness Test Design
status: current
created: 2026-09-20
updated: 2026-11-10
links: [SKILL-0007]
tags: [skill, testing, bi-semantic, correctness]
trigger_phrases: ["test a semantic model", "validate BI metrics", "design semantic correctness tests"]
---

# Semantic-Model Correctness Test Design

Design correctness tests for BI semantic models, governed metrics and analytical relationships.

## Intent-routing contract

This Skill owns semantic-model correctness test design only. Dashboard interactions, security visibility, performance and export/presentation testing are separate actions.

## When to use

Use when metric definitions, grain, relationships, calendars, null behaviour or aggregation correctness must be tested.

## Method

1. Confirm each metric definition, table grain, relationship and calendar semantic.
2. Select known totals and representative dimensional and time slices.
3. Test nulls, blanks, duplicate keys, unmatched keys, joins and fan-out. Normalise only evidenced equivalent key forms, such as case or surrounding whitespace; do not collapse a governed dimensional grain.
4. Reconcile the complete authoritative source population before and after each mapping or relationship. Report unmatched row counts and quantities separately so both sides cannot pass by excluding the same records.
5. Verify the downstream model preserves the metric after all anchors, unions and associations; prove that unrelated anchor rows cannot omit or multiply it.
6. Verify additive, semi-additive and non-additive behaviour where applicable, including selection-state tests that distinguish an actual zero from a field association or filter exclusion.
7. Compare calculated results with governed definitions and authoritative known cases.
8. Record data defects separately from semantic-definition defects.

## Benchmark case

A sales semantic model is tested against governed net-sales totals, date comparisons and dimensional slices; duplicate joins and fan-out are explicitly checked before any presentation verdict.

Missing-input design case: a net-sales metric has no agreed return-sign or calendar rule. Identify that semantic gap before supplying expected totals; visual agreement or a formula copied from the implementation cannot independently establish the intended result.

## Anti-patterns

- Using visual agreement as data proof.
- Checking one total without dimensional or time slices.
- Ignoring grain, calendar semantics or fan-out.
- Reconciling only records that survived the same join on both sides, creating a false zero difference.
- Validating an upstream total without proving that the final anchor, union and associations retain it.
- Treating dashboard interaction behaviour as semantic correctness.

## Stop

Stop when representative metrics, grains, relationships, time logic and edge cases have explicit expected results sufficient for a semantic-correctness verdict.
