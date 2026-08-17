# System and Method Coverage

## Contents

- Define the explanation boundary
- Identify load-bearing elements
- Build the element manifest
- Separate and map system views
- Expand state completely
- Reconcile source fields, manifest, and explanation
- Adapt the model to non-runtime artifacts
- Enforce coverage gates
- Translate analysis into reader language

## Define the explanation boundary

Build an internal explanation graph rooted in the reader's question. Use it to control completeness; do not expose graph-analysis jargon in the final document unless it is a domain concept.

Start from:

- the user-visible outcome or research claim;
- the mechanisms required to produce it;
- the state, information, and decisions those mechanisms depend on;
- the evidence needed to distinguish claimed, implemented, and observed behavior.

Stop recursive expansion at:

- a standard primitive the target reader already understands;
- a stable external boundary whose internals are out of scope;
- a leaf that cannot change the explained outcome, invariant, state, or failure;
- an explicitly declared uninspected boundary.

Do not treat the repository tree as the explanation boundary. Include only files and modules that realize an in-scope element, but include every in-scope element even when it is absent from the representative execution.

## Identify load-bearing elements

Treat an element as load-bearing when at least one is true:

- removing or changing it alters the central outcome or claim;
- it owns a decision, policy, state mutation, side effect, or validation boundary;
- it transfers information across a stable or risky interface;
- it enforces an invariant or creates a major failure mode;
- it is needed to explain why the representative execution behaves as shown;
- it distinguishes current implementation from a prior, planned, or paper-only design.

Classify elements as:

- concept or domain entity;
- component or method stage;
- external boundary;
- control or data transfer;
- state container, state field, or transition;
- invariant, guard, or failure path;
- observable output or side effect;
- claim, experiment, or evaluation dependency.

## Build the element manifest

Create this internal manifest before drafting:

| ID | Domain name | Type | Why load-bearing | Source locator | Status | Explained at | Gap |
|---|---|---|---|---|---|---|---|
| E1 | | component / edge / state / transition / boundary / claim | | | implemented / planned / paper-only / observed / uncertain | section or linked topic | |

Rules:

- give every element shown in a structural visual an ID;
- add elements discovered while tracing code, state, experiments, or a real execution;
- split elements that have different owners, evidence, or implementation status;
- record contradictions rather than selecting a convenient version;
- map every included element to a final section or explicitly mark it out of scope;
- do not call coverage complete while any load-bearing element remains `pending` or has an unexplained gap.

Use a separate relationship list when the manifest cannot express the important contracts:

| From | To | Relationship | Payload or condition | Ordering or transition rule | Evidence |
|---|---|---|---|---|---|
| | | control / data / mutation / validation / temporal | | | |

For a multi-stage action, record its actual commit unit. One user-visible step may append several events or side effects. State whether an intermediate failure rolls back, leaves a partial trace, preserves a prior mutation, or loses locally collected evidence.

## Separate and map system views

Do not collapse different structures into one architecture diagram or explanation. Consider these views independently:

| View | Primary question | Common evidence |
|---|---|---|
| Physical | Where does the implementation live? | repository tree, packages, generated assets |
| Dependency | What can reference, provide, or extend what? | imports, interfaces, build graph, registration |
| Runtime | What instances exist, who creates them, and who owns their lifetime? | constructors, bootstrap code, traces, shutdown paths |
| Control | Who triggers the next action or decision? | calls, events, schedulers, callbacks |
| Data and state | What values cross boundaries or persist? | schemas, messages, mutations, stores, checkpoints |

Select only material views. Map an element's identity across selected views when names or boundaries differ. Record conflicts instead of deriving runtime topology from the physical tree or dependency direction from a runtime trace.

Before the complete topology, identify the smallest runnable or meaningful unit that preserves the essential contracts. Use it as a teaching bridge, not as a substitute for full coverage.

For the representative execution, keep one canonical chain. Record each material step as:

| Step | Trigger or entry | Input object | Responsible component | Event or state change | Output | Next destination | Evidence |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

The final document may render this as prose, a table, or a diagram. The internal form prevents the narrative from skipping data, ownership, or state changes. Do not publish duplicate complete chains in several sections.

## Expand state completely

For every load-bearing state container, create a field-level inventory:

| Container | Field | Meaning | Type or value domain | Initial value | Writer | Transition or guard | Persistence | Behavioral effect | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Check:

- owner and permitted writers;
- enum values, ranges, units, shapes, nullability, and sentinel meanings;
- conditional presence and the alternative paths taken when an optional field, stage, payload, or reader is absent;
- constraints at construction, mutation, serialization or commit, downstream coercion, and output validation; acceptance at one layer does not imply acceptance at the next;
- initialization, defaulting, migration, reset, rollback, and commit behavior;
- transaction or commit granularity, including partial-failure behavior;
- legal and illegal transitions;
- derived versus stored fields;
- downstream branches controlled by each value;
- whether a value changes enforced behavior, only changes an intermediate representation or prompt, or has no current reader;
- current code, configuration, schema, and documentation disagreements.

Keep load-bearing fields and value domains in the main teaching path. Put mechanically exhaustive secondary schemas in a linked reference or appendix.

## Reconcile source fields, manifest, and explanation

Derive candidate fields independently from constructors and reset defaults, schema or model declarations, serialized state and event forms, mutation APIs, migrations, configuration, and tests. Do not build the inventory only from an existing document or the representative happy path.

Distinguish:

- a domain enforced by schema or runtime validation;
- an intended semantic domain stated only in documentation;
- values merely observed in fixtures or traces;
- a default that the current implementation does not continue to enforce.

If a mutation or deserializer accepts a wider domain than the concept suggests, state the implemented boundary rather than silently documenting the intended one.

Treat a value domain as a layered contract when the layers differ: schema or constructor acceptance, mutation acceptance, serialization and commit requirements, downstream reader coercion, and final-output validation. Do not collapse “accepted initially,” “persists successfully,” and “produces the intended behavior” into one domain.

When a stage or field is optional, enumerate each material path and its condition. Do not present the richer path as universal merely because the built-in happy path uses it.

Before drafting and again before delivery, reconcile:

**source-derived candidate fields ↔ internal state manifest ↔ published explanation**

Every candidate must be:

- explained individually;
- grouped only with fields that truly share owner, domain, transition, persistence, and behavioral effect; or
- explicitly scoped out with a reason and locator.

Stable metadata still counts as load-bearing when it controls initialization, identity, visibility, branching, reproducibility, or an invariant. Do not omit it merely because it never changes after reset.

At Standard depth, group only genuinely shared contracts and expose material differences. At Deep depth, list every in-scope field separately.

Keep an explicit accounting row or summary in the internal manifest:

```text
in-scope source candidates
= individually explained
+ validly grouped under a shared contract
+ explicitly scoped out with reason and locator

unaccounted = 0
```

Use exact field paths in this reconciliation. A mention of an initial value in the representative example does not by itself account for the stored field, its persistence, or its later readers.

## Adapt the model to non-runtime artifacts

Do not invent components or mutable state for an artifact that does not have them.

For a theoretical or method paper, map:

- assumptions and definitions;
- representations and variables;
- transformations or derivation steps;
- objectives and constraints;
- predictions and experimental dependencies.

For a dataset or benchmark, map:

- source populations and filters;
- construction and annotation stages;
- schemas and labels;
- splits, leakage boundaries, and metrics;
- consumers and claimed uses.

For paper plus code, keep the paper mechanism, code realization, and observed reproduction as separate element statuses. Link them through claim identifiers rather than treating the implementation as proof of the paper claim.

## Enforce coverage gates

Before delivery, verify:

1. every load-bearing concept, component, boundary, relationship, state field, transition, and claim is present in the manifest;
2. every structural visual element maps to the manifest and a source;
3. every manifest element is explained, linked to a topic document, or explicitly scoped out;
4. every in-scope source-derived candidate field is accounted for by the manifest, including stable initialization and identity fields;
5. every load-bearing state field has an enforced or explicitly unenforced layered value domain, owner, transition rule, persistence, and behavioral effect;
6. the internal field accounting reports zero unaccounted candidates;
7. the representative execution reuses manifested elements and exact state values;
8. optional stages and fields have their material present and absent paths explained;
9. parameters, prompts, or intermediate limits are not described as enforced output postconditions without a validator;
10. every multi-stage action identifies what is atomic, what can remain committed after failure, and what is never persisted;
11. critical branches, failure paths, and cycles not traversed by the example are still explained;
12. implemented, planned, paper-only, observed, and uncertain status remain distinct;
13. the canonical entry and topic documents collectively cover the declared explanation boundary;
14. each selected structural view has a stated question and evidence, and mappings between views do not imply unsupported ownership or order;
15. the document has one canonical complete execution chain, while later explanations deepen it without creating conflicting copies.

Report incomplete coverage honestly. Do not reduce the manifest after drafting merely to make the document appear complete.

## Translate analysis into reader language

Use the manifest as an internal control surface. In the final document:

- name real components, concepts, fields, and decisions;
- organize around reader questions and causal relationships;
- avoid headings such as “node inventory” or “edge coverage” unless the domain uses those terms;
- explain small leaf elements inline and reserve sections for concepts that need sustained reasoning;
- use a concrete execution after the static explanation to reconnect the elements.
