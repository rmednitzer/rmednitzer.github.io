# Single shared stylesheet plus page-unique head styles; system-preference theming

- Status: accepted
- Date: 2026-06-12 (backfilled; the policy is written down in CLAUDE.md
  and has been enforced through the 2026-04/05 cleanup batches in
  CHANGELOG.md)
- Deciders: repository owner

## Context and problem statement

With no templating engine (ADR 0002), styling discipline is the only
thing preventing per-page divergence. The repo needs one obvious place
for shared visual language while allowing genuinely page-specific
layout to stay with its page.

## Decision outcome

- All shared styles live in `style.css`, driven by CSS custom
  properties (`--fg`, `--bg`, `--accent`, fonts, radius).
- A `<style>` block in a page `<head>` is allowed only for layout unique
  to that page (the index hero grid and cards); any pattern used by two
  pages must be promoted to `style.css`.
- No inline `style=""` attributes and no per-page `.css` files.
- Light and dark palettes are selected purely by
  `prefers-color-scheme`; there is no JS theme toggle.
- Motion (keyframe animation and, since the 2026-06-12 audit, smooth
  scrolling) sits behind `@media (prefers-reduced-motion: no-preference)`.

Evidence: CLAUDE.md "Styling" conventions; `style.css` `:root` blocks;
the index `<style>` block contents.

### Consequences

- Good: one source of truth for tokens; both palettes evolve together.
- Good: respects user motion and color-scheme preferences without any
  script.
- Bad: the boundary "page-unique vs shared" needs judgement; dead rules
  can linger in `style.css` after page removals (audit finding Q-06).
