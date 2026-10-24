# Roman Mednitzer · Public profile

Static personal website: **[rmednitzer.github.io](https://rmednitzer.github.io/)**.

A personal introduction bringing together practical systems engineering, independent AI-assisted projects and interests in technology, science fiction and music. Projects precede professional experience; interests have a dedicated section. The two featured projects are **relay-shell** and **osint-workbench**. Professional history, private experiments and personal interests remain distinct.

## Site

- `index.html`: canonical public profile and matching Person/ProfilePage JSON-LD.
- `legal.html`: legal notice and privacy information.
- `style.css`: shared layout, dark/light/high-contrast/print styles.
- `index.md`, `llms.txt`, `profile.json`: alternative public profile formats. They carry the same factual boundaries; they are not a promise of indexing or AI-search placement.

Plain HTML/CSS, no build step, no framework or runtime package dependencies. Fonts and images are self-hosted; Spotify is an outbound listening-profile link, not an embedded player. Existing public anchors are retained.

Pages deploys only the exact files in `.github/pages-files.txt`, not the repository
root. Development documentation and editorial history are not website assets.
The repository and its history are still public. See
[publication verification](docs/operations/publication.md) and [ADR 0011](docs/adr/0011-allowlisted-publication.md).

## Validation

Use the HTML validator pinned in `.github/workflows/validate.yml`. Run the dependency-free checks for CSP hashes, colour contrast, links and public-profile consistency. For visual changes, also check desktop/mobile, keyboard navigation, no-JavaScript rendering, light/dark themes and print. See `CONTRIBUTING.md`.

## Privacy and licensing

Publish only the reviewed public profile. Do not copy private CVs, phone numbers, addresses, interview notes, hostnames, credentials, topology or operational logs into source, issues, commits or PRs.

Code: [Apache-2.0](LICENSE). Content: © Roman Mednitzer. Fonts: [OFL 1.1](fonts/README.md). See [NOTICE](NOTICE) and the [legal notice](https://rmednitzer.github.io/legal).
