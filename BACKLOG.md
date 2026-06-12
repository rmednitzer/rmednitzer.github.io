# Backlog

Deferred findings and proposals from the 2026-06-12 audit pass.
Finding IDs reference `audit/02-security-findings.md`; ADR links are in
`docs/adr/`. Ordered by severity, then effort, within each section.
None of these items is applied yet; binary deletions, structural
changes, and legal wording are deliberately owner decisions.

## Security

### B-01 Decide on a meta Content-Security-Policy
- Findings: S-01, S-02. Severity: low. Effort: M.
- Rationale: GitHub Pages allows no response headers; a hash-based meta
  CSP is the only client-side hardening available, but every inline
  edit then becomes a hash-maintenance event that fails closed.
- Suggested approach: read ADR 0007 (proposed); if accepted, land it
  together with B-05 so CI verifies the hashes.
- Dependencies: ideally B-05 first.
- Suggested owner role: site owner (security trade-off call).

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

## Quality

### B-08 Review og:locale value
- Finding: Q-13. Severity: info. Effort: S.
- Rationale: `en_AT` is syntactically fine but absent from common Open
  Graph consumer locale lists; consumers fall back silently.
- Suggested approach: either keep (harmless) or switch to `en_US` and
  note Austria via existing address markup; decide once, document in
  the CHANGELOG batch.
- Dependencies: none.
- Suggested owner role: site owner.

## Documentation

### B-06 Owner review: GDPR supervisory-authority complaint right in legal.html
- Finding: Q-17. Severity: info (legal completeness). Effort: S.
- Rationale: the current rights list omits the Art. 77 GDPR right to
  complain to the supervisory authority; a pre-2026-04 revision named
  the Austrian DPA explicitly and the sentence was dropped in a
  rewrite. CLAUDE.md gates legal.html changes on confirming legal
  context, so this was not changed during the audit.
- Suggested approach: owner confirms intent; if restoring, re-add one
  sentence naming the Datenschutzbehörde.
- Dependencies: owner legal judgement.
- Suggested owner role: site owner (media owner per § 25 MedienG).

### B-09 Decide whether CONTRIBUTING.md is wanted
- Finding: phase 5 scope note (no register ID). Severity: info.
  Effort: S.
- Rationale: the audit deliberately did not create one: a personal
  profile site solicits no external contributions, so a CONTRIBUTING.md
  is not "clearly appropriate". Recording the decision here keeps the
  gap intentional rather than an oversight.
- Suggested approach: if unwanted, close this item; if wanted, three
  lines pointing at CLAUDE.md conventions and the PR flow.
- Dependencies: none.
- Suggested owner role: site owner.

## Tooling

### B-07 Reconcile .claude/settings.json allow-list with the no-build convention
- Finding: Q-15. Severity: info. Effort: S.
- Rationale: `Bash(hugo:*)` and `Bash(jekyll:*)` are allowed while
  CLAUDE.md forbids build steps; the entries were added deliberately in
  PR #47, so either remove them or note why they exist.
- Suggested approach: owner picks; a one-line comment is impossible in
  JSON, so document the reason in CLAUDE.md if the entries stay.
- Dependencies: none.
- Suggested owner role: site owner.
