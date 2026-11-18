---
id: SKILL-0018
type: skill
title: Change Request Classification
status: current
created: 2026-08-29
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, project-management, change-control, scope]
trigger_phrases: [classify change request, classify scope change, distinguish defect from scope]
---

# Change Request Classification

Classify a new ask against the accepted boundary before authority, implementation or lifecycle control begins.

## Intent-routing contract

This Skill owns initial change-request classification only. Impact assessment, authority routing, lifecycle maintenance, validation scoping and stakeholder-conflict resolution are separate actions.

## When to use

Use when a new ask, clarification, correction or proposed scope change enters active work and must be distinguished from accepted behaviour.

## Method

1. Record the requester, exact ask, reason, evidence and entry date.
2. Compare it with the original scope, accepted behaviour and current authorised baseline.
3. Classify it as clarification, defect correction, material scope change or acceptance decision.
4. State the evidence supporting the classification and any unresolved boundary question.
5. Hand the classified request to the applicable impact, authority or lifecycle Skill without treating it as authorised work.

## Benchmark case

A requested report-field change is compared with the signed requirement and classified as either defect correction or material scope change before implementation or approval routing.

Missing-input design case: the requester calls a field change a defect but the accepted field definition is unavailable. Record the ask and missing baseline as a boundary question; neither the requester label nor technical simplicity establishes classification or implementation authority.

## Anti-patterns

- Treating every new ask as a defect.
- Treating a classification as approval.
- Changing the accepted baseline during classification.
- Hiding an unresolved scope boundary.

## Stop

Stop when the request has one evidenced classification or one precise boundary question that prevents classification.
