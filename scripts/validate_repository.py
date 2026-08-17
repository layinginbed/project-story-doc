#!/usr/bin/env python3
"""Validate the public repository wrapper and packaged Codex Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "project-story-doc"
SKILL_FILE = SKILL_DIR / "SKILL.md"

REQUIRED_PATHS = (
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    SKILL_FILE,
    SKILL_DIR / "agents" / "openai.yaml",
)

ALLOWED_SKILL_ENTRIES = {"SKILL.md", "agents", "assets", "references", "scripts"}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_PATTERNS = {
    "GitHub personal access token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "macOS user path": re.compile("/" + "Users/" + r"[^/\s]+/"),
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def parse_frontmatter(errors: list[str]) -> None:
    lines = SKILL_FILE.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        fail("project-story-doc/SKILL.md must start with YAML frontmatter", errors)
        return

    try:
        end = lines.index("---", 1)
    except ValueError:
        fail("project-story-doc/SKILL.md frontmatter is not closed", errors)
        return

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}", errors)
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")

    if set(metadata) != {"name", "description"}:
        fail("SKILL.md frontmatter must contain only name and description", errors)
    if metadata.get("name") != "project-story-doc":
        fail("SKILL.md name must be project-story-doc", errors)
    if not metadata.get("description"):
        fail("SKILL.md description must not be empty", errors)


def local_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if not target or target.startswith(("#", "http://", "https://", "mailto:", "data:")):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target) if target else None


def check_markdown_links(errors: list[str]) -> int:
    checked = 0
    for markdown_file in sorted(ROOT.rglob("*.md")):
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = local_link_target(raw_target)
            if target is None:
                continue
            checked += 1
            resolved = (markdown_file.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes repository: {markdown_file.relative_to(ROOT)} -> {target}", errors)
                continue
            if not resolved.exists():
                fail(f"broken link: {markdown_file.relative_to(ROOT)} -> {target}", errors)
    return checked


def check_package_boundary(errors: list[str]) -> None:
    entries = {path.name for path in SKILL_DIR.iterdir()}
    unexpected = sorted(entries - ALLOWED_SKILL_ENTRIES)
    if unexpected:
        fail(f"unexpected top-level files inside Skill package: {', '.join(unexpected)}", errors)

    references = sorted((SKILL_DIR / "references").glob("*.md"))
    if not references:
        fail("Skill package must contain reference documents", errors)


def check_sensitive_patterns(errors: list[str]) -> int:
    checked = 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        checked += 1
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                fail(f"possible {label} in {path.relative_to(ROOT)}", errors)
    return checked


def main() -> int:
    errors: list[str] = []

    for required_path in REQUIRED_PATHS:
        if not required_path.is_file():
            fail(f"missing required file: {required_path.relative_to(ROOT)}", errors)

    if not SKILL_FILE.is_file():
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    parse_frontmatter(errors)
    check_package_boundary(errors)
    link_count = check_markdown_links(errors)
    text_file_count = check_sensitive_patterns(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        "Validation passed: "
        f"Skill metadata, package boundary, {link_count} local link(s), "
        f"and {text_file_count} text file(s) checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
