# Writing and Review Standard

## Contents

- Voice
- Paragraph pattern
- Density rules
- Structure rules
- Presentation forms
- Visual rules
- Style smells
- Review passes

## Voice

Aim for the qualities of strong first-principles technical writing:

- start from the real question;
- make each paragraph advance the argument;
- explain abstractions through one concrete case;
- use plain words for hard ideas;
- expose uncertainty and tradeoffs;
- allow a restrained first-person observation when it clarifies the reasoning.

Do not imitate a named living writer's exact voice, cadence, or signature phrases.

## Paragraph pattern

Use:

1. claim;
2. evidence or example;
3. mechanism-level explanation;
4. implication or boundary.

Not every paragraph needs four visible sentences, but each load-bearing paragraph should perform these jobs.

## Density rules

- Replace “很重要” with the user, metric, decision, or capability affected.
- Replace “效果很好” with the exact comparison and evaluation scope.
- Replace “设计合理” with the invariant, constraint, or failure it addresses.
- Replace “具有创新性” with the prior-work boundary and distinguishing mechanism.
- Split sentences that contain more than one evidence class.
- Use exact names only when they help the reader follow causality.
- Prefer one source-backed representative execution that reconnects previously explained components over many toy examples.

## Structure rules

- Design the reader journey before formatting.
- Teach in the order: concepts and boundaries, structural map, node and state expansion, representative execution, evidence and limitations.
- Use the selected artifact route and operating mode; do not expose the internal checklist as a universal table of contents.
- Draft genesis, system model, representative execution, and evidence before the executive summary.
- Keep headings as questions or argumentative steps, not taxonomy labels.
- Use tables for comparison or traceability, not long inventories.
- Keep load-bearing state fields and transition rules in the main explanation; put only secondary schemas, exhaustive file lists, and raw result tables in appendices.
- End major sections with one concrete takeaway or unresolved question.
- Connect sections causally: the next section should answer a question created by the previous one.

## Presentation forms

Choose the form by the information job:

- use prose for causality, reasoning, tradeoffs, and boundaries;
- use a table for repeated fields, exact mappings, state domains, or comparisons across shared dimensions;
- use a diagram for topology, sequence, ownership, feedback, or one-to-many relationships;
- use a compact card or callout for a definition, decision, warning, or current status that readers must retrieve quickly;
- use a linked appendix for exhaustive source locators, secondary schemas, and raw result detail.

When a table, diagram, or card replaces a prose block, remove the duplicate prose. Introduce the artifact with the question it answers and follow it with the implication or boundary the reader should retain.

## Visual rules

Create a visual only when it materially clarifies:

- an end-to-end sequence;
- state or ownership transitions;
- one source affecting several consumers;
- competing designs across repeated dimensions;
- claim-to-evidence relationships.

Give every visual a sentence title that states its conclusion. Keep nodes and labels readable. Do not repeat the same information in an adjacent table.

## Style smells

Revise when the draft contains:

- repeated “不是……而是……” constructions;
- decorative em dashes or quotation marks;
- generic section openings such as “随着技术快速发展”;
- claims about intent with no evidence;
- exact numbers with no locator;
- long code blocks used as explanation;
- a heading for every small fact;
- future plans phrased in the present tense;
- paper claims, code behavior, and observed results in one blended paragraph;
- limitations that could apply to any paper or system.

## Review passes

### 1. Truth pass

- Verify artifact identity and version.
- Check each concrete number, name, category, and status.
- Read back cited code or paper sections.
- Make each published source locator independently resolvable; do not rely on a reader inferring the file from a previous bullet or sentence.
- Search the current entry, topic documents, and changed visuals for stale parallel versions of every corrected load-bearing claim.
- Resolve or surface contradictions.

### 2. Evidence-class pass

- Mark artifact-explicit, external, inferred, and uncertain claims.
- Ensure inference contains premises and alternatives.
- Ensure “not found” is scoped to the inspected evidence.
- Separate exists, enabled, used, validated, deployed, and successful.

### 3. Causal-story pass

- Confirm the problem leads to the reconstructed design pressure.
- Confirm the core mechanism predicts the reported outcome.
- Confirm every load-bearing element in the manifest is expanded, linked, or explicitly scoped out.
- Confirm important state fields have concrete value domains, owners, writers, transition rules, behavioral consequences, and evidence.
- Confirm value domains preserve distinctions among schema acceptance, mutation acceptance, serialization or commit, downstream coercion, and final-output validation when those layers differ.
- Confirm the internal field accounting has exact paths and zero unaccounted in-scope candidates; a field mentioned only inside an example is not yet fully accounted for.
- Confirm the representative execution starts from an explicit state snapshot and ends with committed state and next-cycle consequences.
- Confirm optional fields or stages are not presented as universal, and cover the material path when each is absent.
- Confirm a prompt, intermediate representation, budget, or requested limit is not phrased as an enforced output postcondition without a post-validator.
- Confirm every multi-stage action states its real commit boundary and whether a failure rolls back, leaves partial state or audit records, or loses uncommitted evidence.
- Confirm the representative execution uses concepts already introduced instead of hiding new machinery inside the example.
- Confirm each validation isolates the question it claims to answer.
- Remove sections that do not change the reader's model.

### 4. Conditional attack pass

- Run this pass only for a paper, research deep dive, explicit critique, or follow-up request.
- Verify the weakest assumption is load-bearing.
- Verify the counterexample changes one decisive factor.
- Include a metric and falsification threshold.
- Ensure the follow-up fixes the failure through a distinct mechanism.

### 5. Reader pass

- The first screen resets context in under two minutes.
- A five-minute reader can leave with the essence, evidence, and boundary.
- A deep reader can trace every important claim to a source.
- Terms are defined before use, without front-loading a glossary.
- Required terms form a connected dependency or causal model rather than isolated definitions.
- A smallest runnable or meaningful unit appears before the full system when it materially lowers the prerequisite burden.
- The structural explanation remains complete even when the representative execution traverses only one path.
- Physical layout, dependency structure, runtime topology, and data or state flow are not conflated when more than one view matters.
- One section owns the complete end-to-end chain; other sections deepen it without repeating or contradicting it.
- Examples, diagrams, and tables each perform a unique job.
- No reader exercise is added unless the user requests one.

### 6. Delivery pass

- For a heavily revised document set, confirm that structure and teaching order, terminology, and redundancy or gaps were audited before the final edit map.
- Confirm the canonical entry and current topic set match the output contract.
- Confirm the current topic set stays within the document-set budget or records a concrete justification for every exception.
- Confirm the final section of every created or refreshed current document records the current run's changes.
- Confirm archived files were in scope, were unambiguously superseded, remain recoverable, and left no broken links.
- Confirm dirty-working-tree changes are labelled and were not silently cleaned, overwritten, or represented as released behavior.
- Compare the final Apply delta with the pre-run baseline and declared write/move allowlist; do not use total dirty status as a proxy for this run's changes.
- Confirm the final current-change record matches the attributable file and content delta.
- Check final prose, visuals, examples, locators, and assets for secrets or material outside the intended audience's access boundary.
- Preserve links, comments, and embedded resources when editing an existing document.
- Validate generated Markdown, rich-document markup, citations, and cross-references.
- Render every changed visual in the target format and inspect it at normal reading size and its full aspect ratio or actual embedded container, not only as a thumbnail.
- Re-open or fetch the final artifact after writing.
- Report incomplete verification honestly.
