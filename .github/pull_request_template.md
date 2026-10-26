## Description

<!-- What does this PR change, and why? -->

## Type of change

- [ ] Bug fix (layout, link, metadata)
- [ ] Accessibility fix
- [ ] Styling (`style.css`)
- [ ] Content or legal text
- [ ] CI, tooling, or documentation

## Gate

Run the complete gate using the version pinned in the workflow:

- [ ] `npx -y html-validate@11.17.0 index.html legal.html`
- [ ] `python3 .github/scripts/check_csp_hashes.py`
- [ ] `python3 .github/scripts/check_contrast.py`
- [ ] `python3 .github/scripts/check_links.py`
- [ ] `python3 .github/scripts/check_profile.py`
- [ ] `python3 -m unittest discover -s .github/scripts -p 'test_*.py' -v`

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
