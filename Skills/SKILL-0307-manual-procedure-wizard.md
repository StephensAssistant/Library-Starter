---
id: SKILL-0307
type: skill
title: Manual Procedure Wizard Design
status: current
created: 2026-10-10
updated: 2026-10-24
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["design a manual procedure wizard", "guide a human through manual setup"]
---

# Manual Procedure Wizard Design

Turn a necessary human-operated procedure into a small, verifiable sequence with clear evidence and recovery, without moving secrets into agent-readable state.

## When to use and intent routing contract

Activate for design a manual procedure wizard, guide a human through manual setup or equivalent intent. Exclude collect credentials in a wizard, automate an action already supported safely by tools. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Explain why the operation needs a human and identify prerequisites, permission boundary, risk, success signal and reversibility. Use a supported connector or tool when it can perform the authorised operation safely.
2. Break the procedure into short steps with one meaningful action, expected visible result and recovery instruction each. Allow progress to pause/resume and backtrack; never mark a step complete from a click alone.
3. Keep credentials, tokens, private keys and recovery codes out of HTML, URLs, query strings, localStorage, chat, logs and exported state. For secret entry, use the trusted service or approved secret manager under human control; store only a non-secret completion marker. If a secret was already persisted, stop the unsafe flow, identify the affected stores without echoing its value, remove it through authorised controls and route revocation/rotation to the credential owner.
4. Choose the smallest useful presentation: text checklist normally, an accessible local preview only when requested or materially useful. Do not import upstream wizard templates. Validate the visible final state without reading secrets, and offer cleanup of temporary non-secret artifacts.

## Anti-patterns

- A secret textbox or hidden secret value disguised as convenience.
- Bypassing a permission, login or tool restriction through a human wizard; automatic submission or deployment.

## Benchmark cases

- Positive: Guide a human through a service setting, record the non-secret setting state, and verify a read-only result.
- Negative/boundary: If a step asks for an API token, move entry to the approved service/secret manager and never persist its value.

## Stop

Stop when the human-visible outcome is verified or a step needs missing authority. A completion marker proves only the documented observation, not successful configuration by itself.


## Source adaptation — 2026-10-10

[wizard](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/wizard/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0306` — `shared_method` — Connects stakeholder-question discovery with manual procedure generation for future operational design.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
