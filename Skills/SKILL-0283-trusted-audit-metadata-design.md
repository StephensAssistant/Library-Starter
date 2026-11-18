---
id: SKILL-0283
type: skill
title: Trusted Audit-Metadata Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: []
tags: [skill, audit, metadata, trust]
trigger_phrases: ["design trusted audit metadata", "audit actor and timestamp", "protect audit columns"]
---

# Trusted Audit-Metadata Design

Design trusted, reproducible audit metadata for governed record mutations.

## When to use

Use when a create, update, delete, restore or approval event must record who performed it, when it occurred and what changed without trusting user-editable values.

## Intent-routing contract

This Skill owns audit-event fields, trusted actor/time sources, mutation provenance and edit protection. It does not decide the business lifecycle, deletion mode, implementation platform, approval or deployment.

## Method

1. Define the governed mutation events and the evidence each event must preserve.
2. Source actor identity from the authenticated execution context; never accept a free-text actor supplied by the editable form.
3. Source event time from the authoritative server or database clock and record timezone semantics.
4. Define immutable created metadata and system-managed last-modified, deleted, restored or approved metadata as required.
5. Preserve record identity plus before/after values or an append-only event reference sufficient to reproduce the change.
6. Exclude audit fields from editable controls and reject client-supplied overrides.
7. Verify authorised mutation, unauthorised mutation, spoofed actor/time, repeated event and historical-read behaviour.

## Evidence expected

Record the event catalogue, field definitions, trusted identity and clock sources, immutability rules, mutation tests, residual gaps and source/date context.

## Benchmark case

A Streamlit user soft-deletes a mapping; the database records the authenticated user and server timestamp, rejects submitted audit-field overrides and retains enough event evidence to reconstruct the prior state.

Boundary design case: A client submits a plausible actor and timestamp differing from authenticated/server evidence. Reject the overrides and preserve trusted provenance; matching display text alone is not authentication proof.

## Anti-patterns

- Accepting actor or timestamp values from editable UI input.
- Overwriting creation evidence during later updates.
- Recording only the final row when the required change history cannot be reconstructed.
- Treating a displayed username as authenticated provenance.

## Stop

Stop when the authenticated identity, authoritative clock, required event history, record identity or mutation authority is unresolved. Do not claim trusted auditability without spoofing and historical-read checks.

## Contextual links

- `SKILL-0036` — `shared_method` — Connects the broad capability with a specialised technique in the same delivery family for future method selection.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 1 reciprocal discovery pointer is recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
