#!/usr/bin/env python3
"""Fail CI when an inline <script>/<style> no longer matches the hash
allow-listed in the page's meta Content-Security-Policy (ADR 0007).

A stale hash fails closed in browsers: the year script or the index
style block would silently stop working. JSON-LD data blocks are not
executed and need no allowance, so only bare <script>/<style> tags are
checked.
"""
import base64
import hashlib
import re
import sys

PAGES = ('index.html', 'legal.html')


def sha256_token(content: str) -> str:
    digest = hashlib.sha256(content.encode()).digest()
    return "'sha256-" + base64.b64encode(digest).decode() + "'"


def main() -> int:
    failures = []
    for page in PAGES:
        html = open(page, encoding='utf-8').read()
        meta = re.search(
            r'<meta http-equiv="Content-Security-Policy" content="([^"]+)">',
            html)
        if not meta:
            failures.append(f'{page}: no meta Content-Security-Policy found')
            continue
        policy = meta.group(1)
        for kind, pattern in (('script', r'<script>(.*?)</script>'),
                              ('style', r'<style>(.*?)</style>')):
            for content in re.findall(pattern, html, re.S):
                token = sha256_token(content)
                if token not in policy:
                    failures.append(
                        f'{page}: inline {kind} hash {token} missing from CSP')

    if failures:
        print('\n'.join(failures))
        return 1
    print('CSP hashes match all inline content')
    return 0


if __name__ == '__main__':
    sys.exit(main())
