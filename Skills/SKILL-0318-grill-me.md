---
id: SKILL-0318
type: skill
title: Grill Me
status: current
created: 2026-10-15
updated: 2026-11-08
owner: Library owner
trigger_phrases: ["grill me", "challenge my decision", "stress-test my plan", "validate the plan", "align before acting", "resolve the decision frontier"]
links: [FLOW-0001, FLOW-0002, HAT-0022, PLAY-0006, PLAY-0007, PLAY-0008, PLAY-0009, PLAY-0010, PLAY-0021, PLAY-0024, PLAY-0030, PLAY-0035, PLAY-0069, SKILL-0113]
tags: [skill, grill-me, decision-interrogation, alignment, planning]
---

# Grill Me

Governed routing for Matt Pocock's exact upstream `grill-me` and `grilling` Skills. This record supplies Library identity, authority boundaries and associations; it does not rewrite the upstream Skill text.

## When to use

Use before dependent work whenever a consequential unresolved choice affects outcome, scope, acceptance, approach, sequence, trade-offs or capability selection. Also use when the Library owner explicitly asks to be grilled, challenged or aligned on a plan. Clear, settled routine work proceeds without an invented interview.

## Exact upstream source

- Repository: `mattpocock/skills`
- Pinned revision: `49dd158d1076134a641b33efb035946536778336`
- Dispatcher: `skills/productivity/grill-me/SKILL.md`
- Required implementation: `skills/productivity/grilling/SKILL.md`
- Verified local SHA-256: dispatcher `CAAF8B8DE1684F96E26B28F3C29189DB5C89CCE4B73E1C93D86164F66EF88637`; implementation `BEFDFF1E27A1DFE2A294D5871169AC1AFE16D983911DAA4F32627514A48C1E15`
- Licence: `Reference/matt-pocock-skills-49dd158-license.txt`

The upstream files are installed and used unchanged. `grill-me` delegates to `grilling`; both are required. When automatic decision-first routing is required, load the `grilling` implementation through this governed owner. Never replace the exact source with a locally rewritten imitation. This governed wrapper controls Library-owner-facing cadence and supersedes the upstream instruction to ask the whole frontier in one round: ask only the single highest-leverage material question for the current domino, wait for the Library owner's answer, then recompute the tree. Never batch questions merely because they are currently answerable; one answer may redirect or eliminate the rest.

## Method

1. Read available evidence and settled answers first. Find discoverable facts through authorised sources rather than asking the Library owner to supply them.
2. Map the decision tree internally. Identify the single highest-leverage unresolved fact or user-owned decision for the current domino; retain later branches internally without presenting them yet.
3. Resolve discoverable facts with the smallest bounded authorised check for the current domino before asking the Library owner to decide around them. Skip questions made irrelevant by the result.
4. When the Library owner must decide, invoke the exact upstream Grill Me pair but apply this wrapper's cadence: ask one question with one concise recommendation, then wait. Do not expose the remaining frontier until the answer has been incorporated and the tree recomputed. Wait before dependent implementation; follow AGENTS.md's research/alignment boundary.
5. Incorporate the result, accepted answer, constraints, acceptance criteria and single agreed next step into the existing canonical work record. Recompute the tree from fresh evidence and skip branches that are no longer relevant.
6. Recompute the decision tree after each answer until no material choice is silently assumed. Execute one domino at a time; reuse settled answers and reopen only decisions affected by new evidence, a changed requirement, contradiction or failure.
7. Confirm shared understanding before dependent implementation. Continue independent authorised work only where it cannot prejudice the active domino.

## Working cadence

- Lead with the usable solution and keep user-facing updates to short sentences or bullets.
- Prefer the smallest runnable script or focused test that resolves the next uncertainty.
- Validate each causal link before expanding scope. One proved source, key, filter, join or formula may remove several downstream questions.
- Do not disappear into broad exploration, parallel candidate branches or end-to-end rewrites when a bounded check can decide the next step.
- After every result, explicitly discard invalidated hypotheses and choose only the next blocking domino.
- Treat a blocker as a boundary around the affected dependency, not a reason to stop independent development.
- Do not turn the final response into a monologue; report result, proof, remaining gap and next action.

## Intent routing contract

Route explicit Grill Me requests and consequential unresolved decision alignment here. Do not route simple factual reads, settled implementation, routine corrections or actions whose next step is already agreed.

## Benchmark case

A reporting migration has a large aggregate mismatch. First compare the smallest source/key sample capable of proving one join. Recompute the migration path from that result before asking about fallbacks, acceptance or later transformations. A proved key may eliminate those questions; an ambiguous key becomes the single next domino.

## Anti-patterns

- Rewriting the upstream Skill into a local pseudo-version
- Asking the Library owner for facts available in code, records or tools
- Batching questions before the highest-leverage answer can redirect or eliminate them, or asking dependent/speculative questions before the evidence needed to make them useful
- Treating one blocked field as a stop for the entire authorised development outcome
- Running a broad comparator or rewriting several stages before validating the first causal link
- Producing lengthy explanation where a script, result or one focused decision question is sufficient
- Treating answers as deployment, merge, send or production authority

## Stop

Stop the interview when the relevant decision frontier is empty and the Library owner confirms shared understanding. Continue the authorised work or report the precise dependency that remains blocked.

## Exact retained upstream snapshots — 16 October 2026

Unchanged public source bytes at the pinned revision are retained as Reference/matt-pocock-skills-49dd158-grill-me-SKILL.md and Reference/matt-pocock-skills-49dd158-grilling-SKILL.md, verified against the two SHA-256 values above and original Git blob IDs. Read both exact snapshots when applying this owner; the governed wrapper still controls cadence and authority. Missing or mismatched bytes block that dependent decision procedure; never rewrite an imitation or treat a snapshot as new permission. Retain the upstream licence alongside the snapshots. These are immutable versioned supporting snapshots, not an executable installer or automatic source of accepted policy.
