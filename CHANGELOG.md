# Site Patch Changelog -- 2026-05-06 (batch 2)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Renamed `Live Work` section to `Open-Source Work` (id `live-work-h` → `open-source-h`) | Section now spans static governance-as-code repositories alongside the live sentinel corpus; "Live Work" was too narrow |
| 2 | Added 5 governance-as-code entries to Open-Source Work: platform-assurance, cps-assurance, autonomous-platform-assurance, operator-resilience, isms | Surfaces the legible governance artifact layer to recruiters and search; the site previously claimed work in this area but provided no clickthrough verification |
| 3 | Added `More repositories at github.com/rmednitzer` link below the list | Acknowledges the rest of the public namespace without cluttering the curated list |
| 4 | Updated hero subtitle, `<title>`, meta description, og:title/description, twitter:title/description, JSON-LD jobTitle and description from `Infrastructure & Compliance Engineering` to `Linux Infrastructure, Platform Operations, Systems Assurance` (or middle-dot variant for hero) | CV-attested tagline; the previous text understated the actual scope |
| 5 | Changed `og:locale` from `en_US` to `en_AT` | Locale matches actual residence and primary audience |
| 6 | Updated JSON-LD `dateModified` to 2026-05-06 | Reflects this batch and the prior sentinel cross-reference merge |
| 7 | Extended JSON-LD `knowsAbout` with: Human-Autonomy Teaming, Behavioral Contracts, Cyber-Physical Systems, STPA, Cyber Resilience Act, Machinery Regulation, Boundary Contracts | These are the differentiating keywords matching the article and repo body of work; previously absent from the structured-data surface |

## `enforceable-boundary-contracts.html`, `behavioral-contracts-human-autonomy-teaming.html`, `it-operations-architecture.html`, `agentic-ai-regulated-infrastructure.html`, `legal.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Changed `og:locale` from `en_US` to `en_AT` | Site-wide locale alignment |

## `feed.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated `<subtitle>` to new tagline | Site-wide tagline alignment |
| 2 | Updated feed-level `<updated>` to 2026-05-06T00:00:00Z | Feed staleness signal for crawlers |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Bumped `<lastmod>` for `/` and `/behavioral-contracts-human-autonomy-teaming` to 2026-05-06T00:00:00Z | Index and HAT article both modified by recent merges |

## `site.webmanifest`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated `name` and `description` to new tagline | Site-wide tagline alignment |

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added missing article entry: Behavioral Contracts for Human-Autonomy Teaming | The page existed; the README index lagged |
| 2 | Reordered article table reverse-chronologically | Most recent article first matches the index.html Writing list order |
| 3 | Updated tagline | Site-wide tagline alignment |

## `CLAUDE.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated `Topic` line | Site-wide tagline alignment |

---

# Site Patch Changelog -- 2026-05-06

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
