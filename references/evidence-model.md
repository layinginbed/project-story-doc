# Evidence Model

## Contents

- Four evidence classes
- Source hierarchy
- Artifact identity
- Research coverage manifest
- Claim ledger
- Final presentation
- Manage internal research artifacts

## Four evidence classes

| Class | Meaning | Minimum support | Allowed wording |
|---|---|---|---|
| Artifact-explicit | The target artifact states, implements, or demonstrates it | Exact page, section, file and line, trace event, test, issue, commit, or result locator | “论文声称…”, “源码实现…”, “该 trace 显示…” |
| Externally established | A primary external source supports it | Direct link or bibliographic locator plus version or date | “相关工作发现…”, “官方文档规定…” |
| Evidence-based inference | The conclusion follows from cited facts but is not stated directly | Premises, reasoning step, confidence, and at least one alternative explanation | “基于 A 与 B，可以推断…”, “一种合理解释是…” |
| Uncertain | Evidence is missing, conflicting, stale, or non-identifying | What is missing and how to verify it | “尚不确定…”, “需要通过 X 验证…” |

Do not use confidence words as a substitute for provenance. “Likely” without premises is still unsupported.

## Source hierarchy

Use the source closest to the behavior being claimed.

### Repository

1. Reproducible runtime trace or test
2. Executed code and configuration
3. Versioned interface or schema
4. Design record, issue, or commit history
5. Maintained documentation
6. Comments, names, or memory

### Project

1. Released artifact, accepted result, or measured outcome
2. Reproducible benchmark, trace, or test
3. Current implementation
4. Approved design or milestone record
5. Roadmap or proposal
6. Aspirational narrative

### Paper

1. Main paper, appendix, and supplement
2. Official code, data, and evaluation artifact
3. Cited primary related work
4. Author presentation or project page
5. Later secondary interpretation

When sources disagree, report the conflict and select wording supported by the strongest source. Do not silently merge versions.

For cross-tool, cross-framework, or prior-versus-current comparisons, align versions and observation dates before naming a difference. Recheck commodity capabilities against same-period primary sources. A feature that one artifact once lacked is not a durable differentiator unless the selected snapshots still support that claim.

## Artifact identity

Record enough information to reproduce the reading:

- repository root, worktree, branch, commit, dirty state;
- project release, milestone, dataset, model, environment, and date;
- paper title, venue or archive identifier, version, supplement, and code revision.

State when the artifact changes during the work.

## Research coverage manifest

Before writing, list the evidence areas that must be inspected:

| Area | Why it matters | Primary source | Status | Gaps |
|---|---|---|---|---|
| Problem and constraints | Defines the need | | pending / checked | |
| Genesis evidence | Supports reconstruction | | | |
| Core path | Explains behavior | | | |
| State and ownership | Prevents architecture blur | | | |
| Validation | Supports claims | | | |
| Failure boundary | Supports attack | | | |

This table controls research coverage; it does not prove structural completeness. For a project, repository, dataset pipeline, system paper, or paper-plus-code artifact, also build the element and state manifests defined in `system-coverage.md`.

For any phrase such as “N modules”, “all providers”, or “three stages”, enumerate and count directly from the relevant version. If exhaustive verification is not worth the cost, avoid the exact count.

## Claim ledger

Maintain this during research:

| ID | Claim | Class | Source locator | Confidence | Contradiction or alternative | Final wording |
|---|---|---|---|---|---|---|
| C1 | | artifact / external / inference / uncertain | | high / medium / low | | |

Rules:

- Give every load-bearing claim an ID.
- Split compound claims that rely on different evidence.
- Record negative evidence carefully; absence in inspected files is not proof of global absence.
- Separate “exists”, “enabled”, “used”, “works”, and “produces the claimed outcome”.
- Separate implemented, tested, deployed, planned, and paper-only status.
- Attach observed results to the exact configuration that produced them.

## Final presentation

Keep the ledger internal or place it in an appendix. In the narrative:

- cite factual claims near the sentence they support;
- label inference at the paragraph level when possible;
- mark unresolved claims at the point of use;
- avoid mixing multiple evidence classes in one sentence.

## Manage internal research artifacts

Do not scatter coverage manifests, claim ledgers, extraction notes, or temporary render files through the current documentation tree.

- For a small Brief or Standard task, keep them in memory or an isolated temporary working directory.
- For a large or Deep task, persist them in a run-specific temporary workspace identified by artifact snapshot.
- Use an existing project scratch convention only when it is clearly intended for generated working material.
- Create a project-resident resumable workspace only when the user requests resumability or the established project workflow requires it.
- Publish a ledger or manifest only when it materially helps the reader as an appendix or requested audit artifact.
- Remove only disposable working files created by the current run; never treat source evidence or prior user material as scratch.
