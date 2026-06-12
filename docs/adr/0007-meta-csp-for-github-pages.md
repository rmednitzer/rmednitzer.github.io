# Add a hash-based meta Content-Security-Policy to both pages

- Status: accepted
- Date: 2026-06-12 (proposed and accepted the same day; owner approved
  the backlog burn-down with ADR 0009 landing first)
- Deciders: repository owner
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

Option 1, accepted and implemented after ADR 0009 landed, which removed
the main argument against it: `.github/scripts/check_csp_hashes.py`
recomputes the hashes of every bare inline `<script>`/`<style>` block
on both pages and fails CI when a hash is missing from the page's meta
CSP, so silent breakage cannot reach main through a pull request. Both
pages carry one canonical policy: `default-src 'none'; base-uri 'none';
form-action 'none'; img-src 'self'; style-src 'self' 'sha256-...';
script-src 'sha256-...'; font-src 'self'; manifest-src 'self'`. The
style hash is unused on legal.html (which has no inline style block)
and harmless there; frame-ancestors remains inexpressible via meta and
stays an accepted residual (documented in the audit register, S-01).

### Consequences (if option 1 or 2 is adopted)

- Good: injected or platform-tampered scripts and third-party loads are
  blocked client-side.
- Bad: hash maintenance on every inline-content edit; meta CSP still
  cannot prevent framing.
