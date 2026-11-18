---
id: SKILL-0266
type: skill
title: Sigma Source Configuration
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [PLAY-0012, PLAY-0018, SKILL-0002, SKILL-0046, SKILL-0047, SKILL-0048, SKILL-0049, SKILL-0050]
tags: [skill, sigma, source-configuration]
trigger_phrases: [configure sigma source, add sigma model source, sigma source grain]
---

# Sigma Source Configuration

Configure one approved Snowflake-backed source for use in a Sigma semantic model.

## Intent-routing contract

This Skill owns source selection, source grain, exposed fields and source-level verification. Relationships, reusable metrics and domain boundaries are separate Skills.

## When to use

Use when adding or changing a source table, view, dynamic table or governed semantic object in a Sigma model.

## Method

1. Confirm the approved Snowflake object, environment and access path. For Snowflake-backed reporting, facts and dimensions feed a Snowflake Semantic View, then the per-report golden dynamic table feeds Sigma. A golden view requires the Library owner's direction or an evidenced constraint; temporary testing and explicit front-end capabilities follow their approved exceptions.
2. State the source's one-row grain, keys, freshness contract and intended analytical purpose.
3. Reuse governed Snowflake facts, dimensions and semantic definitions; do not recreate portable modelling in Sigma.
4. Expose only fields required by the domain while preserving governed names, types and business meaning.
5. Verify representative row counts, key populations, freshness and field availability after configuration.
6. Keep expensive reusable cross-tool logic in Snowflake unless an evidenced Sigma-only requirement is approved.

## Benchmark case

A governed sales dynamic table is added as a Sigma source with documented daily-store-department grain, verified key populations and freshness, and no duplicated transformation logic.

Boundary design case: A visible source has the expected columns but its one-row grain or freshness is unknown. Stop dependent configuration/acceptance at that gap; visibility alone cannot prove the approved source contract.

## Anti-patterns

- Selecting a source because its name appears suitable without proving grain.
- Rebuilding governed Snowflake transformations in Sigma.
- Treating source visibility as proof of correct access, freshness or population.

## Stop

Stop when the named source, grain, fields, access and representative population are read back and verified, or when any source contract remains unresolved.
