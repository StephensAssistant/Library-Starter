---
id: SKILL-0259
type: skill
title: Qlik MCP Readiness Assessment
status: current
created: 2026-09-20
updated: 2026-10-31
trigger_phrases: ["Qlik MCP readiness", "Qlik MCP assessment", "prepare Qlik for MCP"]
links: []
tags: [qlik, mcp, readiness]
---

# Qlik MCP Readiness Assessment

Assess whether the live Qlik MCP surface exposes the governed context and authorised operations required for a stated AI workflow.

## Intent routing contract

Activate only for Qlik MCP readiness, Qlik MCP assessment, prepare Qlik for MCP or equivalent intent. This Skill owns one action-level job and does not replace adjacent associated Skills.

## When to use

Use only when the requested action is to assess whether the live Qlik MCP surface exposes the governed context and authorised operations required for a stated AI workflow.

## Method

1. State the target AI workflow and its required read, context and mutation capabilities.
2. Verify the current tenant, live MCP connection, exposed tools, readable metadata and authority boundaries.
3. Test only authorised representative operations; label inaccessible capability as unknown and proven unsupported capability as absent. Missing access is not evidence that a capability does not exist.
4. Produce the smallest evidence-linked remediation roadmap without inferring capability from documentation alone.

## Benchmark case

The current tenant’s exposed MCP tools, readable metadata and mutation limits are verified against one target workflow; unavailable capabilities become explicit gaps.

Boundary design case: The tenant documentation names a mutation tool but the current MCP connection does not expose it. Record the observed surface and unknown/unsupported distinction; do not simulate a mutation or declare global absence.

## Anti-patterns

- Expanding this Skill into planning, approval, verification or another adjacent job.
- Treating tool success or an assumption as outcome evidence.
- Proceeding through an unresolved authority or evidence gap.

## Output and evidence

Record authoritative inputs, direct evidence, result, residual uncertainty, owner and next action.

## Stop

Stop when the live MCP connection, tenant capability, authorised tool surface or target workflow is unknown.

## Relationship evidence

RELATIONSHIP-EVIDENCE: HAT-0015--SKILL-0259 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: HAT-0016--SKILL-0259 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: PLAY-0046--SKILL-0259 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: PLAY-0047--SKILL-0259 | related_to | undirected | user_confirmed | supports

