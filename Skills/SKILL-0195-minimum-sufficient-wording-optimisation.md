---
id: SKILL-0195
type: skill
title: Minimum-Sufficient Wording Optimisation
status: current
created: 2026-09-20
updated: 2026-10-29
owner: Library owner

trigger_phrases: ["shorten skill wording", "minimum sufficient instruction", "compress guidance safely"]
links: []
tags: [skill, library-mechanics, learning, wording]
---

# Minimum-Sufficient Wording Optimisation

Finds the shortest wording that preserves verified behaviour and boundaries.

## When to use

Use when comparing alternate wording for an existing governed instruction.

## Method

1. Name a frozen representative case and explicit output criteria.
2. Test the original and candidate wording.
3. Confirm purpose, trigger, action, authority, evidence, safety and stop conditions remain intact.
4. Prefer the shorter candidate only when results are equal or stronger.
5. Retain proven wording when evidence is absent, mixed, uncertain or weaker.

## Benchmark case

A shorter sentence preserves the action but loses a hard stop; retain the original.

## Anti-patterns

- Assuming shorter means clearer
- Compressing away negations or authority
- Changing wording without comparative evidence

## Stop

Stop with the shortest proven equally strong wording or the unchanged original.

## Matt Pocock method extension — 2026-10-10

For agent-facing instructions, put the invocation contract, prerequisites, decision criteria, branch disclosures and observable completion where they are needed. Keep a single canonical mutable source and use precise pointers rather than duplicate content. Compress only after checking that examples, evidence requirements, exceptions, authority and stops survive. On confusion feedback, re-pitch at the audience's level: lead with the concrete outcome, define the missing concept through one example, then add only the context needed for the next decision. Do not repeat the same dense wording or alter the underlying technical claim merely to simplify it.

## Source adaptation — 2026-10-10

[writing-for-agents](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/writing-for-agents/SKILL.md), [wait-what](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/wait-what/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0322` — `shared_method` — Retrieve technical-document clarity rules that preserve uncertainty, obligation and exact literals.
