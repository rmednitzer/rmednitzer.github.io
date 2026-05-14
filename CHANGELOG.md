# Site Patch Changelog -- 2026-05-14 (batch 5: review fixes for PR #31)

## `legal.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed `<link rel="alternate" type="application/atom+xml">` pointing at the deleted `feed.xml` | Codex review on PR #31: discoverable URL now 404s after feed removal |

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Repointed `sentinel` Open-Source tile from `/sentinel/` to `https://github.com/rmednitzer/sentinel` | Copilot review on PR #31: local `/sentinel/` path is not present in the repo and would 404 on GitHub Pages |

## Removed directory

| Path | Rationale |
|------|-----------|
| `scripts/` (`generate-og-images.js`, `package.json`) | Copilot review on PR #31: script hard-codes the four removed article slugs. Site is now single-page; the only OG image needed is the profile portrait, so the generator and its `scripts/` housing are dead code |

## `CLAUDE.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed all `scripts/`-related notes (Stack bullet, Layout entry, OG-image guidance, "Things to avoid" `scripts/node_modules/` mention) and simplified the OG guidance to "site OG image is the profile portrait" | Reflects deletion of `scripts/` |

---

# Site Patch Changelog -- 2026-05-14 (batch 4: site simplification)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed Writing section entirely | User direction: simplify site to a single-page profile |
| 2 | Reduced Open-Source list from 10 to 5 entries: `platform-blueprint`, `isms`, `sentinel`, `ai-stack`, `core-graph` | User direction: cap repo list at 5; refocus on the most representative artifacts |
| 3 | Rewrote Current Focus paragraph; removed "Windows Server" mention | User direction |
| 4 | Tightened hero tagline, meta/OG/Twitter descriptions, About, and all four Domain card bodies | User direction: rework site text to be more focused |
| 5 | Removed `<link rel="alternate" type="application/atom+xml">` and `hasPart` array from ProfilePage JSON-LD | No articles remain to syndicate |

## Removed files

| File | Rationale |
|------|-----------|
| `behavioral-contracts-human-autonomy-teaming.html` | Writing block removed |
| `agentic-ai-regulated-infrastructure.html` | Writing block removed |
| `it-operations-architecture.html` | Writing block removed |
| `enforceable-boundary-contracts.html` | Writing block removed |
| `og-behavioral-contracts-human-autonomy-teaming.png` | Article OG card no longer used |
| `og-agentic-ai-regulated-infrastructure.png` | Article OG card no longer used |
| `og-it-operations-architecture.png` | Article OG card no longer used |
| `og-enforceable-boundary-contracts.png` | Article OG card no longer used |
| `feed.xml` | Atom feed had only the four removed articles |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed the four article entries; site now lists `/` and `/legal` only | Articles deleted |

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Reduced Pages table to Profile + Legal; updated tagline to match new hero | Site is now single-page |

## `CLAUDE.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed article-pages table, feed.xml references, per-article OG image conventions, "Atom alternate link" requirement, article-page-only markup notes, and Writing-section discoverability step | Reflect simplified single-page layout |

## `.github/copilot-instructions.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Replaced article filenames in Key files list with `legal.html` | Reflect simplified single-page layout |

---

# Site Patch Changelog -- 2026-05-14 (batch 3: trim batch-2 positioning back to conservative restore)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Reverted `<title>` / `og:title` / `twitter:title` to "Roman Mednitzer \| Senior Platform & Infrastructure Engineer · Linux · Kubernetes · GitOps" | User direction (Conservative restore only): drop the " · EU Assurance" extension that batch-2 added to the headline |
| 2 | Reverted `hero-sub` to "Vienna, AT · Senior Platform & Infrastructure Engineer · Linux · Kubernetes · GitOps" | Same — drop the " · Audit-Defensible Platform Ops · EU Assurance" extension |
| 3 | Reverted meta/OG/Twitter description and JSON-LD `description` to batch-1 form | Drop the "Governance-as-code via platform-blueprint; live HAT failure-mode corpus via sentinel" sentence; do not promote centerpieces in description text |
| 4 | Reverted JSON-LD `jobTitle` to "Senior Platform & Infrastructure Engineer" | Drop the " · Audit-Defensible Platform Ops · EU Assurance" extension |
| 5 | Reverted About paragraph 2 and Current Focus to batch-1 form | Drop the "Two active centerpieces — platform-blueprint and sentinel" prose; centerpieces stay in the Open-Source list rather than being promoted in body text |
| 6 | Reverted Open-Source list to batch-1 order: `platform-blueprint`, `platform-assurance`, `isms`, `ansible-ops`, `infra-ops`, `cps-assurance`, `autonomous-platform-assurance`, `operator-resilience`, `sentinel` | Sentinel back to its batch-1 position at the end; descriptions returned to short batch-1 form |
| 7 | Added new Open-Source entry: `6dof-ascent-sim` (Apache 2.0) | User direction: list it — high-fidelity 6DOF orbital launch vehicle simulation, ignition through LEO insertion |
| 8 | Trimmed Domain card 4 body text: removed inline `<code>platform-blueprint</code>` / `<code>sentinel</code>` references; kept the "Assurance & AI Governance" heading and the four-prong scope (governance-as-code mapping, agentic-AI guardrails + HAT, supply-chain, boundary contracts) | Voice-consistent with the reverted About / Current Focus prose; specific artifacts cross-referenced via Writing + Open-Source Work above |
| 9 | Trimmed Technologies tags: removed `Talos`, `VictoriaMetrics`, `Governance-as-Code` (accent), `Boundary Contracts` (accent), `Human-Autonomy Teaming`, `STPA`, `MCP`, `pgvector`, `Apache AGE` that batch-2 added | Conservative restore: re-add only what batch-1 removed (`Wazuh`, `MLOps`, `LLMOps`, `AI Governance` — all kept), not new positioning tags. Accent demoted on `AI Governance` to non-accent for matching tone |
| 10 | Trimmed JSON-LD `knowsAbout`: removed `Talos Linux`, `VictoriaMetrics`, `Governance-as-Code`, `Model Context Protocol`, `Graph Databases`, `pgvector`, `Apache AGE` that batch-2 added | Same rationale as the tag trim. Kept the originally-removed scope entries (`MLOps`, `LLMOps`, `AI Governance`, `Human-Autonomy Teaming`, `Behavioral Contracts`, `Cyber-Physical Systems`, `STPA`, `Boundary Contracts`) — these are what the user asked to put back |

Net result: batch-1 form everywhere except for (a) Apache 2.0 license suffixes on `ansible-ops` / `infra-ops` (Copilot review #2 fix, retained), (b) Domain card 4 "Assurance & AI Governance" rename with broader scope text (per user instruction to "put back Domain text I removed"), (c) `knowsAbout` and Technologies tag restorations of the AI/HAT/governance entries that batch-1 removed (per user instruction), and (d) new `6dof-ascent-sim` Open-Source entry.

---

# Site Patch Changelog -- 2026-05-14 (batch 2: rebalance + Copilot review fixes)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Extended `<title>` / `og:title` / `twitter:title` to "Senior Platform & Infrastructure Engineer · Linux · Kubernetes · GitOps · EU Assurance" | Copilot review (PR #30): previous social-preview titles still surfaced the deprecated "Linux Infrastructure, Platform Operations, Systems Assurance" wording inconsistent with new descriptions and hero-sub |
| 2 | Extended `hero-sub` to include "Audit-Defensible Platform Ops · EU Assurance" | Restores the right half of the LinkedIn headline that batch-1 truncated |
| 3 | Reorganised Open-Source list to lead with `platform-blueprint` and `sentinel` as the two centerpieces | User direction: focus the narrative on the two active centerpieces; other governance-as-code repos remain as supporting context |
| 4 | Tightened repo descriptions for `platform-blueprint` and `sentinel`; promoted `sentinel` from last to second position | Centerpieces deserve descriptive lines, not just slug + license |
| 5 | Added `· Apache 2.0` suffix to `ansible-ops` and `infra-ops` entries | Copilot review (PR #30): license metadata omitted vs. surrounding entries; verified both repos are Apache-2.0 via repo landing page |
| 6 | Renamed Domain card 4 "Assurance & Supply-Chain" → "Assurance & AI Governance"; rewrote body to name `platform-blueprint`, `sentinel`, and supply-chain fundamentals as the four prongs | Batch-1 narrowed this card to supply-chain only; that undersold the governance-as-code + agent-runtime work that the public portfolio actually contains |
| 7 | Restored AI/HAT/governance tags to Technologies: `Governance-as-Code` (accent), `AI Governance` (accent), `Boundary Contracts` (accent), `Human-Autonomy Teaming`, `STPA`, `MLOps`, `LLMOps`, `MCP`, `pgvector`, `Apache AGE`, `Talos`, `VictoriaMetrics`, `Wazuh` | Each tag corresponds to a public artifact: platform-blueprint (governance-as-code, AI governance), operator-resilience + sentinel (HAT, behavioral contracts, STPA), ai-stack + sentinel (MLOps/LLMOps), isms-mcp + vertex (MCP), core-graph (pgvector/AGE), fleet host axiom (Talos, VictoriaMetrics, Wazuh) |
| 8 | Restored `knowsAbout` entries that batch-1 removed: `MLOps`, `LLMOps`, `AI Governance`, `Human-Autonomy Teaming`, `Behavioral Contracts`, `Cyber-Physical Systems`, `STPA`, `Boundary Contracts`, `Model Context Protocol`, `Graph Databases`, `pgvector`, `Apache AGE`, `Governance-as-Code`, `Talos Linux`, `VictoriaMetrics`, `Wazuh`, `Machinery Regulation` | These map 1:1 to public repos or fleet hosts; batch-1 trimmed them as "writing topics" but the artifacts make them legitimate `knowsAbout` claims |
| 9 | Extended JSON-LD `jobTitle` to "Senior Platform & Infrastructure Engineer · Audit-Defensible Platform Ops · EU Assurance" | Mirrors LinkedIn headline; consistent with extended page title and hero-sub |
| 10 | Updated meta/OG/Twitter descriptions and JSON-LD `description` to name the two centerpieces explicitly | Single description string across all surfaces; centers the narrative on `platform-blueprint` + `sentinel` |
| 11 | Rewrote About paragraph 2 and Current Focus to name `platform-blueprint` and `sentinel` by slug | Concrete artifacts beat abstract framing; reader can click through directly |

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated tagline to byte-identically mirror the new `index.html` `.hero-tagline` paragraph | Copilot review (PR #30): README and hero tagline had drifted; align as single source of truth |

## `CHANGELOG.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Restored heading + `## README.md` table header for the orphaned 2026-05-06 batch-2 rows below | Copilot review (PR #30): markdown rendered as broken/ambiguous after the new 2026-05-14 entry was prepended; dated header verified via `list_commits` against `c5131b8` (PR #29, 2026-05-06 10:23 UTC) |

---

# Site Patch Changelog -- 2026-05-14 (batch 1)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Rewrote hero tagline, About, and Current Focus to align with profile (PDF) | Previous wording oversold "design" and "compliance evidence as byproduct" beyond what the operator-level role supports; now leads with what is actually done day-to-day |
| 2 | Updated `hero-sub` to "Senior Platform & Infrastructure Engineer · Linux · Kubernetes · GitOps" | Matches profile headline rather than three abstract focus areas |
| 3 | Re-tiered Technologies tags; removed Keycloak, Wazuh, Checkmk, Proxmox, Zarf, MLOps, LLMOps, AI Governance | None of these appear in profile experience; removing avoids implying hands-on use |
| 4 | Added Windows Server, KVM, Argo CD, OpenTofu, Zabbix, Sigstore, Backup/DR; accented Argo CD, Ansible, Prometheus, NIS2 | Reflects actual stack from profile (EBCONT/Kwizda/medPhoton) |
| 5 | Rewrote Domains "Governance & Compliance" → "Audit-Facing Operations" and "Assurance & AI Integration" → "Assurance & Supply-Chain" | Drops claims of "observability for AI/ML workloads" and "policy-as-code controls"; keeps what is supported by profile (SBOM/SLSA/Sigstore fundamentals, ISO 27001/NIS2 alignment) |
| 6 | Expanded Open-Source list with `platform-blueprint`, `ansible-ops`, `infra-ops`; removed `isms` placeholder note since repo is live | Surfaces operational/IaC repos alongside governance-as-code repos so the mix reflects the actual day job, not only research |
| 7 | Trimmed `knowsAbout` in ProfilePage JSON-LD; removed MLOps, LLMOps, AI Security, AI Governance, Human-Autonomy Teaming, Behavioral Contracts, Cyber-Physical Systems, STPA, Boundary Contracts | These are writing topics, not operational expertise — moved out of the "knows about" claim list |
| 8 | Added `knowsLanguage: ["de", "en"]` to JSON-LD | Profile is bilingual; previously omitted |
| 9 | Updated `jobTitle` from "Linux Infrastructure, Platform Operations, Systems Assurance" to "Senior Platform & Infrastructure Engineer" | Matches profile headline |
| 10 | Updated meta/OG/Twitter descriptions and JSON-LD `description` | Same rationale as 1 — replaced marketing line with profile-accurate one |
| 11 | Bumped `dateModified` to 2026-05-14 | Index content changed substantively |

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated public tagline to match new index tagline | Single source of truth |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Bumped `lastmod` on `/` to 2026-05-14 | Index content changed substantively |

---

# Site Patch Changelog -- 2026-05-06 (batch 2: accuracy pass, PR #29)

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | (row content lost from upstream merge; rows 2 and 3 below are preserved as-committed) | — |
| 2 | Reordered article table reverse-chronologically | Most recent article first matches the index.html Writing list order |
| 3 | Updated tagline | Site-wide tagline alignment |

## `CLAUDE.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated `Topic` line | Site-wide tagline alignment |

---

# Site Patch Changelog -- 2026-05-06 (batch 1: sentinel cross-reference, PR #28)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added new `Live Work` section between Writing and Domains | Surface shipped empirical work alongside theoretical writing. Mirrors `.writing-list` styling. Single entry: link to `/sentinel/`, the continuous HAT failure-mode classification corpus |

## `behavioral-contracts-human-autonomy-teaming.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added one paragraph after the seventh structural-gap paragraph (field study gap) | Cross-references `/sentinel/` as a small counter-example operating in deployed conditions, with explicit acknowledgement of N=1 and LLM-derived classification limits |

---

# Site Patch Changelog -- 2026-03-28 (batch 2)

## `style.css`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `.page--article` shared layout class | Extracted from duplicated `<style>` blocks across article pages |
| 2 | Added `.writing-list li + li` spacing rule | Replaced inline `style="margin-top: .5rem;"` on index.html |
| 3 | Added `.article-related` component styles | Replaced inline styles on related article nav blocks across all article pages |

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Moved Writing section above Domains | Writing is the strongest differentiator and should be seen first |
| 2 | Rewrote About to lead with thesis, not timeline | The differentiating value prop was buried behind a CV opening line |
| 3 | Rewrote Current Focus to be specific and non-overlapping with About | Previous text restated the About thesis |
| 4 | Changed `<div class="page" role="main">` to `<main class="page">` | Semantic HTML |
| 5 | Removed inline `margin-top` styles from writing list items | Moved to style.css per project conventions |
| 6 | Updated animation-delay sequence for new section order | Maintains stagger after reorder |

## `enforceable-boundary-contracts.html`, `it-operations-architecture.html`, `agentic-ai-regulated-infrastructure.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `page--article` class to `.page` div | Uses shared layout from style.css |
| 2 | Removed duplicated `.page` / animation CSS from `<style>` blocks | Now in style.css |
| 3 | Replaced inline styles on `.article-related` with classes | Moved to style.css per project conventions |

## `.well-known/security.txt`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Changed Policy URL from `/` to `/legal` | Points to dedicated legal notice page |

---

# Site Patch Changelog — 2026-03-28

## New file: `legal.html`
- Dedicated legal notice page: Impressum (§ 5 ECG), Offenlegung (§ 25 MedienG), Datenschutzerklärung (DSGVO), copyright notice, liability disclaimer
- Satisfies "large website" Offenlegungspflicht including grundlegende Richtung
- Linked from footer on all pages

## `index.html`, `enforceable-boundary-contracts.html`, `it-operations-architecture.html`, `agentic-ai-regulated-infrastructure.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Replaced inline impressum text in footer with link to `/legal` | Dedicated legal page is cleaner and satisfies MedienG requirement for clearly labelled, easily accessible legal notice |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `/legal` entry (priority 0.3, yearly) | New page needs to be discoverable |

---

# Site Patch Changelog — 2026-03-07

All changes are non-breaking. No content was altered. Verify with diff before commit.

## New file: `favicon.svg`
- Extracted inline `data:` URI SVG to standalone file
- Enables browser caching across page navigations
- Both HTML pages now reference `/favicon.svg` instead of the data URI

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `<link rel="manifest" href="/site.webmanifest">` | Manifest existed but was unreferenced |
| 2 | Added `<link rel="sitemap" type="application/xml" href="/sitemap.xml">` | Aids crawler discovery |
| 3 | Changed `<link rel="icon">` from `data:` URI to `/favicon.svg` | Cacheable across navigations |
| 4 | Removed `:hover` styles from `.domain` and `.tag` | Non-interactive elements should not signal interactivity |
| 5 | Linked org names (IEEE, IEEE SMC, IEEE CIS, OCG) to their URLs | Already in JSON-LD but invisible to users |
| 6 | Rewrote "Current Focus" paragraph | Differentiate from "About" — now references specific regulation set and boundary contracts |
| 7 | Added `2026` fallback text inside `<span id="y">` | Renders correctly if JS is blocked |

## `enforceable-boundary-contracts.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `<meta name="google-site-verification">` | Present on index, missing here |
| 2 | Added `<meta property="article:modified_time">` | Required for crawlers to detect freshness on revision |
| 3 | Added `<link rel="manifest">` | Consistency with index |
| 4 | Added `<link rel="sitemap">` | Consistency with index |
| 5 | Changed `<link rel="icon">` to `/favicon.svg` | Consistency with index |
| 6 | Added `aria-current="page"` to breadcrumb current item | Accessibility: screen readers identify current page |
| 7 | Added `BreadcrumbList` JSON-LD block | Structured data for rich search results |
| 8 | Added `dateModified` to Article JSON-LD | Matches new `article:modified_time` meta |
| 9 | Added `2026` fallback text inside `<span id="y">` | JS-off resilience |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Index priority `0.8` → `1.0` | Landing page is canonical entry point |
| 2 | Article priority `0.9` → `0.8` | Subordinate to index |

## `site.webmanifest`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed `maskable` from 512×512 icon purpose | Portrait photo fails maskable safe-zone crop |

## NOT changed (deferred / optional)

- **Shared CSS file**: Both pages duplicate ~4 KB of identical CSS. Extract to `style.css` when adding a third page.
- **`_headers` / cache control**: GitHub Pages defaults are adequate. Revisit if migrating to Cloudflare Pages.
- **`security.txt` expiry**: Expires 2026-12-31. Calendar reminder to renew.

---

# Site Patch Changelog — 2026-03-24

## New directory: `fonts/`

Self-hosted WOFF2 font files replacing Google Fonts dependency.

| File | Weight | Purpose |
|------|--------|---------|
| `outfit-latin-{300,400,500,600}-normal.woff2` | 300–600 | Body text (latin) |
| `outfit-latin-ext-{300,400,500,600}-normal.woff2` | 300–600 | Body text (extended latin) |
| `dm-mono-latin-{400,500}-normal.woff2` | 400–500 | Monospace (latin) |
| `dm-mono-latin-ext-{400,500}-normal.woff2` | 400–500 | Monospace (extended latin) |

## New file: `fonts/fonts.css`

`@font-face` declarations for all self-hosted font files with correct unicode-range subsetting.

## `index.html`, `enforceable-boundary-contracts.html`, `it-operations-architecture.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed `dns-prefetch` and `preconnect` hints for `fonts.googleapis.com` and `fonts.gstatic.com` | No longer needed — fonts are served from the same origin |
| 2 | Removed `<link href="https://fonts.googleapis.com/css2?…" rel="stylesheet">` | Replaced by self-hosted fonts |
| 3 | Added `<link rel="preload">` for `outfit-latin-400-normal.woff2` and `outfit-latin-300-normal.woff2` | Hint browser to fetch most-used weights early, improving First Contentful Paint |
| 4 | Added `<link rel="stylesheet" href="/fonts/fonts.css">` | Loads self-hosted font declarations |

## `README.md`

Added site link, page index table, and tech notes for GitHub repository visitors.
