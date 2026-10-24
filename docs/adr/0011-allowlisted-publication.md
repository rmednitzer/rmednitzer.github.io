# Publish an explicitly allowlisted artifact

- Status: accepted
- Date: 2026-10-24
- Supersedes: ADR 0004's repository-root publication decision
- Scope: website publication, not repository visibility or history

## Context

Serving the repository root made development guidance, historical audit reports
and editorial change notes reachable on the profile's website origin. Some old
editorial wording conflicted with the current biography. The owner authorised a
narrower publication boundary and cleanup of current editorial documentation.

## Options

1. No change: preserves deployment simplicity but also unintended public URLs.
2. robots.txt exclusions: influence cooperative crawling but do not stop serving
   the files and can obstruct removal of already indexed content.
3. Move all public files into a persistent subdirectory: workable, but changes
   source layout and requires migrating paths and existing checks.
4. Copy exact approved paths into a disposable artifact and publish that artifact.

## Decision

Use option 4. `.github/pages-files.txt` is the reviewed list of exact files.
`.github/scripts/stage_site.py` refuses missing inputs, path traversal, duplicate
entries, repository-only documents, symbolic/hard links and existing output. It
checks that the resulting file set and bytes match the allowlist and source.
Existing link/profile/CSP checks also exercise the staged site in tests.

`publish-pages` runs only for GitHub's main branch. Packaging has read-only
repository permissions; only the deployment job receives Pages write and OIDC
permissions. Deployment uses the existing main-only `github-pages` environment,
SHA-pinned official actions, a run-and-attempt-specific artifact and a stale-main
check. No PR job deploys. No application compilation, generator, external widget
or runtime dependency is added. The repository Pages setting must be `workflow`.

## Publication control and failure behaviour

Trust boundaries: reviewed source -> allowlist staging -> immutable workflow
artifact -> Pages deployment. The principal unwanted outcomes are publishing
repository-only material, publishing unvalidated/stale content, or losing the
site. Missing/bad inputs and failed validation prevent upload/deployment; failed
packaging leaves the existing deployed site unchanged. A new main commit can
still arrive after the final main-SHA check; deployment serialization and the
subsequent current-main run limit that race, not a claim of atomic branch locking.

Unknown paths return the hosting platform's normal 404 response. Required public
files, `.well-known/security.txt`, font licences and code attribution remain
included. No catch-all redirect or robots exclusion conceals missing content.

## Verification and rollback

Before merging, run source validation and publication regression tests. Check
staged links, exact bytes/file membership, and mobile/desktop rendering. After
deployment, compare live public files with the artifact and verify excluded
paths return 404, including documentation, scripts and source-only images.

Preferred content rollback: revert a faulty content commit while retaining this
publication boundary, then redeploy the current main revision. If deployment
code fails, fix/revert that code under the same allowlist and rerun. Do not switch
back to legacy root publication as a routine rollback: that would re-expose the
excluded documents. Previous Git revisions remain available for recovery.

## Limits

The source repository and its Git history remain public. This change is not
confidential storage, history erasure, a CDN-cache purge or a promise of search
removal. Index updates require recrawling. Search Console requires separately
authorised account access. Crawler policy is unchanged. The existing non-EU
hosting provider is retained; this change makes no sovereignty claim.

## References

- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
