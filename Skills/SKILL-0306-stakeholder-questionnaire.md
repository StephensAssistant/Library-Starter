---
id: SKILL-0306
type: skill
title: Stakeholder Questionnaire Design
status: current
created: 2026-10-10
updated: 2026-10-24
links: []
tags: [skill, ai, software-methods]
trigger_phrases: ["prepare a stakeholder questionnaire", "turn unknowns into questions for stakeholders"]
---

# Stakeholder Questionnaire Design

Create a compact, answerable questionnaire for material uncertainties owned by people outside the current conversation.

## When to use and intent routing contract

Activate for prepare a stakeholder questionnaire, turn unknowns into questions for stakeholders or equivalent intent. Exclude send a questionnaire automatically, questions answerable from available source. Own this technique only; orchestration, approvals, release and communications remain with their current owners.

## Method

1. Read the current proposal and available evidence. List unresolved decisions, their owners and the implementation consequence of each answer. Research factual questions first.
2. Group questions by respondent and decision dependency. Put blocking high-impact choices first. Provide enough context for a person unfamiliar with the discussion and identify where a previous answer controls a later question.
3. Use neutral wording, concrete examples, bounded choices where suitable and a free-text escape hatch. Separate required from optional questions; avoid steering respondents toward the author’s preferred answer.
4. Produce a reviewable draft with proposed recipients and answer format. Preserve unknown answers as unknown. Route any actual sending through recipient verification and explicit messaging authority.

## Anti-patterns

- Dumping the whole discussion on a stakeholder or asking the same decision repeatedly.
- Interpreting silence as agreement or sending because a draft is ready.

## Benchmark cases

- Positive: Ask operations which retry failures need escalation, with examples and an explicit consequence for implementation.
- Negative/boundary: Do not ask a stakeholder which configuration value is already present in the repository.

## Stop

Stop at a concise draft and a clear decision-to-question mapping. Pause dependent work only for genuinely blocking missing answers.


## Source adaptation — 2026-10-10

[to-questionnaire](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/to-questionnaire/SKILL.md). Adapted from Matt Pocock’s MIT-licensed methods; retained licence: `Reference/matt-pocock-skills-49dd158-license.txt`. The Library contract and current task authority govern use. No upstream installer, executable template, dependency, agent configuration or schedule is imported.

## Contextual links

- `SKILL-0307` — `shared_method` — Connects stakeholder-question discovery with manual procedure generation for future operational design.
- `SKILL-0312` — `shared_method` — Connects stakeholder questions with decision-frontier mapping so future interviews focus on consequential unknowns.

## Link review — 2026-10-24

- Confirmed result: `no_supported_links`
- Contextual result: `contextual_links_created`; 2 reciprocal discovery pointer(s) are recorded under `## Contextual links`.
- Searches performed: complete current Library frontmatter graph and confirmed relationship ledger, plus exact ID, title, tag, name, organisation, system and source-reference searches.
- Confirmed links: none. No current record links to this ID and no confirmed ledger edge contains it.
- Candidates inspected: all generated relationship candidates for this record were checked against current canonical records and confirmed ledger evidence.
- Rejected or unresolved candidates: similarity, shared terms, body mentions, co-occurrence and graph proximity remained advisory because none supplied direct relationship evidence.
- Evidence: the complete current graph and confirmed ledger contain no supported relationship for this record; its link set therefore remains unchanged.
