---
id: SKILL-0164
type: skill
title: Evidence-based Delivery Forecasting
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, project-management, forecasting, confidence]
trigger_phrases: [forecast delivery, estimate milestone date, delivery confidence]
---

# Evidence-based Delivery Forecasting

Forecast an outcome only as precisely as current evidence permits.

## When to use

Use when a milestone date, delivery range or outcome confidence is requested.

## Method

1. Establish completed acceptance evidence and bounded remaining work.
2. Identify material dependencies, tests, decisions and duration assumptions.
3. Use a date only when supported; otherwise use a range or qualitative confidence.
4. Classify confidence as high, medium or low and state the evidence-based reason.
5. Refresh the forecast after material scope, dependency, test or acceptance changes.

## Decision and evidence details

Record the forecast's as-of date, target outcome, remaining acceptance work, dependency assumptions and evidence supporting its precision/confidence. Make any range conditional on the assumptions actually used; missing duration or external-date evidence cannot become a numerical estimate by default.

Boundary design case: an external dependency has no credible arrival range. State that condition and a qualitative forecast limitation rather than manufacturing bounded dates or interpreting implementation completion as delivery acceptance.

## Benchmark case

Implementation is complete but an external source date is unknown. A passing forecast uses a conditional range and medium or low confidence rather than inventing a delivery date.

## Anti-patterns

- Fabricating dates or percent complete.
- Using confidence for appearance.
- Ignoring unresolved external dependencies.

## Stop

Stop with the most precise defensible forecast and its evidence, assumptions and gaps.
