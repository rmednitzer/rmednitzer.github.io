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
