# Audit Phase 0: Recon and Inventory

Date: 2026-06-12
Auditor: Claude Code session, branch `claude/trusting-allen-3s2fh1`
Scope: full repository `rmednitzer/rmednitzer.github.io` at commit `c81f903`

Note on branch naming: the audit instructions requested branch
`audit/2026-06-12-full-pass`. This managed session is restricted to pushing
the pre-provisioned branch `claude/trusting-allen-3s2fh1`, so all audit work
lives there. Nothing is pushed to `main`.

## 1. What this repository is

A static single-page personal website (profile of Roman Mednitzer, Senior
Linux & Platform Engineer) served by GitHub Pages from the repository root at
https://rmednitzer.github.io/. There is intentionally no build system, no
JavaScript framework, no bundler, and no dependency manifest. See `CLAUDE.md`
for the maintained project conventions.

- Languages: HTML (2 pages), CSS (2 stylesheets), one inline 1-line
  JavaScript snippet per page (footer year updater), JSON (manifest,
  configs), XML (sitemap).
- Build system: none. `.nojekyll` disables Jekyll processing
  (verified: `find . -type f` lists `./.nojekyll`, 0 bytes).
- Entry points: `index.html` (landing page), `legal.html` (served as
  `/legal` by GitHub Pages extensionless resolution).
- CI config: none. Verified: `ls .github/workflows` returns
  "no workflows dir"; `.github/` contains only `copilot-instructions.md`.
  Deployment relies on the implicit GitHub Pages build.
- Container/IaC files: none (full file listing below contains no
  Dockerfile, compose file, Kubernetes manifest, or Terraform).
- Dependency manifests: none (no `package.json`, no lockfiles).
  Direct dependencies: 0. Lockfile state: not applicable.
- Test layout: none. No test framework or test files exist.

## 2. Component map

Verified with `find . -type f -not -path './.git/*' -printf '%s\t%p\n'`
(sizes in bytes):

| Component | Files | Notes |
|---|---|---|
| Pages | `index.html` (20458), `legal.html` (6478) | Self-contained semantic HTML; index carries a page-unique `<style>` block per convention |
| Shared styles | `style.css` (3737) | Single source of truth; light/dark via `prefers-color-scheme` |
| Fonts | `fonts/fonts.css` (4619) + 12 WOFF2 files (Outfit 300/400/500/600, DM Mono 400/500, latin + latin-ext) | Self-hosted, no CDN |
| Images | `profile_roman-mednitzer{,-400}.{png,webp}`, `favicon.{svg,ico}`, `favicon-{32,180,192,512}.png` | Portrait 400x400 and 800x800 PNG (dimensions read from PNG IHDR via Python struct) |
| Crawler/PWA plumbing | `sitemap.xml`, `robots.txt`, `site.webmanifest`, `.nojekyll` | |
| Security contact | `.well-known/security.txt` | RFC 9116; Expires 2026-12-31T00:00:00Z |
| Policy and docs | `README.md`, `CHANGELOG.md` (append-only patch log), `CLAUDE.md`, `SECURITY.md`, `LICENSE` (Apache-2.0, verified via `head -5 LICENSE`), `.github/copilot-instructions.md` | |
| Automation config | `renovate.json5` (Renovate, `config:best-practices`), `.claude/settings.json` (Claude Code permission policy), `.gitignore` | No GitHub Actions |

Working tree size: 1147279 bytes (`du -sb --exclude=.git .`), of which
857110 bytes are the four profile portrait files and 154808 bytes the 12
font files.

## 3. Git state

- Commits reachable from all refs: 171 (`git rev-list --all --count`,
  after `git fetch --unshallow origin`; the session clone started shallow).
- HEAD ancestry: 90 commits on `main` at `c81f903`.
- Authors (`git log --format='%an' | sort | uniq -c`): Roman Mednitzer
  (148), copilot-swe-agent[bot] (16), Claude (6), Copilot (1).
- History includes deleted content: 2026-05-14 commit `38db407` removed
  three article pages and `feed.xml`
  (`git log --diff-filter=D --name-only --all`). Relevant because shared
  CSS still carries one leftover rule for those pages (see Q-06).

## 4. Toolchain available in this audit environment

Recorded by running each command in this session:

| Tool | Version / state |
|---|---|
| Python | 3.11.15 (`python3 --version`) |
| git | 2.43.0 (`git --version`) |
| Node.js / npm / npx | v22.22.2 / 10.9.7 / 10.9.7 |
| html-validate (via `npx -y html-validate`) | 11.5.3 |
| gitleaks | present at `/usr/bin/gitleaks` (binary reports "version is set by build process") |
| xmllint, jq | present |
| semgrep, trufflehog, tidy | not installed (`command -v` empty) |
| curl, wget | present but denied by repo policy `.claude/settings.json` (`Bash(curl:*)`, `Bash(wget:*)` in deny list); external checks used the harness WebFetch tool instead |

## 5. Dependency graph summary

There is no application dependency graph. Direct dependencies: 0.
Transitive dependencies: 0. Lockfiles: none. The only third-party
execution surfaces are platform-level: GitHub Pages (hosting), the
Renovate app if installed (config present in `renovate.json5`; app
installation state not verifiable from this environment, see S-04), and
AI coding agents that read `CLAUDE.md` / `.github/copilot-instructions.md`
/ `.claude/settings.json`.
