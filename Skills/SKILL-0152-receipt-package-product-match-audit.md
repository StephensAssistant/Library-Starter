---
id: SKILL-0152
type: skill
title: Receipt-to-Package Product Match Audit
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["audit receipt product matches", "compare receipt to packaging", "benchmark receipt extraction"]
links: []
tags: [skill, action-specific]
---

# Receipt-to-Package Product Match Audit

Audit extracted receipt facts against later package or barcode evidence without rewriting either source.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use when measuring extraction accuracy or reconciling receipt and physical-product evidence.

## Method

1. When possible, complete receipt extraction before consulting confirmation data; otherwise label the audit retrospective.
2. Use retained receipt lines, not physical units, as the denominator.
3. Separate clear weight/volume, count-only, conflicting fields, unresolved candidates and unavailable attributes.
4. Cross-check later package evidence without rewriting the original receipt evidence.
Save accepted per-line results, conflicts and corrections in the owner-approved canonical artifact.

## Retained ASDA calibration cases

For order 70000074488622, preserve these independently evidenced audit outcomes:

- ASDA garlic doughball tear-and-share: 165g title versus 0.17kg metadata; title wins for extraction and the discrepancy remains recorded.
- Penguin Bites: 125g title versus 0.252kg metadata; title wins for extraction and the discrepancy remains recorded.
- Frijj: receipt and physical-product flavour conflict remains an identity conflict.
- Cadbury Mini Rolls: 26g per roll and 270g per 10-pack describe inner-unit and total-pack levels, not competing remaining-stock values.

## Decision and evidence details

Keep each receipt line's original extraction, later confirmation source and classified outcome separately. Missing packaging evidence is unavailable, not a correct match or an extraction failure. After an authorised audit write, read back the designated per-line entries and verify original source facts remain preserved.

Boundary design case: only some receipt lines have later package photos. Report coverage and unavailable lines using the retained receipt-line denominator; do not claim the photographed subset measures complete-receipt accuracy.

## Benchmark case

A receipt title and package disagree on snack weight; the audit preserves both values, records the confirmed correction and reports the conflict category.

## Anti-patterns

- Claiming blind accuracy from retrospective work
- Changing source evidence to match packaging
- Combining distinct outcome classes

## Sources

- https://openfoodfacts.github.io/openfoodfacts-server/api/

## Stop

Stop when every audited line has a classified outcome and evidence trail.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0061--SKILL-0152 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: PLAY-0062--SKILL-0152 | related_to | undirected | inherited_from_source_split | supports
