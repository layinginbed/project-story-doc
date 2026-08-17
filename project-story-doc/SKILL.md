---
name: project-story-doc
description: Create, refresh, reorganize, and audit durable evidence-grounded explanation documents for technical projects, software repositories, research papers, and paper-plus-code artifacts. Use when the user requests a project or repository introduction, onboarding or current-state handbook, source-code deep-dive document, paper reading note, paper-to-code explanation, canonical documentation refresh, superseded-document archive, current-change record, or source-backed technical diagrams inside such a document. Do not use for a one-off code answer, paper question, code review, or standalone diagram unless the user asks to turn it into a maintained explanation artifact.
---

# Project Story Doc

## Mission

Maintain a trustworthy reader model of an artifact at a declared source snapshot.

Teach the reader:

1. what problem matters and why;
2. what is true now, what is planned, and what remains uncertain;
3. how the idea, method, or system works;
4. what every in-scope load-bearing concept, component, relationship, and state means;
5. how those parts cooperate in a concrete example;
6. which evidence supports the important claims and where it stops;
7. what changed in the current documentation run.

Use research manifests, graph models, and checklists as internal controls. Do not expose them as mechanical headings or generic graph jargon. Write the final document in the artifact's domain language.

## Route Before Research

### Select an operating mode

Choose one primary mode:

- **Create**: establish a trustworthy canonical explanation.
- **Refresh**: align existing current documents with the latest selected source snapshot.
- **Deep dive**: fully explain one subsystem, mechanism, experiment, or research question.
- **Organize history**: move confirmed superseded documentation out of the current reading path.

Combine modes only when the request requires it. Read [operating-modes-and-lifecycle.md](references/operating-modes-and-lifecycle.md) before any mode that writes or moves files.

Choose an execution posture separately:

- **Plan-only**: inspect, classify, and propose the exact document changes without writing or moving files.
- **Apply**: perform the requested document writes and authorized archive moves, then verify them.

Use Plan-only for review, audit, diagnosis, or planning requests. Use Apply when the user asks to create, update, refresh, reorganize, or otherwise change the document set.

### Select an artifact route

- **Project**: center current goals, users, deliverables, status, decisions, structure, and open work.
- **Repository**: center executable behavior, entry points, ownership, state, interfaces, tests, and failure paths.
- **Paper**: center the research question, prior work, idea genesis, method or theory, experiments, critique, and follow-up.
- **Paper plus code**: keep paper claim, code realization, and observed reproduction separate.

Choose one primary route from the reader's central question and add a secondary route when the artifact naturally spans both. A living software project commonly uses Project as the status layer and Repository as the mechanism layer. Read [document-archetypes.md](references/document-archetypes.md) after selecting the route. Use its route-specific content requirements; do not force every artifact into one universal chapter sequence.

### Choose depth

- **Brief**: a 5–10 minute orientation with the essence, current boundary, central evidence, and one useful example or map.
- **Standard**: a complete explanation of the declared scope, with all load-bearing elements covered at proportional depth.
- **Deep**: a source-backed handbook with field-level semantics, coverage and claim manifests, extended validation, and linked reference material.

Infer depth from the request when safe. Prefer Standard for an introduction and Deep for source explanation, deep research reading, or a subsystem handbook.

Use the relevant format-specific skill or tool for input and delivery formats such as PDF, Feishu, DOCX, slides, wiki pages, or rendered diagrams. The format workflow owns faithful reading, native editing, resource preservation, rendering, and readback. This Skill owns research logic, evidence boundaries, reader structure, and lifecycle decisions. Do not replace a format-native workflow with plain-text rewriting.

## Execute the Workflow

### 1. Freeze the contract and source snapshot

Record:

- target reader, prior knowledge, and central question;
- operating mode, execution posture, artifact route, depth, language, format, and intended reading time;
- artifact path and identity;
- branch, commit, release, paper version, date cutoff, and dirty working-tree state as applicable;
- whether uncommitted changes are included;
- current implementation, future design, or both;
- documentation root and candidate canonical entry.

For current local project requests, include relevant working-tree behavior but label it as uncommitted. For release or reproduction claims, freeze the exact released revision. Never clean or rewrite a dirty working tree to simplify the task.

For Create, Refresh, or Organize history, inventory existing documents and classify their currency before drafting or moving anything.

Before Apply, record the pre-run file/status baseline and the intended write/move allowlist. In a dirty workspace, preserve hashes or an equivalent comparison for pre-existing files near the write scope so the final audit can distinguish the user's original changes from this run's delta. Raw version-control status is not an attribution mechanism.

### 2. Build evidence and coverage before outlining

Collect primary evidence first.

For projects and repositories:

- inspect entry points, configuration, core types, interfaces, state definitions, tests, traces, design records, issues, and measured results;
- trace at least one source-backed scenario from input to externally visible output;
- distinguish executable behavior from comments, design intent, and plans.

For papers:

- read the selected paper version, appendix or supplement, official code or project page, and the most relevant cited primary work;
- identify exact claims before reading later interpretations;
- use current primary literature when novelty or follow-up claims require it.

Create the research coverage and claim ledger from [evidence-model.md](references/evidence-model.md). For a system, repository, dataset pipeline, system paper, or paper-plus-code artifact, also read [system-coverage.md](references/system-coverage.md) and build its element, relationship, and state manifests.

For a large corpus, persist structured intermediate results instead of relying on conversation memory. Divide research by independent evidence lanes only, require locators and uncertainty from every lane, and keep synthesis under one owner.

For a stateful Standard or Deep document, materialize the field-level state manifest in a designated scratch or temporary area before drafting. Do not rely on prose memory to reconcile source fields.

### 3. Reconstruct genesis only when it serves the route

Read [reasoning-reconstruction.md](references/reasoning-reconstruction.md) for a paper, a research-oriented deep dive, or a project question about why a design arose.

Build the reasoning only from information available before the solution:

- problem and pressure;
- failure modes;
- constraints and invariants;
- prior mechanisms and available assets;
- observations that could trigger a different direction.

Generate plausible alternatives, explain why they fail, and derive the smallest insight that makes the final direction reasonable. Label this as evidence-based reconstruction unless a source states the author's reasoning.

Do not make genesis the center of a routine current-state refresh unless it changes the reader's current model.

### 4. Establish the concepts and complete static model

State the core idea in a falsifiable form:

> Given **constraint or failure**, the artifact changes **mechanism**, which should improve **observable outcome**, provided **critical assumption** holds.

Define required concepts before using them. Then explain the actual method or system.

For system-like artifacts:

- distinguish the material structural views, such as repository layout, dependency structure, runtime topology, and data or state flow; map them explicitly instead of treating one view as the whole architecture;
- establish the smallest runnable or meaningful unit before presenting the full system when that unit gives the reader a concrete mental model;
- use the element manifest to establish boundaries, ownership, control, data, state, asynchronous work, side effects, and failures;
- recursively expand every load-bearing element until reaching a declared primitive or external boundary;
- enumerate load-bearing state fields, value domains, owners, writers, legal transitions, persistence, and behavioral effects;
- identify the commit or transaction boundary of every multi-stage action, including whether failure rolls back or leaves partial state, output, side effects, or audit records;
- reconcile the source-derived field inventory, internal manifest, and published explanation in both directions; explain, validly group, or explicitly scope out every candidate field;
- explain important branches and cycles even when the representative example does not traverse them.

For non-runtime artifacts, expand assumptions, variables, representations, transformations, objectives, derivations, and experimental dependencies. Do not invent components or mutable state.

Keep graph and coverage terminology internal unless it is meaningful in the domain.

### 5. Run a representative example

After the static explanation is complete, choose a reproducible trace, source-backed case, or explicitly labelled constructed example.

For a stateful system, show:

**initial state → input or event → activated components → transferred values → decision or proposal → guard or validation → visible output and side effects → committed state → next-round effect**

Use actual in-scope names, interfaces, fields, values, and variables. For every step, identify the entry or trigger, input object, responsible component, important event or state change, output, and next destination when the evidence exposes them. Point each step back to a concept already explained. Keep one canonical full chain; later sections should deepen or link to it instead of narrating the same chain again. Add another example only when a critical branch, failure path, or feedback loop cannot otherwise be understood.

For mathematical content, define every symbol, derive the mechanism in small steps, and connect the derivation to the same example. Do not add reader exercises unless requested.

Use the smallest safe source-backed example. Do not expose secrets or sensitive source material.

### 6. Map claims to validation and critique

For every load-bearing claim, answer:

**question → experiment, test, or trace → result → justified conclusion → remaining uncertainty**

Explain what the evidence isolates and whether it supports causation, correlation, equivalence, or feasibility.

Read [attack-and-follow-up.md](references/attack-and-follow-up.md) for a paper, research deep dive, explicit critique, or follow-up request. Identify the weakest assumption, counterexample, one-week validation, and non-incremental follow-up there. Do not force those sections into a routine project overview or refresh.

### 7. Design the reader journey and visuals

Use the selected route in [document-archetypes.md](references/document-archetypes.md). Treat its content roles as an internal plan, not a default table of contents.

Read [visual-explanation.md](references/visual-explanation.md) when a spatial, stateful, temporal, comparative, or claim-to-evidence relationship is materially easier to understand visually.

Select each figure by one reader question. Build it from manifested, sourced elements. Render it in the target format, inspect the rendered result, and retain editable source when applicable.

### 8. Create, refresh, or organize the document set

Follow [operating-modes-and-lifecycle.md](references/operating-modes-and-lifecycle.md).

In Plan-only, return the exact proposed current document set, writes, archive moves, current-change contents, and verification steps without mutating files. In Apply, perform and verify the authorized changes.

- maintain one identifiable canonical current entry;
- respect the document-set budget in the lifecycle reference and justify every additional current topic document;
- create topic documents only for stable questions that need independent depth;
- update current documents in place when possible;
- when a load-bearing claim is corrected, find every parallel statement in the current entry, topic documents, and changed visuals; update it or make the remaining precedence explicit;
- preserve correct content, links, comments, assets, and stable paths;
- move only confirmed superseded documentation and exclusively owned visual assets into recoverable history;
- do not delete historical material or move raw source artifacts by default;
- leave ambiguous documents in place and report them;
- end every current document created or refreshed with a current-run change section.

### 9. Audit and deliver

Read [writing-and-review.md](references/writing-and-review.md).

Verify:

- artifact identity and current-versus-planned status;
- evidence class and source locator for every load-bearing claim;
- element and state coverage for the declared boundary;
- zero unaccounted in-scope state fields after reconciling source candidates with individually explained, validly grouped, and explicitly scoped-out fields;
- the actual Apply delta against the pre-run baseline and write/move allowlist, rather than against a dirty repository's HEAD alone;
- agreement between that actual delta and the final current-change record;
- consistency across the canonical entry, topic documents, structural explanation, representative example, and visuals;
- route-appropriate structure without leaked internal checklists;
- final current-change section;
- canonical and topic links;
- recoverable archive moves and untouched unrelated working-tree changes;
- rendered visual quality in the actual target format;
- final documents, visuals, examples, locators, and assets contain no secrets or material outside the intended audience's access boundary;
- final file set by reopening or reading back the delivered artifacts.

Report incomplete inspection, rendering, or coverage honestly.

## Maintain Evidence Boundaries

Use four classes:

1. **Artifact-explicit**: directly stated, implemented, or demonstrated by the target artifact.
2. **Externally established**: supported by primary external literature or official documentation.
3. **Evidence-based inference**: derived from cited premises but not explicitly stated.
4. **Uncertain**: missing, conflicting, stale, or unresolved.

Use unobtrusive labels such as `论文明确`, `源码显示`, `相关工作`, `推断`, or `尚不确定` where readers could confuse the classes. Keep internal ledgers out of the main narrative unless an appendix benefits the reader.

## Write With a Human Technical Voice

Prefer:

- claim → evidence → explanation → implication;
- specific nouns, verbs, fields, values, and outcomes;
- plain language for hard ideas;
- short paragraphs with one job;
- explicit uncertainty and tradeoffs.

Avoid:

- passive summaries and directory tours;
- generic importance or quality claims;
- repeated “不是……而是……” scaffolding;
- decorative quotation marks and em dashes;
- heading forests, checklist-shaped prose, and giant source dumps;
- invented motivations or unsupported novelty;
- planned work phrased as implemented behavior.

Use the requested qualities of strong first-principles technical communication without imitating a living writer's distinctive phrasing.

## Reference Map

- [operating-modes-and-lifecycle.md](references/operating-modes-and-lifecycle.md): Create, Refresh, Deep dive, Organize history, output contract, dirty worktree, archive safety, and current change record.
- [document-archetypes.md](references/document-archetypes.md): route-specific content requirements and reader journeys.
- [evidence-model.md](references/evidence-model.md): source hierarchy, research coverage, claim ledger, and evidence labels.
- [system-coverage.md](references/system-coverage.md): element, relationship, and state manifests with completeness gates.
- [reasoning-reconstruction.md](references/reasoning-reconstruction.md): disciplined zero-to-one idea and design reconstruction.
- [visual-explanation.md](references/visual-explanation.md): diagram selection, evidence rules, rendering, readback, and visual quality gates.
- [attack-and-follow-up.md](references/attack-and-follow-up.md): weakest assumption, counterexample, one-week validation, and follow-up research.
- [writing-and-review.md](references/writing-and-review.md): voice, structure, review passes, and delivery gates.
