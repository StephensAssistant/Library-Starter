---
id: SKILL-0054
type: skill
title: Sigma Relationship Engineering
status: current
created: 2026-09-20
updated: 2026-09-20
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050, SKILL-0264, SKILL-0265]
tags: [skill, sigma, relationships]
trigger_phrases: [sigma relationship, sigma relationship grain, sigma join cardinality]
---

# Sigma Relationship Engineering

Configure and verify relationships between approved Sigma model sources without changing governed business definitions.

## Intent-routing contract

This Skill owns relationship grain, keys, cardinality and fan-out prevention. Source configuration, reusable metric configuration and domain-boundary configuration are separate Skills.

## When to use

Use when relating existing Sigma model sources or diagnosing relationship-driven duplication, omission or unstable totals.

## Method

1. State the one-row grain of both sources and the business meaning of the relationship.
2. Identify verified relationship keys and null, duplicate and unmatched populations.
3. Prove uniqueness on the intended one side before configuring cardinality.
4. Configure only the relationship needed by the approved model.
5. Compare representative row counts and totals with and without related fields to detect fan-out or omission.
6. Preserve governed Snowflake facts, dimensions and semantic definitions.

## Benchmark case

A sales fact is related to a conformed store dimension only after store-key uniqueness is proven; totals remain stable with and without store attributes and unmatched keys are explicitly reported.

## Anti-patterns

- Guessing keys or cardinality from field names.
- Hiding duplicate one-side keys with aggregation.
- Treating a syntactically accepted relationship as verified behaviour.
- Duplicating governed relationship logic without an evidenced need.

## Stop

Stop when the requested relationship and representative totals are verified, or when grain, keys, uniqueness, access or source evidence is unresolved.

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0054--SKILL-0263 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0054--SKILL-0264 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0054--SKILL-0265 | related_to | undirected | user_confirmed | supports
