# Add a hash-based meta Content-Security-Policy to both pages

- Status: proposed
- Date: 2026-06-12
- Deciders: repository owner (decision pending)
- Source: audit findings S-01 and S-02, backlog B-01

## Context and problem statement

GitHub Pages cannot set HTTP response headers, so the usual CSP,
X-Frame-Options, and frame-ancestors hardening is unavailable
server-side (ADR 0004). The only available mechanism is
`<meta http-equiv="Content-Security-Policy">`, which can restrict
script/style/img/font sources but cannot express frame-ancestors or
reporting.

The site's actual exposure is small: no authentication, no user input,
one constant inline script per page. CSP here is defense in depth
against platform-level compromise, not a fix for an existing hole.

## Considered options

1. Hash-based meta CSP, for example:
   `default-src 'none'; img-src 'self'; style-src 'self' 'sha256-...';
   font-src 'self'; script-src 'sha256-...'; base-uri 'none';
   form-action 'none'`.
   The year-updater script is byte-identical on both pages (one hash);
   the index `<style>` block needs its own hash or `'unsafe-inline'`
   for style-src. JSON-LD data blocks are not executed and need no
   allowance.
2. Meta CSP with `'unsafe-inline'` for style only, hash for script.
3. No CSP (status quo), documented as an accepted residual risk.

## Decision outcome

Pending owner decision. The audit did not apply option 1 because every
future edit to the inline style block or year script silently breaks
the page or the script for visitors (a wrong hash fails closed), which
trades a low-likelihood risk for a recurring operational hazard on a
hand-edited site with no CI. If ADR 0009 (CI validation) is accepted
first, a CI step can recompute and verify the hashes, removing the main
argument against option 1.

### Consequences (if option 1 or 2 is adopted)

- Good: injected or platform-tampered scripts and third-party loads are
  blocked client-side.
- Bad: hash maintenance on every inline-content edit; meta CSP still
  cannot prevent framing.
