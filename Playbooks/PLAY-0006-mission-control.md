---
id: PLAY-0006
type: playbook
title: Mission Control — Skill Ecosystem Orchestrator
status: current
created: 2026-08-14
updated: 2026-11-01
owner: the Library owner
protocol: GODWIT-3305-2026-08-N
links: [HAT-0001, HAT-0002, HAT-0003, HAT-0004, HAT-0005, HAT-0006, HAT-0007, HAT-0008, HAT-0009, HAT-0010, HAT-0011, HAT-0012, HAT-0014, HAT-0015, HAT-0016, HAT-0017, HAT-0018, HAT-0019, PLAY-0001, PLAY-0007, PLAY-0008, SKILL-0318, PLAY-0009, PLAY-0010, PLAY-0013, PLAY-0015, PLAY-0016, PLAY-0017, PLAY-0018, PLAY-0019, PLAY-0021, PLAY-0024, PLAY-0032, PLAY-0036, PLAY-0037, PLAY-0038, PLAY-0039, PLAY-0041, PLAY-0042, PLAY-0044, PLAY-0046, PLAY-0047, PLAY-0048, PLAY-0054, PLAY-0055, PLAY-0056, PLAY-0060, SKILL-0001, SKILL-0002, SKILL-0007, SKILL-0012, SKILL-0013, SKILL-0046, SKILL-0047, SKILL-0048, SKILL-0049, SKILL-0050, SKILL-0059, SKILL-0060, SKILL-0061, SKILL-0062, SKILL-0063, SKILL-0064, SKILL-0080, SKILL-0081, SKILL-0082, SKILL-0083, SKILL-0084, SKILL-0113, SKILL-0114, SKILL-0115, SKILL-0116, SKILL-0117, SKILL-0118, SKILL-0119, SKILL-0120, SKILL-0121, SKILL-0122, SKILL-0123, SKILL-0124, SKILL-0263, SKILL-0264, SKILL-0265, SKILL-0272, SKILL-0273, SKILL-0274, SKILL-0293]
tags: [playbook, mission-control, orchestrator, meta-skill, skill-ecosystem, gated-hierarchy]
migrated_from: PLAY-0006-old-library
---
# Mission Control — Skill Ecosystem Orchestrator

## Trigger

A validated Jev routing envelope arrives, or Jev is unavailable and a raw Library request requires the controlled AI-native fallback.

## Method

Use a valid Jev envelope when present. If Jev or ingress is unavailable, perform the SKILL-0293 AI-native intake pass before substantive investigation and mark the route `ai_fallback`; never fabricate Jev output or numeric probability. Verify the selected existing ID against its canonical record; when either route returns `unknown` or ambiguity remains, ask one targeted question without inventing identity. Then choose answer, create, continue, close or explicit specialist action. Before substantial model-dependent work, apply SKILL-0119 automatically: assess the context, required capabilities and likely tools on the selected lower-cost model; recommend staying or switching with a brief reason. When a switch is needed, the Library owner selects the model in the same chat and sends “continue”; resume the existing task without repeating settled intake. Reassess at material phase changes, including a smaller-model recommendation when appropriate. In manual chat, this workflow needs no dispatcher. In the Library owner 2.0 or terminal Codex CLI with a verified callable model controller, apply the selected model automatically at a safe task/turn boundary, use available Jev to assist bounded selection, preserve the task context and verify execution under SKILL-0119. If that control is absent, report the precise interface gap and manual fallback. Use the selected folder guide for writes. Do the next authorized step, verify and save meaningful state once. Return the usable solution first and keep explanation concise unless the Library owner asks for teaching or detail. Board and registry are valid fallback routing surfaces, not evidence of a confirmed relationship.

## Stop

Requested outcome reached or precise missing evidence/authority reported. No side task, role ladder or routine portfolio audit.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Relationship evidence

RELATIONSHIP-EVIDENCE: HAT-0003--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0004--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0005--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0006--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0007--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0008--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0009--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0010--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0011--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0012--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0014--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0015--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0016--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0017--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0018--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: HAT-0019--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0001--PLAY-0006 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0007 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0010 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0013 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0015 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0016 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0019 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0021 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0037 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0038 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0039 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0041 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0042 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0044 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0046 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0047 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--PLAY-0048 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0001 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0002 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0012 | related_to | undirected | authoritative_record | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0013 | related_to | undirected | authoritative_record | supports

## Relationship evidence (2026-09-20)

RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0263 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0264 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0265 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0272 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0273 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0274 | related_to | undirected | user_confirmed | supports

## Relationship evidence (2026-09-26)

RELATIONSHIP-EVIDENCE: PLAY-0006--SKILL-0293 | related_to | undirected | user_confirmed | supports

## Decision-first routing — 10 October 2026

SKILL-0318 is the first decision workflow whenever a consequential unresolved choice affects the next action, throughout the work. Perform the required evidence/intake checks first, then ask the current round of independent material decision questions under SKILL-0318, use the answers to define the correct steps, and reassess the complete applicable Hats, Skills, Playbooks and confirmed associations under SKILL-0113 before dependent execution. Reuse settled answers; return only to affected decisions when evidence or requirements changes. Clear agreed work proceeds directly. the Library owner's standing instruction replaces the former explicit-invocation-only restriction; it grants no extra external-action authority.

## Ticket and Project intake — 1 November 2026

Before creating or materially reframing Ticket/Project work, apply PLAY-0021's shared intake and reuse assessment. Establish the existing product or new target, inspect relevant Library evidence and consider extending a suitable existing capability before proposing a new build. Clear requests still receive this thin evidence check; they do not need an invented interview. For resumed work, reuse the recorded packet and current phase, checking only changed facts or unresolved dependencies. Do not duplicate intake notes, create a competing work owner or treat a similarity match as a confirmed relationship.

Record the current phase, next-phase evidence and unresolved next decision in the existing owner. The phase is a progress aid, not a lifecycle status, user approval, release permission or instruction to execute every phase. Follow the selected folder's source-save and closure guides within the actual task authority.
