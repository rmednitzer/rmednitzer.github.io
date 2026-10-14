# Security policy: rmednitzer.github.io

## Reporting a vulnerability

Use [GitHub private vulnerability reporting](https://github.com/rmednitzer/rmednitzer.github.io/security/advisories/new).
Do not post exploit payloads, secrets, personal data or sensitive operational
details in public issues. If private reporting is unavailable, use an existing
maintainer security contact where published; otherwise request a private channel
with a minimal, non-sensitive issue. Do not assume an invented email address works.

Include the affected revision/version and paths, prerequisites and trust boundary,
expected versus actual behavior, a minimal sanitized reproduction, impact and any
workaround. Use synthetic data. A dependency issue affecting this project is in
scope: coordinate upstream as appropriate without delaying notification here.
This policy does not authorize testing third-party or live deployments, service
disruption, credential use, persistence or access to other people's data.

Existing response targets are retained below as maintainer goals, not guaranteed
service levels. Coordinate disclosure and advisory timing with the maintainer;
urgent active exploitation or credential exposure should be identified immediately.

## Contributor security requirements

Follow [AGENTS.md](AGENTS.md) for secure coding, dependency/CI integrity, verification,
STPA and threat-analysis requirements. Preserve deployment trust boundaries and
document exceptions, residual risk and recovery. Never suppress a security finding
merely to pass CI. For fixes, capture a reproducer, add a meaningful regression,
check adjacent paths, assess affected versions and coordinate remediation/advisories.
Code review and CI do not prove deployed configuration or legal compliance.

## Support and response targets

Security fixes apply to the current main branch. This static personal website
has no existing response-time commitment; coordinate privately with the maintainer.

## Scope and privacy

Report malicious content injection, CSP weaknesses, publishing-workflow compromise,
unexpected third-party requests, sensitive public content and relevant dependencies.
Static hosting reduces server-side application scope but does not remove browser,
supply-chain or privacy risks. Preserve self-hosted assets, restrictive CSP and
reviewed hashes, no tracking, license notices and accessible semantic content.

Do not include personal or private operational details in public reproductions.
The machine-readable contact is [.well-known/security.txt](.well-known/security.txt).
Keep its contact and expiry valid; legal.html must describe actual site behavior.
Browser/meta CSP cannot provide every HTTP response-header control on Pages;
assess hosting limitations explicitly instead of claiming full hardening.
