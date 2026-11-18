---
id: SKILL-0236
type: skill
title: dbt State-Aware Execution Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, action-specific]
trigger_phrases: ["dbt state modified", "dbt defer", "dbt state optimization"]
---

# dbt State-Aware Execution Assessment

Reusable capability for selecting safe state-aware dbt execution behavior.

## When to use

Use only when the requested action is selecting safe state-aware dbt execution behavior. Route adjacent actions to their own confirmed Skills.

## Intent-routing contract

This Skill owns this action from evidence intake through its stated result. It does not own adjacent architecture, implementation, approval or deployment work.

## Method

1. Confirm the installed dbt/adapter version, target environment, proposed state mechanism, authoritative state artifacts/service context and accepted freshness requirements.
2. Distinguish server-backed State from state:modified and --state deferral; verify version support, hashes, freshness, volatile SQL, billing and sharing.
3. Preserve evidence, assumptions, exceptions and the resulting decision or verified output.
4. Stop or escalate when a missing fact could materially change the result.

## Evidence expected

Retain the inputs used, checks performed, result, unresolved gaps and source/date context needed to reproduce the action.

Return the selected supported state behaviour with artifact/version/freshness evidence, volatile-input and sharing/billing limits, and exact unresolved execution risks.

## Benchmark case

A CI job skips unchanged models only after state semantics and freshness tolerance are evidenced.

Boundary design case: A prior manifest is stale or from an unverified environment. Withhold the skip/deferral decision until its identity and freshness are established; unchanged code alone does not establish fresh data.

## Anti-patterns

- Expanding this Skill into adjacent jobs.
- Treating an unverified assumption or tool success as outcome evidence.
- Hiding a material gap to produce a cleaner answer.

## Stop

Stop when the authoritative input, required access or success condition is unknown. Do not claim completion without evidence of this Skill's specific result.

## Contextual links

- `SKILL-0035` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
