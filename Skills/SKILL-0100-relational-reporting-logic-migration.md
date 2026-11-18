---
id: SKILL-0100
type: skill
title: Relational Reporting Logic Migration
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [data-modelling, sql-migration]
trigger_phrases: ["migrate SQL Server reporting logic", "port relational report SQL to Snowflake", "preserve reporting semantics during migration"]
---

# SKILL-0100 — Relational Reporting Logic Migration

## Purpose

Move relational reporting logic between platforms while preserving business semantics and consumer contracts.

## When to use

Use for: migrate SQL Server reporting logic; port relational report SQL to Snowflake; preserve reporting semantics during migration.

## Method

1. Capture legacy output grain, field aliases, business rules and aligned comparison period.
2. Separate dialect conversion from source-model replacement.
3. Port one logical section at a time and prove intermediate populations.
4. Replace non-portable relationships only with validated business keys.
5. Reconcile outputs before platform-specific optimisation.

## Benchmark case

Port an SSRS query to Snowflake while retaining result aliases and metric logic, classifying timing differences rather than rewriting correct logic to match stale data.

Boundary design case: the translated query compiles but a legacy surrogate has no proven target identity. Block the dependent join and report the key-mapping gap before parity or optimisation; matching key names and syntax validity do not preserve reporting semantics.

## Anti-patterns

- Changing semantics while translating syntax.
- Optimising before parity.
- Forcing equality across different source snapshots.

## Stop

Stop with migrated logic, parity evidence and explicit exceptions.
