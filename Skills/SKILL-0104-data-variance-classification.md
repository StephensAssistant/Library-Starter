---
id: SKILL-0104
type: skill
title: Data Variance Classification
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [data-quality, variance]
trigger_phrases: ["classify a data variance", "population or value variance", "explain a reconciliation difference"]
---

# SKILL-0104 — Data Variance Classification

## Purpose

Classify a reconciliation difference as population, allocation, value or timing variance before root-cause work.

## When to use

Use for: classify a data variance; population or value variance; explain a reconciliation difference.

## Method

1. Compare business-key populations first.
2. Test whether the same total is assigned to different entities, categories or dates.
3. Compare values only across matched populations.
4. Compare source capture timestamps and late-arrival state.
5. Allow multiple labels when evidence proves compound variance; never net exceptions away.

## Benchmark case

Classify two systems with equal totals but different store allocation as allocation variance, not parity.

Boundary design case: the same keys have different values and capture times are unknown. Record the observed value variance and missing timing evidence; do not label it pure timing or a confirmed logic defect until the discriminating source-state comparison is available.

## Anti-patterns

- Treating a matching total as proof.
- Treating row-count equality as content equality.
- Netting positive and negative exceptions.

## Stop

Stop with evidenced variance class, affected population and next diagnostic boundary.



## Worked report-design bridge —15October2026


Valid report-date, established loyalty/tier population and registered-exclusion differences can combine. Fix true allocation defects first and keep them separate. P5 earned-207572.6696 comprises scope-188968 and report-date/load-18604.6696, with negligible allocation arithmetic. Redeemed combines registered-3800, date/load-3981.3552 and customer scope+1200. All-history exclusions-38000 are not the P5 amount.

Use neutral existing customer reporting scope wording for intended filters. Do not infer a customer/source defect, promise dates differ by at most one day, or call a measured date/load residual proven pure timing. A matching grand total is not full store/product/date allocation parity.
