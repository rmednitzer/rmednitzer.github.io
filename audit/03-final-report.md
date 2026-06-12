# Audit Phase 8: Final Report

Date: 2026-06-12
Branch: `claude/trusting-allen-3s2fh1` (session-mandated; the requested
`audit/2026-06-12-full-pass` name was unavailable in this managed
environment). Base: `main` at `c81f903`. Nothing was pushed to main.

## Executive summary

A full audit of the static personal site `rmednitzer.github.io` found a
healthy, deliberately minimal repository with zero dependencies, zero
secrets or PII anywhere in 171 reachable revisions, and no third-party
subresources. No critical, high, or medium findings exist. The audit
registered 22 findings (8 low, 14 info), fixed the 7 that were safe and
local (one HTML validation regression, one stale sitemap date, three
accessibility nits, one dead CSS rule, one security-contact
inconsistency), synced the documentation that had drifted, backfilled
six ADRs, proposed three more, and left 9 prioritized backlog items.
The single most useful next step is CI validation (backlog B-05): the
one defect that reached production did so because nothing runs the
project's own documented validator.

## Baseline vs post-fix metrics

| Metric | Baseline (c81f903) | Post-fix (27b23b1) |
|---|---|---|
| html-validate (11.5.3) errors / warnings | 1 / 0 | 0 / 0 |
| Local serve checks (HTTP 200) | 18 of 19 paths | 18 of 19 paths (the 19th, `/legal`, is a GitHub Pages extensionless route, now documented; verified 200 live) |
| xmllint sitemap.xml; jq manifest/settings; JSON-LD parse | all pass | all pass |
| Dependency vulnerabilities | none possible (0 dependencies) | unchanged |
| Secrets / credentials in history | 0 (gitleaks, 137 commits; pattern greps, 171 revisions) | unchanged |
| Findings: critical / high / medium | 0 / 0 / 0 | 0 / 0 / 0 |
| Findings: low | 8 open | 2 open (S-01 CSP, Q-16 CI; both deferred by design, ADRs 0007/0009) |
| Findings: info | 14 open | 9 open or accepted-as-is, all dispositioned in the register and backlog |
| Tests / coverage | none exist | unchanged (B-05 proposes the first automated check) |

Every fix re-ran the affected validator plus the full baseline suite;
the post-fix run (html-validate, xmllint, jq, JSON-LD parse, 10-path
serve check) is recorded in the session and was fully green.

## Commits on this branch

| Commit | Rationale |
|---|---|
| 80594bc docs: audit phase 0 inventory | repo map, toolchain, zero-dependency state |
| c76d4bf docs: audit phase 1 baseline | serve checks, validators, no-CI/no-test record |
| b4d46b5 docs: audit phase 2 security register | S-01..S-05, input surfaces, passed controls |
| 1fe928b docs: phase 3 quality findings | Q-01..Q-17 appended to the register |
| 61baeb8 fix: encode raw ampersand | Q-01; restores clean html-validate |
| 6b5ba24 security: security.txt Contact | S-03; aligns RFC 9116 file with SECURITY.md |
| d873da3 fix: sitemap lastmod | Q-02; /legal date matched to file history |
| 04eccfe fix: drop contentinfo role | Q-03; index/legal landmark parity |
| a0cc574 fix: aria-hidden on button icons | Q-04; decorative SVGs hidden from AT |
| 58efd99 fix: gate smooth scrolling | Q-05; honors prefers-reduced-motion convention |
| 28dffec refactor: remove dead .repo-list rule | Q-06; selector unmatched since 2026-05-14 |
| 558cdab docs: style.css comment drift | comment referenced deleted article pages |
| 314334a docs: CLAUDE.md sync | Q-10/Q-11; layout map and local-validation note |
| 6886f61 docs: README pointers | LICENSE and SECURITY.md references |
| 7441c49 docs: backfilled ADRs 0001-0006 | decisions embodied in code, evidence-based |
| 23e2bb6 docs: proposed ADRs 0007-0009 + index | CSP, asset pruning, CI validation |
| 22381e6 docs: BACKLOG.md | nine prioritized deferred items |
| 27b23b1 docs: CHANGELOG batch 12 | Q-09; audit recorded, append-only respected |

## Residual risk statement

Accepted or deferred risks, all low or informational:

1. No client-side hardening headers are possible on GitHub Pages and no
   meta CSP is set (S-01). Exposure is bounded by the site's nature
   (static, no auth, no input). Decision packaged as ADR 0007.
2. Nothing automated guards correctness; regressions surface only when
   a human runs the validator (Q-16, ADR 0009).
3. Four platform settings are unverified from this environment: Pages
   "Enforce HTTPS", branch protection, GitHub secret scanning, Renovate
   app installation (S-04, [UNVERIFIED], backlog B-02).
4. Orphaned binaries remain in the tree pending owner decision (Q-07,
   Q-08, ADR 0008); they are never served to visitors.
5. The GDPR rights paragraph omits the Art. 77 complaint right; legal
   wording is gated on owner confirmation (Q-17, B-06).
6. These audit artifacts (`audit/`, `docs/adr/`, `BACKLOG.md`) are
   served by GitHub Pages like everything else in the repo root. They
   contain no sensitive data (the repo is public regardless), but the
   owner may prefer to exclude them from the published site eventually.

Stop conditions: none triggered. No secrets found, nothing
unrunnable, no conflicting embedded instructions encountered.

## Top 5 backlog items

1. B-05 CI html-validate on PRs (low, M): converts the documented
   manual check into an enforced invariant; would have caught Q-01.
2. B-01 meta CSP decision (low, M): the only available client-side
   hardening; pair with B-05 for hash verification.
3. B-02 verify platform settings + security.txt renewal (info, S):
   four one-click checks plus a calendar entry before 2026-12-31.
4. B-03 prune or regenerate orphaned binaries (info, S to M): removes a
   mislabeled duplicate WebP and two unused font files.
5. B-06 GDPR complaint-right wording review (info, S): one sentence,
   owner judgement required.

## Scope notes

- `.github/copilot-instructions.md` was checked against the conventions
  it mirrors and left unchanged: no styling or layout rules changed in
  this pass, and its "Key files" list is a deliberate subset, not a
  full map.
- CONTRIBUTING.md was deliberately not created (B-09 records the
  decision); SECURITY.md and LICENSE existed and are now referenced
  from README.
- All authored prose in this audit uses YYYY-MM-DD dates, SI units, and
  no em-dashes, per the audit ground rules.
