#!/usr/bin/env python3
"""Require both pages to use the shared stylesheet's current content digest."""
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import parse_qs, urlsplit

PAGES = ('index.html', 'legal.html')


class Stylesheets(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.hrefs = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'link' and a.get('rel') == 'stylesheet':
            url = urlsplit(a.get('href', ''))
            if url.path == '/style.css':
                self.hrefs.append(url)


def validate(root: Path) -> list[str]:
    digest = hashlib.sha256((root / 'style.css').read_bytes()).hexdigest()[:12]
    failures = []
    for name in PAGES:
        links = Stylesheets((root / name).read_text(encoding='utf-8')).hrefs
        if len(links) != 1:
            failures.append(f'{name}: expected one shared stylesheet reference')
        elif links[0].netloc or links[0].scheme or links[0].fragment or parse_qs(links[0].query) != {'v': [digest]}:
            failures.append(f'{name}: use /style.css?v={digest} for the current stylesheet')
    return failures


def main() -> int:
    try:
        failures = validate(Path.cwd())
    except (OSError, ValueError) as exc:
        print(f'Asset version check failed: {exc}', file=sys.stderr)
        return 1
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        return 1
    print('Shared stylesheet versions match the current content digest')
    return 0


if __name__ == '__main__':
    sys.exit(main())
