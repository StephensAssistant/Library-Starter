---
id: SKILL-0112
type: skill
title: Qlik Answers Readiness Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
trigger_phrases: ["Qlik Answers readiness", "Qlik Answers assessment", "prepare app for Qlik Answers"]
links: []
tags: [qlik, answers, readiness]
---

# Qlik Answers Readiness Assessment

Assess whether a Qlik app’s governed metadata makes it ready for Qlik Answers.

## Intent routing contract

Activate only for Qlik Answers readiness, Qlik Answers assessment, prepare app for Qlik Answers or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to assess whether a Qlik app’s governed metadata makes it ready for Qlik Answers.

## Method

1. Verify current tenant Qlik Answers capability and the target app.
2. Inspect field naming, visibility/noise, Master Items, descriptions, date behavior and business synonyms using authorised evidence.
3. Score only visible evidence and label inaccessible assignments or vocabulary as unknown.
4. Produce the smallest ordered, evidence-linked remediation roadmap; verify each approved metadata change in the live app.

## Decision and evidence details

For each inspected metadata area, record the target app/tenant, evidence date, observed condition, business question affected and proposed remediation. Keep unknown access separate from a demonstrated metadata defect. Apply only an agreed assessment rubric; do not invent a numerical score or readiness threshold.

Boundary design case: descriptions are visible but synonym assignments are inaccessible. Report the evidenced description findings and the synonym gap; do not infer that synonyms are absent or certify complete readiness.

## Benchmark case

A sales app’s verified fields, Master Items, descriptions, dates and synonyms produce a bounded remediation roadmap while inaccessible metadata remains unknown.

## Anti-patterns

- Expanding this Skill into an adjacent diagnosis, execution or verification job.
- Treating one inconsistent precedent or assumption as authority.
- Proceeding through an unresolved evidence or authority gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when tenant Qlik Answers capability, the target app or required metadata access is unverified.

## Change Log

- 2026-09-20: Narrowed to one action-level responsibility; adjacent jobs moved to independent Skills.
