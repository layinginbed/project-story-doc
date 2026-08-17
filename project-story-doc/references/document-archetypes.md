# Artifact Routes and Reader Journeys

## Contents

- Use content roles, not a universal table of contents
- Compose routes when the artifact spans them
- Project current-state document
- Repository explanation
- Paper introduction
- Paper plus code
- Layer by reading time

## Use content roles, not a universal table of contents

Treat the following as internal content roles:

- orientation and version boundary;
- problem, value, and prior state;
- idea or design genesis when it helps the reader;
- core intuition;
- system, method, or theory;
- element and state expansion where applicable;
- representative example;
- evidence and validation;
- limitations and uncertainty;
- attack, minimal validation, and next direction when the route requires them;
- provenance and current change record.

Do not turn this list into default headings. Select and order roles around the reader's question. Combine adjacent roles, rename headings in domain language, and omit optional roles deliberately.

Keep a teaching dependency:

**define concepts → establish structure or method → expand the important parts → run a concrete example → judge the evidence**

Place the representative example after the reader has enough static understanding to follow it. Use it to reconnect prior explanations, not to hide missing coverage.

Identify the reader's minimum missing prerequisites before choosing the opening. Teach required terms as a connected dependency or causal chain, not as an alphabetical glossary. When a small runnable or meaningful unit exposes the system's essential nouns and contracts, explain that unit after the prerequisites and before the full architecture. Mark exhaustive source tables and secondary schemas as optional reference material so they do not block the main teaching path.

## Compose routes when the artifact spans them

Choose one primary route to determine the reader journey, then add the minimum secondary route needed for complete understanding.

- For a living software project, use Project for current goals, status, decisions, and document ownership; use Repository for runtime, state, interfaces, tests, and source navigation.
- For a research repository, use Paper for the scientific question and mechanism; use Repository for the released implementation and execution boundary.
- For paper plus code, use the dedicated three-layer claim, implementation, and observed-reproduction model.

Do not duplicate the same background, status table, or mechanism explanation across route sections. Let the canonical entry own shared context and link to deeper route-specific topics.

## Project current-state document

Make the present project model the center. Require:

1. current identity, scope, and source snapshot;
2. problem, users, and measurable value;
3. current deliverables and status separated into implemented, tested, deployed, adopted, planned, blocked, and uncertain as applicable;
4. domain concepts and the current technical structure;
5. load-bearing decisions, state, boundaries, and dependencies;
6. one representative execution or usage example when the project has runtime behavior;
7. evidence, known limitations, and open decisions;
8. links to current topic documents;
9. the current change record as the final section when creating or refreshing files.

Add idea genesis, rejected alternatives, weakest assumptions, counterexamples, or a one-week validation when they materially improve a research or design decision. Do not force them into a routine status refresh.

Avoid a chronological work log. Explain time only when it changes current status, invalidates an old belief, or justifies a decision.

## Repository explanation

Make executable behavior and ownership the center. Require:

1. repository identity, revision, working-tree boundary, and user-visible purpose;
2. entry points and configuration that select behavior;
3. actual structure, including control, data, state, side effects, asynchronous work, and external boundaries;
4. element-level and field-level coverage for the declared scope;
5. one source-backed execution from a user-visible input to output and committed state;
6. tests, traces, benchmarks, failure handling, and unvalidated behavior;
7. a small navigation map from explained concepts to source locations;
8. the current change record as the final section when creating or refreshing files.

Separate structural views that answer different questions:

- repository layout: where source and assets live;
- build or dependency structure: which modules depend on which contracts;
- runtime topology: which instances exist and who owns their lifetime;
- control, data, and state flow: what moves or changes during execution.

Use only the views that materially affect the reader's model. State the mapping between views. Never infer runtime ownership or call order from directory nesting alone.

Explain:

- who owns each decision, state mutation, policy, and side effect;
- what each important interface transfers and guarantees;
- what is synchronous, asynchronous, cached, persisted, retried, or atomic;
- which branches and failure paths the representative execution does not traverse;
- which current behavior differs from design documents or comments.

Maintain one canonical end-to-end execution from external entry and selected configuration through construction, runtime work, visible output, persistence or commit, and shutdown or next-cycle behavior. At each material step, identify the trigger or function, input object, called component, event or state mutation, output, and next destination when source evidence exposes them. Other sections should explain one mechanism, branch, or boundary and link back to this chain instead of repeating it in full.

Do not use the directory tree as the narrative. Do not present generic graph terminology when project language is clearer.

## Paper introduction

For a deep research reading, preserve this reasoning sequence:

1. research question, background, importance, and value;
2. prior solutions and their concrete insufficiency;
3. evidence-based reconstruction of the pre-contribution reasoning path;
4. concise intuition;
5. method or theory, with all required concepts and variables;
6. a real input–process–output example after the method is established;
7. mathematical derivation and prerequisites when material;
8. experiments as question → design → answer;
9. takeaways and evidence boundary;
10. weakest assumption;
11. one-week minimal reproduction and a counterexample;
12. literature-checked follow-up direction.

Compress or omit items 10–12 only for a brief orientation or when the user explicitly excludes research critique.

Do not force runtime components, mutable state, or an architecture graph onto a theoretical artifact. Expand assumptions, variables, representations, transformations, objectives, and experimental dependencies instead.

Separate what the paper states from what its results justify. Explain whether each experiment tests the full claim, one mechanism, or only feasibility.

## Paper plus code

Keep three synchronized but distinct models:

1. paper claim and paper evidence;
2. released code realization and configuration;
3. observed reproduction status.

Use a claim-to-implementation matrix:

| Claim ID | Paper mechanism and evidence | Code path and approximation | Run status | Gap |
|---|---|---|---|---|
| | | | not run / partial / reproduced / contradicted | |

Require:

- the paper reasoning and method needed to understand the claim;
- the concrete code path implementing or approximating it;
- configuration and default differences from reported experiments;
- data, checkpoint, metric, and evaluation boundaries;
- one example that links paper variables to actual code inputs, transformations, and outputs;
- explicit gaps where released artifacts cannot support the paper claim.

Do not let code existence count as reproduction and do not let a paper diagram count as current code behavior.

## Layer by reading time

### Five-minute layer

- current identity and one-sentence essence;
- why the artifact exists;
- one structural or method map when useful;
- central evidence;
- one important boundary.

### Thirty-minute layer

- necessary genesis or prior-state reasoning;
- load-bearing structure, state, method, or theory;
- one representative example;
- claim-to-evidence summary;
- current limitations.

### Reference layer

- exact source locators;
- element and claim manifests;
- field-level state or schema details;
- mathematical derivations;
- extended tests, experiments, and reproduction protocol;
- historical decisions and unresolved questions.
