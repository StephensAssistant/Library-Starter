---
id: SKILL-0288
type: skill
title: Sigma Export Presentation Configuration
status: current
created: 2026-09-21
updated: 2026-10-31
owner: Library owner

links: []
tags: [skill, sigma, export, presentation]
trigger_phrases: [format sigma export, sigma pdf export layout, sigma excel export options]
---

# Sigma Export Presentation Configuration

Configure PDF, Excel and packaged-output presentation for a Sigma export without changing its recurrence or audience logic.

## Intent-routing contract

Activate for page width, page breaks, row expansion, pivot headers, Excel metadata, attachment merging or ZIP packaging. Use SKILL-0270 to execute the export and SKILL-0287 to schedule it.

## When to use

Use when exported output must meet a defined page, spreadsheet or attachment presentation requirement.

## Method

1. Confirm export scope, target format, page or spreadsheet acceptance criteria and destination limits.
2. For PDF, choose a tested page width; Sigma examples use 1050 px for letter portrait and 1380 px for letter landscape.
3. Add page-break elements where required and validate page boundaries in the rendered PDF.
4. Use **Expand table to first 1k rows** only when the table placement qualifies; for full-page or workbook PDF expansion, keep the table alone on its row and outside a container.
5. For CSV or Excel, enable repeated pivot headers when downstream readers require them; include Excel metadata only when requested.
6. Merge two or more PDF or Excel attachments only when a single combined file is the acceptance target; otherwise preserve separate files. Apply ZIP packaging when required.
7. Keep combined email attachments within 30 MB and test the complete exported artifact, not only the workbook canvas.
8. Reconcile page count, clipping, headers, row population, number formats, metadata and file opening before handoff.

## Benchmark case

A landscape P&L PDF uses a tested width, explicit page breaks and first-1,000-row expansion, then passes clipping, pagination and total checks.

Boundary design case: The target tenant does not expose a stated expansion or packaging option. Verify current supported behaviour and report the capability gap; do not substitute a remembered option or claim full-row PDF output from canvas appearance.

## Anti-patterns

- Assuming the workbook canvas guarantees PDF layout.
- Expanding a table that shares its row or sits inside a container.
- Merging attachments without an explicit single-file requirement.
- Enabling metadata or repeated headers without checking the consumer.
- Ignoring the 30 MB combined email-attachment limit.
- Adding scheduling or audience segmentation to this Skill.

## Stop

Stop with a presentation-validated export configuration or the precise format, layout, size or compatibility gap.

## Relationship evidence

RELATIONSHIP-EVIDENCE: SKILL-0270--SKILL-0288 | related_to | undirected | user_confirmed | supports
