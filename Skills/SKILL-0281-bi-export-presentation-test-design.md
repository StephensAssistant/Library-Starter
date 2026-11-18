---
id: SKILL-0281
type: skill
title: BI Export and Presentation Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0007]
tags: [skill, testing, bi, export, presentation]
trigger_phrases: ["design BI export tests", "test dashboard export", "validate report presentation"]
---

# BI Export and Presentation Test Design

Design tests for BI export fidelity and final user-facing presentation after data correctness is established.

## Intent-routing contract

This Skill owns export and presentation test design only. Semantic correctness, interaction, security and performance testing are separate actions.

## When to use

Use when PDF, image, spreadsheet or other supported exports and the final rendered presentation require validation.

## Method

1. Confirm semantic and metric correctness has already passed.
2. List supported export formats, intended audience, scope and presentation constraints.
3. Test headers, labels, units, ordering, pagination, truncation, wrapping, conditional formatting and visible filters.
4. Reconcile exported rows and material totals to the validated report state.
5. Test representative screen sizes or presentation modes where required.
6. Record platform limitations separately from defects.

## Benchmark case

A validated sales report is exported to PDF and spreadsheet; the PDF preserves layout and visible filter context while the spreadsheet retains complete rows, columns and reconciled totals.

Boundary design case: The PDF looks complete but source metric correctness has not passed. Preserve the presentation observations and block dependent fidelity acceptance; appearance cannot replace the required semantic proof or executed export tests.

## Anti-patterns

- Testing presentation before data correctness.
- Checking appearance without reconciling exported data.
- Assuming one export format represents every format.
- Hiding a platform limitation as a passed test.

## Stop

Stop when every required format and presentation mode has an explicit fidelity and data-reconciliation test or one precise unsupported capability.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0281 | related_to | undirected | inherited_from_source_split | supports
