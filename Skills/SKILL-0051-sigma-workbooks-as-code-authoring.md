---
id: SKILL-0051
type: skill
title: Sigma Workbooks-as-Code Authoring
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050, SKILL-0264, SKILL-0265]
tags: [skill, sigma]
trigger_phrases: [sigma-workbooks-as-code, workbook representation, coco sigma workbook]
---

# Sigma Workbooks-as-Code Authoring

Author and mutate Sigma workbook representations using the current official schema and safe mutation boundaries.

## When to use

Use when creating, inspecting or changing a Sigma workbook through Workbooks as Code, CoCo, CLI or an agent.

## Method

1. Confirm the current official Sigma workbook schema and capability.
2. Retrieve the current workbook representation before mutation; preserve IDs and unsupported properties.
3. State source, grain, pages, controls, metrics, visuals, layout, style, interactions and validation explicitly.
4. Change only the intended workbook representation; distinguish workbook from report objects.
5. Read back the result and compare behaviour, formulas, references and governed totals.

## Benchmark case

An existing manual workbook is rebuilt as code; the result round-trips, retains supported interactions and reconciles to the manual workbook's metrics.

Boundary design case: an exported workbook contains properties the current mutation schema does not support. Preserve them and identify the mutation limit before writing; a generated representation that drops those properties is not a faithful round-trip or evidence of equivalent workbook behaviour.

## Anti-patterns

- Inventing Sigma capabilities, identifiers, schemas or successful evidence.
- Duplicating governed logic without a measured reason.
- Treating a syntactically accepted change as verified behaviour.

## Stop

Stop after the named outcome is read back and verified, or the precise capability, access, source or evidence gap.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0051--SKILL-0263 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0051--SKILL-0264 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0051--SKILL-0265 | related_to | undirected | user_confirmed | supports
