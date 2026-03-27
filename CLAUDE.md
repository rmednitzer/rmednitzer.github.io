# CLAUDE.md — Project Instructions for Claude Code

## Project

Static personal website for Roman Mednitzer, hosted on GitHub Pages at `rmednitzer.github.io`.

## Stack

- Pure HTML/CSS — no build step, no JavaScript framework
- Self-hosted fonts (Outfit + DM Mono WOFF2) in `fonts/`
- `.nojekyll` disables Jekyll processing
- GitHub Pages serves from the repo root

## Key files

| File | Purpose |
|------|---------|
| `index.html` | Profile landing page |
| `style.css` | Shared stylesheet |
| `enforceable-boundary-contracts.html` | Article |
| `it-operations-architecture.html` | Reference architecture article |
| `agentic-ai-regulated-infrastructure.html` | Article |
| `favicon.svg` | Site favicon |
| `site.webmanifest` | PWA manifest |
| `sitemap.xml` | Sitemap for search engines |
| `robots.txt` | Crawler directives |

## Conventions

- All pages share `style.css` — do not add inline styles or page-specific stylesheets
- HTML pages are self-contained (no templating engine) — keep markup clean and semantic
- Fonts are referenced from `fonts/` — never load from external CDNs
- Keep private details out of this repo (no phone, address, or day-level dates)
- Update `sitemap.xml` when adding or renaming pages
- Images: prefer WebP with PNG fallback; optimise before committing

## Testing

No build or test pipeline — validate changes by opening HTML files in a browser or running a local HTTP server:

```sh
python3 -m http.server 8000
```
