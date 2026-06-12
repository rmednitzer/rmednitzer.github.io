# Audit Phases 2 and 3: Findings Register

Date: 2026-06-12
Reference commit: `c81f903`. Severity scale: critical / high / medium /
low / info. Effort scale: S / M / L. Every entry cites the session
command(s) that produced the evidence. Items marked [UNVERIFIED] could
not be confirmed from this environment and are asserted as unknown, not
as fact.

## Scope and method

- Dependency audit: not applicable; zero dependency manifests and zero
  lockfiles exist (Phase 0, section 1). No ecosystem audit tool applies.
- SAST: semgrep is not installed in this environment (`command -v
  semgrep` empty), so a manual OWASP-oriented pass was done instead.
  Applicable categories for a static no-input site were checked:
  XSS/injection (the only script writes a constant via `textContent`),
  unsafe inline content, clickjacking, information disclosure, supply
  chain. Server-side categories (SSRF, deserialization, authz, path
  traversal) have no surface here.
- Secret scanning: gitleaks over the full unshallowed history plus
  pattern greps over every reachable revision.
- Input boundary enumeration: section "Input surfaces" below.

## Input surfaces

Enumerated from the full file listing and page sources:

1. None server-side. Static hosting; no forms, listeners, file parsers,
   webhook handlers, query parameter consumers, or cookies.
2. Client-side JavaScript: exactly one statement per page,
   `document.getElementById('y').textContent = new Date().getFullYear();`
   (`index.html:343`, `legal.html:100`). It reads no user input and
   writes via `textContent`, so no DOM XSS sink exists.
3. Machine-consumed configs: `renovate.json5` (Renovate app),
   `.claude/settings.json` (Claude Code permission policy), `CLAUDE.md`
   and `.github/copilot-instructions.md` (AI agent instructions). These
   are trust/instruction surfaces for automation rather than runtime
   inputs; see S-05.

## Security findings (S-)

### S-01 No HTTP security headers and no in-page CSP fallback
- Severity: low. CWE-1021 (improper restriction of rendered UI layers)
  is the closest match for the missing frame-ancestors control.
- Location: `index.html` / `legal.html` `<head>` (no
  `http-equiv="Content-Security-Policy"` meta; verified by reading both
  files end to end).
- Evidence: GitHub Pages does not allow custom response headers
  (platform constraint). Live response headers could not be captured
  this session (Globalping MCP returned HTTP 401, no token), so the
  exact live header set is [UNVERIFIED]; the absence of any meta CSP in
  the source is verified.
- Exploit plausibility: low. The site has no authentication, no user
  input, and no actions to hijack; framing or UI redressing gains an
  attacker little. HTTPS is enforced for `*.github.io` by HSTS
  preload of the parent domain (public preload-list fact; repo-level
  "Enforce HTTPS" setting is [UNVERIFIED], see S-04).
- Recommended fix: evaluate a hash-based `<meta http-equiv="Content-Security-Policy">`
  as defense in depth, accepting that meta CSP cannot express
  frame-ancestors. Proposed, not applied, because a wrong hash silently
  breaks the year script and every copy edit to inline content becomes a
  CSP maintenance event. See ADR 0007 (proposed) and backlog B-01.
- Effort: M.
- Post-audit addendum (2026-06-12): implemented. ADR 0007 accepted; a
  hash-based meta CSP now ships on both pages and CI verifies the
  hashes on every pull request (ADR 0009). frame-ancestors remains an
  accepted residual.

### S-02 Inline script and style constrain any future CSP
- Severity: info.
- Location: `index.html:45-169` (page-unique `<style>` block, allowed by
  project convention), `index.html:343`, `legal.html:100` (inline year
  script).
- Evidence: file reads as above. JSON-LD `<script type="application/ld+json">`
  blocks are data blocks and are not executed, so they do not require
  script-src allowances.
- Exploit plausibility: not itself a vulnerability; it only shapes the
  S-01 design space (hashes or 'unsafe-inline').
- Recommended fix: none standalone; folded into ADR 0007 analysis.
- Effort: included in S-01.

### S-03 Vulnerability-reporting channels inconsistent between SECURITY.md and security.txt
- Severity: low.
- Location: `.well-known/security.txt` (Contact: mailto only);
  `SECURITY.md` (directs to GitHub private vulnerability reporting).
- Evidence: both files read this session; live security.txt fetched via
  WebFetch and identical to the working tree.
- Exploit plausibility: not exploitable; this is a coordination gap that
  can slow or misroute a real report.
- Recommended fix: add the GitHub private vulnerability reporting URL as
  an additional `Contact:` line in security.txt (RFC 9116 permits
  multiple Contact fields in preference order). Applied in phase 4.
  Renewal note: `Expires: 2026-12-31T00:00:00Z` is valid today
  (2026-06-12) and within the RFC's 1-year window, and `CLAUDE.md`
  already tracks the renewal; backlog B-02 adds an explicit owner task.
- Effort: S.

### S-04 Repository/platform security settings not verifiable from this session [UNVERIFIED]
- Severity: info.
- Location: GitHub repository settings (Pages "Enforce HTTPS", branch
  protection on `main`, GitHub secret scanning / push protection,
  Renovate app installation).
- Evidence of the gap: no API surface for these settings was available
  among the session's GitHub MCP tools; nothing in-repo encodes them.
  Renovate config exists (`renovate.json5`) but no `renovate[bot]`
  commits appear in history (`git log --format='%an' | sort | uniq -c`),
  consistent with either a recent install or no install.
- Exploit plausibility: unknown until verified.
- Recommended fix: owner verifies the four settings in the GitHub UI;
  backlog B-02.
- Effort: S.

### S-05 Supply chain and automation trust surface (awareness)
- Severity: info.
- Location: `renovate.json5`, `.claude/settings.json`, `CLAUDE.md`,
  `.github/copilot-instructions.md`.
- Evidence: zero dependencies and zero GitHub Actions exist, so the
  classic vectors (typosquats, unpinned actions, install scripts,
  lockfile tampering) have no surface (full file listing, Phase 0).
  Remaining surface is platform and agent tooling: Renovate consumes
  `renovate.json5` (preset `config:best-practices`, which pins digests
  for any future workflows; semantic commits; weekly schedule;
  vulnerability alerts labeled). Claude Code consumes
  `.claude/settings.json`, whose deny list blocks reads of env/SSH/AWS
  credentials and blocks `curl`/`wget` and force-pushes; this denial was
  observed working during this audit. AI instruction files are a prompt
  surface: agents must treat repo content as data, not as override
  instructions.
- Exploit plausibility: low; requires compromise of GitHub account or
  the platform itself.
- Recommended fix: none required now. Keep the deny rules when editing
  settings; see Q-15 for one consistency nit.
- Effort: n/a.

## Controls verified as sound (no finding)

| Check | Command | Result |
|---|---|---|
| Secret scan, full history | `git fetch --unshallow origin` then `gitleaks detect --source . --redact` | "137 commits scanned ... no leaks found" |
| Credential patterns, all revisions | `git grep -l -iE '(api[_-]?key|secret[_-]?key|password\s*[:=]|BEGIN (RSA|OPENSSH|EC) PRIVATE|ghp_...)' $(git rev-list --all)` | zero hits |
| Personal-data leakage in history (repo privacy rule: no phone, street address, day-level life dates) | `git grep -l -iE '(\+43[ /0-9]|telefon|telephone|phone[:>]|gasse [0-9]|stra(ß|ss)e [0-9]|geboren|birth)' $(git rev-list --all)` | only benign matches: the Austrian DPA's public address in pre-2026-04 `legal.html` revisions (for example `ead314d`) and a `format-detection` meta tag in old `index.html` revisions; no owner PII |
| SVG favicon free of active content | `cat favicon.svg` | no `<script>`, no event handlers, no external references |
| No third-party requests (fonts/CSS/JS) | grep of both pages and both stylesheets for external URLs; `fonts/fonts.css` read in full | all subresources same-origin, matching the privacy claims in `legal.html` |
| Reverse tabnabbing | grep for `target=` in both pages | no `target="_blank"` anywhere, so no `rel="noopener"` gap |
| `google-site-verification` meta token | by design a public value, not a secret | no action |
| security.txt RFC 9116 shape | file read + live fetch | five valid fields; Expires in the future and within 1 year of last modification (file last changed 2026-03-28, `git log -1 -- .well-known/security.txt`) |

## Code quality findings (Q-), appended in phase 3

### Q-01 Raw ampersand breaks HTML validation
- Severity: low. Effort: S.
- Location: `index.html:237` (core-graph project card, "MITRE ATT&CK").
- Evidence: `npx -y html-validate index.html legal.html` reports
  `237:314 error Raw "&" must be encoded as "&amp;" no-raw-characters`;
  the only validator error in the repo. Regression after the 2026-05-28
  validation-cleanup batches, introduced with PR #43 (`cf30a74`).
- Exploit plausibility: n/a (correctness).
- Fix: encode as `ATT&amp;CK`. Applied in phase 4.

### Q-02 Stale lastmod for /legal in sitemap.xml
- Severity: low. Effort: S.
- Location: `sitemap.xml` (legal URL entry, lastmod 2026-04-29).
- Evidence: `git log -1 --format='%as %h' -- legal.html` returns
  `2026-05-28 4adba6d` (batch 11 markup changes), so the sitemap
  understates the modification date by 29 days.
- Fix: set lastmod to 2026-05-28T00:00:00Z. Applied in phase 4.
- Post-review addendum (2026-06-12): since this PR itself modifies both
  pages, both sitemap entries and the index JSON-LD dateModified were
  subsequently bumped to 2026-06-12 (commit `b63e6cf`, prompted by a
  review comment applying the same convention).

### Q-03 Redundant contentinfo landmark inside main (index only)
- Severity: low. Effort: S.
- Location: `index.html:336` (`<footer role="contentinfo">` nested in
  `<main>`).
- Evidence: file read. CHANGELOG batch 11 (2026-05-28) removed exactly
  this "redundant ARIA role" from `legal.html` but `index.html` kept it,
  leaving the two pages inconsistent and exposing a landmark nested
  inside main, which landmark semantics discourage.
- Fix: drop the role attribute, matching legal.html. Applied in phase 4.
- Post-review addendum (2026-06-12): the Copilot review on PR #48
  correctly noted that a footer inside `<main>` maps to no landmark at
  all in HTML-AAM, so the role removal left both pages without any
  contentinfo landmark (legal.html had carried the same gap since
  batch 11). With owner approval, both footers were moved out of
  `<main>` to be siblings inside the `.page` wrapper (commit `64ce9b8`),
  restoring a native top-level contentinfo landmark on both pages with
  layout unchanged.

### Q-04 Decorative SVG icons exposed to assistive technology
- Severity: low (WCAG 1.1.1 / 4.1.2 hygiene). Effort: S.
- Location: `index.html:192`, `index.html:196`, `index.html:200` (inline
  SVGs inside the Email / LinkedIn / GitHub buttons).
- Evidence: file read; the SVGs carry no `aria-hidden`, `role`, or
  accessible name, while the adjacent text already labels each link.
- Fix: add `aria-hidden="true"` to all three. Applied in phase 4.

### Q-05 Smooth scrolling not gated by prefers-reduced-motion
- Severity: low (WCAG 2.3.3 hygiene; also a stated project convention).
- Effort: S.
- Location: `style.css:33` (`html { scroll-behavior: smooth; ... }`).
- Evidence: file read. CLAUDE.md requires animations behind
  `@media (prefers-reduced-motion: no-preference)`; the fadeUp keyframes
  honor this but smooth scrolling (triggered by the skip link) does not.
- Fix: move `scroll-behavior: smooth` into the existing reduced-motion
  gate. Applied in phase 4.

### Q-06 Dead CSS rule for removed article pages
- Severity: info. Effort: S.
- Location: `style.css:153` (`.repo-list li + li`).
- Evidence: `grep -rn 'repo-list' index.html legal.html style.css`
  matches only the stylesheet; the article pages that used the class
  were deleted 2026-05-14 (`git log --diff-filter=D`, commit `38db407`).
  The neighboring `.article-*` rules stay: legal.html uses them.
- Fix: delete the one-line rule. Applied in phase 4.

### Q-07 Orphaned full-size portrait pair; "full" WebP is a duplicate
- Severity: info. Effort: M (owner decision plus image tooling).
- Location: `profile_roman-mednitzer.png` (800x800, 646867 bytes),
  `profile_roman-mednitzer.webp` (9244 bytes).
- Evidence: reference count 0 for both across all HTML/CSS/manifest
  (grep loop in phase 0); `sha256sum` shows the full-size WebP is
  byte-identical to `profile_roman-mednitzer-400.webp`
  (`376196e0...`), so it is a mislabeled duplicate rather than an
  800 px encode. The 646867-byte PNG is 56 % of the working tree.
- Fix: not applied (binary deletion/regeneration is gated): either keep
  the 800 px PNG as the documented source-of-truth and delete the
  duplicate WebP, or regenerate a real 800 px WebP. Backlog B-03,
  ADR 0008 (proposed).
- Post-audit addendum (2026-06-12): ADR 0008 accepted and executed; the
  duplicate WebP is deleted, the 800 px PNG master kept.

### Q-08 Unused Outfit 300 font faces and files
- Severity: info. Effort: S (deletion) gated as an owner decision.
- Location: `fonts/fonts.css:1-19` (two 300-weight @font-face rules),
  `fonts/outfit-latin-300-normal.woff2` (13956 bytes),
  `fonts/outfit-latin-ext-300-normal.woff2` (6384 bytes).
- Evidence: `grep -n 'font-weight' style.css fonts/fonts.css index.html
  legal.html` shows no rule outside fonts.css uses weight 300. Browsers
  fetch fonts lazily, so the files are never downloaded by visitors;
  the cost is repo weight and a misleading fonts.css. Backlog B-03,
  ADR 0008 (proposed).
- Post-audit addendum (2026-06-12): ADR 0008 accepted and executed; the
  300-weight files and their @font-face rules are deleted.

### Q-09 CHANGELOG missing batches for the two latest site-content PRs
- Severity: info. Effort: S.
- Location: `CHANGELOG.md` (newest batch: 2026-05-28 batch 11).
- Evidence: `git log --oneline` shows later site-content changes
  PR #43 `cf30a74` (projects 2 to 5) and PR #44 `8edff6c` (hero wording,
  skills casing) with no corresponding batch; CLAUDE.md requires dated
  batches for non-trivial changes. The log is append-only, so the gap is
  recorded (not backfilled) in the 2026-06-12 batch added in phase 5.

### Q-10 CLAUDE.md layout map omits five tracked files
- Severity: info. Effort: S.
- Location: `CLAUDE.md` "Layout" tree.
- Evidence: tree lacks `SECURITY.md`, `LICENSE`, `renovate.json5`,
  `.claude/settings.json`, and `.gitignore`, all present in the file
  listing; SECURITY.md and renovate.json5 arrived 2026-06-04 (#46) after
  the map was last touched. Fixed in phase 5.

### Q-11 Local validation flow 404s on /legal
- Severity: info. Effort: S.
- Location: `CLAUDE.md` "Local validation"; `index.html:339` links
  `/legal`.
- Evidence: phase 1 serve check (`python3 -m http.server` flow): /legal
  returns 404 locally while GitHub Pages resolves it to legal.html
  (live 200 verified via WebFetch). Documented in CLAUDE.md in phase 5.

### Q-12 theme-color meta covers only the dark palette
- Severity: info. Effort: S.
- Location: `index.html:10`, `legal.html:10`.
- Evidence: single `<meta name="theme-color" content="#0a0e13">` per
  page while style.css defines a light palette behind
  prefers-color-scheme; light-mode mobile browser chrome keeps the dark
  color. Enhancement deferred to backlog B-04 to keep this pass
  fix-focused.

### Q-13 og:locale value en_AT is nonstandard
- Severity: info. Effort: S.
- Location: `index.html:22`, `legal.html:19`.
- Evidence: file read; en_AT is syntactically valid for Open Graph but
  absent from the common consumer locale lists (en_US, de_AT, ...).
  Consumers fall back gracefully. Logged only; no change.
- Post-audit addendum (2026-06-12): owner approved the switch; both
  pages now use en_US (B-08).

### Q-14 .gitignore targets a directory that no longer exists
- Severity: info. Effort: none.
- Location: `.gitignore` (`scripts/node_modules/`,
  `scripts/package-lock.json`).
- Evidence: no `scripts/` directory in the file listing; the directory
  was removed 2026-05-14. Harmless and forward-looking; intentionally
  left as-is.

### Q-15 Claude settings allow hugo/jekyll despite the no-build convention
- Severity: info. Effort: S.
- Location: `.claude/settings.json` allow list (`Bash(hugo:*)`,
  `Bash(jekyll:*)`).
- Evidence: file read; CLAUDE.md lists "adding a build step" under
  things to avoid. The allow entries were added deliberately in #47
  (`c81f903`, 2026-06-08), so this is flagged for owner review rather
  than changed. Backlog (tooling section).
- Post-audit addendum (2026-06-12): owner chose removal; the hugo and
  jekyll allow entries are deleted (B-07).

### Q-16 No automated validation anywhere in the pipeline
- Severity: low (process). Effort: M.
- Location: repository-wide; `.github/workflows` absent.
- Evidence: phase 1. The one validator the project documents
  (html-validate) is manual, and the Q-01 regression shipped to
  production precisely because nothing runs it. Recommended: a minimal
  GitHub Actions workflow running html-validate on pull requests.
  Backlog B-05, ADR 0009 (proposed).
- Post-audit addendum (2026-06-12): implemented. ADR 0009 accepted;
  `.github/workflows/validate.yml` runs html-validate plus XML, JSON,
  JSON-LD, and CSP-hash checks on every pull request.

### Q-17 GDPR rights paragraph omits the supervisory-authority complaint right
- Severity: info (legal completeness, owner decision). Effort: S.
- Location: `legal.html:79`.
- Evidence: the current rights list stops at objection; the pre-2026-04
  revision (`ead314d`) additionally named the Austrian DPA
  (Datenschutzbehörde) complaint right per Art. 77 GDPR, and the
  sentence was dropped in a later rewrite. CLAUDE.md forbids changing
  legal.html boilerplate without confirming legal context, so this goes
  to the owner: backlog B-06. No change in this pass.
- Post-audit addendum (2026-06-12): owner confirmed the restoration;
  the Art. 77 sentence naming the Austrian DPA is back in the privacy
  section (B-06).

## Severity totals after phases 2 and 3

| Severity | Count | IDs |
|---|---|---|
| critical | 0 | |
| high | 0 | |
| medium | 0 | |
| low | 8 | S-01, S-03, Q-01, Q-02, Q-03, Q-04, Q-05, Q-16 |
| info | 14 | S-02, S-04, S-05, Q-06 to Q-15, Q-17 |
