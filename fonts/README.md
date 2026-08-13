# Fonts

Self-hosted WOFF2 subsets, loaded by [`fonts.css`](fonts.css). Nothing here is
fetched from Google Fonts or any other CDN at runtime, which is both a privacy
property (no third-party request carrying the visitor's IP and user agent) and
a CSP property (no external origin to allow).

## What is here

| Family | Role | Weights | Licence |
| ------ | ---- | ------- | ------- |
| Outfit | `--font-body` | 400, 500, 600 | [OFL 1.1](OFL-Outfit.txt) |
| DM Mono | `--font-mono` | 400, 500 | [OFL 1.1](OFL-DMMono.txt) |

Each weight ships as two files, `latin` and `latin-ext`, split by
`unicode-range` so a visitor who never renders a Latin Extended glyph never
downloads that subset.

## Licensing

Self-hosting makes this repository a **redistributor** of both families. SIL
Open Font License 1.1 clause 2 permits that, on the condition that each copy
carries the copyright notice and the licence text:

> Original or Modified Versions of the Font Software may be bundled,
> redistributed and/or sold with any software, provided that each copy
> contains the above copyright notice and this license.

`OFL-Outfit.txt` and `OFL-DMMono.txt` are the upstream licence files, copied
verbatim, and they satisfy that condition. Do not edit them, and do not delete
one while its `.woff2` files are still present.

Neither family declares a Reserved Font Name, so clause 3 imposes no naming
restriction. The OFL covers the font binaries only; it does not reach the
site's own code, which is Apache-2.0. See [`../NOTICE`](../NOTICE) for the full
split.

## Adding a weight

1. Add the `.woff2` files (both `latin` and `latin-ext` subsets).
2. Add the matching `@font-face` rules to `fonts.css`, keeping the
   `unicode-range` values and `font-display: swap`.
3. If it is a primary weight, add a `<link rel="preload">` to each page.
4. If the weight comes from a **new family**, add that family's upstream
   `OFL.txt` here as `OFL-<Family>.txt` and record it in `../NOTICE`. A new
   family without its licence file is a redistribution defect, not a style
   choice.
