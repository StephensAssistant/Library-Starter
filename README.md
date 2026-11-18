# Library Starter

The owner's shared reference Library. Read AGENTS.md once, then the current task and relevant relationships. Work on one authorized outcome; verify, save meaningful state and stop.

## Connect an assistant to the Library

Use this shared instruction in the host's startup settings, or as the startup instruction in an existing Library adapter adapter:

> For Library work, including a named Ticket or Project, discover the approved GitHub connection first. Use it exclusively when available. Read the complete root `AGENTS.md` from the owner’s configured GitHub repository on explicit `staging` (use explicit `main` for a requested released-version read) once at task start, before selecting downstream capabilities. If a read is truncated, retrieve the missing ranges. Then open the named record and its used plan. Use an existing authorised checkout only when the GitHub route is unavailable or the owner explicitly requests local checkout work for a named reconciliation or isolation purpose. If the fallback checkout is dirty, stale or unsuitable, preserve it and stop. Report the exact access gap if there is no authorised route.

On first setup, check the host's configured startup instructions or installed adapter for this behaviour. If it is current, use it. If missing, place the quoted instruction in the host's supported startup settings during authorised setup. If a setting or adapter is stale, replace only its Library entry instruction at its maintained source during authorised setup and refresh the active copy. Preserve its other responsibilities. Where installation or settings access is unavailable, apply the instruction for the current session and report that persistent setup is pending. Normal Library requests can proceed through the approved connection without installing a skill.

Verify setup in a fresh session. Connect the AI to the repository you own and select only that repository where the provider offers repository selection. Ask it to list branches and read `AGENTS.md` from `staging`. Check the activity for GitHub discovery before checkout commands and a complete remote read. A fresh Library has no Ticket, so use the first-Ticket check below after verifying read access.

## Work

- Create: apply PLAY-0021 for shared Ticket/Project intake, evidence-based reuse and the next-phase check; search for a canonical owner, then copy `{folder}/_TEMPLATE.md` and follow `{folder}/_HOW-TO-CREATE.md`. Reserve required IDs, define outcome/acceptance/next action and an inline checklist. Substantial work may use one linked plan (`Planning/_TEMPLATE.md` and `Planning/_HOW-TO-CREATE.md`).
- Continue: read the named record and used plan/dependencies; execute the next step without repeating intake.
- Close: for Tickets and Projects follow `{folder}/_HOW-TO-CLOSE.md`. Reuse valid evidence, check task-owned residue and affected links, then save once. No full-roster or mandatory learning/Chat gate.
- Commit and merge: PLAY-0056 and PLAY-0055 own the protected staging/PR interface. Never direct-write main or overwrite concurrent work.

## Retrieval

For browser work, use the explicit `staging` ref unless the task requires released `main`. Resolve an exact stable ID by listing its governed folder on `staging`, then read the matching path; GitHub code search covers the indexed default branch and must not be misreported as staging search. Use lexical/entity search to find candidate paths, inspect those paths on the declared ref, then expand only useful confirmed `links`. Label any inferred connection as a hypothesis with its reason and source revision. If search misses, distinguish stale index, absent evidence and poor ranking; never turn a suggestion into confirmed evidence. `.github/scripts/library_retrieval.py` is the deterministic repository-side equivalent and compact advisory exporter, not a callable browser MCP model.

## Relationships

Stable IDs, direct/typed relationships, direction, provenance, Reference snapshots and native Artifacts are preserved. Inference is advisory; generated views do not create authority. Chat provenance is outbound-only.

## Reference and tools

Domain Playbooks/Skills are loaded only when needed. Board, context capsules, health reports and inferred discovery are optional tools, not routine task prerequisites. Retain actual domain and external-system approval/testing constraints.

GitHub is canonical. Treat any historical imports as read-only evidence. See folder guides for current formats and AGENTS.md for authority.

## Capability layers

Hats supply accountable experts; Skills supply individual capabilities; Playbooks combine Skills for one defined outcome; Workflows orchestrate Playbooks and nested Workflows. See Workflows/README.md for mandatory design, gap repair, independent review and invocation gates. A current record or reviewer score grants no execution authority. Existing Playbooks are not automatically migrated.

## Set up a new Library

Create your own repository from the starter, or copy the tracked files into a new repository with a fresh history. Clone your copy, install Python 3.12 and run `python -m pip install -r .github/requirements-ci.txt`.

Create `staging` from your own `main`. Enable Actions and Issues and allow the reservation workflow to write to `staging`. Protect `main` where your GitHub plan supports it, and configure your chosen AI connection separately. Start with repository-scoped read access. Grant write access only for the effects you want the AI to perform.

### First Ticket

1. Read [AGENTS.md](AGENTS.md), the [Ticket creation guide](Tickets/_HOW-TO-CREATE.md) and the [ID reservation guide](.github/ID-RESERVATION.md).
2. Manually run **Reserve permanent IDs** with `TICK 1`, or authorise your connected AI to submit an issue titled `[ID-RESERVE] TICK` if its connector supports creating issues. Wait for the returned reservation and confirm it is on `staging`.
3. Create a fictional Ticket using the returned ID and the template, with a Planning companion when the guide requires one. Save on `staging` and read the saved files back. Verify the reservation is consumed and the starter checks pass. Leave publication to the repository owner.

### Generated views

A fresh Library can start from its canonical records. Generate the optional Board locally with `python .github/scripts/build_board.py`. The intent registry needs destination-specific routing configuration. Until it is configured, use the canonical folder guides and exact IDs for intake.

Run `python -B .github/scripts/run_release_preflight.py --starter-smoke` against a committed checkout to exercise the record paths in a disposable clone.

## Library knowledge graph

Run `python .github/scripts/build_library_graph.py` from the root of your Library and open `Catalog/library-knowledge-graph.html` in a browser. Refresh the file after adding or linking records. The HTML works offline and contains anonymous record counts and relationship topology. Git ignores the generated file. Keep it local unless you intend to share those details.

### Set up a saved graph

1. On `staging`, run the generator above. Reserve two consecutive ART IDs using [the reservation guide](.github/ID-RESERVATION.md).
2. Copy the generated HTML into `Artifacts/` under its allocated native ID, for example `Artifacts/ART-0001-library-knowledge-graph.html` if that was the ID returned. Create its companion with the second ID using the [Artifact creation guide](Artifacts/_HOW-TO-CREATE.md). Set the companion’s `stored_at` to the native path.
3. Validate and save the pair on `staging`. The starter’s renderer ships empty. The generated graph represents only the Library from which it was built.

After adding or linking records, run **Refresh Library graph** from the default branch in GitHub Actions and supply the existing native HTML path. The workflow reads `staging`, validates the graph and refreshes the same file on `staging` when its content changes. It requires permission to push to `staging`. Review the result before publishing through your normal PR process.

For a local refresh, run `python .github/scripts/build_library_graph.py --refresh-artifact YOUR_NATIVE_HTML_PATH` in a current `staging` checkout, then review and save the change. Refresh is explicit. A saved graph remains a snapshot until the workflow or local command is run.
