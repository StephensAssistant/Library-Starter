---
id: SKILL-0270
type: skill
title: Sigma Workbook Export Execution
status: current
created: 2026-09-20
updated: 2026-10-31
owner: Library owner

links: [PLAY-0012, PLAY-0018, SKILL-0002, SKILL-0046, SKILL-0047, SKILL-0048, SKILL-0049, SKILL-0050, SKILL-0287, SKILL-0288, SKILL-0289]
tags: [skill, sigma, export, execution]
trigger_phrases: [export sigma workbook, download sigma page, export sigma element]
---

# Sigma Workbook Export Execution

Execute and validate one authorised, non-recurring export of a named Sigma workbook, page or element. Scheduling, presentation tuning and email bursting use their independent Skills.

## Intent-routing contract

Activate only for a one-off Sigma export whose source object, scope, output format and destination are known or can be resolved without mutation.

## When to use

Use to download one workbook, page or element in a currently verified supported format after access and destination authority are established. Recipient communications remain drafts for the Library owner to review and send; export authority does not authorise sending, bursting or publication.

## Method

1. Verify document access, destination permission, published/tagged/saved-view source where required and the execution identity.
2. Resolve the exact workbook, page or element and choose a format supported for that scope.
3. Verify the current mechanism's query/cache behaviour and workload impact, then request the export once; do not assume materialized-result reuse.
4. Wait for completion and inspect the resulting artifact rather than treating request acceptance as success.
5. Validate filters, security scope, totals, row/page population, format, provenance and destination before handoff.
6. Record the exported artifact reference and avoid duplicate requests while the first request remains active.

## Supported-format verification

Resolve the supported formats for the exact workbook, page or element from current official documentation and the available tenant mechanism before choosing a format. Retain the source and verification date; if support cannot be established, report the capability gap before requesting an export. Use SKILL-0287 for recurrence, SKILL-0288 for PDF/Excel presentation options and SKILL-0289 for recipient-split email delivery.

## Benchmark case

Given one authorised workbook and a PDF requirement, resolve the exact workbook, issue one export, wait for completion and reconcile the resulting pages before handoff.

Boundary design case: The export request is accepted but completion or artifact retrieval cannot be established. Preserve the request identity and active/unknown state; do not request a duplicate or call the artifact validated.

## Anti-patterns

- Treating object retrieval as an export.
- Reissuing an export while its job remains active.
- Claiming completion from request acceptance.
- Sending output to an unverified destination.
- Assuming the export reuses materialized results.
- Adding a schedule, burst or layout design to this Skill.

## Stop

Stop with one validated exported artifact and provenance, or the precise capability, access, job or output gap.
