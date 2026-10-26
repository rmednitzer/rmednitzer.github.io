#!/usr/bin/env python3
"""Check inline executable content against its effective CSP directive.

JSON-LD is data, not executable JavaScript. HTML attributes must not hide
executable blocks from this check. This is a site policy check, not a CSP engine.
"""
import base64
import hashlib
from html.parser import HTMLParser
import sys
from urllib.parse import urlsplit

PAGES = ('index.html', 'legal.html')


def sha256_token(content: str) -> str:
    digest = hashlib.sha256(content.encode()).digest()
    return "'sha256-" + base64.b64encode(digest).decode() + "'"


class InlineContent(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.policies = []
        self.blocks = []
        self.current = None
        self.errors = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'content-security-policy':
            self.policies.append(a.get('content', ''))
        if tag == 'link' and a.get('rel') == 'stylesheet':
            if urlsplit(a.get('href', '')).path not in ('/style.css', '/fonts/fonts.css'):
                self.errors.append('Only the shared site and font stylesheets are allowed')
        if 'style' in a or any(key.startswith('on') for key in a):
            self.errors.append('Inline style attributes and event handlers are not allowed')
        if tag in ('script', 'style'):
            if a.get('src'):
                self.errors.append('External scripts are not allowed')
            if tag == 'script' and a.get('type', '').lower().strip() == 'application/ld+json':
                return
            self.current = (tag, [])

    def handle_data(self, data):
        if self.current:
            self.current[1].append(data)

    def handle_endtag(self, tag):
        if self.current and self.current[0] == tag:
            kind, parts = self.current
            self.blocks.append((kind, ''.join(parts)))
            self.current = None


def validate(html: str) -> list[str]:
    page = InlineContent()
    page.feed(html)
    failures = list(page.errors)
    if len(page.policies) != 1:
        return failures + ['Expected exactly one meta Content-Security-Policy']
    directives = {}
    for item in page.policies[0].split(';'):
        words = item.split()
        if not words:
            continue
        name = words[0].lower()
        if name in directives:
            failures.append(f'Duplicate CSP directive: {name}')
        directives.setdefault(name, words[1:])
    for kind, content in page.blocks:
        effective = directives.get(kind + '-src-elem',
                    directives.get(kind + '-src', directives.get('default-src', [])))
        token = sha256_token(content)
        if token not in effective:
            failures.append(f'Inline {kind} hash {token} missing from effective CSP directive')
    return failures


def main() -> int:
    failures = []
    for page in PAGES:
        with open(page, encoding='utf-8') as source:
            failures.extend(f'{page}: {message}' for message in validate(source.read()))
    if failures:
        print('\n'.join(failures))
        return 1
    print('CSP hashes match all inline executable content')
    return 0


if __name__ == '__main__':
    sys.exit(main())
