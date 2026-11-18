---
id: PLAY-0043
type: playbook
title: Prototype Spike
status: current
created: 2026-08-22
updated: 2026-10-10
owner: the Library owner
protocol: GODWIT-3305-2026-08-N
links: [HAT-0003, PLAY-0038]
tags: [playbook, prototype, spike, architect, design-review]
migrated_from: PLAY-0043-old-library
---
# Prototype Spike

## Trigger

One feasibility question cannot be resolved from available evidence.

## Method

Name the question and bounded time/scope. Run the smallest useful experiment. Record answer, limits or an explicit inconclusive result. Label prototype artifacts; keep/discard within task authority.

## Stop

Question answered or bound reached. Do not silently convert an experiment to a production build.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0038--PLAY-0043 | related_to | undirected | authoritative_record | supports

## Matt Pocock method extension — 2026-10-10

Choose the prototype around one uncertainty. For logic, make a small runnable example with explicit inputs, output and state so the mechanism can be tested and discarded. For UI, compare materially different structures or interaction approaches rather than cosmetic colour variants; route visible design through the governing design gate. Use an isolated disposable location, real constraints where feasible and clear limitations. Keep prototype findings in the canonical work record; do not promote throwaway code, commit a new branch or deploy merely because the spike succeeds.

## Source adaptation — 2026-10-10

[prototype](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.
