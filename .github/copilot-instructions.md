# Copilot Instructions

## Project

Static personal website for Roman Mednitzer, hosted on GitHub Pages at `rmednitzer.github.io`.

## Stack

- Pure HTML/CSS — no build step, no JavaScript framework, no bundler
- Self-hosted fonts (Outfit + DM Mono WOFF2) in `fonts/`
- GitHub Pages serves directly from the repo root

## Conventions

- All pages share `style.css` — do not add inline styles or page-specific stylesheets
- HTML pages are self-contained with clean, semantic markup
- Fonts are loaded from `fonts/` — never reference external CDNs (e.g. Google Fonts)
- Keep private details out of this repo (no phone, address, or day-level dates)
- Update `sitemap.xml` when adding or renaming pages
- Images: prefer WebP with PNG fallback; optimise before committing

## Key files

- `index.html` — Profile landing page
- `style.css` — Shared stylesheet
- `enforceable-boundary-contracts.html` — Article
- `it-operations-architecture.html` — Reference architecture article
- `agentic-ai-regulated-infrastructure.html` — Article
- `favicon.svg` — Site favicon
- `site.webmanifest` — PWA manifest
- `sitemap.xml` — Sitemap for search engines
