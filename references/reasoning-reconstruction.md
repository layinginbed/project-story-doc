# Reconstructing the Zero-to-One Path

## Goal

Teach how an idea or design could be generated from prior knowledge. This is a constrained reconstruction, not biography and not mind-reading.

## Freeze the information boundary

Choose a cutoff immediately before the target idea, commit, architecture, or paper contribution. Build the first pass without using:

- the final method name;
- the finished module decomposition;
- the paper's contribution list;
- downstream benchmark results;
- post-hoc explanations that depend on success.

Later compare the reconstruction with the artifact and clearly label the comparison.

## Build the pre-solution packet

Collect six inputs:

1. **Pressure**: What user, scientific, operational, or economic outcome is failing?
2. **Failure modes**: What breaks in concrete cases? Avoid generic “performance is limited”.
3. **Constraints**: What cannot be changed? Include budget, data, latency, safety, compatibility, and evaluation constraints.
4. **Available mechanisms**: Which prior techniques, components, or abstractions already exist?
5. **Observations**: Which repeated anomaly, asymmetry, or invariant could trigger a new idea?
6. **Success test**: What observation would show the problem is actually reduced?

Every item needs a source locator or an inference label.

## Simulate the search, not the answer

Generate three to five candidate moves from the packet. They should be plausible at the cutoff, including at least one simple baseline.

For each candidate, ask:

- Which failure mode does it target?
- Which constraint does it violate?
- What new assumption does it introduce?
- What evidence would distinguish it from the alternatives?

Eliminate candidates with explicit reasons. The goal is not to pretend the authors considered these exact options; the goal is to make the design pressure legible.

## Derive the decisive insight

Express the smallest useful leap:

> Because **observation** persists under **constraint**, move **responsibility or representation** from **old mechanism** to **new mechanism**, then test **distinguishing prediction**.

If the insight cannot produce a distinguishing prediction, it is probably a slogan rather than a mechanism.

## Compare with the actual artifact

After the reconstruction is complete:

1. reveal the actual method or architecture;
2. identify where it matches the reconstructed direction;
3. identify surprising choices not implied by the prior packet;
4. trace those choices to explicit evidence when available;
5. label remaining motivation as inference or unknown.

Use wording such as:

- “从当时可见的约束出发，一条合理路径是…”
- “论文没有陈述这段推导；以下是基于 A、B、C 的重建。”
- “提交历史支持其中两步，第三步仍是推断。”

Avoid:

- “作者一定是这样想到的”;
- using the final architecture to justify why the final architecture was inevitable;
- presenting one clean path when evidence suggests trial and error;
- inventing inspiration from naming similarity alone.

## Artifact-specific evidence

### Project or repository

Prefer design records, issue threads, commit history, reverted attempts, tests added with fixes, performance traces, and migration constraints. Current code explains what survived, not necessarily why it was first chosen.

### Paper

Prefer cited prior work, problem formulation, motivating examples, ablations, appendix notes, and author statements. Related work establishes the idea space; experiments cannot be used as pre-idea evidence.

### Hybrid

Reconstruct the scientific idea and the engineering realization separately. The implementation may introduce constraints and insights absent from the paper.

## Quality test

Remove the final method name from the section. A good reconstruction should still lead a technically informed reader toward the same class of solution while leaving room for alternatives.
