---
id: SKILL-0291
type: skill
title: Sigma Transposed Nested Pivot Construction
status: current
created: 2026-09-21
updated: 2026-10-31
owner: Library owner

links: [SKILL-0003]
tags: [skill, sigma, pivot, transpose]
trigger_phrases: [sigma pivot in pivot, sigma transposed pivot, nested sigma pivot headers]
---

# Sigma Transposed Nested Pivot Construction

Construct one transposed Sigma pivot with nested period headers, deterministic custom ordering and mixed metric formatting.

## Intent-routing contract

Activate for the Franklin-style transpose pattern. Union-based multi-component pivots use SKILL-0290.

## When to use

Use when a report needs merged-header-style nesting across periods and metrics with independent row and column formatting.

## Method

1. Group the base table and create the required period columns plus period-specific metric columns.
2. Duplicate the grouped result and transpose columns to rows while retaining the row dimension separately.
3. Create input-table reference rows for metric rank, period rank and category nesting.
4. Derive Period and Metric from transposed labels with `SplitPart()`.
5. Attach Period Rank and Metric Rank using `Lookup()`.
6. Build the pivot and sort categories by the reference ranks rather than label order.
7. Apply conditional-format rules for currency, percentages, negative values, font and background in deliberate precedence order.
8. Reconcile period/metric parsing, lookup completeness, rank uniqueness, header nesting and format precedence.

## Benchmark case

A segment report transposes monthly revenue and margin columns, rebuilds Period and Metric fields, orders them from input-table ranks and renders currency and percentage columns correctly.

Boundary design case: A transposed label cannot be parsed unambiguously or has no unique reference rank. Return the exact parsing/lookup gap before accepting the pivot; do not use alphabetical order to conceal it.

## Anti-patterns

- Depending on alphabetical order for financial periods or metrics.
- Parsing transposed labels without validating delimiters.
- Leaving missing or duplicate lookup ranks unresolved.
- Treating conditional-format rule order as immaterial.
- Using this pattern for a simple ordinary pivot.
- Mixing the component-pivot union method into this Skill.

## Stop

Stop with one ordered and formatting-validated transposed nested pivot, or the precise parsing, lookup, rank or formatting gap.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0003--SKILL-0291 | related_to | undirected | user_confirmed | supports
