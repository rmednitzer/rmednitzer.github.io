# Contributing

This is a personal website, not a community project. That shapes what is
useful to send.

## What is welcome

- **Bug reports.** Broken layout, a link that 404s, something that renders
  wrong in your browser, a validation error CI did not catch.
- **Accessibility findings.** Contrast, focus order, landmark structure,
  screen-reader behaviour, reduced-motion handling. These are the most valuable
  reports this repository can receive, because they are the hardest for one
  person to test alone.
- **Security reports.** Privately, see [`SECURITY.md`](SECURITY.md).
- **Small correctness fixes** as pull requests: typos, a stale link, a metadata
  tag that is wrong.

## What will be declined

- **Content changes.** The prose, the biography, and the portraits are personal
  content and rights reserved (see [`NOTICE`](NOTICE)). Corrections to a factual
  error are welcome as an issue; rewrites are not.
- **Redesigns**, or changes to the visual identity.
- **Adding a build step, framework, or bundler.** The site is deliberately pure
  HTML and CSS with no build. This is a standing constraint, not an oversight.
- **External CDN references** for fonts, CSS, or JS. Everything is self-hosted
  on purpose, for privacy and for the content security policy.

If you want to reuse the layout, take the code (Apache-2.0) and supply your own
content. You do not need permission for that, and you do not need to ask.

## Making a change

No build step, no dependencies to install. Edit the file, then run the gate.

### The gate

CI runs these on every pull request and they all run locally in about a second:

```sh
npx -y html-validate index.html legal.html
python3 .github/scripts/check_csp_hashes.py
python3 .github/scripts/check_contrast.py
python3 .github/scripts/check_links.py
```

Off-site link reachability is checked weekly rather than per pull request, so a
rate-limited host never blocks a merge. Run it on demand with
`python3 .github/scripts/check_links.py --external`.

For a visual check:

```sh
python3 -m http.server 8000
# open http://localhost:8000/
```

Extensionless URLs such as `/legal` resolve only on GitHub Pages. Locally, open
`/legal.html`.

### Things that will fail CI

- **Editing an inline `<style>` or `<script>` without updating the CSP hash.**
  `check_csp_hashes.py` catches this. It is the most common surprise.
- **Changing `--fg`, `--fg-strong`, `--muted`, or `--accent`** so that any
  palette drops below 4.5:1 against `--bg` or `--bg-surface`. The budget is
  enforced across dark, light, both `prefers-contrast: more` variants, and
  print.
- **Adding an inline `style="…"` attribute** or a per-page `.css` file. Shared
  styles belong in `style.css`, using the custom properties already defined
  there.
- **Adding a page without adding it to `sitemap.xml`.**

## Conventions

The full set lives in [`CLAUDE.md`](CLAUDE.md), which is the source of truth for
conventions in this repository and is mirrored for Copilot in
`.github/copilot-instructions.md`. Keep the two consistent.

Append a dated section to [`CHANGELOG.md`](CHANGELOG.md) for anything
non-trivial. Do not rewrite past entries.

## Privacy

Do not add private data to this repository: no phone number, no street address,
no day-level dates of life events. The public e-mail address is fine. This
applies to issues and pull request descriptions too, not only to committed
files.

## Code of conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
