---
id: SKILL-0140
type: skill
title: Snowflake Semantic View Capability Verification
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["verify semantic view feature support", "check Snowflake semantic capability", "semantic view preview feature"]
links: []
tags: [skill, action-specific]
---

# Snowflake Semantic View Capability Verification

Verify that a Snowflake account currently supports the Semantic View capabilities required by a proposed design.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use before relying on volatile, preview or format-specific Semantic View features.

## Method

1. List every required capability and its role in the design.
2. Check current authoritative documentation and the target account.
3. Distinguish generally available, preview, unsupported and permission-blocked features.
4. Return supported alternatives where a required capability is unavailable.

## Decision and evidence details

For each required feature, record current documentation evidence, target account/context, actual check and result. Distinguish unsupported from permission-blocked and unavailable evidence; only a verified supported alternative can replace the requirement.

Boundary design case: an account check is denied while documentation describes general availability. Keep account support unresolved and identify the access/evidence owner. Do not label the feature unsupported or claim the design is ready from documentation alone.

## Benchmark case

A design requiring scoped datasets is checked against current documentation and the target account before any definition is authored.

## Anti-patterns

- Inferring availability from examples
- Treating documentation as proof of account enablement
- Building around an unverified preview feature

## Sources

- https://github.com/Snowflake-Labs/coco-skills/tree/main/skills/semantic-view-patterns

## Stop

Stop when each required capability is verified or replaced by an agreed supported pattern.

## Contextual links

- `SKILL-0041` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
