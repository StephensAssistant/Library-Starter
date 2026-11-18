---
id: SKILL-0096
type: skill
title: Cross-Platform Key Mapping
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [data-modelling, key-mapping]
trigger_phrases: ["map keys across platforms", "replace a surrogate key join", "identify portable business keys"]
---

# SKILL-0096 — Cross-Platform Key Mapping

## Purpose

Prove identity across systems and define a portable key mapping before cross-platform joins.

## When to use

Use for: map keys across platforms; replace a surrogate key join; identify portable business keys.

## Method

1. Inventory candidate natural, business and surrogate keys with generating systems.
2. Measure uniqueness, nulls, formatting and stability at the intended grain.
3. Prove component-level mapping and unmatched populations.
4. Define composite normalization rules when required.
5. Retain legacy surrogates only as trace attributes unless portability is proven.

## Benchmark case

Replace a SQL Server-to-Snowflake VARIANT_KEY join with validated product, colour and size business-key components and quantify unmatched rows.

Boundary design case: normalization maps two distinct source identities to one target key. Retain the collision population and block the affected cross-platform join until identity is resolved; choosing one row or generating a surrogate does not prove the mapping portable.

## Anti-patterns

- Joining because column names match.
- Generating a surrogate before understanding identity.
- Ignoring null and formatting rules.

## Stop

Stop with a proven mapping, exception population and ownership.
