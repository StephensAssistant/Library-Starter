---
id: SKILL-0279
type: skill
title: BI Security-Visibility Test Design
status: current
created: 2026-09-20
updated: 2026-10-31
links: [SKILL-0007]
tags: [skill, testing, bi, security]
trigger_phrases: ["design BI security tests", "test dashboard role visibility", "validate report access boundaries"]
---

# BI Security-Visibility Test Design

Design representative allow-and-deny tests for BI content and data visibility.

## Intent-routing contract

This Skill owns BI security-visibility test design only. Access implementation, semantic correctness, interaction, performance and export testing are separate actions.

## When to use

Use when report, page, element, row, column or metric visibility depends on identity, role, group or policy.

## Method

1. State the intended audience, authoritative access policy and every content or data boundary.
2. Define representative permitted, restricted and unassigned identity/role cases from that policy. Record missing real identities or test access as execution gaps rather than inventing them.
3. Specify content-discovery, open-access and applicable row, column and metric-visibility cases with independently expected allow/deny results.
4. For each case, name the effective execution context, observation needed to prove the result and evidence to retain; configured grants alone do not prove effective visibility.
5. Include export and shared-link bypass cases where applicable. Keep configured policy, expected visibility and any actual observations separate.
6. Return the reviewable test matrix, unresolved expectations/access gaps and execution handoff to the authorised test/validation owner in the governing work record. This design does not execute tests or waive their required security-acceptance evidence.

## Benchmark case

Design case: a regional sales dashboard receives an allow/deny matrix for an authorised regional analyst, another-region analyst and unassigned user. Each case states expected discovery/data/export visibility and the observation needed to prove it; these expectations are not executed results.

Boundary design case: Only an administrator session is available and restricted identities are unverified. Produce the allow/deny design and access gap; do not invent personas, change permissions or claim effective-denial tests ran.

## Anti-patterns

- Testing only with an administrator.
- Treating a successful grant as effective-access proof.
- Verifying allowed access without denied cases.
- Using guessed personas or permissions.

## Stop

Stop with a reviewable allow/deny matrix covering the complete stated visibility boundary, expected results, evidence checks and the named execution handoff, or the precise unresolved policy/identity/access gap. Security acceptance still requires the authorised execution/validation owner to obtain actual permitted and denied visibility evidence; design completion is not that verdict.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0007--SKILL-0279 | related_to | undirected | inherited_from_source_split | supports
