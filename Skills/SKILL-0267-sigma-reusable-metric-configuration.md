---
id: SKILL-0267
type: skill
title: Sigma Reusable Metric Configuration
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050]
tags: [skill, sigma, metrics]
trigger_phrases: [configure sigma reusable metric, sigma governed metric, sigma metric definition]
---

# Sigma Reusable Metric Configuration

Configure a reusable Sigma metric from an approved governed business definition.

## Intent-routing contract

This Skill owns reusable metric expression, naming, format and validation in Sigma. Source, relationship and domain-boundary configuration are separate Skills.

## When to use

Use when an approved metric must be exposed consistently to multiple Sigma analyses without changing its governed definition.

## Method

1. Identify the authoritative business definition, grain, inclusion/exclusion rules and source fields.
2. Reuse the approved Snowflake metric or semantic definition and expose it through the approved golden serving source; do not create a competing Sigma calculation. A missing governed metric is a dependency for Snowflake modelling, not permission to implement portable business logic in Sigma. Apply only approved temporary-testing or explicit front-end exceptions.
3. Configure the Sigma metric name, expression or reference, aggregation behaviour, format and description.
4. Prove behaviour at total and representative dimensional slices, including null, zero and edge populations.
5. Compare results with the authoritative metric evidence and record any approved platform-specific presentation difference.
6. Search for duplicate local calculations before promoting the metric for reuse.

## Benchmark case

Net Sales is exposed as one reusable Sigma metric referencing the governed Snowflake definition; totals and store/day slices reconcile and duplicate workbook formulas are identified for retirement.

Boundary design case: The requested reusable metric has no approved Snowflake definition. Record the modelling dependency instead of creating portable business logic in Sigma or treating a matching headline total as authority.

## Anti-patterns

- Reimplementing governed business logic for convenience.
- Leaving aggregation behaviour implicit.
- Approving a metric from one headline total without dimensional checks.

## Stop

Stop when the reusable metric's definition, aggregation, formatting and representative reconciliation are verified, or when metric authority or source fields are unresolved.

