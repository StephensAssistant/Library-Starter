---
id: PLAY-0005
type: playbook
title: Morning Brief
status: current
created: 2026-08-12
updated: 2026-10-01
owner: the Library owner
links: [HAT-0009]
tags: [playbook, morning-brief, tickets, projects, boss-reporting]
---

# Morning Brief

AI-agnostic procedure. Any assistant asked for a morning brief follows this contract.

## Trigger

Run when the Library owner asks for a morning brief or an active schedule invokes this playbook.

## Method

1. Review the configured Library repository, using `staging` when it exists and `main` otherwise. Begin with `Catalog/BOARD.md`. In a fresh Library without that generated file, use the canonical Project and Ticket records directly, or generate the board from an authorised checkout with `python .github/scripts/build_board.py`. Verify ambiguous material rows against their authoritative Ticket or Project and use recorded facts only.
2. Refresh the owner-approved workbook when configured and authorised. Otherwise flag the workbook gap in chat. Include every eligible active or blocked in-scope item and a distinct `Closed yesterday` group for eligible in-scope work whose recorded completion or closure date is the preceding calendar day.
3. Keep the established worklist columns: BI Worklist ID, External Ref, Title, Type, Status, Work State, Priority, Effort, Owner, Waiting On / Next Action, Age (days), Age Since Last Worked (days). Include a compact summary sheet with refresh date, work-state counts and previous-day closure count.
4. Deliver `# Morning Brief — <date>` directly in chat. Start with `## Closed yesterday (<count>)`, then these six sections in order: Waiting on Customer / Requester; Waiting on Vendor / Third Party; Waiting on Colleague; Blocked — Internal Dependency; Active — In Progress; Ready to Start.
5. Use one concise bullet per item: `**TICK-/PROJ-** (SR-/INC- if applicable) — current position. Next: single action.` Include owners only for an actionable wait, blocker or gate. Attach the workbook if created.

## Stop

Deliver the current brief and any verified workbook refresh. Exclude personal ventures, Library/Apps Script meta-tooling, backlog, and completed or archived items older than yesterday; do not infer a closure from unchanged status.
