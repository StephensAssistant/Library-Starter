---
id: SKILL-0151
type: skill
title: Household Product Attribute Enrichment
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["find grocery pack size", "research household product", "enrich receipt product"]
links: []
tags: [skill, action-specific]
---

# Household Product Attribute Enrichment

Research missing household product attributes from authoritative product and retailer evidence.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use after receipt or barcode extraction when identity, pack configuration or planning-relevant attributes remain unresolved.

## Method

1. Search the exact retailer variant or SKU first, then manufacturer and reputable retailer listings.
2. Open the supporting page and record URL, retrieval date and whether each value is explicit, calculated or provisional.
3. Keep competing candidates when flavour, count, size or SKU conflicts.
4. Keep net and drained weights separate; never substitute nutrition per-100g values for pack weight.
5. Ask for one relevant photo or barcode only when evidence cannot resolve a material choice.

## Decision and evidence details

Return the candidate product identity and each enriched attribute with its evidence URL/date, exact variant and explicit/calculated/provisional status. Keep calculations traceable to their evidenced inputs; unresolved identity must not become a confirmed product value.

Boundary design case: the current retailer page has the same name but a different pack count from the receipt. Retain both candidates and the historical-edition gap instead of replacing the purchased pack configuration with today's listing.

## Benchmark case

A six-count bread product is enriched from an exact retailer page showing 225g total and 37.5g per item, with provenance retained.

## Anti-patterns

- Choosing by similar wording alone
- Treating a current listing as proof of a historical edition
- Hiding conflicting sizes

## Sources

- https://openfoodfacts.github.io/openfoodfacts-server/api/

## Stop

Stop when useful attributes are evidenced or each unresolved attribute has one precise evidence request.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0061--SKILL-0151 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: PLAY-0062--SKILL-0151 | related_to | undirected | inherited_from_source_split | supports
