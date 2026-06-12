# Run html-validate in CI on every pull request

- Status: proposed
- Date: 2026-06-12
- Deciders: repository owner (decision pending)
- Source: audit finding Q-16, backlog B-05

## Context and problem statement

The repository has no CI at all. The one validator the project
documents (`npx -y html-validate`) is run manually, and the audit
showed the failure mode concretely: a raw-ampersand validation error
(finding Q-01) shipped to production in PR #43 and lived there for two
weeks, immediately after two changelog batches that had celebrated a
clean validator run.

This does not contradict ADR 0002: the site keeps no build step; CI
would only check, never build.

## Considered options

1. A single GitHub Actions workflow on pull_request (and push to main)
   running `npx -y html-validate index.html legal.html` plus
   `xmllint --noout sitemap.xml`, with actions pinned by digest
   (Renovate's best-practices preset, ADR 0006, then maintains the
   pins) and a least-privilege `permissions: contents: read` block.
2. A pre-commit hook documented in CLAUDE.md (no server-side
   enforcement; agents and the web UI bypass it).
3. Status quo: manual validation on memory.

## Decision outcome

Pending owner decision. Option 1 is recommended; it is about 20 lines
of YAML, introduces the repo's first workflow (which finally gives
Renovate something to maintain), and turns the project's own
documented validator into an enforced invariant. The workflow file was
deliberately not added during the audit because introducing CI is a
structural change reserved for the owner.

### Consequences (option 1)

- Good: the Q-01 class of regression cannot reach main unnoticed.
- Bad: first GitHub Actions surface (pinning and permissions must be
  kept tight); occasional false positives from validator upgrades.
