# Enforce a contrast budget and link integrity in CI

- Status: accepted
- Date: 2026-08-05
- Deciders: repository owner
- Supersedes nothing; extends ADR 0009 (CI validation on pull requests)

## Context and problem statement

ADR 0009 put html-validate and the data-file checks in CI, which catch
malformed markup. They do not catch two classes of defect that this site
is structurally prone to:

**Contrast.** The palette is a small set of custom properties consumed by
every rule, so a single token edit restyles both themes at once. There is
no build step and no browser test, so the only review a colour change
gets is the author's eye, in whichever theme happened to be active. That
failed in practice: `--muted` sat at 4.25:1 against `--bg-surface` in
dark mode, below the WCAG AA small-text ratio of 4.5:1, while carrying
most of the page's secondary text (every skill and principle tag, every
section lede, the footer, the hero subtitle). Light mode passed, which is
presumably why it survived review.

**Links.** The page is largely a set of pointers: repository links, asset
references, favicons, the manifest, the sitemap, and a skip link that has
to match an `id`. A renamed asset or a mistyped anchor degrades silently,
and the sitemap can drift from the pages that actually exist.

## Considered options

1. Two dependency-free Python scripts in `.github/scripts/`, matching the
   pattern ADR 0007 already established with `check_csp_hashes.py`, wired
   into the existing `validate` workflow.
2. An off-the-shelf accessibility runner (pa11y-ci, axe) plus a link
   checker action (lychee). Broader coverage, at the cost of a headless
   browser download per run, a new pinned third-party action, and
   findings that are mostly noise on a two-page static site.
3. Status quo: check by eye, per ADR 0009's manual-validation critique.

## Decision outcome

Option 1.

`check_contrast.py` parses the palette out of `style.css` and asserts a
4.5:1 floor for `--fg`, `--fg-strong`, `--muted`, and `--accent` against
both `--bg` and `--bg-surface`, across all five palettes the stylesheet
defines (dark, light, each one's `prefers-contrast: more` variant, and
print). It layers each media block's overrides on the palette it
inherits from, mirroring the cascade. Every one of those tokens is used
at small text sizes somewhere on the page, so all are held to the
small-text ratio rather than the 3:1 large-text one.

`check_links.py` has two modes. The default resolves internal links,
asset references, in-page anchors, CSS `url()` targets, and every
sitemap `<loc>` against the files on disk, using GitHub Pages' own
resolution order (exact file, then `<path>.html`, then
`<path>/index.html`) so that extensionless URLs like `/legal` are checked
the way they are served. It also fails any external reference appearing
in the stylesheets, which is ADR 0003's no-third-party-requests rule made
executable. `--external` checks off-site reachability and runs from a
separate weekly workflow, not on pull requests.

### Consequences

- Good: the specific regression that shipped cannot ship again, and the
  check is deterministic, offline, and adds no dependency, no browser
  download, and no measurable CI time.
- Good: a colour change now has to state its intent. Lowering the budget
  is a visible edit to the script rather than an invisible drift.
- Bad: the contrast check knows only what tokens declare. Hard-coded
  colours, opacity, and colours composited over `--accent-dim` are out of
  scope, so it is a floor and not a full audit.
- Bad: external link rot is found up to a week late. Accepted
  deliberately: gating merges on third-party availability would make CI
  fail for reasons no pull request can fix, and GitHub already answers CI
  runners with 403.
