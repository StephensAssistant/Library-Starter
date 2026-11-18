---
id: SKILL-0114
type: skill
title: Library Relationship-Evidence Routing
status: current
created: 2026-09-20
updated: 2026-10-24
links: [PLAY-0042, PLAY-0059]
tags: [library, relationships, evidence-routing]
trigger_phrases: ["traverse Library links", "relationship confidence", "linked context"]
---

# SKILL-0114 — Library Relationship-Evidence Routing

## Purpose

Use governed Library relationships to route retrieval without inventing authority or transitive meaning.

## Intent routing contract

Activate only for traverse Library links, relationship confidence, linked context or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## Method

1. Start from confirmed frontmatter links and their recorded relationship evidence.
2. Load the complete confirmed association closure required by AGENTS.md before applying the governed relationship ledger to discovery ranking and consequential use. Task relevance determines where loaded instructions apply; it must not suppress required association loading.
3. Use confirmed high-confidence evidence first; inspect medium evidence before consequential use.
4. After confirmed traversal, use reciprocal `## Contextual links` and generated candidates as secondary discovery prompts. They may improve retrieval ranking but never establish a fact, association closure, dependency, causality, identity, status or authority.
5. Use low, unknown or candidate edges only to prompt inspection; exclude contested or rejected edges from consequential reliance. If a required confirmed association has contradictory ledger evidence, inspect and resolve that conflict rather than silently dropping the required record.
6. Never infer transitive, causal, identity or authority relationships from graph position.
7. Preserve provenance for every selected or excluded edge and label whether discovery came from the confirmed or contextual layer.

## Anti-patterns

- Treating a similarity score as authority.
- Raising relationship confidence through repetition or reciprocal healing.
- Turning traversal into a new confirmed link.

## Benchmark case

Starting from a Ticket, a passing route follows its confirmed Project and Skill links, inspects a medium-evidence edge before use and excludes a contested candidate.

## Output and evidence

Record inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the relationship evidence needed for a consequential selection is absent or contradictory.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`; existing reciprocal relationships remain supported and no new confirmed relationship was found.
- Contextual result: `no_contextual_links`; the useful routing relationships are already confirmed, and no separate advisory pointer would improve retrieval.

## Change Log

- 2026-09-20: Created by splitting a combined Skill into a precise independent capability while inheriting the source Skill's links.

