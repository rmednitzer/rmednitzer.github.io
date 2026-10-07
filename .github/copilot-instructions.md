# Copilot Instructions

## Project

Static personal website for Roman Mednitzer, hosted on GitHub Pages at `rmednitzer.github.io`.

## Stack

- Pure HTML/CSS — no build step, no JavaScript framework, no bundler
- Self-hosted fonts (Outfit + DM Mono WOFF2) in `fonts/`
- GitHub Pages serves directly from the repo root

## Conventions

- Voice: first-person, plain, systems-minded, and concrete. Explain why a system exists and how failure/recovery/authority are handled; avoid résumé/SEO noun stacks and generic professional claims.
- Human-facing section order is deliberate: About -> Experience -> Technical scope -> Personal projects -> Lab.
- `relay-shell`, `infra`, and `automation` are representative personal projects. Keep the explicit AI-assisted-work boundary; do not present them as professional software-development experience.
- All pages share `style.css` — do not add inline styles or page-specific stylesheets
- Colours come from the `:root` custom properties; CI holds `--fg`, `--fg-strong`, `--muted`, and `--accent` to 4.5:1 against `--bg` and `--bg-surface` in every palette (`.github/scripts/check_contrast.py`)
- Editing an inline `<style>`/`<script>` block means recomputing its `sha256` in that page's meta CSP (`.github/scripts/check_csp_hashes.py`)
- HTML pages are self-contained with clean, semantic markup
- Fonts are loaded from `fonts/` — never reference external CDNs (e.g. Google Fonts); a new font family must ship its upstream `OFL.txt` as `fonts/OFL-<Family>.txt` and be recorded in `NOTICE` (OFL 1.1 § 2 redistribution condition)
- Keep private details out of this repo (no phone, address, or day-level dates)
- Update `sitemap.xml` when adding or renaming pages
- Keep `index.md`, `llms.txt`, and `profile.json` aligned with the canonical facts and JSON-LD in `index.html`; avoid volatile lab counts and topology in machine-readable profile data
- Images: prefer WebP with PNG fallback; optimise before committing

## Key files

- `index.html` — Profile landing page (single-page site)
- `legal.html` — Impressum / DSGVO / MedienG legal notice
- `style.css` — Shared stylesheet
- `favicon.svg` — Site favicon
- `site.webmanifest` — PWA manifest
- `sitemap.xml` — Sitemap for search engines
- `index.md` — Markdown representation of the public profile
- `llms.txt` — Concise AI-readable public profile
- `profile.json` — Dated machine-readable public profile
- `.github/workflows/validate.yml` — CI gate: html-validate, data files, CSP hashes, contrast budget, internal links
