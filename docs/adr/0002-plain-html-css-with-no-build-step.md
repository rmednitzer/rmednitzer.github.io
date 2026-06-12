# Plain HTML/CSS with no build step, framework, or bundler

- Status: accepted
- Date: 2026-06-12 (backfilled; the decision predates this record and
  has held since the repository's first commits in 2026-03)
- Deciders: repository owner

## Context and problem statement

A personal profile site needs to stay cheap to maintain, fast to load,
and trivially auditable. Static-site generators and JS frameworks add a
toolchain, dependency surface, and upgrade treadmill that a two-page
site does not need.

## Decision outcome

The site is hand-written HTML and CSS. No build step, no JavaScript
framework, no bundler, no dependency manifests. The only JavaScript is
a one-line footer-year updater per page, with a literal year fallback
so the page renders with JS disabled.

Evidence: CLAUDE.md "Stack" and "Things to avoid"; zero manifests or
lockfiles in the tree; `.nojekyll` present. The 2026-06-12 audit
confirmed the consequence empirically: the dependency-vulnerability
surface is zero and there is nothing to build or break.

### Consequences

- Good: no supply-chain exposure from app dependencies; entire site
  auditable by reading two HTML files and two stylesheets.
- Good: page weight stays small (working tree minus portraits and fonts
  is about 40 kB).
- Bad: no templating, so head metadata is duplicated across pages and
  must be kept in sync by hand (audit finding Q-03 was exactly this
  class of drift).
- Bad: nothing enforces validity automatically; see ADR 0009 (proposed).
