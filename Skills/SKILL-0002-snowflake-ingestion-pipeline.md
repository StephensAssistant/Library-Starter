---
id: SKILL-0002
type: skill
title: Snowflake Ingestion Architecture Selection
status: current
created: 2026-08-22
updated: 2026-10-31
owner: Library owner

links: [SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0054, SKILL-0056, SKILL-0057, SKILL-0058, SKILL-0267, SKILL-0268, SKILL-0269, SKILL-0271]
tags: [skill, snowflake, ingestion, architecture]
trigger_phrases: [snowflake ingestion architecture, choose ingestion pattern, classify data source]
source_skill: snowflake-ingestion-pipeline
migrated_from: SKILL-0002-old-library
---

# Snowflake Ingestion Architecture Selection

Select the correct Snowflake ingestion pattern from the source mechanism and required control objectives. This Skill chooses the route; implementation belongs to the action-specific Skill for that route.

## When to use

Use before designing a new Snowflake ingestion route or materially changing how a source reaches Snowflake. Classify the source as staged file, managed connector, API/GraphQL, CDC/event feed, application-maintained data, or already-landed derived transformation.

## Method

1. Confirm the authoritative source, grain, stable identifiers, extraction boundary, update/delete semantics, replay needs, consumer contract and credential boundary.
2. Select only layers with a defined responsibility. File routes commonly use source → transport → Snowflake stage → RAW → STAGING → INGESTED; direct connectors, APIs and applications may enter through a different verified boundary.
3. Require traceability, repeatability, recoverability, reconciliation and governed consumer access for every route.
4. Add FACT, DIM, semantic or serving objects only when the consumer or reusable business model requires them; a governed pipeline may stop at INGESTED.
5. Hand implementation to the matching independent Skill. Do not absorb its procedure here.

## Benchmark case

**Scenario:** Shopify data could arrive through OpenFlow or a custom GraphQL extractor.

A passing application classifies both mechanisms, compares their owned state and recovery boundaries, preserves the same governed consumer contract, and routes each implementation to its specific Skill without forcing either through an unsuitable file pattern.

Missing-input design case: the source exposes updates but its delete and replay semantics are unknown. Record the unresolved semantics and block selection dependent on them; a convenient connector or familiar file pattern does not establish recoverability.

## Anti-patterns

- Treating every source as a five-object file pipeline.
- Choosing a mechanism before source authority, grain or recovery needs are known.
- Adding modelling layers only to complete a diagram.
- Mixing architecture selection with connector, API or load implementation.

## Stop

Stop with one evidenced ingestion pattern and named implementation Skill, or the precise missing fact that prevents selection.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0018--SKILL-0002 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0025--SKILL-0002 | related_to | undirected | authoritative_record | supplies canonical ingestion architecture judgement

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0002--SKILL-0266 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0002--SKILL-0267 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0002--SKILL-0268 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0002--SKILL-0269 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0002--SKILL-0270 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0002--SKILL-0271 | related_to | undirected | user_confirmed | supports
