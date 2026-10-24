# Public profile publication and retrieval verification

## Publish

1. Edit only reviewed public facts; keep the HTML and text/JSON representations aligned.
2. Review `.github/pages-files.txt` when an intended asset is added or removed.
3. Run the pinned HTML validator from `.github/workflows/validate.yml` and the existing Python checks.
4. Run `python3 .github/scripts/test_stage_site.py -v`.
5. Run `python3 .github/scripts/stage_site.py` into a new, disposable `_site` directory.
6. Review the staged page and verify it contains only the approved file list.
7. Merge through the protected main-branch PR workflow.
8. Confirm `publish-pages` deployed that revision, not merely that CI passed.
9. Compare public responses with the staged bytes; expect excluded development paths to return 404.

The Pages source is GitHub Actions (`build_type=workflow`). The protected
`github-pages` environment allows main only. Public files are copied, not built
by a static-site generator. Do not upload the repository root or weaken the
allowlist to repair a missing asset. A default `_site` already present must be
reviewed and intentionally removed by its owner or a fresh checkout used; the
staging program never removes or overwrites it.

## Check retrieval separately

Live HTTP content, search-index content and generated AI answers are different
observations. Record the observation date, exact URL, evidence and limitations.
Do not infer Google index state from an ordinary web-fetch cache or a successful
deployment. `llms.txt` and `profile.json` are supplementary representations, not
commands guaranteed to control third-party models.

With an authorised Google Search Console owner/full-user connection, inspect the
homepage's indexed version and last crawl. Request reindexing of the homepage
through URL Inspection when necessary. The URL Inspection API can read indexed
state but cannot itself submit a reindexing request. A valid sitemap remains
available at `/sitemap.xml`; do not use obsolete sitemap ping endpoints.

For source-only representation tests in a fresh browsing-enabled AI session,
use the canonical website and ask independently:

- What is this person's professional engineering background?
- What does the site say about personal AI-assisted projects and contribution?
- Which topics are interests rather than established professional specialisms?
- Does the site establish a current employer, recruitment status, auditor
  credential or academic degree? Report only what the supplied page states.
- Is the Spotify link a listening profile or an artist profile?

Acceptance: factual separation between professional work, personal projects and
interests; no invented current employer, credential, research career or artist
identity. Record the cited sources and their freshness. A single model's output
is not evidence for every model; do not call an in-context summary an independent
test. If authenticated indexing or independent AI access is unavailable, mark
those checks as unverified rather than reporting success.

## Public-source boundary

Historical Git revisions, public PR discussions and external caches may retain
superseded information. Do not describe removed website paths as private or
irretrievably deleted. Public repository documentation should discuss technical
changes without repeating private biographical context or obsolete personal
claims. Adding a caveat to a public document is not access control.
