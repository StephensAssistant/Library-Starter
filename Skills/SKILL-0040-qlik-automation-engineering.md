---
id: SKILL-0040
type: skill
title: Qlik Automation Workspace Authoring
status: current
created: 2026-09-17
updated: 2026-10-31
trigger_phrases: ["automation workspace JSON", "build Qlik automation JSON", "wire Qlik automation blocks"]
links: []
tags: [skill, qlik, automation, workspace-json]
---

# Qlik Automation Workspace Authoring

Author valid Qlik Automate workspace JSON from a defined requirement and verified block metadata.

## Intent-routing contract

This Skill owns workspace structure and block wiring only. Connector discovery, connection binding, mutation and execution verification are separate actions.

## When to use

Use after trigger, inputs, outputs, failure path, idempotency boundary, target systems and exact block definitions are known.

## Method

1. Map the requirement into trigger, iterable, conditional, action and error-path blocks.
2. Load only the current block-category definitions used by the draft.
3. Use the connector and block selected from live discovery: prefer the product-native connector/block that directly supports the required operation and authentication; use a generic HTTP block only when no verified native option satisfies the contract.
4. Emit every required input ID exactly and reference only verified connector and block identities.
5. Wire data, iterable, conditional and failure edges from verified block roles.
6. Validate workspace schema and required business values without mutating the tenant.

## Benchmark case

A reload-notification requirement becomes schema-valid workspace JSON using verified blocks, complete input IDs and explicit success and error paths.

Missing-input design case: a required block input or connector identity is absent from current metadata. Mark the dependent workspace section incomplete and route discovery; do not copy a GUID from another tenant or treat schema validation as proof that the business value is correct.

## Anti-patterns

- Copying block GUIDs from another tenant
- Replacing an available native connector with a generic HTTP block without an evidenced capability reason
- Omitting input IDs because labels look sufficient
- Treating schema-valid JSON as deployment or execution proof

## Authoritative source

- https://github.com/qlik-oss/agentic-skills/tree/main/official/skills/qlik-automation-builder

## Stop

Stop when the workspace is schema-valid and every block, input and edge is traceable to the approved design.

## Contextual links

- `SKILL-0136` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0137` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0138` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0139` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 4 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
