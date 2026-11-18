---
id: SKILL-0009
type: skill
title: Dimensional Model Design
status: current
created: 2026-08-23
updated: 2026-10-31
links: []
tags: [dimensional-modelling, star-schema, fact, dimension]
trigger_phrases: ["design a dimensional model", "define fact and dimension tables", "choose model grain", "design a star schema", "choose an SCD strategy"]
source_skill: sql-and-dimensional-modelling
---

# SKILL-0009 — Dimensional Model Design

## Purpose

Design an analytical dimensional model with explicit business process, one-row grain, fact behaviour, conformed dimensions, history and portable identity.

## When to use

Use when defining fact/dimension structures or history behaviour. Route SQL authoring, key mapping, semantic boundaries, serving choice, join proof, migration and performance to their specific Skills.

## Method

1. Confirm the business process, analytical question, consumers, security and freshness.
2. State the one-row grain before selecting fields or relationships.
3. Classify measures as additive, semi-additive or non-additive.
4. Define dimensions, conformed meanings, business keys, warehouse surrogate keys and unknown-member behaviour.
5. Choose overwrite, Type 2, accumulating snapshot, periodic snapshot or bridge from the decision need.
6. Document relationship cardinalities, history rules, calendar/timezone and acceptance measures.
7. Return a model packet with grain, fact/dimension definitions, relationships and unresolved business decisions.

## Benchmark case

Design daily sales facts with conformed store, product and date dimensions, explicit additive and semi-additive measures, portable business keys and justified history behaviour without combining unrelated grains.

Missing-input design case: sales lines and daily inventory balances are proposed for one fact without an agreed grain. Keep the distinct grains visible and return the required business decision; do not use aggregation or an arbitrary SCD choice to conceal it.

## Anti-patterns

- Selecting columns before grain.
- Combining unrelated processes into one mega-fact.
- Treating matching surrogate-key names as shared identity.
- Choosing SCD behaviour by habit.
- Inventing business definitions.

## Stop

Stop with an implementable dimensional specification or the exact unresolved grain, key or measure decision.

## Relationship evidence

RELATIONSHIP-EVIDENCE: HAT-0015--SKILL-0009 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0016--SKILL-0009 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0046--SKILL-0009 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0047--SKILL-0009 | related_to | undirected | authoritative_record | supports
