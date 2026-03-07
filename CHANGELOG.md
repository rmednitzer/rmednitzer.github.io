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

- **Self-hosted fonts**: Would eliminate Google Fonts dependency (privacy, render-blocking). Requires downloading Outfit + DM Mono WOFF2 files and updating CSS `@font-face`. Recommend as a follow-up.
- **Shared CSS file**: Both pages duplicate ~4 KB of identical CSS. Extract to `style.css` when adding a third page.
- **`_headers` / cache control**: GitHub Pages defaults are adequate. Revisit if migrating to Cloudflare Pages.
- **`security.txt` expiry**: Expires 2026-12-31. Calendar reminder to renew.
