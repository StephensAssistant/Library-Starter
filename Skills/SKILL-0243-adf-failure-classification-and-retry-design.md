---
id: SKILL-0243
type: skill
title: ADF Failure Classification
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific, adf, failure-classification]
trigger_phrases: ["classify ADF failure", "ADF activity failure type", "is this ADF failure transient"]
---

# ADF Failure Classification

Classify an evidenced Azure Data Factory failure without assigning or executing its recovery policy.

## When to use

Use when an ADF activity or pipeline failure must be assigned to a defined failure class. Retry-policy design, implementation and execution are separate actions.

## Intent-routing contract

This Skill owns failure classification only. It does not own retry design, recovery execution, architecture, approval or deployment.

## Method

1. Confirm the failing pipeline, activity, run evidence, error boundary and expected outcome.
2. Separate authorization, unavailable or no data, missing file, schema drift, copy, downstream, timeout and validation failures.
3. Determine whether the class is transient, persistent, deterministic or unresolved from direct evidence.
4. Preserve the observed error, class, evidence, assumptions and unresolved gaps.
5. Hand the classified result to retry-policy design only when recovery behaviour is required.

## Evidence expected

Retain the run inputs, error evidence, checks, failure class, unresolved gaps and source/date context needed to reproduce the classification.

## Benchmark case

An ADF permission denial is classified as an authorization failure requiring authority resolution, not as a transient technical failure.

Boundary design case: Only a red activity status is available, without the run error or source response. Return unresolved classification and the precise missing evidence; do not label it transient or design a retry.

## Anti-patterns

- Assigning generic retries before classification.
- Treating no data as the same as unavailable data.
- Inferring a cause from activity status alone.
- Executing recovery during classification.

## Stop

Stop with one evidenced failure class, or the precise missing run, error, access or source fact preventing classification.

## Contextual links

- `SKILL-0036` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
