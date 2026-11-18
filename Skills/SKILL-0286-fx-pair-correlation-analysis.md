---
id: SKILL-0286
type: skill
title: FX Pair-Correlation Analysis
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, fx, correlation, trading]
trigger_phrases: ["analyse FX pair correlations", "measure rolling FX correlation", "compare stressed pair correlation"]
---

# FX Pair-Correlation Analysis

Measure current and stressed dependence between FX pair returns without treating historical correlation as permanent.

## Intent-routing contract

This Skill owns pair-correlation analysis only. Common-currency, macro-factor and effective portfolio-concentration assessment are separate actions.

## When to use

Use when relationships between specified FX pair returns must be measured over defined current and comparison windows.

## Method

1. Confirm the pair universe, return interval, weighting and analysis windows.
2. Align timestamps and handle missing observations without manufacturing returns.
3. Calculate pairwise rolling dependence over the declared windows.
4. Compare normal, recent and stressed periods where sufficient evidence exists.
5. Report direction, magnitude, stability, sample limitations and materially changed relationships.
6. Do not convert historical estimates into fixed future assumptions.

## Output evidence

Retain the price/data source and capture time, return construction, timestamp alignment, missing-observation treatment and actual sample coverage for each reported window. State which stressed/current comparisons lack enough evidence rather than filling them with another period.

## Benchmark case

Correlations among a defined FX pair set are measured over normal and stressed windows, showing which relationships strengthened, weakened or changed sign without claiming permanence.

Boundary design case: The stressed window lacks aligned returns for one pair. Report that pair/window as unassessed with the sample limitation; do not manufacture returns or apply a normal-window estimate as stressed evidence.

## Anti-patterns

- Using price levels instead of aligned returns without justification.
- Mixing windows or frequencies without disclosure.
- Treating one historical estimate as constant.
- Converting correlation alone into factor or concentration conclusions.

## Stop

Stop when pairwise current and stressed dependence, window choices, instability and evidence limitations are explicit.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0016--SKILL-0286 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0286 | related_to | undirected | inherited_from_source_split | supports
