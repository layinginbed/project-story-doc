# Security Policy

## Supported version

Security and data-handling fixes target the latest commit on `main`.

## Reporting a problem

Do not publish credentials, private repository content, proprietary documents, personal data, or sensitive traces in a GitHub issue.

For a non-sensitive problem, open a minimal issue that includes the affected Skill section, the expected safety boundary, and sanitized reproduction steps.

For a sensitive problem, first open an issue containing only a request for private maintainer contact. Do not include the sensitive details until a private channel has been established.

## Scope

Relevant reports include:

- instructions that could expose secrets or source material outside the intended audience;
- unsafe handling of dirty working trees or archive candidates;
- validation that silently misses repository credentials or broken package boundaries;
- examples that encourage publishing private data;
- supply-chain risks in repository automation.

This repository contains instructions and validation tooling. It does not operate a hosted service or collect telemetry.
