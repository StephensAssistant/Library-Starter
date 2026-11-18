---
id: SKILL-0108
type: skill
title: Qlik Associative-Model Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [qlik, associative-model, diagnostics]
trigger_phrases: ["Qlik association issue", "synthetic key", "circular reference", "composite key"]
---

# SKILL-0108 — Qlik Associative-Model Diagnosis

## Purpose

Diagnose Qlik associative-model failures and identify the earliest proven key or grain defect.

## Intent routing contract

Activate only for Qlik association issue, synthetic key, circular reference, composite key or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. State each table's grain and intended relationship.
2. Inspect the table viewer for synthetic keys, circular references, unintended concatenation and fan-out.
3. For composite keys, compare every component's type, case, trimming, null handling and formatting.
4. Count distinct, matched, unmatched and duplicate key populations on both sides.
5. Check preload renaming and non-portable surrogate components.
6. Change only the earliest proven failing boundary and repeat the population checks.

## Anti-patterns

- Adding associations merely to populate a blank visual.
- Assuming equal field names prove compatible populations.
- Fixing fan-out without first proving intended grain.

## Benchmark case

For blank store coverage, a passing diagnosis identifies the composite components, proves unmatched populations, isolates one renamed component and verifies the repaired association without synthetic keys.

Boundary design case: a visual is blank but source keys and intended table grain are unavailable. Record those exact diagnosis gaps and inspect the load/association evidence first; do not create an association or remove a key merely to make the visual populate.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when intended grain, authoritative keys or representative populations cannot be established.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.
