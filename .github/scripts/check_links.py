#!/usr/bin/env python3
"""Check that the site's links and asset references actually resolve.

Two modes, deliberately split so that only the deterministic half gates a
pull request:

  (default)    Internal links, asset references, in-page anchors, and the
               sitemap, resolved against the files on disk using GitHub
               Pages' own rules. Offline, fast, no false failures.

  --external   Reachability of off-site links. Runs on a schedule instead
               of on pull requests, because a rate-limited or
               bot-filtered host is not a reason to block a merge.

Extensionless URLs (/legal) resolve the way Pages serves them: exact file,
then <path>.html, then <path>/index.html.
"""
import argparse
import os
import re
import sys
import urllib.error
import urllib.request

PAGES = ('index.html', 'legal.html')
CSS_FILES = ('style.css', 'fonts/fonts.css')
SITEMAP = 'sitemap.xml'
SITE_ORIGIN = 'https://rmednitzer.github.io'

# Hosts that answer a real browser but not a CI runner; a failure here says
# nothing about whether the link is good. 999 is LinkedIn's own
# non-standard status for "request denied to a non-browser client" (seen
# regardless of User-Agent); treat it the same as the 403/429 bot-block cases.
EXTERNAL_TIMEOUT = 20
ACCEPTED_STATUSES = {200, 201, 202, 203, 204, 206, 301, 302, 303, 307, 308,
                     403, 429, 999}
USER_AGENT = ('Mozilla/5.0 (compatible; rmednitzer.github.io link check; '
              '+https://github.com/rmednitzer/rmednitzer.github.io)')

SKIP_SCHEMES = ('mailto:', 'tel:', 'data:', 'javascript:')


def references(html: str):
    """Every href/src in a document, in source order."""
    return re.findall(r'(?:href|src)="([^"]+)"', html)


def css_urls(css: str):
    return re.findall(r'url\(([^)]+)\)', css)


def resolve(path: str, relative_to: str) -> str | None:
    """Map a site path to a file on disk the way GitHub Pages would."""
    if path.startswith('/'):
        base = path.lstrip('/')
    else:
        base = os.path.normpath(os.path.join(os.path.dirname(relative_to),
                                             path))
    if base in ('', '.'):
        base = 'index.html'
    for candidate in (base, f'{base}.html', os.path.join(base, 'index.html')):
        if os.path.isfile(candidate):
            return candidate
    return None


def check_internal() -> list:
    failures = []

    for page in PAGES:
        html = open(page, encoding='utf-8').read()
        ids = set(re.findall(r'\sid="([^"]+)"', html))

        for ref in references(html):
            if ref.startswith(SKIP_SCHEMES):
                continue

            if ref.startswith('#'):
                if ref[1:] and ref[1:] not in ids:
                    failures.append(f'{page}: anchor {ref} has no matching id')
                continue

            if ref.startswith('http'):
                if ref.startswith(SITE_ORIGIN):
                    tail = ref[len(SITE_ORIGIN):] or '/'
                    if resolve(tail.split('#')[0], page) is None:
                        failures.append(
                            f'{page}: self-link {ref} does not resolve')
                continue

            target, _, fragment = ref.partition('#')
            resolved = resolve(target, page) if target else page
            if resolved is None:
                failures.append(f'{page}: {ref} does not resolve to a file')
            elif fragment and resolved == page and fragment not in ids:
                failures.append(f'{page}: anchor #{fragment} has no matching id')

    for css_file in CSS_FILES:
        css = open(css_file, encoding='utf-8').read()
        for url in css_urls(css):
            url = url.strip('\'"')
            if url.startswith(('http', 'data:')):
                failures.append(
                    f'{css_file}: {url} is an external reference; assets are '
                    f'self-hosted (ADR 0003)')
                continue
            if resolve(url, css_file) is None:
                failures.append(f'{css_file}: url({url}) does not resolve')

    sitemap = open(SITEMAP, encoding='utf-8').read()
    for loc in re.findall(r'<loc>([^<]+)</loc>', sitemap):
        if not loc.startswith(SITE_ORIGIN):
            failures.append(f'{SITEMAP}: {loc} is not on {SITE_ORIGIN}')
            continue
        tail = loc[len(SITE_ORIGIN):] or '/'
        if resolve(tail, SITEMAP) is None:
            failures.append(f'{SITEMAP}: {loc} does not resolve to a page')

    return failures


def check_external() -> list:
    targets = {}
    for page in PAGES:
        html = open(page, encoding='utf-8').read()
        for ref in references(html):
            if ref.startswith('http') and not ref.startswith(SITE_ORIGIN):
                targets.setdefault(ref, page)

    failures = []
    for url, page in sorted(targets.items()):
        request = urllib.request.Request(url, method='GET',
                                         headers={'User-Agent': USER_AGENT})
        try:
            with urllib.request.urlopen(request,
                                        timeout=EXTERNAL_TIMEOUT) as response:
                status = response.status
        except urllib.error.HTTPError as exc:
            status = exc.code
        except Exception as exc:                      # DNS, TLS, timeout
            failures.append(f'{page}: {url} -> {type(exc).__name__}: {exc}')
            continue

        if status in ACCEPTED_STATUSES:
            print(f'  ok  {status}  {url}')
        else:
            failures.append(f'{page}: {url} -> HTTP {status}')

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--external', action='store_true',
                        help='check off-site links instead of internal ones')
    args = parser.parse_args()

    failures = check_external() if args.external else check_internal()
    if failures:
        print('\n'.join(failures))
        return 1
    print('External links reachable' if args.external
          else 'Internal links, assets, anchors, and sitemap all resolve')
    return 0


if __name__ == '__main__':
    sys.exit(main())
