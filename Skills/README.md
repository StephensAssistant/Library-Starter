# Skills — `SKILL`

A reusable capability for a class of work — tools, standards, and judgement, with worked examples and anti-patterns. Skills perform individual capabilities; Playbooks combine them for one defined outcome; Workflows connect Playbooks and nested Workflows into a governed process. A Skill can hand off to a Playbook and vice versa.

Filenames: `SKILL-<NNNN>-<slug>.md`

Added 2026-08-21, per the Library owner's explicit sign-off (the same rule Playbooks was added under).

Create from `_TEMPLATE.md` using `_HOW-TO-CREATE.md`.

## Before changing this folder

- Create a Skill only for a distinct reusable technique; do not turn a one-off procedure into a Skill.
- For a new record, reserve the `SKILL` ID, satisfy base frontmatter, use `current` or `superseded` status, and add evidence-backed reciprocal links.
- Add its intent-routing contract and benchmark case before candidate validation.

## Complete support for a calling Playbook

A Skill used by a Playbook must actually cover the required technique and its applicable inputs, outputs, prerequisites, limits, failure cases and verification. A matching name or link is insufficient. When workflow design exposes missing or incomplete support, search current owners; reuse a suitable Skill, amend the same capability owner, or create a distinct carefully scoped Skill only when no owner fits. Remove material ambiguity through explicit instructions or a decision/stop condition, test the relevant cases and affected callers, and obtain the required independent review before the workflow is approved. Follow Workflows/README.md for the coverage evidence contract; do not copy its mutable rules into each Skill.

## Explicit capability contracts

For new or revised Skills define the owned outcome, required inputs/provenance/freshness, permitted operations/effects, decision predicates, recovery limits and observable proof proportionately to the actual technique. Use MUST/MUST NOT/MAY ONLY with explicit conditions. Missing or conflicting required evidence is a gap; investigate accessible sources and route the dependent decision rather than guessing a value, branch or success. An authorised default must name its trigger and value. Reuse canonical rules by reference; do not duplicate mutable workflow policy. Apply Workflows/README.md's five-part design framework when the Skill supports workflow construction or qualification. Written examples are not executed tests; preserve actual verification type and limits.

## Authoring for AI use

Use the existing Skill as the capability owner; improve diagnosed gaps rather than copying a universal checklist into every record.

- Put the owned user intent, specific trigger phrases, important exclusions and adjacent handoff in the routing contract. Test natural paraphrases and plausible near-misses; keyword overlap alone is insufficient.
- Specify the inputs the agent cannot safely infer: target/environment, source revision, domain parameters, access and required dependencies. Identify the resulting object or decision and the observable acceptance check.
- Teach the domain operation. Replace vague instructions such as "verify the result" with what to compare, the expected relationship and the evidence to retain. Preserve justified flexibility; use exact sequences for fragile operations.
- Put conditions before their actions. Explain missing/conflicting evidence, partial effects and safe re-entry where applicable. Reuse canonical authority and recovery limits; a Skill cannot grant permissions.
- Account for every material decision in the owned technique: required evidence, branch condition, allowed action and resulting check or stop. An unresolved or unevaluable branch remains a named gap; do not hide it behind a default or completion claim.
- Keep one coherent job. Retain non-obvious local constraints and failure lessons; avoid generic padding. Use precise references with a stated read condition for optional details. Mandatory dependencies and confirmed associations still follow AGENTS.md.
- For scripts, distinguish execution from reading as reference. State verified prerequisites, inputs, outputs and failure signals; prefer existing tested helpers for repeated deterministic work. Do not assume tools, packages, network access or credentials exist.
- Keep normal, boundary and near-miss cases proportionate to the mechanism. Label written examples as design cases. Apply SKILL-0194 for changed behaviour and SKILL-0195 for compression; inspect actual outputs and required non-author evidence before acceptance.
- Preserve exact literals, obligation, uncertainty and authority during edits, using SKILL-0322's clarity method. Keep sources, dates and verification limits separate from instructions that govern current execution.

These are governed Library records, not automatically installed Agent Skills packages. Retain the Library schema and stable IDs. Apply a target host's current `SKILL.md` schema only during separately authorised packaging. External length targets, phrasing styles and suggested test counts are authoring heuristics; they do not replace local contracts or prove reliability.

When the authorised review requires multiple passes, record their actual independent scopes and findings against the final revision. Fix and recheck material findings before documentary sign-off. Passing those reviews does not prove 100% reliability over unknown tasks; state the tested scope and remaining unexecuted checks.

Research and estate review: [31 October 2026 evidence](../Reference/ai-skill-authoring-20261031-review.md). Source staging, independent documentary review, behavioural evaluation and candidate acceptance are distinct claims.
