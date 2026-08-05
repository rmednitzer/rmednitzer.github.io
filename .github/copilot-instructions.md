# Copilot Instructions

## Project

Static personal website for Roman Mednitzer, hosted on GitHub Pages at `rmednitzer.github.io`.

## Stack

- Pure HTML/CSS — no build step, no JavaScript framework, no bundler
- Self-hosted fonts (Outfit + DM Mono WOFF2) in `fonts/`
- GitHub Pages serves directly from the repo root

## Conventions

- All pages share `style.css` — do not add inline styles or page-specific stylesheets
- Colours come from the `:root` custom properties; CI holds `--fg`, `--fg-strong`, `--muted`, and `--accent` to 4.5:1 against `--bg` and `--bg-surface` in every palette (`.github/scripts/check_contrast.py`)
- Editing an inline `<style>`/`<script>` block means recomputing its `sha256` in that page's meta CSP (`.github/scripts/check_csp_hashes.py`)
- HTML pages are self-contained with clean, semantic markup
- Fonts are loaded from `fonts/` — never reference external CDNs (e.g. Google Fonts)
- Keep private details out of this repo (no phone, address, or day-level dates)
- Update `sitemap.xml` when adding or renaming pages
- Images: prefer WebP with PNG fallback; optimise before committing

## Key files

- `index.html` — Profile landing page (single-page site)
- `legal.html` — Impressum / DSGVO / MedienG legal notice
- `style.css` — Shared stylesheet
- `favicon.svg` — Site favicon
- `site.webmanifest` — PWA manifest
- `sitemap.xml` — Sitemap for search engines
- `.github/workflows/validate.yml` — CI gate: html-validate, data files, CSP hashes, contrast budget, internal links
