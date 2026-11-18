---
id: PLAY-0018
type: playbook
title: Data Documentation
status: current
created: 2026-08-17
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0008, PLAY-0006, PLAY-0007, PLAY-0010, PLAY-0011, PLAY-0012, PLAY-0014, PLAY-0015, PLAY-0019, PLAY-0028, SKILL-0002, SKILL-0003, SKILL-0046, SKILL-0047, SKILL-0048, SKILL-0049, SKILL-0050, SKILL-0051, SKILL-0052, SKILL-0053, SKILL-0054, SKILL-0055, SKILL-0056, SKILL-0057, SKILL-0058, SKILL-0263, SKILL-0264, SKILL-0265, SKILL-0266, SKILL-0267, SKILL-0268, SKILL-0269, SKILL-0270, SKILL-0271]
tags: [playbook, data-documentation, documentation, handoff, close, writing-style, style-guide]
migrated_from: PLAY-0018-old-library
---
# Data Documentation

## Trigger

Technical documentation is requested or necessary for this deliverable.

## Method

Read actual schema/code/model and current decisions. Document only audience-needed grain, keys, mappings, lineage, measures, operations, security and verification. Apply [[PLAY-0028]] for one canonical home; reuse acceptance evidence instead of a second workflow.

## Stop

Accurate useful document, with unknowns visible and current sources linked. No inferred meanings, owners, formulas or schedules.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Domain procedure and evidence

Consult only the detail needed for the current step. The reduced Method above and AGENTS.md replace the older intake, role, capture and handoff choreography below. Domain constraints, unresolved decisions and evidence remain applicable.

<details>
<summary>Existing domain detail</summary>

## Trigger / entry condition

Use when pipeline, data-dictionary, runbook, Qlik, ML-model, or Sigma documentation is requested, or when a user guide, process or SOP doc, Knowledge entry, or Playbook needs writing, or when closing work requires a durable technical record. The House writing style section in this playbook governs every one of those, whichever route you arrive by.

## Stages

### Stage 1 — Classify document and audience

**Goal:** Select the right deliverable and level of detail.

**Action:** Identify the document type and audience. Confirm when ambiguous. Audience choices include the Library owner/future self, a new team member, manager/stakeholder, BI consumer, or data-science/ML consumer. Default to new-team-member depth only for presentation depth, never for missing facts.

**Exit:** Document type, audience, purpose, and destination are known.

### Stage 2 — Inspect authoritative inputs

**Goal:** Ground every technical claim in real objects or supplied evidence.

**Action:** Inspect tables, schemas, code, models, workbooks, measures, schedules, security configuration, and prior decisions as applicable. Ask for undiscoverable context. Mark missing facts explicitly; never infer column meanings, owners, formulas, schedules, or controls.

**Exit:** Required inputs are present or named as blocking/TODO items.

### Stage 3 — Apply architecture gate

**Goal:** Prevent documentation from silently legitimising architectural drift.

**Action:** For pipeline material, apply SKILL-0002 and document three separate parts: optional acquisition/orchestration from the source; the governed Snowflake landing and ingestion route, commonly Snowflake stage → RAW → STAGING or STAGED → INGESTED for files; and optional FACT/DIM/reporting objects justified by the consumer need. A pipeline may stop at INGESTED. If reality differs from the approved design, present the mismatch to the Library owner and the relevant design workflow.

**Exit:** Architecture aligns, or the document is blocked/qualified by an explicit decision.

### Stage 4 — Draft from the matching template

**Goal:** Produce consistent, audience-calibrated Markdown.

**Action:** Use the applicable appendix template. Use H2/H3 headings, tables for mappings and fields, code blocks for SQL/config/commands, short sentences, and explicit TODO markers. Write every sentence to the House writing style section in this playbook, and do not invent content to fill a template.

**Exit:** A complete draft exists with evidence and gaps visible.

### Stage 5 — Validate

**Goal:** Confirm factual fidelity, completeness, and usability.

**Action:** Read back the draft against source objects, intended audience, upstream decisions, links, and requested outcome. Ask the Library owner to resolve material ambiguity. Return to Stage 2 for missing or conflicting facts.

**Exit:** The document is verified for its stated purpose or carries explicit unresolved gaps.

### Stage 6 — File or hand off

**Goal:** Leave one durable canonical record.

**Action:** Update an existing canonical document in place when appropriate; otherwise create the authorised artefact and record reciprocal links. Do not duplicate a current document. External publication or communication requires the Library owner's live choice.

**Exit:** The verified document is filed/handed off and the receiving Ticket or Project records it.

## Decision gates / branches

- Pipeline Technical Spec / Runbook → gather source, layers, keys, schedule, data quality (DQ), owner.
- Data Dictionary → inspect actual columns before defining them.
- Qlik document → inspect app purpose, model, associations, master items, and Section Access.
- ML Model Card → inspect model/version, intended use, data, features, evaluation, limitations, monitoring, and output.
- Sigma document → inspect model, relationships, metrics, Materialization, workbooks, controls, and security.
- Existing canonical document → update in place rather than duplicate.
- Architecture mismatch or material unknown → stop for evidence/the Library owner; do not guess.

## Loop-back rules

Missing or contradictory facts return to Stage 2. An architecture decision returns to Stage 3. Review corrections return to the earliest affected stage. Do not patch only the prose when the underlying governed architecture has changed.

## Overall exit condition

One evidence-grounded, audience-appropriate document is verified and durably handed off, or the exact missing inputs and owner are recorded. A plausible-looking draft is not completion.

## Hand-offs

- PLAY-0006 / PLAY-0007 — routing and framing.
- Pipeline Architect, ML Model Design, Dashboard Ideation, or Sigma Migration playbook — upstream design context.
- Disciplined Coding Practice playbook — code changes exposed during documentation.
- SKILL-0002 / the approved reporting platform reference — canonical ingestion judgement and Sigma reference.

## Audience rules

- the Library owner/future self: terse, operational, commands where appropriate.
- New team member: patient, explicit, explain rationale.
- Manager/stakeholder: outcomes, ownership, risk, and decisions; minimal implementation detail.
- BI consumer: plain English about available data and use.
- Data-science/ML consumer: features, training/evaluation, bias, outputs, and refresh.

## House writing style

Source: Google developer documentation style guide, developers.google.com/style, retrieved 2026-08-19. This section restates the parts that apply to the Library owner's document types and records where the Library owner departs from them.

**Scope.** This section governs every document the Documentarian seat produces, including material outside this playbook's Trigger — user guides, process and SOP docs, Knowledge entries, and Playbooks. The Audience rules section governs tone and depth. This section governs grammar, voice, and formatting mechanics. Where the two meet, Audience rules win on how much you write and this section wins on how you write it.

**Grandfather clause.** This section takes effect on 2026-08-19. Every document filed before that date predates it and is not retrospectively non-compliant. The Appendix templates in this playbook were brought into line on 2026-08-19 and are compliant. Apply this section in full to every document you draft from 2026-08-19. Where an Appendix template conflicts with this section, this section wins: correct the draft, and record the template defect as an Intake line.

### Voice and grammar

- Write in the second person. "You rebuild the staging layer", never "the user rebuilds" and never "we rebuild".
- Write in the active voice and name the actor. "The DAG truncates CUSTOMERS_STG", never "CUSTOMERS_STG is truncated".
- Write in the present tense by default. "The job runs at 06:00." Use "will" only for an event genuinely later than the action you are describing, and never to describe behaviour that arrives in a future release.
- Put the condition before the instruction. "To rebuild from scratch, truncate the staging table."
- Keep one idea in each sentence, and keep sentences short.
- Write timelessly. Drop "currently", "recently", and "the new pipeline". State the date when timing matters.
- Define jargon and expand every acronym on first use, including RAW, STG, FACT, DIM, and DQ.

### Banned wording

- Difficulty claims: "just", "simply", "easy", and "quickly".
- "Please" in an instruction. Write "Click Run", not "Please click Run".
- Filler openers: "please note", "note that", "at this time", and "it should be noted".
- Exclamation marks, slang, idiom, and pop-culture references.
- Anthropomorphism. "The query returns no rows", never "Snowflake thinks the table is empty".
- Directional language. Name the section, or write "the preceding table", rather than "above", "below", or "on the right".
- Pre-announcement. Document what exists today, not what a future release adds.
- Excessive claims. "Reduces reconciliation time", never "eliminates all reconciliation issues".

### Formatting mechanics

- Sentence case in every heading. "Rebuild the fact table", not "Rebuild The Fact Table".
- Numbered lists for ordered steps, one action in each step. Bulleted lists for unordered sets. Description lists for pairs of related data, such as a field and its definition.
- A serial comma in every list of three or more.
- Code font for table names, column names, schemas, paths, commands, parameters, and literal values, as a backtick span.
- Bold for UI element names.
- ISO dates: 2026-08-19. Never 08/19/26.
- Descriptive link text. Never "click here", and never a bare URL inside prose.
- Heading levels in order, H2 then H3, with no level skipped.

### Accessibility

- Alt text on every image and diagram, describing what it shows rather than naming it "diagram".
- Introduce every table in the sentence that precedes it, because a screen reader does not reliably announce a table's purpose.
- Header row and header column only. No merged cells, and no cell spanning rows or columns.
- Prefer a description list or prose to a table when the content is not a genuine same-dimension comparison.

### Inclusive language

- Gender-neutral wording, no ableist terms, and varied names, genders, ages, and locations in examples.
- Do not repeat a problematic legacy identifier in prose. Cite it once in code font as the literal object name, and describe it in neutral words.

### Notices

- Note marks useful context. Caution marks a step that risks data loss or downtime. Warning marks a step that is irreversible.
- Put a Warning on every destructive or irreversible step in a Runbook rebuild, troubleshooting, or rollback section.
- Use notices sparingly. A page of notices marks nothing.

### Deviations from Google's guide

- British English, not American: "optimise", "behaviour", and "organise" — the Library owner's decision, 2026-08-19, since the reader base is UK-internal. Switch a single document to American English when its audience is US or external, and state the switch in that document. Repository-governed filenames, code, identifiers, and quoted source text retain their canonical spelling; prose uses audience-appropriate English consistently.
- Literal names keep their real spelling. Quote a table, column, schema, file, product, or vendor feature name exactly as it exists.
- Match an existing tag's spelling rather than anglicising it. A tag is an exact-match key into `Catalog/TAG-INDEX.md`, so a British variant of a tag already filed in American English splits the row and breaks the reverse lookup.
- Warmth scales with audience. The Audience rules section wins on tone and depth, so a runbook written for the Library owner stays clipped and command-first.
- H1 belongs to the destination document's own title. Every heading you write starts at H2.

### Carve-outs

A banned word is exempt when the sentence mentions it rather than uses it, and a source citation is exempt from the bare-URL rule. This section names its own banned words and cites its own source, and neither fails the pre-publish check.

### Pre-publish check

Read the draft against this list before you file it or hand it off.

- Every heading is sentence case, and you skip no heading level.
- No unquoted instance of "just", "simply", "easy", "quickly", "please", "please note", "note that", "at this time", "it should be noted", "currently", or "recently".
- No directional language.
- Every sentence in a procedure names who or what acts, and carries one idea.
- Every table, column, schema, and path is in code font, and you introduce every table in the sentence that precedes it.
- Every link carries descriptive text.
- Every irreversible step carries a Warning.
- No claim about a future release, and no excessive claim.
- Every unknown carries an explicit TODO marker naming what is missing, per Stage 2.

## Anti-patterns

- Guessing field meanings or system configuration.
- Documenting intended design as current reality.
- Hiding missing inputs with generic prose.
- Creating a duplicate rather than updating the canonical document.
- Writing for an unspecified audience without stating the assumption.
- Silently documenting a pipeline that violates governed architecture.

## Appendix A — Pipeline technical spec

```
## Overview
[Purpose, source system, consumer]

## Architecture
[Source → optional acquisition/orchestration → Snowflake landing/stage → RAW → STAGING/STAGED → INGESTED → optional FACT/DIM/reporting → Consumer. Include only approved objects; state when the governed contract stops at INGESTED.]

## Layer detail
| Step or layer | System/Object | Responsibility | Grain | Load or refresh strategy |
|---|---|---|---|---|

## Keys
Natural key: `...`  Surrogate key: `...`

## Schedule
[Frequency, trigger, dependencies]

## Known data quality (DQ) issues / edge cases
[Evidence, or TODO naming what is missing]

## Owner
[Verified name/role]
```

## Appendix B — Data dictionary

```
## Table: `[DATABASE].[SCHEMA].[TABLE]`
[Verified one-line purpose]

| Column | Data Type | Description | Nullable | Source |
|---|---|---|---|---|
```

Populate from actual metadata; never guess definitions.

## Appendix C — Runbook

```
## Purpose
[Rebuild, re-run, troubleshoot, or recover]

## Preconditions
[Verified prerequisites]

## Rebuild steps
Caution: a rebuild truncates and reloads. Mark any step that cannot be undone with a Warning.
1. [Step] — expected result: [...]

## Troubleshooting
| Symptom | Likely Cause | Fix |
|---|---|---|

## Rollback
[Verified recovery/reversal path, authorised operator, prerequisites, expected checks, and stop/escalation when recovery is unavailable. Identify any point of no return; put a Warning on each actual irreversible step. Do not assert that every rollback step is irreversible.]
```

## Appendix D — Qlik app / data model

```
## App overview
[Name, purpose, audience]

## Data model
[Tables and key associations]

## Master items
| Measure/Dimension | Expression | Used On |
|---|---|---|

## Section access
[Verified rules, or "None"]
```

## Appendix E — ML model card

```
## Model details
Name / version / owner / date

## Intended use
[Primary use and explicitly out-of-scope uses]

## Target variable and problem type
[Prediction target and task type]

## Training data
[Sources, window, size, known biases]

## Features
| Feature | Source | Transformation |
|---|---|---|

## Evaluation
[Split strategy, metrics, baseline comparison]

## Limitations and caveats
[Known failure modes, weak segments, biases]

## Monitoring and retraining
[Drift signals and confirmed trigger/frequency]

## Prediction output
[Table and refresh frequency]
```

## Appendix F — Sigma workbook / data model

```
## Data model
[Name, source FACT/DIM tables, relationships]

## Metrics
| Metric | Formula | Description |
|---|---|---|

## Materialization
[Verified schedule, or "None"]

## Associated workbooks
| Workbook | Audience | Purpose |
|---|---|---|

## Security
[Column security and folder permissions]
```

</details>

## Guardrail correction — 2026-10-13

Documentarian and Reliability: the runbook template now identifies actual irreversible operations, verified recovery evidence, an authorised operator and the unavailable-recovery stop path.
