---
id: SKILL-0003
type: skill
title: Sigma Workbook Engineering
status: current
created: 2026-08-22
updated: 2026-11-02
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050, SKILL-0264, SKILL-0265, SKILL-0291]
tags: [skill, sigma, workbook, implementation]
trigger_phrases: [sigma workbook, build sigma report, sigma workbook element]
source_skill: sigma-computing
migrated_from: SKILL-0003-old-library
---

# Sigma Workbook Engineering

Build and modify native Sigma workbooks using verified tenant capabilities and governed Snowflake sources. This Skill owns workbook implementation; specialised modelling, composition, performance, code authoring, formulas, writeback and automation use their independent Skills.

## When to use

Use for implementing pages, elements, controls, filters, interactions and supported workbook behaviour in Sigma.

## Method

1. Confirm audience, business question, governed source, grain, metrics, security and acceptance criteria.
2. Verify current Sigma capability before prescribing a menu path, property or element.
3. Build from shared parent elements where that preserves grain and lets common controls apply once.
4. Use native Sigma capabilities first; compose verified elements when one object cannot express the required result.
5. Validate source totals, filters, interactions, formatting and user-facing response before release.
6. Report unsupported or unverified behaviour rather than substituting another platform's features.
7. For dynamic Top/Bottom N, target the native control at the aggregate metric that changes with the Rank By selection. Use the control's verified ranking function; do not add a displayed row-number measure unless its evaluation grain is independently proved. Reconcile the selected population and tie-break order to a warehouse query.
8. After a serving-layer column rename, resynchronise the Sigma source and inspect every custom-SQL and formula reference for the exact new identifier. Quoted business aliases replace underscore identifiers literally; a successful source refresh does not rewrite dependent SQL.
9. When a rendered measure is unexpectedly null, trace the same keys directly through the governed facts before changing joins or coercing nulls to zero. A populated field elsewhere proves availability, not that the selected products have matching source rows.

## Tenant evidence

Test Top/Bottom N at the intended grain. Compare native ranking against an independent warehouse result and recheck exact quoted aliases after a source change.



## Benchmark case

A governed sales workbook needs KPIs, controls, ranking and detail. A passing application verifies each Sigma element, preserves metric grain, applies shared controls correctly and reconciles the rendered result to governed totals.

Boundary design case: a requested control property is absent from the current tenant. Record the observed capability limit and the affected requirement; propose only a verified native composition and leave acceptance open until its filters and totals are reconciled.

## Anti-patterns

- Inventing Sigma controls or menu paths.
- Treating visual similarity as data correctness.
- Rebuilding business logic separately in each workbook.
- Using custom SQL as the default semantic layer.

## Stop

Stop after the requested workbook behaviour is built and reconciled, or the precise capability, source, grain, security or acceptance gap.

## Learning evidence — 30 October 2026

Test Top/Bottom N at the intended grain. Compare native ranking against an independent warehouse result and recheck exact quoted aliases after a source change.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0012--SKILL-0003 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0018--SKILL-0003 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: SKILL-0002--SKILL-0003 | related_to | undirected | authoritative_record | supports

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0003--SKILL-0263 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0003--SKILL-0264 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0003--SKILL-0265 | related_to | undirected | user_confirmed | supports


## Relationship evidence (2026-09-21 atomic Sigma split)

RELATIONSHIP-EVIDENCE: SKILL-0003--SKILL-0290 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0003--SKILL-0291 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0003--SKILL-0292 | related_to | undirected | user_confirmed | supports

## Contextual links

