---
id: SKILL-0139
type: skill
title: Qlik Automation Execution Verification
status: current
created: 2026-09-20
updated: 2026-10-24
owner: Library owner

trigger_phrases: ["test Qlik automation", "verify Qlik Automate run", "check automation idempotency"]
links: []
tags: [skill, action-specific]
---

# Qlik Automation Execution Verification

Verify a saved Qlik automation with representative execution, failure evidence and safe rerun behaviour.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use after creation or update and before enabling production triggering.

## Method

1. Verify the exact saved automation/revision, execution identity and permitted downstream effects before a representative manual execution with controlled inputs. Communications remain draft-only under AGENTS.md: disable or replace send/post/notification effects with a verified non-sending test boundary; do not use a real message as test evidence.
2. Verify expected outputs, controlled failure/error handling and permitted downstream effects. Retain run identity and actual partial-processing state; inspect applied effects and duplicate guards before retrying a failed or ambiguous run.
3. Repeat safely to prove idempotency or an explicit duplicate guard.
4. Retain run evidence and block production triggering on unresolved failures.

## Benchmark case

A reload-notification design is exercised through a verified non-sending test boundary; one successful run, one controlled failure and a guarded repeated run prove the expected draft/output and duplicate behaviour without sending a message.

## Anti-patterns

- Treating valid JSON as execution proof
- Retrying a non-idempotent action without a guard
- Enabling production triggers before representative testing

## Sources

- https://github.com/qlik-oss/agentic-skills/tree/main/official/skills/qlik-automation-builder

## Stop

Stop when representative success, controlled failure and safe rerun behaviour are evidenced.


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
