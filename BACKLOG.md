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

One item remains. It requires repository-settings access that only the
owner has.

## Security

### B-02 Verify platform security settings and calendar the security.txt renewal
- Findings: S-03 (renewal note), S-04. Severity: info. Effort: S.
- Rationale: four settings are invisible from the repo and unverified:
  Pages "Enforce HTTPS", branch protection on main, GitHub secret
  scanning / push protection, Renovate app installation. security.txt
  expires 2026-12-31T00:00:00Z.
- Suggested approach: one pass through repo Settings; set a reminder
  (2026-11) to bump `Expires` in `.well-known/security.txt`.
- Dependencies: none.
- Suggested owner role: repository admin.
