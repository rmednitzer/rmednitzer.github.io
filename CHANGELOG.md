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
