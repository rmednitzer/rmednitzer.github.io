## Description

<!-- What does this PR change, and why? -->

## Type of change

- [ ] Bug fix (layout, link, metadata)
- [ ] Accessibility fix
- [ ] Styling (`style.css`)
- [ ] Content or legal text
- [ ] CI, tooling, or documentation

## Gate

- [ ] `python3 .github/scripts/validate_site.py`
- [ ] Both stylesheet URLs match the current CSS digest, if CSS changed
- [ ] Relevant browser checks completed; missing modes reported explicitly

## Checklist

- [ ] No inline `style="…"` attribute and no per-page `.css` file; shared styles went to `style.css` using the existing custom properties
- [ ] No external CDN reference for fonts, CSS, or JS
- [ ] No build step, framework, or bundler added
- [ ] Inline `<style>` or `<script>` changes have matching CSP hashes
- [ ] A palette change stays at or above the 4.5:1 contrast budget in every palette (dark, light, both `prefers-contrast: more` variants, print)
- [ ] A new or renamed page is in `sitemap.xml` and cross-linked from `index.html`
- [ ] `CHANGELOG.md` has a dated entry for anything non-trivial
- [ ] Agent guidance still points to canonical `AGENTS.md` if conventions changed
- [ ] No private data (phone, street address, day-level dates) in the diff
- [ ] A new font family ships its upstream `OFL.txt` in `fonts/` and is recorded in `NOTICE`
