---
id: SKILL-0136
type: skill
title: Qlik Connector and Block Discovery
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["discover Qlik connector blocks", "find Qlik Automate block", "Qlik connector metadata"]
links: []
tags: [skill, action-specific]
---

# Qlik Connector and Block Discovery

Resolve current Qlik Automate connectors, blocks, required inputs and authentication options from live tenant metadata.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use before authoring an automation when connector, block, input or connection identifiers are not already verified.

## Method

1. Define the required operation and target system.
2. Discover current connectors and block definitions from the live tenant.
3. Rank candidates by exact operation support, required authentication, input/output contract and tenant availability.
4. Select the product-native connector/block when it satisfies the contract; select a generic HTTP block only when no verified native option does, and record the missing native capability.
5. Resolve exact block roles, required input IDs and supported authentication.
6. Record unresolved connections or unavailable operations as blockers; never copy tenant-specific IDs from examples.

## Decision and evidence details

Return the required operation mapped to verified connector/block identity, required input IDs, authentication options, tenant and inspection date. Preserve rejected alternatives with the specific unmet requirement; labels and examples are discovery aids only.

Boundary design case: an example block exists upstream but cannot be resolved in the tenant metadata. Report the unavailable operation or access gap and stop authoring that dependency; do not substitute the example's identifiers.

## Benchmark case

For a reload notification, the exact reload and HTTP request blocks plus required inputs are resolved from tenant metadata before JSON is authored.

## Anti-patterns

- Guessing connector or block IDs
- Treating labels as input IDs
- Assuming a generic HTTP block supports the required authentication
- Choosing a generic connector because it is familiar when a verified native block meets the requirement

## Sources

- https://github.com/qlik-oss/agentic-skills/tree/main/official/skills/qlik-automation-builder

## Stop

Stop when every required connector, block and input has a verified current identity and capability.

## Contextual links

- `SKILL-0040` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
