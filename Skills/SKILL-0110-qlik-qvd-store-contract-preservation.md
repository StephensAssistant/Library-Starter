---
id: SKILL-0110
type: skill
title: Qlik QVD and Store Contract Preservation
status: current
created: 2026-09-20
updated: 2026-10-12
links: []
tags: [qlik, qvd, interface-contract]
trigger_phrases: ["QVD contract", "Qlik STORE output", "Qlik text output"]
---

# SKILL-0110 — Qlik QVD and Store Contract Preservation

## Purpose

Preserve QVD and stored-output interfaces consumed by other applications or processes.

## Intent routing contract

Activate only for QVD contract, Qlik STORE output, Qlik text output or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Identify every consumer and the authoritative current output contract.
2. Record filename, path, format, delimiter, field names, types and grain.
3. Separate internal source changes from the published Qlik output interface.
4. Compare output schema and representative populations before and after change.
5. Change the interface only with explicit scope, consumer migration and acceptance.

## Anti-patterns

- Treating output filenames as incidental.
- Renaming fields during a source-only migration.
- Assuming technically equivalent output is backward compatible.

## Benchmark case

When a source moves to Snowflake, a passing result emits the same QVD filename, fields and grain and proves a dependent app reloads against it.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when consumers or the accepted output contract are unknown.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.

## Versioned QVD first-run bootstrap — 12 October 2026

Trigger: an accepted replacement changes its internal development QVD version. Before reading reuse mode, prove that exact QVD exists or run its generation branch. Digital Analytics creates only when vETL_SI_FactSalesOrder=1; >=1 permits reading, so reuse value2 cannot bootstrap a missing version. Respect vOverride and set the existing controlling configuration, not a later assignment that is overwritten.

Verify this procedure with representative destination inputs and retain reproducible evidence in the canonical record.
