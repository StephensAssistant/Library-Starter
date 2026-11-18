---
id: SKILL-0268
type: skill
title: Sigma Domain-Boundary Configuration
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0002, SKILL-0047, SKILL-0049, SKILL-0050]
tags: [skill, sigma, semantic-domain]
trigger_phrases: [define sigma model boundary, split sigma semantic domain, sigma domain scope]
---

# Sigma Domain-Boundary Configuration

Define a coherent Sigma semantic-model boundary for an approved analytical domain.

## Intent-routing contract

This Skill owns model scope and domain inclusion/exclusion decisions. Source, relationship and reusable metric configuration are separate Skills.

## When to use

Use when deciding which governed facts, dimensions and metrics belong together in one Sigma model or should remain separate.

## Method

1. State the users, decisions, subject area and governed business processes the domain must support.
2. Identify required facts, conformed dimensions, reusable metrics and cross-domain dependencies. Snowflake owns the modelling and Semantic View; Sigma consumes approved per-report golden dynamic tables. This domain boundary organises presentation consumption and does not authorise a competing Sigma semantic layer or direct FACT/DIM serving outside approved exceptions.
3. Keep sources together only when they share coherent analytical purpose, compatible grain and governed relationships.
4. Avoid both one estate-wide mega-model and isolated report fragments that duplicate definitions.
5. Record explicit inclusions, exclusions, hand-offs and ownership boundaries.
6. Verify representative questions can be answered without importing unrelated data or duplicating governed logic.

## Benchmark case

A sales-performance domain includes sales facts, store/product/date dimensions and approved sales metrics, while loyalty-member detail remains in its own domain with an explicit governed hand-off.

Boundary design case: Two facts share a date column but have incompatible grain and no governed relationship. Do not combine them into one presentation domain merely from that common field; name the unresolved boundary.

## Anti-patterns

- Defining a domain from one report layout.
- Combining unrelated facts because they share a date field.
- Splitting every report into an isolated model with duplicate metrics.

## Stop

Stop when domain purpose, included and excluded governed objects, cross-domain hand-offs and ownership are explicit, or when an unresolved boundary changes model scope.

