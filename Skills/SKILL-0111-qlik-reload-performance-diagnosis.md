---
id: SKILL-0111
type: skill
title: Qlik Reload Failure Diagnosis
status: current
created: 2026-09-20
updated: 2026-10-31
trigger_phrases: ["Qlik reload failure", "failed Qlik reload", "diagnose Qlik reload"]
links: []
tags: [qlik, reload, failure-diagnosis]
---

# Qlik Reload Failure Diagnosis

Prove the earliest failing boundary of a Qlik reload and its safe recovery.

## Intent routing contract

Activate only for Qlik reload failure, failed Qlik reload, diagnose Qlik reload or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to prove the earliest failing boundary of a Qlik reload and its safe recovery.

## Method

1. Collect the current failed run identity, complete reload log, schedule context and last accepted result.
2. Classify the first failure as source availability, authentication, script, model or platform-resource behavior.
3. Reproduce only the earliest failed boundary with representative conditions and preserve the exact error.
4. Apply the smallest evidenced repair, rerun the full reload and verify recovery plus output parity.

## Decision and evidence details

Before rerunning, inspect which source reads, stores and other effects completed in the failed run. Retain the last confirmed boundary and distinguish failed, completed and unknown effects. If a repeated operation could overwrite or duplicate output, resolve that recovery boundary before replay; a failed reload does not prove no output changed.

Boundary design case: the reload fails after a STORE. Inspect that stored output before retrying, then verify full recovery and parity rather than reporting success from the repaired fragment.

## Benchmark case

A failed reload is classified from its current log, repaired at the first failing boundary and accepted only after full reload and output-parity evidence.

## Anti-patterns

- Expanding this Skill into an adjacent diagnosis, execution or verification job.
- Treating one inconsistent precedent or assumption as authority.
- Proceeding through an unresolved evidence or authority gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the current reload log, failing run identity, schedule context or recovery boundary is unavailable.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; adjacent jobs moved to independent Skills.
