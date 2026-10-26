#!/usr/bin/env python3
"""Check local page/asset/fragment references; optionally probe off-site links.

Run from the source or staged site root. External rate limits and access denials
are reported as inconclusive and do not block a merge. No browser is implied.
"""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

PAGES = ('index.html', 'legal.html')
CSS_FILES = ('style.css', 'fonts/fonts.css')
SITEMAP = 'sitemap.xml'
SITE_ORIGIN = 'https://rmednitzer.github.io'
EXTERNAL_TIMEOUT = 20
INCONCLUSIVE_STATUSES = {403, 429, 999}
USER_AGENT = ('Mozilla/5.0 (compatible; rmednitzer.github.io link check; '
              '+https://github.com/rmednitzer/rmednitzer.github.io)')
SKIP_SCHEMES = ('mailto', 'tel', 'data', 'javascript')


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.ids = set()
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if a.get(key):
                self.references.append(a[key])
        if a.get('srcset'):
            # This site's source sets contain local URLs and optional w/x descriptors.
            # Data URLs (which contain commas) are deliberately unsupported here.
            for candidate in a['srcset'].split(','):
                fields = candidate.split()
                if fields:
                    self.references.append(fields[0])


def references(html: str):
    return Document(html).references


def css_urls(css: str):
    return re.findall(r'url\(([^)]+)\)', css)


def is_external(url: str) -> bool:
    parts = urlsplit(url)
    origin = urlsplit(SITE_ORIGIN)
    return bool(parts.netloc) and (parts.netloc != origin.netloc or
                                  parts.scheme not in ('', origin.scheme))


def resolve(path: str, relative_to: str) -> str | None:
    path = unquote(urlsplit(path).path)
    base = Path(path.lstrip('/')) if path.startswith('/') else Path(relative_to).parent / path
    root = Path.cwd().resolve()
    if not (root / base).resolve().is_relative_to(root):
        return None
    if str(base) in ('', '.'):
        base = Path('index.html')
    for candidate in (base, Path(str(base) + '.html'), base / 'index.html'):
        if candidate.is_file():
            return str(candidate)
    return None


def check_internal() -> list[str]:
    failures = []
    documents = {name: Document(Path(name).read_text(encoding='utf-8')) for name in PAGES}
    for page, document in documents.items():
        for ref in document.references:
            parts = urlsplit(ref)
            if parts.scheme in SKIP_SCHEMES or is_external(ref):
                continue
            if parts.scheme not in ('', 'http', 'https'):
                failures.append(f'{page}: unsupported URL scheme: {ref}')
                continue
            target = resolve(ref, page) if parts.path or parts.netloc else page
            if target is None:
                failures.append(f'{page}: {ref} does not resolve to a file')
            elif parts.fragment:
                destination = documents.get(target)
                if destination is None and target.endswith('.html'):
                    destination = Document(Path(target).read_text(encoding='utf-8'))
                if destination is not None and unquote(parts.fragment) not in destination.ids:
                    failures.append(f'{page}: {ref} has no matching destination id')
    for css_file in CSS_FILES:
        for url in css_urls(Path(css_file).read_text(encoding='utf-8')):
            url = url.strip().strip('\'"')
            if urlsplit(url).scheme or urlsplit(url).netloc:
                failures.append(f'{css_file}: external reference {url}; assets must be self-hosted')
            elif resolve(url, css_file) is None:
                failures.append(f'{css_file}: url({url}) does not resolve')
    for icon in json.loads(Path('site.webmanifest').read_text(encoding='utf-8')).get('icons', []):
        if is_external(icon['src']) or resolve(icon['src'], 'site.webmanifest') is None:
            failures.append(f'site.webmanifest: icon {icon["src"]} does not resolve locally')
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for loc in ElementTree.parse(SITEMAP).findall('.//s:loc', ns):
        url = loc.text or ''
        if not url.startswith(SITE_ORIGIN + '/') or is_external(url) or resolve(url, SITEMAP) is None:
            failures.append(f'{SITEMAP}: {url} does not resolve to a site page')
    return failures


def check_external() -> list[str]:
    targets = {}
    for page in PAGES:
        for ref in references(Path(page).read_text(encoding='utf-8')):
            if is_external(ref):
                targets.setdefault(ref, page)
    failures = []
    inconclusive = 0
    for url, page in sorted(targets.items()):
        request = urllib.request.Request(url, method='GET', headers={'User-Agent': USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=EXTERNAL_TIMEOUT) as response:
                status = response.status
        except urllib.error.HTTPError as exc:
            status = exc.code
        except (urllib.error.URLError, OSError) as exc:
            failures.append(f'{page}: {url} -> {type(exc).__name__}: {exc}')
            continue
        if status in INCONCLUSIVE_STATUSES:
            inconclusive += 1
            print(f'  inconclusive  {status}  {url}')
        elif 200 <= status < 300:
            print(f'  ok  {status}  {url}')
        else:
            failures.append(f'{page}: {url} -> HTTP {status}')
    print(f'External probes: {len(targets)} targets, {inconclusive} inconclusive')
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--external', action='store_true')
    args = parser.parse_args()
    failures = check_external() if args.external else check_internal()
    if failures:
        print('\n'.join(failures))
        return 1
    print('External probes completed without definitive failures' if args.external
          else 'Internal links, assets, anchors, and sitemap all resolve')
    return 0


if __name__ == '__main__':
    sys.exit(main())
