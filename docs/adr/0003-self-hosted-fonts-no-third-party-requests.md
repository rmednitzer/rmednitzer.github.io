# Self-hosted fonts; no third-party requests of any kind

- Status: accepted
- Date: 2026-06-12 (backfilled; in force since at least 2026-03-24,
  the last change to `fonts/fonts.css`)
- Deciders: repository owner

## Context and problem statement

Loading fonts or other subresources from third-party CDNs leaks visitor
IP addresses to those parties. For an Austrian site owner this is a
concrete GDPR concern (German case law on Google Fonts made the risk
explicit), and `legal.html` promises visitors that no such requests
happen.

## Decision outcome

Outfit and DM Mono are self-hosted as WOFF2 under `fonts/`, split into
latin and latin-ext subsets with `unicode-range`, loaded via
`fonts/fonts.css`, with the primary weight preloaded. No external font,
CSS, or JS references are permitted (CLAUDE.md "Assets"; mirrored in
`.github/copilot-instructions.md`).

The privacy rationale is documented user-facing text, not
reconstruction: `legal.html` states "Fonts are self-hosted. No requests
are made to Google Fonts or other external font services." The
2026-06-12 audit verified the claim: every subresource in both pages
and both stylesheets is same-origin.

### Consequences

- Good: the legal page's privacy claims are technically true and
  verifiable; no consent banner needed.
- Good: no render-blocking third-party origin.
- Bad: font upgrades are manual (download, subset, commit), and unused
  faces can linger; the audit found the Outfit 300 pair unused (finding
  Q-08, ADR 0008).
