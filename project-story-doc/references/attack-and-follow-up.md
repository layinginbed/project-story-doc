# Attack, Minimal Validation, and Follow-up

## Contents

- Find the weakest load-bearing assumption
- Design a counterexample
- Plan a one-week validation
- Generate a follow-up direction
- Report novelty honestly

## Find the weakest load-bearing assumption

List assumptions by layer:

- problem framing and user need;
- data coverage and distribution;
- representation or model mechanism;
- independence, stationarity, or causal interpretation;
- metric validity;
- baseline and comparison fairness;
- compute, latency, cost, and scaling;
- human behavior and operational adoption;
- reproducibility and implementation fidelity.

Rank each assumption on:

1. **centrality**: how much of the claim collapses if it fails;
2. **plausibility of failure**: whether realistic cases violate it;
3. **evidence deficit**: how weakly the artifact tests it.

Select the highest combined risk. Explain why it is more dangerous than the runners-up.

Use this failure chain:

> If **assumption** fails under **realistic condition**, then **mechanism** produces **specific error**, which degrades **observable outcome**. Existing evidence misses this because **coverage gap**.

## Design a counterexample

Target one central claim, not the entire artifact.

Specify:

- claim under attack;
- minimal input or environment;
- controlled variables;
- changed variable that isolates the assumption;
- baseline or comparison;
- predicted failure signature;
- metric and falsification threshold;
- what result would defend the original claim.

Prefer the smallest decisive case. A larger benchmark is not automatically a stronger attack.

Counterexample families:

- adversarial boundary case;
- distribution shift preserving superficial cues;
- two cases the mechanism maps together but should separate;
- same case with a nuisance factor changed;
- delayed or feedback-driven effect absent from offline evaluation;
- resource limit exposing hidden dependence;
- baseline strengthened with equal information and budget;
- metric gaming where score rises but desired behavior worsens.

## Plan a one-week validation

Choose one load-bearing claim with a result that can change belief.

Day-scale protocol:

1. Freeze artifact version and environment.
2. Reproduce one baseline and one target condition.
3. Use a small public or already available dataset or scenario set.
4. Define the metric, variance estimate, and pass/fail threshold before running.
5. Log inputs, configuration, seeds, outputs, failures, and cost.
6. Inspect a small qualitative slice to check metric validity.
7. End with one of: supported, contradicted, or inconclusive with the missing evidence named.

Do not promise full reproduction in a week. Optimize for information gain per unit effort.

## Generate a follow-up direction

Start from a failure, not from a fashionable method.

1. Name the unmet need.
2. Trace why the current mechanism cannot satisfy it without violating a constraint.
3. Identify the missing capability or representation.
4. Propose a different mechanism.
5. State a distinguishing prediction against the strongest current alternative.
6. Design the smallest experiment that could reject the idea.
7. Search current primary literature for direct precedents and adjacent mechanisms.

Reject ideas that only:

- use a larger model or dataset;
- add another loss term without a new causal story;
- apply the same method to a new domain;
- combine two named methods without explaining the missing capability;
- depend on unavailable labels or unrealistic infrastructure;
- cannot be distinguished empirically from an existing approach.

## Report novelty honestly

Use one of:

- **Directly precedented**: essentially present in prior work.
- **Adjacent**: components exist, but the proposed mechanism or problem framing differs.
- **Potentially novel**: no direct precedent found in the searched scope.
- **Novelty unverified**: literature coverage is insufficient.

Record search date, queries, and closest works. Never turn “not found” into “does not exist”.
