# Host on GitHub Pages, serving the repository root with Jekyll disabled

- Status: accepted
- Date: 2026-06-12 (backfilled; in force since the repository was
  created as `rmednitzer.github.io`)
- Deciders: repository owner

## Context and problem statement

The site needs zero-cost, low-operations hosting with HTTPS. The
repository name `rmednitzer.github.io` selects GitHub Pages' user-site
model, which serves from the default branch.

## Decision outcome

GitHub Pages serves the repository root directly. `.nojekyll` disables
Jekyll so files are published as-is (required because there is no
generator and dotted paths like `.well-known/` must be served).
No custom domain is configured (no CNAME file).

Why GitHub Pages rather than an alternative host was chosen is not
recorded anywhere in the repository; the operational properties below
are evidence-based, the original comparison (if any) is unknowable.

### Consequences

- Good: no servers to run; deploys are `git push`.
- Good: HTTPS is effectively guaranteed in browsers because github.io
  is HSTS-preloaded (the repo-level "Enforce HTTPS" toggle should still
  be verified by the owner: audit finding S-04, backlog B-02).
- Bad: no control over HTTP response headers, so CSP and frame-ancestors
  cannot be set server-side (audit finding S-01, ADR 0007).
- Quirk: extensionless URLs (`/legal`) resolve to `.html` only on
  Pages; plain local servers 404 on them (documented in CLAUDE.md,
  audit finding Q-11).
