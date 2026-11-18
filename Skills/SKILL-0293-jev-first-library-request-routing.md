---
id: SKILL-0293
type: skill
title: Jev-first Library request routing
status: current
created: 2026-09-26
updated: 2026-09-26
owner: Library owner

trigger_phrases: [route request through Jev first, resolve Library item before AI, build Jev intake envelope, route request when Jev is unavailable]
links: [PLAY-0006]
tags: [skill, ai-engineering, typesafe, jev, intent-routing, library-intelligence]
---

# Jev-first Library request routing

Prefer routing a raw request through Jev before any downstream AI receives it; when that connection is unavailable, require the AI to perform the same bounded referent-resolution stage before substantive work.

## Intent-routing contract

Use this Skill only for pre-AI request and Library-referent routing. Use SKILL-0045 for primitive selection, SKILL-0154 for typed-question design, SKILL-0155 for dependent calls, SKILL-0156 for deterministic confidence policy, SKILL-0157 for evaluation and SKILL-0158 for production data security. Permissions, ID allocation, relationship confirmation and execution remain outside Jev.

## When to use

Use on every inbound request to an AI working with the Library owner. Prefer upstream Jev; use the controlled AI-native fallback only when Jev or the ingress connection is unavailable.

## Method

1. The ingress service receives the raw request and a revision-pinned Library routing index containing existing IDs, types, titles, aliases, status and concise routing descriptions.
2. Ask Jev one bounded Choice question over existing candidates with an explicit `unknown` option. For a large estate, rank broadly, then re-check a small shortlist in a dependent second request; do not let the downstream AI perform either stage.
3. Validate the returned model, question ID, answer type, selected option and complete probability distribution. Preserve them with the Library-index revision and routing timestamp in the envelope.
4. Apply evaluated confidence, ambiguity and freshness policy in deterministic code. Low confidence, close alternatives, no match, stale context and malformed responses produce `unknown` or one targeted human question.
5. When Jev succeeds, release the original request inside the validated envelope. The AI verifies a selected ID by opening its canonical record and follows confirmed links; Jev output remains routing advice, not evidence or authority.
6. When Jev or ingress is unavailable, the AI performs only the intake pass first: use current Library routing surfaces to select one existing ID/type or `unknown`; record `route_source: ai_fallback`, the failure reason, alternatives, evidence anchors, Library revision and timestamp; and use qualitative uncertainty rather than invented Jev probabilities. Verify the selected canonical record before substantive reasoning. Ask one targeted question if the route is not uniquely supported.
7. Require the downstream AI to return the usable solution first and remain concise unless the Library owner requests education or more detail.

## Benchmark case

Given “continue the reporting migration” and a revision-pinned index containing several active migration records, the ingress service returns the best existing ID plus its full Choice distribution and confidence, or `unknown` when the top candidates are not safely distinguishable. Only then is the request released to the AI.

## Anti-patterns

- Letting the downstream AI start substantive investigation before either routing path completes
- Giving Jev permission to mint an ID, confirm a link or authorize an action
- Omitting `unknown` or suppressing the probability distribution
- Treating confidence as factual verification
- Pretending an AI-native fallback result or confidence is Jev output
- Freezing a threshold without representative evaluation

## Authoritative sources

- https://docs.typesafe.ai/api
- https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/patterns/intent-routing
- https://docs.typesafe.ai/cookbooks/skill_suggestion
- https://docs.typesafe.ai/model-jaggedness/jev-1.13

## Stop

Stop when Jev has produced a validated envelope, or the AI-native fallback has produced its explicitly labelled route record, and the selected canonical record is verified or one targeted question is required.
