# Visual Explanation

Use diagrams as teaching instruments. Create one only when it makes an important relationship materially easier to understand than prose.

## Select by reader question

| Reader question | Preferred visual |
|---|---|
| What is inside the system and where are its boundaries? | Context or component map |
| How do information and control move? | Flow or data-flow diagram |
| Which values can state take and how may they change? | State diagram |
| In what order do components cooperate? | Sequence diagram |
| How does one concrete run change state? | Sequence or trace with before-and-after state snapshots |
| How do current implementation and future design differ? | Layered comparison with an explicit status legend |
| How do paper claims, code paths, and experiments correspond? | Claim-to-evidence map |

Do not expose internal graph-analysis language by default. Draw the real relationships using domain names. Name a topology as a DAG, cyclic graph, or state machine only when that classification affects behavior or is already a meaningful project concept.

## Use a teaching hierarchy

For a deep system explanation, consider three levels:

1. an overview that establishes boundaries, ownership, and major relationships;
2. a focused mechanism or state view that expands the part carrying the behavior;
3. a representative execution that shows those previously explained parts operating together.

This is a selection heuristic, not a quota. Omit a level when prose is clearer. Add another focused view when a critical branch, failure path, or feedback loop would otherwise remain hidden.

Prefer an overview plus readable drill-downs over one exhaustive but illegible graph. Do not force every field or leaf component into the overview.

## Ground every visual in evidence

- Use real component, interface, state-field, enum, and experiment names when they improve understanding.
- Verify every node, arrow, transition, label, and status against a source locator.
- Do not infer direction, ownership, ordering, or causation from layout alone.
- Mark implemented, planned, paper-only, externally established, and uncertain elements with distinguishable styles and a legend.
- Do not merge passed or validated evidence with a merely present, frozen, configured, or blocked artifact in one status style. Subdivide the visual or use a neutral artifact style with explicit per-item status.
- Place the relevant version, revision, or evidence note in the caption or nearby prose when the figure could become stale.
- Update or archive stale diagrams together with the document that contains them.

Treat arrows as claims. A control arrow, data transfer, state mutation, and temporal transition are different statements; do not represent them with one unexplained style.

## Make the figure teach

- Give each figure one primary question and a sentence title that states its takeaway.
- Use domain nouns rather than `Node A`, `Module B`, or generic graph terminology.
- Keep labels short; explain causes, tradeoffs, and exceptions in nearby prose.
- Use consistent shapes, colors, line styles, and direction within one document.
- Keep text readable at the document's normal viewing size.
- Do not repeat the figure line by line in prose. Explain why the depicted relationship matters.
- Keep exhaustive secondary schemas and navigation maps out of the main teaching flow.

For a representative execution, show:

**initial state → triggering input → activated components → transferred values → decision or proposal → validation or guard → visible output → committed state → next-round effect**

Reuse concepts and state fields already defined in the document. Do not introduce unexplained machinery only inside the figure.

## Choose an editable format

- Prefer Mermaid for repository Markdown when the renderer supports it.
- Use flowcharts for structure or flow, state diagrams for value transitions, and sequence diagrams for concrete execution order.
- When the target format cannot render Mermaid reliably, produce SVG or PNG and retain the editable source beside the document assets.
- Prefer deterministic vector diagrams for text-heavy technical figures. Do not use generative image models when exact labels, arrows, or state values are load-bearing.
- Follow the target document's format-specific workflow for Feishu, DOCX, PDF, slides, wiki pages, or other rich artifacts.

## Render and read back

Do not validate a visual only by reading its source.

1. Write the editable visual source from the evidence-backed element manifest.
2. Validate diagram syntax with the available renderer or parser.
3. Render or insert the figure in the actual target format.
4. Inspect the rendered result at normal reading size.
5. Inspect the full intrinsic aspect ratio or the real embedded container, not only a square thumbnail. If a preview crops the figure, distinguish viewer cropping from an asset whose own bounds are wrong.
6. Check clipped text, overlapping edges, ambiguous arrow direction, contrast, legend use, and current-versus-planned styling.
7. Verify captions, alt text when supported, asset paths, document links, and source-to-rendered-file correspondence.
8. Record the renderer or target surface and the readback result in the delivery report; keep temporary render artifacts outside the maintained document set.
9. Re-render and inspect after any source, label, layout, or document-format change.

For a rich or remote document, fetch or reopen the delivered artifact and inspect the figure in place. For Markdown, verify that the target renderer supports the chosen Mermaid syntax; otherwise deliver a rendered asset and retain its source.

If rendering or visual inspection is unavailable, state that the figure is source-validated only. Do not claim visual verification.

## Review before delivery

Reject or revise a visual when:

- it contains an unsupported relationship;
- it mixes current and planned behavior without a legend;
- it is readable only when heavily zoomed;
- it duplicates adjacent prose without adding structure;
- its title merely names the diagram instead of stating a conclusion;
- a reader can follow the happy path but cannot tell where state is owned or changed;
- the example path is mistaken for complete system coverage;
- the editable source, rendered asset, and embedded document version disagree;
- changed or archived documents leave broken figure links.
