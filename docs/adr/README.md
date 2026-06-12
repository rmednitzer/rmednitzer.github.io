# Architecture decision records

MADR-style records, numbered `NNNN-title.md`. Statuses: proposed,
accepted, superseded. Backfilled records (0002 to 0006) document
decisions that predate the log; each marks what is evidence and what is
unknowable. See ADR 0001 for the process.

| ADR | Title | Status | Date |
|---|---|---|---|
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions as ADRs | accepted | 2026-06-12 |
| [0002](0002-plain-html-css-with-no-build-step.md) | Plain HTML/CSS with no build step, framework, or bundler | accepted | 2026-06-12 (backfilled) |
| [0003](0003-self-hosted-fonts-no-third-party-requests.md) | Self-hosted fonts; no third-party requests | accepted | 2026-06-12 (backfilled) |
| [0004](0004-github-pages-hosting-from-repo-root.md) | GitHub Pages hosting from the repo root, Jekyll disabled | accepted | 2026-06-12 (backfilled) |
| [0005](0005-single-shared-stylesheet-with-page-scoped-extras.md) | Single shared stylesheet plus page-unique head styles | accepted | 2026-06-12 (backfilled) |
| [0006](0006-renovate-for-dependency-automation.md) | Renovate (best-practices preset) for dependency automation | accepted | 2026-06-04 (backfilled) |
| [0007](0007-meta-csp-for-github-pages.md) | Hash-based meta CSP for both pages | accepted | 2026-06-12 |
| [0008](0008-prune-or-regenerate-orphaned-binary-assets.md) | Prune or regenerate orphaned portrait and font binaries | accepted | 2026-06-12 |
| [0009](0009-ci-html-validation-on-pull-requests.md) | Run html-validate in CI on pull requests | accepted | 2026-06-12 |

The 2026-06-12 audit's phase 4 fixes were single-line, behavior-
preserving corrections; the one structural follow-up (footers moved out
of `<main>` after review to restore the contentinfo landmark) is
recorded in `audit/03-final-report.md`. None rose to ADR significance,
so no per-fix ADRs exist.
