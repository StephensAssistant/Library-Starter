---
id: SKILL-0285
type: skill
title: Change-Control Lifecycle Maintenance
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, project-management, change-control, lifecycle]
trigger_phrases: [maintain change control, update change request state, track authorised change]
---

# Change-Control Lifecycle Maintenance

Maintain the governed state of an already-classified change from proposal through authorisation, implementation, validation and acceptance.

## Intent-routing contract

This Skill owns change-control lifecycle maintenance only. Initial request classification, impact assessment, authority identification, validation scoping and stakeholder-conflict resolution are separate actions.

## When to use

Use after a change is classified and its status, authorised behaviour, delivery state or acceptance evidence must be maintained.

## Method

1. Record the accepted classification, scope boundary, requester, reason and evidence.
2. Preserve the last authorised behaviour until a replacement is explicitly authorised.
3. Track the change as proposed, authorised, implemented, UAT or signed off without collapsing those states.
4. Record the decision authority, implementation evidence, validation evidence and acceptance evidence as each becomes available.
5. Update the governing parent and plan when the authorised change alters acceptance, sequence or forecast.
6. Stop progression when required authority or evidence is absent.

## Benchmark case

A material scope change remains proposed until the named owner authorises it, then moves separately through implementation, analyst validation and sign-off while the parent plan reflects the changed sequence.

Boundary design case: A tracker says signed off but no acceptance evidence exists in the controlling record. Preserve the discrepancy and stop progression at the last evidenced authorised state; do not convert implementation or silence into sign-off.

## Anti-patterns

- Treating a proposal as authorised work.
- Replacing the accepted baseline without decision evidence.
- Calling implementation accepted before validation or sign-off.
- Updating the change record without synchronising a materially affected parent or plan.

## Stop

Stop when the current lifecycle state, controlling authority, evidence and next gate are explicit and synchronised to the governing work.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0046--SKILL-0285 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: PLAY-0049--SKILL-0285 | related_to | undirected | inherited_from_source_split | supports
RELATIONSHIP-EVIDENCE: PLAY-0050--SKILL-0285 | related_to | undirected | inherited_from_source_split | supports
