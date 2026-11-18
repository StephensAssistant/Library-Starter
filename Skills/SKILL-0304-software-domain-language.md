---
id: SKILL-0304
type: skill
title: Software Domain Language
status: current
created: 2026-10-10
updated: 2026-10-24
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["model software domain language", "resolve ambiguous domain terms"]
---

# Software Domain Language

Build a shared, evidence-backed vocabulary connecting business concepts, state transitions and software names.

## When to use and intent routing contract

Activate for model software domain language, resolve ambiguous domain terms or equivalent intent. Exclude general copy editing, invent business rules. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Read existing glossary, domain documents, code and examples. Extract overloaded terms, actor distinctions, identities, lifecycle states, invariants and ownership. Mark each claim as evidenced, assumed or unresolved.
2. Resolve terms with concrete positive examples, counterexamples and near-neighbours. Ask for business decisions only when source evidence cannot settle them; do not force implementation words onto domain meaning.
3. Record each accepted term’s definition, synonyms to avoid, relationships, valid transitions, owner and source. Capture a significant modelling choice as a decision with context, alternatives, rationale and consequences.
4. Keep one canonical glossary/decision owner. Reconcile code and documentation naming within authorised scope, retaining historical aliases when needed for compatibility. Load relevant domain sections lazily for design or interrogation.

## Anti-patterns

- A dictionary disconnected from actual scenarios or silently changing the meaning of an existing field.
- Creating a parallel glossary or treating tentative decisions as accepted policy.

## Benchmark cases

- Positive: Separate order, shipment and delivery using identity and lifecycle examples before designing an API.
- Negative/boundary: Do not infer that all shipments constitute a completed delivery merely because one table uses those names interchangeably.

## Stop

Stop when terms needed for the task are unambiguous or unresolved business questions are explicitly assigned. Domain authority, not code convenience, decides policy.


## Source adaptation — 2026-10-10

[domain-modeling](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0303` — `shared_method` — Connects architecture-friction analysis with domain-language design for future boundary and naming work.
- `SKILL-0305` — `shared_method` — Connects domain-language design with specification synthesis so future requirements preserve consistent concepts.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 2 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
