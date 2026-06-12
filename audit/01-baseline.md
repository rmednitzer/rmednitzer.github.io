# Audit Phase 1: Validation Baseline

Date: 2026-06-12
Reference commit: `c81f903` (branch state before any remediation).
This baseline is the regression reference for every later change in this
audit. All commands below were executed in this session.

## 1. Build

Not applicable by design: the site is plain HTML/CSS with no build step
(`CLAUDE.md`, "Stack"). "Build from clean state" therefore reduces to
serving the working tree as-is.

## 2. Serve check (local)

Command: Python stdlib server (`http.server` on 127.0.0.1:8000, the
documented validation flow in `CLAUDE.md`) plus `urllib` requests against
every page and referenced asset. Note: `curl`/`wget` are denied by repo
policy, so Python was used.

Result: 19 paths requested, 18 returned HTTP 200 with the expected
Content-Type and exact on-disk byte size. The one failure:

| Path | Local result | Live result |
|---|---|---|
| `/legal` | 404 (plain static server does not resolve extensionless paths) | 200, title "Legal Notice & Privacy" (verified live via WebFetch on https://rmednitzer.github.io/legal) |

This is a known GitHub Pages behavior (extensionless URLs resolve to
`.html`), not a defect, but it means local link-walking from `index.html`
breaks at the footer link. Recorded as Q-11 (documentation note).

Live spot-checks via WebFetch (2026-06-12): `/` serves the current
profile (h1 "Roman Mednitzer", sections About / Open-source projects /
Homelab / Skills), and `/.well-known/security.txt` serves the same five
fields as the working-tree file. An attempt to capture live response
headers via the Globalping MCP failed with HTTP 401 (no API token), so
header-level claims about the live site are marked [UNVERIFIED] in
phase 2.

## 3. Test suite

None exists (Phase 0, section 1). Pass/fail counts, flakiness, and
runtime: not applicable. Coverage tooling: absent; nothing to measure.
The absence of any automated check is recorded as a tooling gap (Q-16 /
backlog B-05).

## 4. Linters and validators (check-only)

| Check | Command | Result |
|---|---|---|
| HTML validation | `npx -y html-validate index.html legal.html` (html-validate 11.5.3, no repo config; tool defaults) | 1 error: `index.html:237:314` raw `&` must be encoded as `&amp;` (rule `no-raw-characters`), in the text "MITRE ATT&CK". `legal.html`: clean. Exit code 1. |
| XML well-formedness | `xmllint --noout sitemap.xml` | OK |
| JSON validity | `jq -e . site.webmanifest`, `jq -e . .claude/settings.json` | OK, OK |
| JSON-LD blocks | Python `json.loads` over each `<script type="application/ld+json">` extracted by regex | index block 1 OK, index block 2 OK, legal block 1 OK |
| CSS lint | No CSS linter is installed or configured in the repo | Not run; absence noted |

The html-validate error is a regression relative to the 2026-05-28
CHANGELOG batches 10 and 11, which record a "clear remaining
html-validate issues" pass; the raw ampersand arrived afterwards with the
project-card expansion (PR #43, `cf30a74`). Registered as Q-01 and fixed
in phase 4.

## 5. CI reproduction

There is no CI to reproduce (`ls .github/workflows`: no workflows dir).
Drift between CI and local: not applicable. Deployment is the implicit
GitHub Pages publish of the repo root; its server-side behavior was
spot-checked live (section 2).

## 6. Baseline summary (regression reference)

- Serve: 18/19 paths 200 locally; `/legal` works live only.
- html-validate: 1 error, 0 warnings (index.html), 0/0 (legal.html).
- XML/JSON/JSON-LD: all valid.
- Tests: none. Coverage: none. CI: none.
- gitleaks over full history: no leaks (see phase 2).
