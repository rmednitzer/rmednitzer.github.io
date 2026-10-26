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

There is no application build step or application dependency installation. The gate requires Python 3 and Node.js 24 with npx; npx obtains the exact pinned HTML validator when needed. Edit the file, then run the gate.

### The gate

CI and publication run the same complete gate:

```sh
python3 .github/scripts/validate_site.py
```

The HTML validator version lives in that script and is tracked by Renovate.
The gate checks HTML, JSON/XML and JSON-LD, CSP, contrast, local references,
profile consistency, stylesheet versions and the publication/validator regressions.

When editing `style.css`, calculate its SHA-256 digest and use the first 12 hex
characters in `/style.css?v=<digest>` on both HTML pages. The gate rejects stale,
missing or duplicate version values. It checks content identity, not CDN state.

Off-site link reachability is checked weekly rather than per pull request, so a
rate-limited host never blocks a merge. Run it on demand with
`python3 .github/scripts/check_links.py --external`.

For a visual check:

```sh
python3 -m http.server --bind 127.0.0.1 8000
# open http://localhost:8000/
```

Extensionless URLs such as `/legal` resolve only on GitHub Pages. Locally, open
`/legal.html`.

### Enforced checks and review requirements

- **Editing an inline `<style>` or `<script>` without updating the CSP hash.**
  `check_csp_hashes.py` catches this. It is the most common surprise.
- **Changing `--fg`, `--fg-strong`, `--muted`, or `--accent`** so that any
  palette drops below 4.5:1 against `--bg` or `--bg-surface`. The budget is
  enforced across dark, light, both `prefers-contrast: more` variants, and
  print.
- **Adding an inline `style="…"` attribute** or referencing a stylesheet other than the shared site/font stylesheets. Shared styles belong in `style.css`.
- **Changing shared public-profile statements in only one format.** The profile check compares professional capabilities, project descriptions and limitations, attribution, lab context and personal perspective.
- **Missing a local image source, manifest icon or destination fragment.**

New pages require review of the page lists in the validators, the publication allowlist, sitemap and navigation; CI does not discover arbitrary new pages automatically.

## Conventions

The canonical workflow and conventions live in [`AGENTS.md`](AGENTS.md).
`CLAUDE.md` imports it; `.github/copilot-instructions.md` points to it and
summarises repository essentials. Keep those references consistent.

Append a dated technical section to [`CHANGELOG.md`](CHANGELOG.md) for substantive
changes. Do not copy superseded personal claims, private context or editorial
rationale into the log. Owner-authorised publication-hygiene condensation is
recorded explicitly; original revisions remain in Git history.

## Privacy

Do not add private data to this repository: no phone number, no street address,
no day-level dates of life events. The public e-mail address is fine. This
applies to issues and pull request descriptions too, not only to committed
files.

## Code of conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).


## Dependency automation

Renovate policy is owned by this repository in `renovate.json5`. It does not
inherit another project's policy. Keep update grouping, release-age delays,
major-version review and lock-maintenance behavior explicit here. Built-in
Renovate presets supply standard defaults; repository-specific decisions remain
local. Review policy changes and actual dependency extraction before merging.


## CI run ownership

The PR-validation workflows updated here coalesce first attempts for the same PR.
Manual reruns use separate run-ID/attempt groups, so rerunning an old revision
cannot cancel or replace current-head validation. Non-PR invocations also use
unique run-ID/attempt groups to preserve each revision's evidence.
GitHub does not guarantee chronological ordering of initial attempts: a late event
can still interrupt another initial attempt. Required checks bind to the current
head; a cancelled current-head check needs a successful rerun before merge.
Explicit diagnostic/publication serialization in other workflows remains separate. Reusable
workflows have distinct file prefixes to avoid cancelling a caller or sibling.
Cancelling an obsolete PR run is not a successful check; the current head still
needs all required results. Revision identity and signing gates remain separate.
Publication workflows retain their existing serialization and cache isolation.
Revert this repository's workflow change to restore the earlier scheduling;
no service deployment or application-data migration is involved.

## Publication boundary

GitHub Pages receives only the artifact selected by `.github/pages-files.txt`.
See [publication and retrieval verification](docs/operations/publication.md).
Do not deploy the repository root. The source repository remains public.
