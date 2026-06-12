# Prune or regenerate the orphaned portrait and font binaries

- Status: proposed
- Date: 2026-06-12
- Deciders: repository owner (decision pending)
- Source: audit findings Q-07 and Q-08, backlog B-03

## Context and problem statement

The 2026-06-12 audit found three orphan groups (binary deletion is
gated as an owner decision, so nothing was removed):

1. `profile_roman-mednitzer.png` (800x800, 646867 bytes, 56 % of the
   working tree) is referenced by nothing; CLAUDE.md documents it as
   the second, full-size portrait, so it may be an intentional
   source-of-truth master.
2. `profile_roman-mednitzer.webp` (9244 bytes) is byte-identical to
   `profile_roman-mednitzer-400.webp` (same SHA-256), so the "full
   size" WebP is a mislabeled duplicate, not an 800 px encode.
3. `fonts/outfit-latin-300-normal.woff2` and
   `fonts/outfit-latin-ext-300-normal.woff2` (20340 bytes combined)
   plus their two `@font-face` rules: no rule anywhere uses
   `font-weight: 300`. Browsers fetch fonts lazily, so visitors never
   download these; the cost is repo weight and a misleading fonts.css.

## Considered options

1. Keep the 800 px PNG as the documented master; delete the duplicate
   WebP; delete the Outfit 300 files and their @font-face rules.
2. Same as 1, but regenerate a real 800 px WebP (needs cwebp or
   similar, not available in the audit environment).
3. Keep everything (status quo) and fix only CLAUDE.md wording so the
   duplicate is not mistaken for an 800 px encode.

## Decision outcome

Pending owner decision. Option 1 is recommended: it removes 29584 bytes
of misleading assets (duplicate WebP + unused fonts), keeps the PNG
master, and requires updating the CLAUDE.md "two sizes" note plus a
CHANGELOG batch. Visitor-facing behavior does not change under any
option (none of these files is ever served to a visitor today).

### Consequences (option 1)

- Good: fonts.css describes only faces that exist for a reason; no
  mislabeled duplicate waiting to be wired in by mistake.
- Bad: if a future page wants weight 300 or an 800 px WebP, the assets
  must be re-produced.
