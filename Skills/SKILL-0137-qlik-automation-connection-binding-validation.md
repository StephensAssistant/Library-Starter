---
id: SKILL-0137
type: skill
title: Qlik Automation Connection Binding Validation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["bind Qlik automation connection", "validate Qlik connector connection", "resolve Qlik connection ID"]
links: []
tags: [skill, action-specific]
---

# Qlik Automation Connection Binding Validation

Resolve and validate Qlik Automate connection bindings for an existing automation design.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use when blocks require tenant connections or authentication bindings before validation or execution.

## Method

1. List every block requiring a connection and its verified connector.
2. Resolve zero, one or multiple eligible connections explicitly.
3. Bind exact connection and required input IDs; never assume null will auto-bind.
4. Validate connection state and identify missing authority before mutation.

## Decision and evidence details

For zero eligible connections, return the exact missing binding as a blocker. For one, still prove intended tenant, connector and environment; uniqueness alone is not intent. For multiple, resolve the intended binding from authorised design evidence before changing it. Retain IDs and state evidence without credentials.

Boundary design case: two same-named connections exist and environment cannot be distinguished. Leave the block unbound with that precise decision gap rather than choosing the first.

## Benchmark case

A notification block has two eligible HTTP connections; the intended non-production connection is verified and bound explicitly before testing.

## Anti-patterns

- Assuming an unbound block will bind itself
- Selecting the first same-named connection
- Exposing credentials in workspace JSON

## Sources

- https://github.com/qlik-oss/agentic-skills/tree/main/official/skills/qlik-automation-builder

## Stop

Stop when every connection-dependent block is bound to the intended verified connection or has one precise blocker.

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
