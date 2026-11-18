---
id: SKILL-0119
type: skill
title: AI Model Escalation Routing
status: current
created: 2026-09-20
updated: 2026-10-11
links: [HAT-0015, PLAY-0006, PLAY-0046, PLAY-0047]
tags: [ai, model-routing, cost-control]
trigger_phrases: ["choose AI model", "model escalation", "low-cost model route"]
---

# SKILL-0119 — AI Model Escalation Routing

## Purpose

Automatically assess the model needed for the next phase of conversational work and act on that assessment. In a chat with a user-controlled model picker, give the Library owner a concise stay-or-switch recommendation before substantial work. the Library owner selects the model and sends “continue”; resume the same task from the available conversation and canonical records. In Library Assistant or terminal Codex CLI, automatically apply the selection through a verified callable controller when available; use Jev to assist bounded semantic selection.

## Intent routing contract

Apply automatically through PLAY-0006 when work starts and when its complexity, required tools or task phase materially changes. Existing phrases “choose AI model”, “model escalation” and “low-cost model route” remain discovery aliases. This is a standing behaviour for any AI loading these instructions, not a Skill the Library owner must explicitly request each time.

## Method

1. Begin task intake on the lower-cost adequate initial model: the Library owner's selection in manual chat, or the controller's verified selection in an automated CLI runtime. Discover the actual switching interface; do not infer it merely from the presence of a CLI. Use the conversation, current work record and necessary evidence to identify the outcome, acceptance criteria, required Hats/Skills/Playbooks, likely tools and complexity.
2. Keep this assessment bounded. Inspect only evidence that can change the model choice; avoid doing the substantial SQL investigation, Sigma build or other main work merely to decide which model should do it. Reuse settled context and verified capabilities.
3. Select the smallest adequate available model and reasoning effort for the next phase. Consider task quality, ambiguity, sustained reasoning, context, modalities, required tools, latency and expected total usage including assessment overhead and retries. Use verified capabilities and accepted representative results; never invent availability, precise costs or comparative performance. A missing tool, credential or source is a capability/evidence blocker, not automatically a reason for a larger model.
4. In manual-picker chat, give one brief recommendation: stay with the current model, or switch to the named available model and reasoning effort, with the task-specific reason. Do this before substantial work when a switch is warranted. No switch is needed for routine work the current model can adequately complete; proceed within existing authority without a confirmation loop.
5. In manual-picker chat, when a switch is warranted, preserve the task, accepted decisions and next action in the existing checkpoint when durable state is needed. Tell the Library owner to select the recommended model in the same chat and then send “continue”. Pause the work that needs the recommended capability. Do not require him to repeat the brief or start another chat, and do not claim that changing the picker alone automatically reruns the task.
6. On “continue”, resume from available chat context and the existing canonical work record, honouring the selected model and original authority. Do not repeat settled intake or re-ask answered questions. Treat the Library owner's statement that he switched as user-reported; mark runtime identity unknown if it is not exposed. Never invent verification of a model switch.
7. Reassess only at a material phase or requirement change, or after an evidenced acceptance failure. Recommend a smaller model when the remaining work no longer needs the larger one. Add a foreseeable switch recommendation to an answer already being produced where possible; avoid a separate expensive turn solely for model selection. For a new task, still recommend before substantial work rather than waiting until it is done.
8. Use the Jev decision skill for a narrow typed judgement only when callable, authorised and expected to improve the decision enough to justify its overhead. Validate its response and apply evaluated policy; permissions and execution remain outside Jev. If unavailable, use the bounded AI assessment and record `route_source: ai_fallback` where routing evidence is retained. Jev is optional for this chat workflow; no dispatcher is required for the Library owner to change the picker.
9. In Library Assistant or terminal Codex CLI, where a verified callable controller or dispatcher exposes model selection, execute the selected route automatically within the Library owner's standing routing authority; do not stop at a recommendation or require manual “continue”. Follow the CLI contract below. Keep governed prerequisites, attempt caps and budgets, including `.github/model-routing.json` for Library automation. Routing does not expand the task's write, send, deployment or merge authority.

## CLI execution contract

- Verify the installed CLI/controller version, authentication, model catalogue, supported reasoning settings and callable switching interface. A catalogue entry does not prove entitlement; verify the selected model on a completed authorised turn. Do not change shared model defaults merely to route one task.
- Prefer the existing Library Assistant controller for automatic selection before each material task phase. When it uses Codex app-server, current documentation supports `model/list` discovery and a `model`/`effort` override on `turn/start` for the retained `threadId`. Resume the known thread when necessary; do not start a context-free conversation.
- A shell-backed controller may launch a bounded `codex exec` run with an explicit model, or resume a specific saved session using the installed version's supported options. Inspect local help before relying on flag placement. Carry the task checkpoint, instructions, tools, workspace, permissions and acceptance criteria into any child run. Label a child run as delegation, not a switch of the parent terminal session.
- Switch at a safe task/turn boundary. Do not launch a concurrent resumed writer against the active parent session, recursively spawn routers, restart unfinished external mutations, weaken approval/sandbox settings or treat a steering message/configuration edit as proof that the in-flight model changed.
- Prefer available Jev for a narrow Choice over eligible model/effort routes plus `unknown`. Supply a compact task/phase description, capability requirements and evidence-backed candidate profiles. Keep credentials server-side; validate the returned type, option, model, probabilities and evaluated confidence policy. Deterministic code checks eligibility, budgets and permissions and performs the switch. Missing Jev uses the labelled bounded AI fallback; low-confidence/unknown results require evidence resolution rather than an invented route. Measure routing overhead and outcome quality before claiming efficiency gains.
- Retain the selected and reported model, thread/session/task reference, completed-turn or child-process receipt and acceptance result. No supported callable switching control means `blocked_auto_switch_unavailable`: provide the precise manual selection fallback without claiming automatic activation. A Skill write alone is not runtime installation or a successful switch.

Sources verified 2026-10-11: [Codex app-server](https://learn.chatgpt.com/docs/app-server), [non-interactive sessions](https://learn.chatgpt.com/docs/non-interactive-mode), [model selection controls](https://learn.chatgpt.com/docs/models), [TypeSafe API](https://docs.typesafe.ai/api). Recheck current documentation and installed help before implementing or changing an adapter.

## Anti-patterns

- Requiring the Library owner to invoke the Skill or ask which model to use.
- Completing substantial work on an unsuitable model before recommending the change.
- Assuming the cheapest model always suffices or the largest model should always run.
- Reassessing on every message despite an unchanged task phase.
- Charging an unnecessary extra model turn for a recommendation that could accompany an existing answer.
- Claiming automatic host switching or treating a missing dispatcher as a blocker to manual picker selection.
- Losing accepted decisions or making the Library owner repeat the task after switching.

## Benchmark cases

- SQL investigation: intake identifies an ambiguous multi-step diagnosis; recommend an adequate available model before the main investigation; after the Library owner switches and sends “continue”, resume the agreed diagnosis.
- Sigma formatting: the selected lower-cost model has the necessary tools and the task is bounded; recommend staying and proceed.
- Later simple summary: the complex investigation is complete; recommend a smaller adequate model for the remaining phase in the existing answer.
- CLI phase change: available Jev selects an eligible route; deterministic policy validates it; the controller starts the next phase on the retained thread with that model; verify a completed turn. If only a child run is available, verify its checkpoint and report delegation accurately.
- CLI without switching control: report the missing interface and manual fallback; do not claim that loading the Skill switched the model.
- Unavailable Sigma tool: name the access gap; do not promise that a larger model supplies the missing connection.

These are acceptance cases, not claimed runtime tests.

## Output and evidence

Return a concise stay-or-switch recommendation and its reason, followed by the usable work when the current route is adequate or the switch has been made. Preserve material routing decisions and checkpoints in the existing work record. Report measured usage only when exposed; estimates are not actual charges.

## Stop

Complete the authorised task, automatically execute and verify the CLI-selected route when supported, pause manual-chat capability-dependent work for the Library owner's model selection and “continue”, or report a precise source/access/authority blocker. Do not ask for routine model-selection permission separately from the recommendation.
