# Operating Modes and Document Lifecycle

## Contents

- Select an operating mode
- Select an execution posture
- Discover the current document set
- Apply the output contract
- Set a document-set budget
- Freeze the source snapshot
- Isolate the Apply delta
- Create or refresh documents
- Organize historical material safely
- Write the current change record
- Verify delivery

## Select an operating mode

Choose one primary mode. Combine modes only when the request clearly requires it.

| Mode | Use when | Primary result |
|---|---|---|
| Create | No trustworthy current explanation exists | Establish one canonical entry document and only the necessary topic documents |
| Refresh | Existing explanations may lag behind the artifact | Update current documents against a frozen source snapshot and record the present delta |
| Deep dive | One subsystem, mechanism, experiment, or research question needs full treatment | Create or update one linked topic document without duplicating the overview |
| Organize history | Current and obsolete documents are mixed together | Keep current documents in the main area and move confirmed superseded documents into a recoverable history area |

Treat “write an introduction” as Create when no current document exists and as Refresh when one does. Treat “bring me up to date” as Refresh. Treat “clean up old docs” as Organize history, normally combined with Refresh.

## Select an execution posture

Keep intent separate from side effects:

| Posture | Behavior |
|---|---|
| Plan-only | Inspect, classify, compare, and return exact proposed writes and moves; do not modify the document set |
| Apply | Perform the requested writes and in-scope archive moves, then run delivery verification |

Use Plan-only for review, audit, diagnosis, or planning. Use Apply for an explicit create, update, refresh, rewrite, or cleanup request. A mode name does not itself authorize mutation when the request is read-only.

In Plan-only, show the intended canonical document, topic set, archive candidates, change-record contents, unresolved ambiguities, and verification plan. Do not claim that files were refreshed or archived.

## Discover the current document set

Inspect before writing:

1. repository or project documentation conventions;
2. candidate entry documents and topic documents;
3. links between documents and from code or configuration;
4. existing history, archive, assets, generated sites, or published copies;
5. version control state and recent document changes;
6. raw sources that must not be mistaken for authored documentation.

Classify each candidate:

| Class | Meaning | Default action |
|---|---|---|
| Canonical current | The present entry point for the reader | Update in place |
| Current supporting | A still-valid topic or reference document | Keep and link |
| Superseded | Replaced by a newer current explanation | Archive when the scope authorizes organization |
| Historical evidence | Useful for understanding past decisions | Keep in history; do not rewrite as current truth |
| Raw source | Paper, dataset, source code, configuration, trace, or externally supplied artifact | Preserve in place unless explicitly asked otherwise |
| Uncertain | Currency or ownership cannot be established | Leave in place and report the ambiguity |

Do not infer authority from filenames such as `final`, `new`, or `v2`. Prefer inbound links, current code references, version history, recent maintenance, and agreement with the frozen artifact.

## Apply the output contract

Preserve an existing coherent documentation layout. When none exists, use the smallest suitable structure:

```text
docs/
├── overview.md
├── topics/
├── assets/
└── history/
    └── YYYY-MM-DD/
```

Adapt names and language to the project. Do not create empty directories.

Maintain:

- one canonical entry document for the current reader model;
- topic documents only when a subsystem or research question cannot be explained cleanly in the entry document;
- links from the entry document to every current topic document;
- editable visual sources beside or predictably linked to rendered assets;
- historical material outside the main current reading path.

Do not split documents by arbitrary chapter count or by one runtime path. Split when a topic has a stable reader question, independent evidence boundary, substantial detail, and a reason to evolve separately.

For specialized formats, keep responsibilities separate:

| Stage | Owner |
|---|---|
| Faithful extraction from PDF, rich document, slide deck, or other source format | Format-specific reader |
| Evidence model, coverage, reader journey, and lifecycle decision | This Skill |
| Native editing, comments, embedded resources, and stable object preservation | Format-specific writer |
| Render, reopen or fetch, and visual acceptance | Format-specific verifier |

Do not flatten a rich document into plain text when the task requires preserving its native structure.

## Set a document-set budget

Use a budget to prevent a documentation refresh from creating a new navigation problem.

| Mode | Default maximum new current narrative documents | Normal behavior |
|---|---:|---|
| Create | 2 | One canonical entry and, only when justified, one topic document |
| Refresh | 0 | Update the current set in place |
| Deep dive | 1 | One focused topic document, linked from the current entry when in scope |
| Organize history | 0 | Move confirmed superseded material; do not create replacement documents unless combined with Create or Refresh |

The budget is a default, not a hard correctness limit. Exceed it only when every additional document has:

- one stable reader question that is difficult to answer cleanly in the entry document;
- an independent evidence or ownership boundary;
- enough depth to justify separate navigation;
- a credible reason to evolve separately;
- a clear inbound link and no duplicated canonical explanation.

Record the justification in the internal output contract. Diagrams and their editable assets do not count as narrative documents. Internal manifests, ledgers, and render files belong in scratch space and do not count as delivered current documents.

## Freeze the source snapshot

Record:

- artifact path and identity;
- branch, commit, release, paper version, or date cutoff;
- clean or dirty working-tree state;
- whether uncommitted changes are included;
- inspected source and document scope.

For a request about the “current local project,” include relevant working-tree changes by default, label the snapshot as dirty, and distinguish them from committed or released behavior. For a request about a release, paper result, or reproducible baseline, freeze the corresponding revision and do not silently include later working-tree behavior.

Never clean, reset, stash, overwrite, or otherwise normalize a dirty working tree merely to simplify documentation. Preserve unrelated user changes.

If the artifact changes during the run, either refreeze and recheck affected claims or finish against the original snapshot and state that boundary.

## Isolate the Apply delta

Before writing or moving files:

1. record the pre-run version-control status and candidate file set;
2. declare the exact intended write and move paths;
3. preserve a comparison basis for pre-existing dirty files in or near that scope, using hashes, a temporary manifest, a safe snapshot, or an equivalent read-only method;
4. keep baseline evidence outside the current document set unless the project already has a designated scratch area.

After Apply:

1. compare the final tree with the pre-run baseline, not only with repository HEAD;
2. separate the total dirty worktree from files changed by this run;
3. reject or investigate every run-attributable path outside the declared allowlist;
4. verify that files claimed as untouched are byte-identical or otherwise unchanged;
5. reconcile the actual run delta with the current change record and delivery report.

Raw `git status` or an equivalent total-status view cannot attribute a pre-existing modification to this run. Do not report an unrelated user change as a Skill mutation, and do not claim preservation without a baseline comparison.

## Create or refresh documents

### Create

1. Build the evidence and coverage artifacts before choosing headings.
2. Create the canonical entry document in the existing documentation area.
3. Create only topic documents justified by the output contract.
4. Add current links and visuals.
5. End each created current document with the current change record.

### Refresh

1. Read the existing current documents before drafting replacements.
2. When the current set has accumulated substantial edits, audit structure and teaching order, terminology consistency, and redundancy or gaps before choosing local changes.
3. Combine those findings into one edit map with one canonical owner for each explanation. Do not let independent edits create competing versions of the same claim.
4. Compare every load-bearing claim, status statement, structural element, state definition, example, visual, and source locator with the frozen artifact.
5. Preserve correct explanations, useful links, comments, embedded resources, and stable paths.
6. Rewrite stale passages rather than layering corrections around them.
7. Remove obsolete claims from the current narrative; preserve meaningful history through version control or the history area.
8. Update topic links, visuals, and cross-references.
9. For every corrected load-bearing claim, search the whole current document set and changed visuals for parallel statements. Update stale copies or make the remaining source-of-truth precedence explicit.
10. Replace the previous “current change” section with the new run's record. Do not accumulate a chronological changelog in the current document.

### Deep dive

1. Define one stable reader question and evidence boundary.
2. Link the topic from the canonical entry document when that entry is in scope.
3. Reuse definitions from the entry document instead of copying large sections.
4. State the topic's current implementation and validation status near the beginning.
5. End the topic document with its current change record.

## Organize historical material safely

Limit automatic organization to documentation and visual assets placed in scope. Do not move source code, papers, datasets, configurations, test fixtures, logs, or other raw evidence merely because they are old.

Before moving anything:

1. resolve the exact source and destination paths;
2. identify inbound links and assets used by current documents;
3. confirm that a current document supersedes the candidate;
4. leave ambiguous or partly current documents in place;
5. preserve enough path and date information to recover the move.
6. verify that the history destination is durable and recoverable; do not rely on a gitignored or ephemeral directory as the only archive.

Move confirmed superseded documents into a dated history directory. When the project already has a coherent archive organized by artifact type or another stable convention, preserve that structure and record the archive date in its index and the archived file instead of adding incompatible nesting. Preserve relative grouping when several files belong together. Move an asset only when it is exclusively used by archived material; otherwise keep it current and repair links.

Do not delete archived material. Do not overwrite an existing history file with the same name. Prefer version-control-aware moves when the workspace uses version control.

Do not stage or commit an archive move unless the user authorized that action. When staging is out of scope, verify that the destination exists, is not ignored, is included in the run delta, and is ready to be tracked or backed up; report its current status precisely.

After moving:

- repair current and archived links;
- verify that the canonical entry path still works;
- update the canonical entry's current change record when that document is in scope;
- verify that archived files are tracked, backed up, or otherwise recoverable as intended;
- inspect version-control status for unintended changes;
- report what moved, why, and where it can be recovered.

## Write the current change record

Place a final section named for the document language, such as `本次变化` or `Changes in this refresh`, at the end of every current document created or refreshed.

Include:

- source snapshot and inspection date;
- newly added understanding;
- corrected or invalidated understanding;
- status transitions such as planned → implemented or implemented → validated;
- documents or visuals archived in this run;
- unresolved questions and uninspected boundaries.

Describe the current run only. Rely on version control or archived documents for older change history.

## Verify delivery

Do not claim completion until:

- the canonical current entry is identifiable;
- every current topic document is reachable from that entry or intentionally standalone;
- the current change record is the final section;
- no confirmed obsolete document remains in the main reading path when organization was requested;
- no uncertain document was moved;
- all changed links and visual assets resolve;
- the final file set and version-control status contain no unintended changes.
