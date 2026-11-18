---
id: SKILL-0135
type: skill
title: Presentation Medium Adaptation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

trigger_phrases: ["adapt presentation for live delivery", "convert deck to pre-read", "adapt slides for meeting"]
links: [SKILL-0037]
tags: [skill, action-specific]
---

# Presentation Medium Adaptation

Adapt an existing evidence-backed presentation for live, pre-read or post-meeting use.

## Intent-routing contract

This Skill owns only the action named above. Load associated Skills and Playbooks separately when their distinct jobs are required.

## When to use

Use when the same story must work in a different presentation medium without changing its supported meaning.

## Method

1. Identify the target medium, audience, decision and available attention.
2. Reduce live-slide density; add self-contained context for pre-read or reference use.
3. Preserve the evidence chain, metric definitions and requested action across versions.
4. Check that navigation and detail do not obscure the primary message.

## Decision and evidence details

Retain the original and adapted versions, target medium and evidence locations. Check that the target audience can recover the takeaway, metric meaning and requested action using the material actually available in that medium.

Boundary design case: a live slide depended on spoken definitions that are absent from a pre-read. Add the verified context or mark the gap before acceptance; a readable chart alone does not preserve the complete story.

## Benchmark case

A dense pre-read is adapted for live delivery by retaining the headline and decisive chart while moving definitions and supporting detail to reference slides.

## Anti-patterns

- Using one unchanged deck for every medium
- Removing evidence to create visual simplicity
- Adding unsupported explanation

## Sources

- https://www.storytellingwithdata.com/

## Stop

Stop when the target version is understandable in its intended medium and preserves the validated story.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0037--SKILL-0135 | related_to | undirected | inherited_from_source_split | supports
