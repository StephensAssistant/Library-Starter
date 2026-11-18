---
id: PLAY-0053
type: playbook
title: Governed Reporting Platform — Compliant Change & Migration Workflow
status: current
created: 2026-08-30
updated: 2026-10-28
owner: the Library owner
links: [PLAY-0014, PLAY-0046, PLAY-0064, PLAY-0065, PLAY-0072, PLAY-0074]
tags: [playbook, governed-reporting-platform, dbt, snowflake, azure-devops, engineering-workflow, migration]
---

# Governed reporting platform change gate

1. Identify the target repository, deployed revision, environment, role and approved change route. Read the current repository conventions, access rules, engineering workflow, migration guide, document catalogue and troubleshooting guidance. Stop if a required source or permission cannot be verified.
2. Check the proposed branch, naming, environment-neutral implementation, destination and validation against live repository policy. Require the named human reviewer and any production or documentation approval. Treat deployment and release as separate authority.
3. For a report migration, inventory the source, compare grain, metrics, filters, access and output parity, and verify the target. Obtain the route decision and release acceptance before cutover, monitor through the agreed hypercare, and retire only with explicit approval.
4. Keep generated documentation as draft until its owner accepts it. Use current platform evidence for troubleshooting and escalate any unrecognised case or contradiction.
5. Return the verified next action or precise blocker, with the source revision and evidence. Never infer a deployed state or overwrite newer work from an exported snapshot.
