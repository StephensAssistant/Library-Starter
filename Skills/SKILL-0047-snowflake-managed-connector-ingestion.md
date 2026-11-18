---
id: SKILL-0047
type: skill
title: Snowflake Managed-Connector Ingestion
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0003, SKILL-0051, SKILL-0052, SKILL-0054, SKILL-0056, SKILL-0057, SKILL-0058, SKILL-0267, SKILL-0268, SKILL-0269, SKILL-0271]
tags: [skill, snowflake, ingestion, managed-connectors]
trigger_phrases: [snowflake managed connector, openflow ingestion, connector state]
---

# Snowflake Managed-Connector Ingestion

Implement and validate ingestion where OpenFlow or another managed connector owns extraction and landing behaviour.

## When to use

Use when a managed connector supplies source objects to Snowflake and owns some combination of pagination, state, retries, schema, deletes or destination writes.

## Method

1. Verify connector definition, source scopes, delivered grain and stable identifiers.
2. Record exactly which extraction, checkpoint, retry, schema-evolution and delete behaviours the connector owns.
3. Do not duplicate connector state downstream without evidenced need.
4. Add governed downstream layers only for history, contract stability, transformation or reconciliation.
5. Prove field, grain, incremental, recovery, performance and cost behaviour before retiring a working fallback.

## Benchmark case

OpenFlow is proposed to replace a Shopify extractor. A passing application proves object coverage, stable IDs, update/delete behaviour and recoverability against the existing route before decommissioning it.

Boundary design case: a connector returns zero rows after a scope change. Verify effective object/field permissions and expected source population before declaring source absence; keep the working fallback until coverage and incremental/recovery behaviour are evidenced, rather than retiring it from the successful status alone.

## Anti-patterns

- Wrapping a connector in unnecessary file layers.
- Assuming connector-managed state is complete or replay-safe without evidence.
- Retiring the fallback after one successful load.
- Treating missing permissions as missing data.

## Stop

Stop after connector behaviour and downstream contract are evidenced, or the precise scope, state, recovery or parity gap.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0047--SKILL-0266 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0047--SKILL-0267 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0047--SKILL-0268 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0047--SKILL-0269 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0047--SKILL-0270 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0047--SKILL-0271 | related_to | undirected | user_confirmed | supports
