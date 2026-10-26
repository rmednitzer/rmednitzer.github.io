# Backlog

Deferred findings and proposals from the 2026-06-12 audit pass.
Finding IDs reference `audit/02-security-findings.md`; ADR links are in
`docs/adr/`.

Resolution log (all 2026-06-12, see CHANGELOG batches): B-04 closed by
batch 16 (light theme-color); B-01, B-03, B-05 closed by batch 18 (meta
CSP, asset pruning, CI validation; ADRs 0007 to 0009 accepted); B-06,
B-07, B-08 closed by batch 19 (owner decisions applied); B-09 closed
without action, recording the deliberate decision that a CONTRIBUTING.md
is not appropriate for a personal site that solicits no contributions.
Addendum (2026-08-13): that decision was reconsidered and reversed by
batch 33, which added `CONTRIBUTING.md` (plus `CODE_OF_CONDUCT.md`,
`.github/CODEOWNERS`, a pull request template, and issue forms) as part
of the repository-paperwork pass — see that batch for the current
rationale.

## Current follow-up (2026-10-26)

The earlier Renovate uncertainty is resolved as operational evidence: PRs #98,
#99, #100 and #104 were authored by Renovate, including extracted npm validator
and GitHub Actions updates. This is observed operation, not verification of
current account-level installation permissions.

The repository review corrections now cover public-format consistency, validator
regressions, documentation reconciliation and obsolete CSS. See CHANGELOG.md.

Remaining scope limits:
- Fresh mobile, dark/high-contrast, print and assistive-technology runtime checks
  remain necessary after substantive presentation changes.
- The notice makes no categorical ECG exemption or comprehensive GDPR-compliance
  claim. Confirm legal applicability separately; correspondence-provider and
  retention facts must be established before documenting email processing.
- Current-source credential patterns and GitHub scanning are not a renewed
  full-history secret scan.
