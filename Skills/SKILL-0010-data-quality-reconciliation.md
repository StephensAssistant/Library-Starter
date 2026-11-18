---
id: SKILL-0010
type: skill
title: Source-to-Target Reconciliation
status: current
created: 2026-08-23
updated: 2026-10-26
links: [HAT-0015, HAT-0016, PLAY-0046, PLAY-0047, PLAY-0072, PLAY-0073]
tags: [data-quality, reconciliation, source-to-target]
trigger_phrases: ["reconcile source to target", "find where data diverges", "compare source and target totals", "identify the earliest failing boundary"]
source_skill: data-quality-and-reconciliation
---

# SKILL-0010 — Source-to-Target Reconciliation

## Purpose

Reconcile expected populations and material values boundary by boundary to identify the earliest point where source and target diverge.

## When to use

Use for a defined source-to-target lineage with known grain, keys, period and acceptance tolerance. Route freshness, migration parity, variance classification, control design and root-cause classification to their specific Skills.

## Method

1. Confirm decision, authoritative source, lineage, grain, keys, period, timezone/currency rules, tolerance and owner.
2. Capture source rows, distinct keys, nulls, duplicates, date range and material totals before transformation.
3. Reconcile each boundary in sequence, keeping population differences separate from value differences.
4. Segment mismatches by date, entity, source, status and rule.
5. Identify the first boundary where expected population or value changes incorrectly.
6. Retest the full affected population after correction and preserve residual exceptions.
7. Return a ledger with source, target, variance, tolerance, verdict, exception population, earliest divergence, owner and timestamp.

## Benchmark case

Trace a missing sales population from source through landing, staging, fact and report, proving the first boundary where expected keys disappear rather than rewriting the final report.

## Anti-patterns

- Starting with downstream rewrites.
- Comparing grand totals only.
- Netting positive and negative exceptions.
- Moving tolerance after seeing the result.
- Inventing outages, missing records or successful reruns.

## Stop

Stop with the earliest failing boundary and evidence ledger, or the exact ambiguity preventing a valid comparison.

## Worked reporting-projection evidence —15October2026


- FACT allocation may reconcile while a downstream rejoin repeats/loses points. Prove projected contributions reproduce actual allocation-bearing output before diagnosing them. Counting nonmatched sales rows overstated the exceptions and was rejected; corrected projection matched exactly.
- Compare allocated sums at transaction/order/component grain, never summed repeated source amounts. Keep42 registered exclusions (-38000) separate from coverage defects; missing442 earned/2500 redeemed was a real gap, not rounding.
- Independent QUALIFY runs with incomplete tie-breaking can select different sales rows. A failed preservation check remains failed. Freezing one baseline then enriching its selected rows passed; this did not fix the selector's determinism.
- NULL line equality lost292 earned/-500 redeemed. Missing sales date failed an earlier year join despite a later fallback. Recovery preserved original allocations and appended no sales/margin amount.
- Separate exclusions, reporting date/load scope and customer reporting scope. A zero arithmetic identity is not causal proof; independently compare Qlik reproduction, source controls and unique tiers. Do not call the combined date/load residual pure timing.

No production action, candidate execution or independent guidance acceptance follows from these examples.



## Verified liability selected-scope and deployment boundaries — 21 October 2026


- Independently align source business dates, selected customer eligibility and visible merchandise filters before calling an allocation defect. A 200-point date-boundary difference and a restaurant-filter difference were distinct from source coverage.
- Endpoint-dependent eligibility makes separately correct period totals non-additive across independently scoped endpoints. One common selected endpoint reconciled P5 20,558,512.33, P4–P5 36,837,377.31 and all-history 227,722,099 earned points.
- A read-only proof is not deployment evidence. Track the view apply, correct row flag/field load, Qlik refresh and rendered result separately. The old raw-RnR loader returned 37,027,762.31 for P4–P5 until it selected the new scoped rows.
- Preserve original output using count plus an explicit-column value fingerprint. Here 97,910,786 Yotpo rows and fingerprint 5142255540999825893 were unchanged; owner and six SELECT grants were verified independently.
- Keep floating residuals visible under the established 0.005-point tolerance; do not force fractional source points to integer precision. User sign-off covered every full-history metric, not just net arithmetic.

This is a scoped worked example, not authority to add snapshots or alter eligibility in another app. No new core method, trigger, relationship, source call, runtime or merge authority is introduced.
