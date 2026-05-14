# CLAUDE.md — Project Instructions for Claude Code

## Project

Static single-page personal website for Roman Mednitzer, hosted on GitHub Pages at `rmednitzer.github.io`.
Topic: Linux Infrastructure, Platform Operations, Systems Assurance — Kubernetes, GitOps, ISO 27001, EU regulatory compliance (NIS2, CRA, AI Act).

## Stack

- Pure HTML/CSS — no build step, no JavaScript framework, no bundler
- Self-hosted fonts (Outfit + DM Mono WOFF2) in `fonts/`, loaded via `fonts/fonts.css`
- `.nojekyll` disables Jekyll processing
- GitHub Pages serves from the repo root

## Layout

```
/                              repo root = site root
├── index.html                  Profile landing page (single-page site)
├── style.css                   Shared stylesheet (single source of truth)
├── legal.html                  Impressum / DSGVO / MedienG legal notice
├── sitemap.xml                 Sitemap for crawlers
├── robots.txt                  Crawler directives
├── site.webmanifest            PWA manifest
├── favicon.{svg,ico}           Favicons (+ favicon-{32,180,192,512}.png)
├── profile_roman-mednitzer*    Profile portraits (PNG + WebP, 400px + full)
├── fonts/                      Self-hosted WOFF2 fonts + fonts.css
├── .well-known/security.txt    Security contact (Expires 2026-12-31 — renew)
├── .github/copilot-instructions.md   Mirror of conventions for GitHub Copilot
├── CHANGELOG.md                Site patch log (append-only, dated batches)
└── README.md                   Public README (page index for repo visitors)
```

## Conventions

### Styling

- **All shared styles live in `style.css`.** Use the CSS custom properties already defined there (`--fg`, `--bg`, `--accent`, `--font-body`, `--font-mono`, `--radius`, etc.) — do not introduce new colour or font literals.
- A `<style>` block in `<head>` is acceptable only for genuinely page-unique layout (e.g. the index hero grid). If a pattern appears on more than one page, promote it to `style.css`.
- **No inline `style="…"` attributes.** No page-specific `.css` files.
- Light/dark mode via `prefers-color-scheme` is already wired in `:root` — keep both palettes in mind when adding tokens.
- Animations sit behind `@media (prefers-reduced-motion: no-preference)`; preserve that gate.

### Markup

- HTML pages are self-contained — no templating engine. Keep markup clean and semantic (`<main>`, `<nav>`, etc.).
- Every page must include: canonical link, description meta, theme-color, favicon stack, manifest link, sitemap link, preload of `outfit-latin-400-normal.woff2`, then `fonts/fonts.css`, then `style.css`.
- Footer year uses `<span id="y">2026</span>` with a JS updater — keep the literal fallback so it renders with JS disabled.

### Assets

- **Fonts:** load only from `fonts/`. Never reference Google Fonts or other CDNs. When adding a weight, add the WOFF2 file, the `@font-face` rule in `fonts/fonts.css`, and (if it's a primary weight) a `<link rel="preload">` in each page.
- **Images:** prefer WebP with a PNG fallback. Optimise before committing. Profile portraits exist in two sizes (`-400` and full).
- **OG images:** the site OG image is the profile portrait (`profile_roman-mednitzer-400.png`).
- **Favicons:** `favicon.svg` is the primary; PNG fallbacks at 32/180/192/512. Update all if rebranding.

### Discoverability — when adding or renaming a page

1. Add the URL to `sitemap.xml` (set `lastmod`, `priority`, `changefreq`).
2. Cross-link from `index.html` where appropriate.

### Privacy & legal

- **No private details in this repo:** no phone, no street address, no day-level dates of life events. Public e-mail (`r.mednitzer@ieee.org`) is fine.
- `legal.html` covers Austrian Impressum (§ 5 ECG), Offenlegung (§ 25 MedienG), and DSGVO. If site content materially changes (e.g. new tracking, new contact channel, new legal entity), update `legal.html`.
- `.well-known/security.txt` has an `Expires` field — renew before it lapses.

### Sync points

- `.github/copilot-instructions.md` mirrors a subset of these conventions for GitHub Copilot. Keep it consistent when changing styling or layout rules here.
- `CHANGELOG.md` is the human-readable patch log — append a dated section for non-trivial changes (style.css additions, new pages, structural HTML changes). Don't rewrite history.

## Local validation

No build or test pipeline. Validate by serving locally and checking pages in a browser:

```sh
python3 -m http.server 8000
# open http://localhost:8000/
```

For HTML/structured-data sanity, paste a built page into the [Rich Results Test](https://search.google.com/test/rich-results) or run `npx -y html-validate <file.html>` if you want a quick lint.

## Things to avoid

- Adding a build step, framework, or bundler for the site itself
- External font/CSS/JS CDNs
- Inline `style="…"` attributes or per-page `.css` files
- Committing un-optimised images or anything containing private data
- Touching `legal.html` boilerplate without confirming the legal context still matches
