---
id: SKILL-0011
type: skill
title: Qlik Load-Script Engineering
status: current
created: 2026-08-23
updated: 2026-10-31
links: [HAT-0015, HAT-0016, PLAY-0046, PLAY-0047]
tags: [qlik, load-script, preload]
trigger_phrases: ["Qlik load script", "Qlik preload", "Qlik script change"]
---

# SKILL-0011 — Qlik Load-Script Engineering

## Purpose

Engineer app-local Qlik load-script changes while preserving the established field and consumer contract.

## Intent routing contract

Activate only for Qlik load script, Qlik preload, Qlik script change or equivalent intent. Use associated records for their own jobs; this Skill does not silently expand into adjacent work.

## Method

1. Read the current script, source contract, dependent expressions and accepted baseline.
2. State every loaded table's grain and final Qlik-facing fields.
3. Keep reusable warehouse transformation upstream; keep only intentional app-local shaping in Qlik. For the initial source-only Qlik SQL Server-to-Snowflake migration, preserve the existing load-script transformations under PLAY-0063; moving them upstream or introducing the reporting-model layers belongs to the later rebuild scope.
4. Use explicit preload aliases when physical source names differ from established Qlik names.
5. Change one logical section at a time, reload, and regress dependent fields and selections.

## Anti-patterns

- Mixing source migration, model repair and measure redesign in one change.
- Renaming Qlik-facing fields as incidental cleanup.
- Treating a successful reload as proof of behavioural parity.

## Benchmark case

Given a required new source column, a passing result adds it through an explicit load/preload contract, preserves existing Qlik field names, reloads successfully and proves dependent selections still behave as accepted.

Boundary design case: the revised script reloads but the accepted selection baseline is unavailable. Retain reload evidence separately and report behavioural parity as unverified; do not rename fields or redesign associations to manufacture an acceptance result.

## Output and evidence

Record the inputs, decisions, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop on an unknown field contract, unresolved grain, circular/synthetic-key risk, missing baseline or unavailable reload evidence.

## Verified liability row-class and control contract — 21 October 2026


- Read the current deployed row-class contract before reload changes. IS_YOTPO_ROW selected the preserved daily ledger; IS_RNR_SCOPE_ROW selected finished customer-period endpoint snapshots. IS_RNR_ROW instead returned raw RnR values and caused the observed post-SQL-proof mismatch.
- Load the required RNR_SCOPE_END_DATE under its exact Qlik alias [RnR Scope End] as a numeric date. A measure referencing a helper or field absent from the loaded model is not a complete deliverable.
- Keep warehouse allocations, eligibility and balances upstream. The app's final expressions used inline scope filters and its existing vYotpoRnR/vPointsToPounds controls. The earlier optional vRnRScope helper was not required by those final measures.
- On the user's button object, footnotes were unavailable. The accepted presentation used next-action button labels and one separate full-width current-view expression above the table. Preserve the existing working actions; do not introduce variables for styling alone.
- For expression-based text, Qlik's current Text & image documentation describes styling the inserted measure token through the text toolbar. A text-colour function wrapper was not used. Native control availability is tenant/version-specific; do not claim a click sequence was executed solely from documentation.

Existing field contracts and target-grain limits remain explicit. This example supplies no new deployment, send or candidate-validation authority.
