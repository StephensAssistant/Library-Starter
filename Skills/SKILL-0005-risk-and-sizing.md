---
id: SKILL-0005
type: skill
title: FX Position Sizing
status: current
created: 2026-08-22
updated: 2026-10-31
links: [PLAY-0026, SKILL-0001, SKILL-0004, SKILL-0059, SKILL-0060, SKILL-0061, SKILL-0062, SKILL-0063, SKILL-0064, SKILL-0065, SKILL-0066, SKILL-0067, SKILL-0068, SKILL-0069, SKILL-0272, SKILL-0273, SKILL-0274, SKILL-0275, SKILL-0276, SKILL-0286]
tags: [fx, position-sizing, trading-risk]
trigger_phrases: ["calculate FX position size", "how much should I trade", "size this strategy", "choose lot size", "risk per position"]
source_skill: risk-and-sizing
migrated_from: SKILL-0005-old-library
---

# SKILL-0005 — FX Position Sizing

## Purpose

Calculate an evidence-bounded position-size range for the current account and strategy configuration from survivability, broker constraints, uncertainty and accepted loss tolerance.

## When to use

Use when a current lot size or capital-allocation range is required. Do not use historical thresholds or configuration without verification.

## Method

1. Verify the current account, broker constraints, executable configuration and representative outcome sample.
2. Take current portfolio-dependence evidence and actual configured grid/path exposure from their action-specific Skills.
3. Define expected, severe and tail loss consequences, liquidation distance and accepted drawdown policy; do not invent acceptance thresholds.
4. Apply uncertainty haircuts to edge, payoff, volatility, correlation and tail estimates.
5. Calculate a range of feasible sizes with assumptions, margin consequences and de-risking points.
6. Recommend only a size that remains inside verified constraints and the Library owner's explicitly accepted risk policy.

## Benchmark case

Given current equity, broker margin rules, configured grid limits, dependence evidence and three stress-loss estimates, produce a sizing range with free-margin and drawdown consequences rather than a falsely precise lot number.

Missing-input design case: equity is current but the broker margin contract or accepted drawdown policy is missing. Identify the exact missing constraint; return no recommended executable size until it is verified, rather than inserting a remembered limit.

## Anti-patterns

- Multiplying single-trade risk by pair count as if pairs were independent.
- Sizing from the worst observed loss alone.
- Increasing size to recover losses.
- Hard-coding remembered broker or drawdown thresholds.
- Recommending size while execution or configuration is unverified.

## Stop

Stop with a bounded sizing recommendation, evidence, assumptions and residual risk, or identify the exact missing input that prevents a safe calculation.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0001--SKILL-0005 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0026--SKILL-0005 | related_to | undirected | authoritative_record | supplies current risk and sizing evidence gate

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0272 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0273 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0274 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0275 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0276 | related_to | undirected | user_confirmed | supports

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: SKILL-0005--SKILL-0286 | related_to | undirected | user_confirmed | supports
