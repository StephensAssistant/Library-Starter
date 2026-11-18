---
id: SKILL-0175
type: skill
title: Qlik Migration Source-Field Mapping Diagnosis
status: current
created: 2026-09-20
updated: 2026-09-20
owner: Library owner

links: [SKILL-0107]
tags: [skill, qlik, diagnosis, blank-values]
trigger_phrases: [diagnose Qlik migration field mapping, trace missing Qlik source field, compare SQL Server Snowflake Qlik aliases]
---

# Qlik Migration Source-Field Mapping Diagnosis

Prove whether a migrated Qlik blank begins at the SQL Server-to-Snowflake source-field, alias or preload mapping boundary.

## When to use

Use first when a Snowflake-backed Qlik measure, dimension or visual is blank and the required source fields or aliases have not yet been proven present and populated. Association/key diagnosis then routes to SKILL-0206; expression evaluation routes to SKILL-0257.

## Intent-routing contract

This Skill owns source-field availability, naming, alias and preload mapping only. It does not diagnose associations, composite keys or expression semantics.

## Method

1. Start with one affected output and list every required source field and expected legacy-to-Snowflake mapping.
2. Compare legacy names, Snowflake connector casing, aliases and preceding-load transformations.
3. Prove each required field exists and is populated at the Qlik load boundary.
4. Isolate the earliest missing, renamed, mistyped or unpopulated field mapping.
5. Repair only that proven mapping and rerun the field-presence check.
6. Hand off to SKILL-0206 only after required fields are proven available.

## Benchmark case

A migrated measure is blank because an uppercase Snowflake connector field no longer matches its preceding-load alias; the mapping is corrected and field population is proven before association testing.

## Anti-patterns

- Rewriting the front-end expression before field mapping is proven.
- Diagnosing composite associations inside this Skill.
- Treating reload success as proof of populated fields.

## Stop

Stop when every required migrated field and alias is proven available and populated, or with the precise missing source-field evidence; then route the next failed boundary explicitly.
