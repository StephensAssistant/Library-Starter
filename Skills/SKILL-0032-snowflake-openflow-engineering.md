---
id: SKILL-0032
type: skill
title: OpenFlow Connector and Object-Definition Configuration
status: current
created: 2026-09-16
updated: 2026-10-31
links: []
tags: [skill, snowflake, openflow, connector]
trigger_phrases: ["OpenFlow connector", "OpenFlow object definition", "OpenFlow field scope", "OpenFlow connector override"]
---

# OpenFlow Connector and Object-Definition Configuration

Reusable capability for configuring an OpenFlow connector and its source object definition.

## When to use

Use only when the requested action is configuring an OpenFlow connector and its source object definition. Use the independent action-specific Skills for adjacent validation, recovery, testing, performance, rehearsal or delivery work.

## Intent-routing contract

This Skill owns this one action from authoritative inputs to its evidenced result. It does not absorb adjacent jobs merely because they use the same platform or subject.

## Method

1. Confirm authoritative inputs, scope and success condition.
2. Prove authentication and object/field authorization with the smallest representative query. Inspect the connector contract, remove inaccessible scope deliberately, and use an override only with explicit rollback.
3. Preserve evidence, assumptions, result and any unresolved material gap.


### Application checks

Before changing the definition, retain its current object/field scope and the exact failing request. Distinguish authentication, object access and individual field access using the representative query. For a justified narrow override, identify the fields removed, affected consumer contract and explicit restoration path; compare the resulting definition and query evidence with that intended change. If access or override behaviour remains unknown, stop that change rather than broadening credentials or hiding a required field.

## Evidence expected

Retain the inputs, checks, chosen result, source/date context and any condition that requires reassessment.

## Benchmark case

An Orders definition fails ACCESS_DENIED; the exact unsupported field is isolated with a minimal query before a narrow override is applied.

Missing-input design case: the minimal query fails authentication before any field is evaluated. Record an authentication gap rather than removing fields or applying an object override; an ACCESS_DENIED label alone does not prove which field is inaccessible.

## Anti-patterns

- Expanding this Skill into another action because the subject is similar.
- Treating tool success or polished output as verified evidence.
- Proceeding through an unresolved material input or authority gap.

## Stop

Stop when the authoritative input or success condition is unknown. Route the next distinct action to its own Skill.

## Contextual links

- `SKILL-0208` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0209` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0210` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0211` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0212` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0213` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0214` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.
- `SKILL-0282` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 8 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
