---
id: SKILL-0102
type: skill
title: Data Freshness and Missing-Period Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-11
links: [HAT-0015, HAT-0016, PLAY-0046, PLAY-0047]
tags: [data-quality, freshness]
trigger_phrases: ["diagnose missing data", "investigate a missing business date", "check source freshness"]
---

# SKILL-0102 — Data Freshness and Missing-Period Diagnosis

## Purpose

Determine whether missing or late data originates at the source, extraction, landing, transformation or consumption boundary.

## When to use

Use for: diagnose missing data; investigate a missing business date; check source freshness.

## Method

1. Confirm the expected date/window, arrival time, timezone and normal late-arrival behaviour.
2. Check the authoritative source or API for the exact period.
3. Distinguish successful-empty response from technical error and compare adjacent volumes.
4. Verify extraction parameters, landing population and each later boundary in order.
5. After an unchanged empty rerun, stop downstream retries and escalate with source evidence.

## Benchmark case

For one missing footfall date, prove whether the source returns zero rows before diagnosing warehouse tasks, and record a successful-empty response distinctly from failure.

## Anti-patterns

- Blaming the pipeline before checking source availability.
- Repeatedly rerunning unchanged downstream logic.
- Ignoring timezone and late-arrival rules.

## Stop

Stop with the earliest freshness boundary, evidence and responsible owner.

## Recovery versus residual exceptions — 2026-10-11

When a delayed delivery arrives, verify the file/version, landing population, each ingestion boundary, and affected report separately. Compare physical rows and distinct transaction IDs at their actual grains. Retain customer-quality exclusions, orphan keys, unmatched orders, and reporting filters as separate exceptions rather than silently clearing them with the delivery incident.


Representative checks: recovered files and report visibility may resolve a bounded delivery incident while an excluded transaction remains open evidence. A successful empty upstream response is not a technical load failure. Do not claim a reload log, supplier cause, or complete numerical parity when only user-confirmed report visibility exists.

Stop with the earliest failing boundary or scoped recovery evidence and a separate residual-exception ledger. Ticket closure remains subject to the owner's instruction and the folder closure guide.
