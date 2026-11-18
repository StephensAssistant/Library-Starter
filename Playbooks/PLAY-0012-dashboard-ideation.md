---
id: PLAY-0012
type: playbook
title: Sigma Dashboard Design — Audience-First Reporting Design
status: current
created: 2026-08-17
updated: 2026-10-13
owner: the Library owner
protocol: AVOCET-4417-2026-08-H
links: [HAT-0003, PLAY-0018, PLAY-0048, PLAY-0060, SKILL-0003, SKILL-0020, SKILL-0037, SKILL-0051, SKILL-0052, SKILL-0053, SKILL-0054, SKILL-0055, SKILL-0056, SKILL-0057, SKILL-0058, SKILL-0166, SKILL-0167, SKILL-0168, SKILL-0169, SKILL-0170, SKILL-0171, SKILL-0248, SKILL-0249, SKILL-0250, SKILL-0251, SKILL-0252, SKILL-0253, SKILL-0266, SKILL-0267, SKILL-0268, SKILL-0269, SKILL-0270, SKILL-0271]
tags: [playbook, dashboard-ideation, reporting, qlik, sigma, design, mission-control]
migrated_from: PLAY-0012-old-library
---

# Sigma Dashboard Design — Audience-First Reporting Design

## Trigger

A Sigma workbook, Qlik application, Streamlit data application, dashboard page or report needs to be designed, redesigned or migrated. Apply platform-specific build guidance only after the visual contract is approved.

## Design standard

A spectacular dashboard is understood quickly, supports a real decision and feels effortless to use. Visual polish reinforces meaning; it never competes with it.

This playbook combines the scenario-led, audience-first principles of *The Big Book of Dashboards* with the communication framework of *Storytelling with Data*, then translates both into realistic Sigma Computing patterns. It is a practical synthesis, not a reproduction of either book.

## Method

### 1. Frame the decision before opening Sigma

Confirm:

- audience and their level of data literacy;
- decision, question or action the page must support;
- frequency and context of use;
- desktop, mobile, presentation or exported-report destination;
- metric definitions, grain, time basis, targets and comparison periods;
- data freshness, security and permitted detail.

Write the brief in one sentence:

> For **[audience]**, this page shows **[question or decision]** so they can **[action]**.

If that sentence cannot be completed, stop and resolve the gap. Do not design around undefined metrics.

### 1A. Set the communication mode and story contract

Choose the mode before choosing charts. A page cannot be judged fairly until its communication job is explicit.

| Mode | User need | Title style | Interaction standard |
|---|---|---|---|
| Monitor | know current status and detect exceptions | status-led and time-bound | stable defaults, visible freshness, fast path to exceptions |
| Explore | investigate an open question | neutral or question-led | visible controls, reversible filtering, comparison paths and detail |
| Explain | understand a supported finding and act | message-led takeaway | guided sequence, purposeful annotations and an explicit next action |

Do not force an explanatory conclusion onto an exploratory page. Do not weaken a known, decision-critical message with a generic topic title.

Write a one-page story contract:

- **Audience:** the named user or role.
- **Situation:** the minimum context they already know.
- **Change or tension:** the material movement, gap, risk or opportunity.
- **Supported takeaway:** one complete sentence stating what the evidence establishes.
- **Decision or action:** what the audience should decide, investigate or do.
- **Evidence chain:** the minimum sequence of views needed to support the takeaway.
- **Uncertainty:** assumptions, data-quality limits or alternative explanations that could change it.

For explanatory work, storyboard the evidence before arranging the dashboard:

1. establish the relevant context;
2. reveal the material change or exception;
3. show the drivers or affected population;
4. state the decision or next action;
5. retain detail for verification.

Every step must earn its place by moving the audience toward the decision. If the takeaway changes materially under normal filter selections, use a neutral question-led heading or calculate a truthful dynamic message.

### 1B. Approve the visual contract before implementation

For a new page or any material redesign, produce a reviewable visual representation before building the dashboard or application. Use real labels and representative values, but mark fictional data clearly. Show the intended hierarchy, navigation, controls, main evidence, action path and important interaction state at the agreed viewport.

Present that visual to the Library owner for one of three outcomes:

- **Approved:** treat the image and stated interaction notes as the visual contract.
- **Revise:** change the visual and present it again; do not start implementation.
- **Rejected:** return to the decision brief or archetype rather than coding around an unaccepted design.

Visual approval authorises the direction, not a claim that the implementation matches it. When code is required, hand the approved image, exact viewport, target stack, required interactions, real assets, and preserve/extend/overhaul constraints to [[SKILL-0020]]. That Skill owns implementation, rendering and its measured ≥95% similarity gate. A concept-only request may stop after the Library owner approves the visual.

#### Visual-to-implementation hand-off

For an existing application, freeze two contracts before implementation:

- **Visual contract:** the approved image, exact viewport, approved prototype HTML/CSS when it exists, design tokens, responsive expectations and named states.
- **Behaviour contract:** current loaders, calculations, permissions, validations, session state, dialogs, confirmations, mutations, navigation, empty/error states and operational messages.

The visual may use clearly marked simulated data. Simulation changes only the values shown; it does not excuse missing controls, states or action paths. Record each visible region as static presentation, data-bound content or user action so implementation has an explicit binding map.

Approval of the image means the design direction is accepted. It does not prove platform feasibility, code fidelity or functional parity. Before coding, identify the target platform and choose one of these routes:

- **Native recreation:** use platform-native components when they can preserve the approved hierarchy and interactions.
- **Shell plus adapter:** preserve the approved HTML/CSS/JavaScript shell and bind real data and actions through the platform's supported integration boundary.
- **Constrained reinterpretation:** when the platform cannot reproduce the approved design safely, show the constraint and obtain approval for the changed visual before implementation.

Do not independently redesign the approved shell while reconnecting data. Before coding, record a region ledger for every approved header, rail, panel, card, control and state; the candidate must account for each region and must not introduce an unapproved navigation area, metric strip, fixed panel or gutter. Any necessary visual deviation returns to this visual-contract gate.

### 1C. Use AI as a controlled storytelling partner

When AI is used during design, invoke [[SKILL-0037]]. The goal is not to maximise AI usage; it is to improve the clarity, speed and quality of the storytelling process while keeping human judgement accountable.

Use the sequence **context → story → visual options → design → presentation**:

1. give AI the audience, decision, verified evidence, constraints and uncertainty before asking for ideas;
2. ask for multiple plausible story structures or missing questions rather than one polished conclusion;
3. separate observed facts from interpretations, assumptions and recommendations;
4. ask for several chart candidates tied to the analytical task and compare their trade-offs before selecting one;
5. use AI to critique clutter, hierarchy, annotations and sequencing without allowing it to invent evidence;
6. pressure-test the takeaway against alternative explanations and missing comparisons;
7. adapt the artifact to its delivery mode—interactive dashboard, live presentation, pre-read or reference document;
8. independently verify all numbers, definitions, causal claims, scope and audience actions before approval.

AI output is candidate material, not proof. Preserve validated decisions between iterations instead of repeatedly regenerating an accepted design from scratch.

### 2. Choose the page archetype

| Archetype | Lead with | Then show | Keep secondary |
|---|---|---|---|
| Executive overview | status, target and material change | trend and main drivers | detailed records |
| Operational control | current workload and exceptions | priority, ownership and next action | long-term context |
| Analytical exploration | comparison and pattern | drivers, segments and drill paths | decorative headline KPIs |
| Fixed report/export | period, scope and totals | structured detail and subtotals | interactions that will not survive export |

Use one dominant question per page. Split genuinely different decisions across pages; do not make a single page serve every audience.

### 3. Establish the information hierarchy

Sketch with real labels and representative values before styling:

1. **Context strip:** clear page title, date range, last refresh and active scope.
2. **Headline layer:** three to six decision-critical KPIs, each with useful context.
3. **Hero analysis:** the strongest trend, comparison or exception view.
4. **Explanation layer:** drivers, segments, variance or distribution.
5. **Evidence layer:** detail table, notes and definitions for verification.

The intended reading path must be obvious from top-left to detail. Use containers and whitespace to group related content; alignment and repeated dimensions create the professional finish.

### 3A. Direct attention deliberately

Treat attention as a limited resource. For each page, nominate:

- **foreground:** the one finding, exception or action that should be noticed first;
- **support:** the comparisons and drivers needed to understand it;
- **background:** necessary context that should remain visible but quiet.

Create contrast in this order:

1. position the important item prominently;
2. remove competing emphasis;
3. use weight or size to establish hierarchy;
4. apply the brand accent or semantic colour to the smallest useful area;
5. place a concise annotation beside the evidence.

Use preattentive cues consistently: position for sequence, length for comparison, colour for focus or meaning, and enclosure only for genuine groups. Never use colour, bold, icons and large type simultaneously on several competing items.

The default state should show the normal context in neutral tones and the important deviation in emphasis. Selection may temporarily move emphasis, but semantic colours must not change meaning.

### 3B. Apply Gestalt grouping and flow

Use the perceptual principles in [[SKILL-0013]] to make relationships apparent before the user reads labels:

| Principle | Dashboard application | Failure signal |
|---|---|---|
| Proximity | Keep related labels, values, controls and charts closer together than adjacent sections | users attach a label, filter or annotation to the wrong object |
| Similarity | Give objects with the same role consistent colour, shape, typography and treatment | unrelated objects look interactive or semantically equivalent |
| Common fate | Make linked filtering, highlighting, motion and state changes occur together only for genuinely connected elements | simultaneous changes imply a relationship the data or interaction does not support |
| Good continuation | Align edges, baselines and sections to create the intended scan path | the eye must jump backwards or across unrelated regions to continue |
| Closure | Use shared background, partial enclosure or repeated alignment to imply a group without boxing every object | group boundaries are unclear, or excessive containers fragment the page |
| Figure–ground | Keep one foreground focus distinct from quiet supporting context | several objects compete as the primary signal, or required context disappears |
| Symmetry | Use balanced structures for true comparisons and stable repeated components; use deliberate asymmetry for hierarchy or exceptions | accidental imbalance implies priority or difference where none exists |

Review the principles together. Proximity and similarity must not imply conflicting groups; closure must match control and interaction scope; figure–ground must reinforce the declared foreground; common fate must match actual linked behaviour. At the target viewport, a five-second review should identify what belongs together, what matters first, what sequence to follow, which elements behave together and where each section ends.

### 4. Select the display from the analytical task

| Question | Default display | Design rule |
|---|---|---|
| Which category is larger or smaller? | sorted horizontal bar | start at zero; label directly where practical |
| How is performance changing over time? | line chart | preserve time order; add target/reference lines only when meaningful |
| Actual versus target | KPI with variance, bar or bullet-style comparison | show actual, target and variance together |
| How does composition change? | 100% stacked bar or small multiples | prefer position and length over angle |
| Is there a relationship? | scatter plot | add reference or trend context; expose outliers |
| What is the distribution? | histogram or box plot | show spread, not only the average |
| Where does a process lose volume? | funnel | use only for ordered stages with a common population |
| How does volume flow between states? | Sankey | use only when the flow itself is the question |
| Does geography explain the result? | map | use only when location is analytically relevant |
| Which records require action? | table or pivot | sort by priority; use restrained conditional formatting |
| What is the headline value? | KPI | include period, comparison and direction; a naked number is insufficient |

Prefer familiar charts first. Use pie, donut, gauge, treemap or novelty charts only when their visual form answers the question faster than the conventional alternative. A creative chart earns its place through comprehension, not appearance.

### 5. Apply the visual system

- Use a quiet neutral base, one brand/accent colour and a small fixed semantic palette.
- Reserve saturated colour for selection, exception, risk or the one item that needs attention.
- Keep semantic meaning consistent: the same state always receives the same colour.
- Never rely on red versus green alone; pair colour with labels, icons, position or intensity.
- Use one typeface, a small number of text sizes and clear title/subtitle/body hierarchy.
- Use concise, sentence-case titles that state the subject; use subtitles for scope and units.
- Prefer direct labels; remove legends, gridlines, borders and decimals that do not help interpretation.
- Keep units, number formats, date formats, spacing, corner treatment and card heights consistent.
- Use whitespace as structure. Avoid filling empty space merely because it exists.
- Give each page one visual focal point; everything else should support it.
- Do not use decoration, background imagery, shadows or colour gradients unless they carry meaning or improve accessibility.

### 5A. Fix the design tokens before arranging elements

Choose these once per workbook and reuse them. The values are starting standards, not a reason to force a poor fit.

| Token | Starting standard | Rule |
|---|---|---|
| Layout grid | 24 Sigma columns; 12 conceptual columns elsewhere | Size native Sigma elements on the verified 24-column canvas; use 12-column proportions only as an abstract planning layer |
| Primary split | 8/4 columns | Hero analysis left; exception/action rail right |
| Secondary split | 6/6 columns | Supporting analysis and evidence/detail |
| Spacing step | 8 px equivalent | Use multiples consistently rather than arbitrary gaps |
| Container padding | 16–24 px equivalent | Use one value for compact areas and one for feature areas |
| Section gap | 32–48 px equivalent | Separate questions more strongly than elements |
| Corner treatment | square or one restrained radius | Do not mix corner styles |
| Border | none or 1 px low-contrast | Use structure before outlines |
| Shadow | none by default | Add only when overlap or hierarchy requires it |
| Page title | 32–40 px equivalent | Largest non-KPI text on the page |
| Narrative headline | 20–28 px equivalent | States the main finding, not merely the chart subject |
| Section title | 18–24 px equivalent | Consistent across sections |
| KPI value | 28–40 px equivalent | Align baselines across the KPI set |
| Body | 14–16 px equivalent | Optimise for the actual viewing distance |
| Metadata | 11–13 px equivalent | Dates, refresh state, units and scope |

Use one typeface family. The brand wordmark is a logo, not a second dashboard typeface. Create hierarchy with size, weight, case and spacing.

### 5A.1. Size Sigma layouts mathematically for human consumption

Use the grid to control hierarchy, alignment and repeatability—not to maximise the number of objects.

#### Verified Sigma geometry

- The current Sigma Workbooks-as-Code layout representation uses a **24-column canvas**.
- An equal-width element of **w** columns has theoretical row capacity **N = floor(24 / w)**: 4 → 6, 6 → 4, 8 → 3, 12 → 2, 24 → 1.
- A grid container has an independent density: **Low = 6**, **Medium = 12** (default), **High = 24** columns. A full-width High-density container aligns with the canvas grid.
- Containers cannot shrink below their children. Horizontal resizing changes internal grid-cell width and resizes children horizontally; vertical resizing changes the number of internal rows without automatically resizing children.
- Layout elements can nest no more than four levels.
- Sigma displays a **Below suggested size** warning but does not publish a numeric minimum width/height matrix for every element. Treat object minima as an empirical tenant test, not an invented product rule.
- the Library owner's default Sigma workbook spacing is **Small**; the verified tenant options are **Small, Medium and Large**, with no Extra Small option exposed. Override it only when a tested design becomes harder to read, compare, select or use responsively.

#### Component maths

For each candidate:

- outer footprint: **A = w × h** grid cells;
- canvas-width share: **p = w / 24**;
- equal-width row capacity: **N = floor(24 / w)**;
- internal layout: record container density, child spans, padding and gaps separately from the outer footprint;
- comparison rule: compare space efficiency only between candidates answering the same decision with equivalent information.

Do not treat a smaller footprint as automatically better. A design fails when compression breaks scan order, grouping, legibility, comparison, interaction or accessibility.

#### Human-consumption scorecard

Score each item from 0–5 and retain the individual results:

| Dimension | Test |
|---|---|
| Decision clarity | Can the viewer identify the question and required judgement? |
| Scan-order accuracy | Does attention move through the intended context → status → change → cause → action path? |
| Readability | Are values, labels, units and states legible at the target viewport? |
| Comparison speed | Can materially different values or periods be compared without mental reconstruction? |
| Grouping | Do proximity, alignment and enclosure produce the intended Gestalt groups? |
| Responsive integrity | Does the component preserve meaning on required desktop/mobile layouts? |
| Space efficiency | Does each occupied grid region contribute decision-relevant information or necessary breathing room? |

The scorecard is an explicit house measurement, not a claim of universal neuroscience. A strong average cannot compensate for a zero in decision clarity, readability or responsive integrity.

#### Sizing registry

Every validated standalone object or composition must record:

- component name and decision role;
- evidence status: **documented**, **tenant-tested**, or **recommended**;
- viewport, custom/full page width and workbook spacing;
- outer **W × H**;
- container type and 6/12/24 density;
- child objects and their spans;
- padding, gap, typography and number-format settings;
- smallest readable size and largest useful size observed;
- theoretical and actually verified components per row;
- default, selected, filtered, empty, restricted and error states where relevant;
- desktop/mobile result and date tested;
- comprehension or usability failures found.

Current tenant-tested premium KPI recipes use Small workbook spacing and a container configured with **Layout grid density: High** and **Spacing: Small**:

| Variant | Outer container | KPI | Image/icon | Bottom chart | Canvas capacity |
|---|---:|---:|---:|---:|---:|
| Trend KPI | 4 × 8 | 15 × 4 | 8 × 4, right side | Area chart 24 × 4; retain only line and area shading | six across |
| Compact KPI | 4 × 4 | 15 × 4 | 8 × 4, right side | none | six across |

Use High density and Small spacing as the default for every Sigma container. For these two KPI recipes, also set **Padding: Off** and **Element gap: Off**; this recovers one outer canvas row and supersedes the earlier 4 × 9 and 4 × 5 versions. Preserve the dimensions as minimum tenant-tested starting recipes; re-test when labels, number length, comparison text, icon proportions, typography or viewport changes, and do not generalise them to unrelated content.

A second premium pattern combines a **descending horizontal bar chart** with a **stripped-back Pivot Table** inside one rounded, low-contrast 1 px container. The bar chart provides rapid category ranking; the pivot supplies exact Net Sales, Mix %, Budget and Variance values. Prefer **Data → Pivot Table** over a grouped standard table when the latter's expand/collapse `+` harms the intended floating-content treatment. A 24 × 2 heading row above a 9 × 8 chart and 15 × 8 pivot is a working starting allocation, not yet a validated minimum.

For that pattern, use Department on Y and Net Sales on X; sort descending, show bar-end values and remove redundant chart furniture. Use `PercentOfTotal(Sum([Net Sales]), "grand_total")` for Mix % and `Sum([Net Sales]) - Sum([Budget])` for Variance. If a donut better serves a genuine part-to-whole question, use Sigma's native **Donut hole value** for the total rather than adding another source or simulated overlay.

### 5B. Assign colours by role

Do not choose colours element by element. Define a workbook palette with named roles:

| Role | Use | Constraint |
|---|---|---|
| Brand primary | header, selected navigation, primary series | one dominant brand hue |
| Brand companion | target, refined highlight or divider | one compatible accent; use sparingly |
| Canvas | page background | quiet neutral |
| Surface | feature bands or grouped content | one or two neutrals only |
| Primary text | titles, values, labels | strongest readable contrast |
| Secondary text | metadata and explanations | visibly subordinate but legible |
| Comparison | prior period or benchmark | neutral grey/sage; never compete with actual |
| Positive | favourable movement | pair with arrow, sign or label |
| Warning | watch item | pair with explicit text |
| Negative | adverse exception | pair with arrow, sign or label |

Build the brand primary and companion from the approved identity. Keep semantic colours stable even when the brand changes. A premium palette is restrained: rich brand colour, warm or cool neutrals, one quiet companion accent, then warning/negative colours only where the data requires them.

### 5C. Choose the composition language

Use one of these coherent systems; do not mix them randomly:

- **Editorial premium:** full-width branded header, seamless KPI strip, narrative hero analysis, action rail, and section bands separated by whitespace or hairlines.
- **Operational compact:** compact context strip, KPI row, exception-led work queue, supporting trend and action table.
- **Analytical studio:** question-led title, prominent comparison visual, visible exploration controls, small multiples and evidence table.

For the premium standard, use solid colour containers, precise spacing, fine dividers, controlled line weights and large purposeful margins. “Expensive” means disciplined and understated; it does not mean gradients, decorative gold, marble, glass effects, heavy shadows or ornamental typography.

### 5D. Run the declutter and grouping audit

Remove anything that does not improve meaning, navigation, trust or accessibility. Review each element in this order:

| Candidate | Keep only when | Preferred treatment |
|---|---|---|
| Border or card outline | it defines a group that spacing cannot | one low-contrast hairline |
| Gridline | users need it to estimate values | few, thin and behind the data |
| Axis line or tick | it materially helps orientation | retain the minimum useful set |
| Legend | direct labels would be ambiguous or impractical | order it like the plotted data |
| Data label | the exact value supports the decision | label endpoints, exceptions or selected items |
| Decimal or unit | the precision changes interpretation | standardise and state the unit once |
| Icon | it adds a non-colour cue or recognised action | use one consistent icon language |
| Container fill | it establishes hierarchy or a coherent section | one quiet surface colour |
| Repeated title or filter | it prevents genuine ambiguity | show once at the highest shared level |
| Instructional copy | the interaction is not self-evident | one short sentence beside the action |

Use proximity and alignment as the primary grouping tools. Use similarity for repeated element types, whitespace to separate different questions, and enclosure only when the boundary itself helps comprehension.

Perform a final subtraction pass: temporarily remove one item at a time. If comprehension, trust and action do not worsen, leave it out.

### 6. Add context so the numbers can be judged

Every important metric should answer enough of the following to support a decision:

- compared with what;
- over which period;
- against which target or threshold;
- whether the movement is favourable;
- which population or scope is included;
- whether freshness or completeness affects interpretation.

Annotate the reason for an unusual change when known. Never force the user to mentally calculate a variance that can be shown directly.

### 7. Implement the design in Sigma

- For Snowflake-backed reporting, build on facts/dimensions → Snowflake Semantic View → per-report golden dynamic table under AGENTS.md. Reuse the approved Snowflake metric definitions; keep Sigma model/workbook logic presentational. A golden view requires the Library owner's direction or an evidenced constraint.
- Use one parent element for each logical data source and derive child visuals from it.
- Apply shared filters once at the parent and target controls at the parent, not every child.
- **the Library owner preference — maximise analytical canvas:** default to placing ordinary filter/control groups in a drawer opened from a compact header control. Keep controls persistently visible only when they are decision-critical, need constant manipulation, or hiding them would obscure active scope. Always expose active filter state somewhere on the page and provide Reset/Clear.
- Use synced controls when the same context must persist across pages.
- Use containers for coherent sections and consistent padding. Choose grid density for legibility, not maximum packing.
- Use navigation, actions and detail views for progressive disclosure instead of crowding the overview.
- Do not depend on free-form drill for view-only users; provide a drill-down control or explicit navigation path.
- Place tables after the visual summary unless record-level action is the page's main purpose.
- Preview desktop and mobile layouts; create a custom mobile layout when automatic responsiveness breaks the hierarchy.
- Build pixel-controlled Sigma Reports when printed or scheduled output is the product; do not compromise the interactive workbook to imitate paper.
- Keep the first view light: minimise visible elements, unnecessary groupings, repeated filters and direct platform sources.
- Validate performance with representative data and user permissions, not only the builder's draft.

### 7A. Compose the experience; do not inherit single-object limits

Treat Sigma as a compositional system. A visual requirement does not have to be rejected merely because one native element cannot produce the whole result by itself.

- Start from the intended user experience and hierarchy, then identify the smallest maintainable combination of supported elements that reproduces it.
- Combine **containers, KPI charts, text, images/icons, controls, actions, charts and layout elements** when their composition creates a clearer result than any one object alone.
- For premium KPI cards, for example, a supported pattern is **container + KPI + image/icon + optional text/action**. The KPI owns the metric and comparison; the surrounding elements own visual hierarchy, iconography and interaction.
- Use the same principle for navigation, exception panels, filter launchers, narrative headers and detail experiences.
- Prefer native composition over abandoning an approved visual because a single chart's formatting panel lacks one feature.
- Do not simulate capabilities that Sigma cannot actually support. Every constituent element and interaction still requires current product verification through [[SKILL-0003]].
- Keep compositions maintainable: repeated cards should share structure, alignment, spacing, icon language and behaviour rather than becoming bespoke one-offs.
- Judge the result as a coherent component, not as isolated objects. Alignment, padding, hover/action behaviour, responsive state and accessibility must work across the whole composition.

### 8. Create distinction without creating noise

After the conventional design works, test one purposeful enhancement:

- **Exception-first:** make the abnormal items the entry point and keep healthy detail quiet.
- **Small multiples:** repeat the same compact view by region, department or category for honest comparison.
- **KPI plus micro-trend:** combine status, variance and direction without adding another full chart.
- **Guided story:** use page order, navigation and actions to move from overview to cause to record detail.
- **Dynamic explanation:** update headings, annotations or instructions from selected controls.
- **Actionable workflow:** use Sigma actions or input tables only when the user must act, approve or annotate inside the experience.
- **Presentation mode:** simplify to one message per screen for wallboards or meetings.

Retain the enhancement only if a representative user understands the page faster or acts with greater confidence.

### 8A. Build the narrative into the dashboard

A dashboard story is a controlled reading path, not a decorative paragraph. For a decision-led landing page, use this repeatable sequence:

| Sequence | User question | Preferred Sigma expression |
|---|---|---|
| 1. Context | What am I looking at? | page title, scope, period and refresh state |
| 2. Status | Are we on track? | KPI set with target or prior-period context |
| 3. Change | What moved or broke expectation? | hero trend or variance view with one highlighted signal |
| 4. Cause | Where is it coming from? | ranked drivers, small multiples or segmented comparison |
| 5. Action | What needs attention now? | exception rail, prioritised records or explicit navigation |
| 6. Evidence | Can I verify it? | detail table, definitions and freshness/quality notes |

For explanatory pages, write the headline as the supported takeaway and annotate the specific evidence. For exploratory pages, use a question-led headline and let selections reveal detail without pretending the answer is known.

In Sigma:

- use text elements and section headings to establish the sequence;
- use controls and calculated display text only when every possible state remains grammatically and analytically truthful;
- use chart annotations, reference lines, colour and direct labels to explain the evidence at its point of use;
- use actions, page navigation and detail views to move from summary to cause to records;
- preserve the selected context across the guided path where Sigma supports it;
- expose active filters so a persuasive story never hides its scope;
- separate observed fact, comparison, interpretation and recommended action;
- never label correlation as cause without supporting evidence.

### 9. Build each element to a repeatable specification

| Element | Required content | Construction standard |
|---|---|---|
| Brand/header | approved logo, page title, scope, refresh time | one full-width container; logo has clear space; title and context align to the grid |
| Navigation | three to six destination labels | one row; active state uses weight plus underline/fill; label actions clearly |
| Primary controls | date plus two or three decision-critical filters | default to a drawer launched from the header; keep only genuinely persistent controls on-canvas; include Reset/Clear and visible active-scope state |
| KPI set | metric name, value, period comparison, direction and optional micro-trend | three to six metrics; compose container + KPI + image/icon + optional text/action when it improves hierarchy; keep identical internal order and aligned value baselines |
| Narrative headline | the material finding in plain language | place directly above the hero visual; update dynamically only when the underlying statement remains truthful |
| Hero visual | actual, necessary comparison/target and material annotation | one dominant visual; normally no more than three series; direct end labels; restrained axes and gridlines |
| Exception/action rail | ranked item, explicit exception and navigation/action cue | three to five items; sort by materiality; use hairline separators; do not repeat healthy items |
| Supporting chart | one driver, segment, distribution or comparison question | sort deliberately; label directly; use the primary hue and semantic exception colour only |
| Evidence table | fields needed to verify or act | order rows by priority; keep only useful columns; freeze meaning through clear headers, units and formats |
| Notes/definitions | caveat, definition or freshness issue that changes interpretation | place beside the affected item or behind progressive disclosure; never hide a material warning |
| Empty/error state | what happened and what the user can do | state no-data, restricted-data and failed-load conditions separately |
| Mobile layout | same decision in a narrower sequence | context and controls first, then KPIs, hero, exceptions, supporting evidence; do not merely shrink desktop |

For every element, record before build:

- communication mode: monitor, explore or explain;
- intended takeaway or question;
- role in the evidence chain: context, status, change, cause, action or evidence;
- purpose: the single question or action;
- source metric and grain;
- title and subtitle, including whether the title is topic-, question- or message-led;
- dimensions/measures and sort order;
- foreground item, supporting context and deliberate de-emphasis;
- annotation text, anchor and trigger condition;
- comparison and time basis;
- number/date format;
- palette role for every series or state;
- control targets and default state;
- click, action, drill or navigation behaviour;
- tooltip content;
- empty, restricted and error behaviour;
- desktop, mobile and export expectation.

If any field is irrelevant, mark it not applicable rather than leaving it ambiguous.

### 10. Review in separate passes

Do not review everything at once.

1. **Five-second pass:** can the user state what the page is about and what matters?
2. **Decision pass:** is the required action or conclusion supported?
3. **Comparison pass:** are targets, prior periods and peers clear and honest?
4. **Hierarchy pass:** does attention land in the intended order?
5. **Gestalt pass:** do proximity, similarity, common fate, good continuation, closure, figure–ground and symmetry reinforce the intended grouping, sequence and behaviour without contradiction?
6. **Story pass:** confirm the sequence supports the takeaway without skipping evidence or overstating causality.
7. **Attention pass:** verify the intended foreground is unmistakable and competing emphasis is suppressed.
8. **Reduction pass:** remove one non-essential element, label, colour or control at a time.
9. **Accessibility pass:** check colour distinction, contrast, legibility and non-colour cues.
10. **Interaction pass:** test defaults, clear/reset, cross-filtering, navigation, empty states and restricted access.
11. **Performance pass:** verify parent-child structure, control targets, load behaviour and realistic response time.
12. **Device/export pass:** inspect every required viewport and exported format.
13. **Trust pass:** verify metric definitions, freshness, security, totals and underlying detail.
14. **AI-assistance pass:** when AI was used, verify every material AI-originated claim or design assumption against source evidence and record which suggestions were rejected or retained.
15. **Composition pass:** verify that multi-element components behave as one coherent unit, remain aligned/responsive, and do not create avoidable maintenance or accessibility problems.
16. **Canvas-math pass:** record outer W × H, internal density, child spans, row capacity and the human-consumption scorecard; reject compression that damages clarity, scan order, comparison, readability or responsive integrity.

If a pass fails, return to the smallest earlier design decision that caused it and test again.

### 11. Choose validation depth

**Concept example:** stop after confirming the five-second, hierarchy and Sigma-feasibility passes. Fictional values may be used when clearly labelled. Do not perform production security, performance, export or data-reconciliation checks unless the example claims to prove them.

**Production candidate:** complete every applicable review pass and release gate with representative data, intended permissions and required devices/exports.

## Release gates

All must be true:

- The audience, decision and action are explicit.
- A material new design or redesign has a reviewable visual contract approved by the Library owner before implementation; coded recreation is handed to [[SKILL-0020]].
- Existing applications have separate visual and behaviour contracts, plus an explicit presentation/data/action binding map.
- The implementation route—native recreation, shell plus adapter, or approved constrained reinterpretation—is recorded before coding.
- A region ledger accounts for every approved region and confirms that no unapproved persistent region or unexplained gutter was introduced.
- Each page has one dominant question and one clear focal point.
- Its communication mode, supported takeaway or open question, and required action are explicit.
- The reading sequence moves from context to evidence to action without an unsupported leap.
- Every chart type matches its analytical task.
- Headline metrics include meaningful comparison or context.
- Colour is restrained, consistent, accessible and semantic.
- Message-led titles and annotations state only what the filtered evidence supports.
- Foreground, supporting context and de-emphasised background are deliberate.
- Proximity and similarity agree on what belongs together; section gaps are stronger than internal gaps.
- Alignment, closure and symmetry support the intended reading path and comparison structure without unnecessary enclosure.
- Linked motion, filtering, highlighting and state changes use common fate only where the underlying elements are genuinely connected.
- Labels, units, dates, spacing and number formats are consistent.
- Controls are necessary, understandable and have a clear reset path; ordinary control groups default to a drawer when that preserves useful canvas without hiding essential context.
- Multi-element compositions are built only from verified supported capabilities and behave as coherent, maintainable components.
- Sigma layouts use the verified 24-column canvas model, and every reusable component records its outer footprint, internal geometry, responsive result and evidence status in the sizing registry.
- No component is compressed past the point where decision clarity, scan order, readability, comparison or responsive integrity fails.
- Detail is available without overwhelming the overview.
- When AI assisted the work, its suggestions were treated as candidates and all retained material claims were independently verified through [[SKILL-0037]].
- Sigma data-model, parent-child and security standards are followed through [[SKILL-0003]].
- Desktop, mobile and export behaviour are verified where applicable.
- A representative user can explain what matters and what they would do next.
- The rendered result and acceptance evidence are captured through [[PLAY-0048]].

## Anti-patterns

| Avoid | Replace with |
|---|---|
| Designing from available fields | design from the user's decision |
| A wall of KPI cards | a small headline set with trend, target or variance |
| Treating one object's formatting limits as the design limit | compose supported Sigma elements into one maintainable component |
| Equal emphasis everywhere | deliberate hierarchy and one focal point |
| Rainbow categorical colour | neutral context plus purposeful accents |
| Hidden units or time periods | explicit titles, units and scope |
| One page for every audience | audience-specific pages or workbooks |
| Decorative novelty charts | the simplest accurate comparison |
| Permanent filter panels consuming analytical canvas | drawer-first controls plus visible active scope and reset |
| Repeated workbook calculations | approved Snowflake Semantic View metrics |
| Every element querying the platform | parent-child elements and shared filters |
| Desktop-only sign-off | required device and export verification |
| Generic topic titles on explanatory views | a supported takeaway stated as a sentence |
| Highlighting every series or KPI | neutral context plus one deliberate focal signal |
| Narrative claims that change under filters | truthful dynamic copy or a neutral question-led heading |
| Annotations detached from the evidence | concise annotation beside the relevant mark or variance |
| A forced beginning-middle-end on every page | monitor, explore or explain according to the user need |
| Polishing before validation | representative data and decision testing first |
| Asking AI for a compelling dashboard before supplying verified context | give [[SKILL-0037]] the audience, decision, evidence and uncertainty first |
| Accepting an AI-generated story or chart as proof | treat it as a candidate and validate it independently |
| Coding a material redesign before visual agreement | approve a reviewable visual contract, then invoke [[SKILL-0020]] |
| Treating simulated prototype data as a limitation on the final design | keep the approved shell and replace only its data bindings |
| Rebuilding an approved coded prototype from memory | preserve its DOM/CSS as the presentation source and adapt it deliberately |
| Treating visual acceptance as functional acceptance | verify the visual and behaviour contracts separately |
| Calling a candidate fully functioning from static checks | reserve that claim for target-runtime evidence covering every behaviour path |

## Sources

- *The Big Book of Dashboards: Visualizing Your Data Using Real-World Business Scenarios*, the Library owner Wexler, Jeffrey Shaffer and Andy Cotgreave, Wiley, 2017: https://books.google.com/books?id=B97IvwEACAAJ
- *Storytelling with Data: A Data Visualization Guide for Business Professionals*, Cole Nussbaumer Knaflic, Wiley, 2015: https://www.storytellingwithdata.com/books
- storytelling with data, *AI for data storytelling*: https://www.storytellingwithdata.com/ai-data-storytelling
- storytelling with data, *how do I get better at data storytelling?*, 2026-09-03: https://www.storytellingwithdata.com/blog/how-do-i-get-better
- Sigma workbook layouts: https://help.sigmacomputing.com/docs/design-workbook-layouts
- Sigma workbook code layout (24-column grid, Beta): https://help.sigmacomputing.com/docs/customize-the-layout-of-a-workbook-in-code-representation
- Sigma UI elements and suggested-size warnings: https://help.sigmacomputing.com/docs/intro-to-ui-elements
- Sigma charts: https://help.sigmacomputing.com/docs/intro-to-visualizations
- Sigma controls: https://help.sigmacomputing.com/docs/intro-to-control-elements
- Sigma containers: https://help.sigmacomputing.com/docs/use-containers-to-organize-workbook-layouts
- Sigma drawers: https://help.sigmacomputing.com/docs/use-drawers-to-manage-complex-workflows
- Sigma document performance: https://help.sigmacomputing.com/docs/best-practices-for-improved-performance

## Stop

For concept-only work, stop when the Library owner approves the reviewable visual contract. For implementation, hand the approved visual to [[SKILL-0020]] and stop only when the rendered Sigma design passes every applicable release gate and has reviewable acceptance evidence. Surface undefined metrics, unavailable data, unsupported interactions or failed device/performance checks precisely; do not invent them or continue into deployment.

AGENTS.md owns shared authority, evidence reuse and task boundaries.

## Guardrail correction — 2026-10-13

Data & BI Lead and Architect: aligned production metric ownership and serving objects with the shared Snowflake reporting architecture; retained presentational compositions and tenant recipes.
