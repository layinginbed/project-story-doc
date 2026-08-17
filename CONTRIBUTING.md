# Contributing

Thank you for helping improve Project Story Doc.

The repository accepts changes that make the Skill more accurate, general, safe, or easier to use across projects, repositories, papers, and paper-plus-code artifacts.

## Before proposing a change

1. Start from a concrete documentation failure or usage example.
2. Confirm that the problem applies beyond one private artifact.
3. Identify whether the change belongs in `SKILL.md`, one existing reference, repository documentation, or validation tooling.
4. Prefer editing an existing file over adding another document.
5. Do not weaken evidence boundaries, dirty-worktree safety, archive safety, or delivery verification.

## Development setup

```bash
git clone https://github.com/layinginbed/project-story-doc.git
cd project-story-doc
python3 scripts/validate_repository.py
```

The validation command uses only the Python standard library.

## Pull requests

Keep each pull request focused on one behavior class. Explain:

- the concrete failure or missing capability;
- why the current instructions do not handle it;
- the files changed and why each file owns that rule;
- the validation or forward test used;
- any behavior that remains unverified.

Before submitting, confirm:

- [ ] `python3 scripts/validate_repository.py` passes.
- [ ] The Skill still has one clear trigger boundary.
- [ ] Detailed rules live in references instead of duplicating `SKILL.md`.
- [ ] New rules use imperative language and preserve explicit evidence classes.
- [ ] No private source, user data, credential, or local absolute path is included.
- [ ] README examples still match the actual Skill behavior.

## Scope boundaries

Good contributions include:

- closing a general evidence or coverage gap;
- clarifying Create, Refresh, Deep dive, or Organize history behavior;
- improving support for a declared artifact route;
- strengthening safe Apply or delivery verification;
- fixing broken links, metadata, examples, or validation.

Changes that need stronger justification include:

- adding a new top-level mode or artifact route;
- creating another reference document instead of extending an existing owner;
- embedding assumptions from one domain or one repository;
- adding generic writing advice that Codex already knows;
- weakening uncertainty labels to make output sound more confident.

## Sensitive material

Use synthetic or already-public examples. Do not attach proprietary documents, private repository excerpts, credentials, personal data, or sensitive traces to issues or pull requests.

For security-sensitive reports, follow [SECURITY.md](SECURITY.md).
