---
id: SKILL-0167
type: skill
title: Existing-application Behaviour Preservation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0013]
tags: [skill, application, behaviour, redesign]
trigger_phrases: [preserve app behaviour, redesign existing application, functional parity]
---

# Existing-application Behaviour Preservation

Preserve an existing application's required behaviour during visual reconstruction.

## When to use

Use before changing the presentation of a working application.

## Method

1. Inventory loaders, calculations, permissions, validations, state, dialogs, confirmations, mutations, navigation, errors, notifications and external calls.
2. Map presentation, data adapter, action adapter and runtime-host responsibilities.
3. Trace each required behaviour through the proposed change.
4. Test functional parity independently from visual fidelity.
5. Expose missing or intentionally changed behaviour for approval.

## Decision and evidence details

Retain the current application revision and map each required behaviour to its implementation path, reconstruction change and observed parity check. Keep intentionally changed behaviour linked to its approval; inaccessible behaviour remains an evidence gap.

Boundary design case: a screenshot shows an upload button but no loader, validation or error path is available. Preserve the missing behavioural contract as a blocker; visual reconstruction alone cannot prove that the original workflow survives.

## Benchmark case

A Streamlit page is restyled from a mock-up. A passing application preserves upload validation, procedure calls, session state and mutation refresh while assessing appearance separately.

## Anti-patterns

- Rebuilding from the screenshot alone.
- Trading behaviour for visual similarity.
- Replacing a functional input with decorative HTML.

## Stop

Stop with evidenced functional parity or a precise approved deviation or blocker.
