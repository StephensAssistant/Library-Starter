---
id: SKILL-0138
type: skill
title: Qlik Automation Mutation Deployment
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["create Qlik automation", "update Qlik automation", "deploy Qlik Automate workspace"]
links: []
tags: [skill, action-specific]
---

# Qlik Automation Mutation Deployment

Create or update a Qlik automation from an approved, validated workspace definition.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use only after workspace schema, identifiers, connections and business values are verified and mutation is authorised.

## Method

1. Default development to a manual trigger unless scheduled, event or webhook behaviour is verified and authorised.
2. Present resolved identifiers and intended change before mutation.
3. Create or update only within the approved mutation scope. For an update, re-read the exact target/revision immediately before writing; if it changed, preserve it and stop the write. Retrieve the saved automation and compare its workspace, connections, business values and trigger state against the approved definition. On a failed or partial mutation, inspect the actual saved state before any bounded repair/retry; a failed response does not prove nothing changed.
4. Match its returned ID through live search and use the resolved editor URL rather than constructing one.

## Decision and evidence details

Retain the approved workspace/revision, target identity, pre-write read and saved-definition comparison. Report created/updated, rejected or unknown effects separately; an unresolved saved state blocks a repeat mutation.

Boundary design case: creation times out after submission. Resolve whether the automation exists and inspect its trigger state before attempting another create. Do not turn a timeout into an assumption that nothing was created or enable triggering from response success alone.

## Benchmark case

An approved manual automation is created, retrieved by its returned identity and opened through the resolved tenant URL without guessing.

## Anti-patterns

- Creating schedules before manual proof
- Guessing editor URLs
- Mutating with unresolved business values

## Sources

- https://github.com/qlik-oss/agentic-skills/tree/main/official/skills/qlik-automation-builder

## Stop

Stop when the saved automation matches the approved definition and its exact identity is verified.


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
