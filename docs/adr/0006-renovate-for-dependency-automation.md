# Use Renovate (shared best-practices preset) for dependency automation

- Status: accepted
- Date: 2026-06-04 (backfilled record of the merged configuration:
  commits `cabc60f`, `bfa2dec`, and PR #46 `470797e`)
- Deciders: repository owner

## Context and problem statement

The site itself has zero dependencies (ADR 0002), but the repository
may grow automation (GitHub Actions, local tooling) whose versions
should not rot. A dependency-update bot configured before it is needed
costs little and prevents unpinned drift later.

## Decision outcome

`renovate.json5` extends `config:best-practices` (which includes digest
pinning), `:semanticCommits`, Vienna timezone, a weekly schedule,
lockfile maintenance, OSV vulnerability alerts, and groups non-major
GitHub Actions updates into one PR while keeping majors separate.

Why Renovate was preferred over Dependabot is not recorded in the
repository or commit messages; that rationale is unknowable from the
evidence. What is verifiable: the config is currently a forward-looking
no-op (no manifests, no workflows, no lockfiles exist), and no
`renovate[bot]` commits appear in history, so whether the app is
installed on the repository is unverified (audit finding S-04,
backlog B-02).

### Consequences

- Good: any future workflow or manifest gets pinning and scheduled
  updates from day one.
- Neutral: until such files exist, the config does nothing.
- Action: owner should confirm the Renovate app is actually installed,
  or the config is dead weight.
