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

One item remains, narrowed to Renovate installation verification. The
current OAuth token can administer the repository but cannot list GitHub App
installations, so that point cannot be proven from this environment.

## Security

### B-02 Verify Renovate app installation
- Findings: S-04. Severity: info. Effort: S.
- Resolved 2026-10-05: GitHub Pages reports HTTPS enforcement enabled; the
  active `main-protection` ruleset prevents deletion/non-fast-forward pushes,
  requires linear history and pull requests, and requires the `validate` status
  check; repository secret scanning and push protection are enabled. Issues
  were enabled to match the existing issue templates and `CONTRIBUTING.md`.
- Resolved 2026-10-05: `.well-known/security.txt` was renewed to
  2027-09-30T00:00:00Z, keeping the expiry less than a year ahead.
- Remaining: Renovate app installation is unverified. `GET /user/installations`
  returns HTTP 403 for the current OAuth token because it is not a GitHub App
  user access token. No Renovate-authored pull request is present in the
  repository history inspected here, which is not proof of absence.
- Suggested approach: verify the Renovate GitHub App under account Settings >
  Applications > Installed GitHub Apps, or authorize a token that can list app
  installations.
- Dependencies: account-level GitHub App visibility.
- Suggested owner role: repository admin.
