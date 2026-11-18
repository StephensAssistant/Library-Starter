---
id: SKILL-0099
type: skill
title: Join Cardinality and Fan-Out Validation
status: current
created: 2026-09-20
updated: 2026-10-12
links: []
tags: [data-modelling, joins]
trigger_phrases: ["validate join cardinality", "check for join fan-out", "prove a relationship before aggregation"]
---

# SKILL-0099 — Join Cardinality and Fan-Out Validation

## Purpose

Prove a join's intended cardinality and measure its population and value effects before exposing aggregates.

## When to use

Use for: validate join cardinality; check for join fan-out; prove a relationship before aggregation.

## Method

1. Count rows and distinct join keys on both sides.
2. Measure duplicate keys, null keys and unmatched populations.
3. Declare expected one-to-one, one-to-many or many-to-many behaviour.
4. Compare rows and material sums before and after the join.
5. Segment unexpected multiplication and identify the responsible key population.

## Benchmark case

Validate a sales-to-product join by proving product-key uniqueness and showing that totals remain stable while unmatched sales are explicit.

## Anti-patterns

- Assuming a successful join is correct.
- Aggregating before cardinality proof.
- Checking row count but not material sums.

## Stop

Stop with a cardinality verdict, exception population and aggregation-safety decision.

## Non-product keys and safe dimension maps — 12 October 2026

Delivery/adjustment records can reuse synthetic product keys across thousands of dimension rows; profile by record type and key domain before a join. Digital Analytics legacy delivery keys matched4,394 dimension rows, inflating source values. Product2_id and Shopify_id were different domains in the verified feed.

Collapse a dimension into one row per intended join key only with an explicit unique-value policy (count distinct code/key=1). MAX inside that guard returns the sole distinct value; MAX outside it arbitrarily hides ambiguity. Preserve unresolved facts and compare additive totals at every stage. Multiple barcodes are not multiple sales/stock facts. NULL native line IDs for delivery/appeasements prohibit a universal product-line uniqueness claim.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.
