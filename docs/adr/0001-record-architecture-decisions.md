# Record architecture decisions as ADRs

- Status: accepted
- Date: 2026-06-12
- Deciders: repository owner (introduced by the 2026-06-12 audit pass)

## Context and problem statement

The repository's significant decisions (no build step, self-hosted
fonts, hosting model, stylesheet policy) lived implicitly in CLAUDE.md
conventions and CHANGELOG batches. Rationale was scattered or
unrecorded, which makes future changes harder to evaluate.

## Decision outcome

Keep architecture decision records in `docs/adr/`, MADR style, numbered
`NNNN-title.md`, each with a status field (proposed / accepted /
superseded) and a date. Decisions already embodied in the code are
backfilled with status accepted and explicitly marked where the original
rationale is reconstructed from evidence rather than known.

### Consequences

- Good: future structural proposals (CSP, CI, asset pruning) have a
  place to be argued and decided.
- Bad: one more artifact to keep current; a stale ADR log is worse than
  none, so superseding records must update status fields.
