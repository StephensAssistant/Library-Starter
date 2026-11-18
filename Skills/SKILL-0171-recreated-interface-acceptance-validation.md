---
id: SKILL-0171
type: skill
title: Recreated-interface Acceptance Validation
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [SKILL-0013]
tags: [skill, interface, acceptance, validation]
trigger_phrases: [accept recreated interface, validate rebuilt ui, interface acceptance]
---

# Recreated-interface Acceptance Validation

Produce separate evidence-based visual and functional acceptance verdicts for a rebuilt interface.

## When to use

Use after implementing a screenshot or approved mock-up.

## Method

1. Confirm source visual, viewport, target and intended use.
2. Review the actual implementation rather than an embedded screenshot.
3. Trace and test required behaviour.
4. Verify material platform mappings and list approximations.
5. Check accessibility, overflow and focus basics where applicable.
6. Record separate visual-fidelity and functional-parity verdicts.
7. Confirm no unapproved paid service or credential was introduced.

## Decision and evidence details

Bind each verdict to the exact implementation/build, source visual, viewport, tested identity and states. List which required behaviours were actually tested and which remain inaccessible; keep acceptance limited to that evidence. An approximation is acceptable only against the agreed target contract.

Boundary design case: the rendered interface is inspectable but mutation access is unavailable. Report the visual findings and incomplete functional verdict separately; do not turn lack of access into a functional pass.

## Benchmark case

A constrained-platform dashboard closely matches the hierarchy but lacks one decoration. A passing application can accept capability-equivalent visuals while failing functional acceptance if a filter does not work.

## Anti-patterns

- Combining visual and functional PASS.
- Ignoring unsupported assumptions.
- Accepting a screenshot as the implementation.

## Stop

Stop with two explicit verdicts, evidence and residual deviations.
