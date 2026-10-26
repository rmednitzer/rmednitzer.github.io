#!/usr/bin/env python3
"""Check public-profile consistency without fetching or generating site content.

This guards representation drift; it is not a factual or SEO certification.
"""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]


class ProfilePage(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.meta: dict[str, str] = {}
        self.links: list[dict[str, str]] = []
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.headings: list[int] = []
        self.sections: list[str] = []
        self.visible: list[str] = []
        self.title: list[str] = []
        self.in_title = False
        self.in_body = False
        self.hidden_depth = 0
        self.remote_embeds: list[str] = []

    def handle_starttag(self, tag: str, attributes: list[tuple[str, str | None]]) -> None:
        a = {key: value or '' for key, value in attributes}
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'section' and 'id' in a:
            self.sections.append(a['id'])
        if tag == 'meta':
            self.meta[a.get('name', a.get('property', a.get('http-equiv', '')))] = a.get('content', '')
        if tag == 'link':
            self.links.append(a)
        if tag == 'a':
            self.hrefs.append(a.get('href', ''))
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headings.append(int(tag[1]))
        if tag == 'title':
            self.in_title = True
        if tag == 'body':
            self.in_body = True
        if tag in ('script', 'style'):
            self.hidden_depth += 1
        if tag in ('iframe', 'object', 'embed') or (tag == 'script' and a.get('src')):
            self.remote_embeds.append(tag)
        if tag in ('img', 'source', 'link'):
            url = a.get('src', a.get('srcset', ''))
            if tag == 'link' and a.get('rel') in ('stylesheet', 'preload', 'preconnect', 'dns-prefetch'):
                url = a.get('href', '')
            if url.startswith(('https://', 'http://', '//')):
                self.remote_embeds.append(url)

    def handle_endtag(self, tag: str) -> None:
        if tag == 'title':
            self.in_title = False
        if tag == 'body':
            self.in_body = False
        if tag in ('script', 'style'):
            self.hidden_depth -= 1

    def handle_data(self, text: str) -> None:
        if self.in_title:
            self.title.append(text)
        if self.in_body and not self.hidden_depth:
            self.visible.append(text)


def validate(root: Path) -> list[str]:
    failures: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    profile = json.loads((root / 'profile.json').read_text(encoding='utf-8'))
    person = profile['person']
    html = (root / 'index.html').read_text(encoding='utf-8')
    page = ProfilePage()
    page.feed(html)
    visible = ' '.join(' '.join(page.visible).split())
    canonical = profile['canonicalUrl']
    description = person['description']
    expected_title = person['name'] + ' | ' + person['headline']
    check(''.join(page.title) == expected_title, 'Title differs from structured profile')
    for key in ('description', 'og:description', 'twitter:description'):
        check(page.meta.get(key) == description, f'{key} differs from public description')
    for key in ('og:title', 'twitter:title'):
        check(page.meta.get(key) == expected_title, f'{key} differs from page title')
    check(page.meta.get('og:url') == canonical, 'Open Graph URL differs from canonical URL')
    canonicals = [a.get('href') for a in page.links if a.get('rel') == 'canonical']
    check(canonicals == [canonical], 'Missing, duplicate or inconsistent canonical link')
    check(page.headings.count(1) == 1, 'Expected exactly one h1')
    check(all(b <= a + 1 for a, b in zip(page.headings, page.headings[1:])), 'Skipped heading level')
    check(len(page.ids) == len(set(page.ids)), 'Duplicate HTML ids')
    check('#content' in page.hrefs and 'content' in page.ids, 'Skip navigation is missing')
    check(not page.remote_embeds, 'Unexpected remote resource or embedded widget')
    check(person['headline'] in visible and person['name'] in visible, 'Identity absent from visible content')
    check('noindex' not in page.meta.get('robots', '').lower(), 'Profile unexpectedly excludes indexing')
    check('unsafe-inline' not in page.meta.get('Content-Security-Policy', ''), 'CSP allows unsafe inline content')
    check('interests' in page.sections and '#interests' in page.hrefs,
          'Personal interests must remain a directly linked section')
    check('open-source' in page.sections and 'stack' in page.sections,
          'Projects or professional work summary is missing')
    check('experience' not in page.sections and 'track-item' not in html,
          'Employment timeline must remain absent')
    check('experience' not in profile and 'education' not in person,
          'Employment chronology and education records must remain absent')
    check(profile.get('formatVersion') == 2, 'Unexpected public profile format')
    check(profile['professionalWork']['background'] in visible,
          'Professional background differs from the visible summary')
    for capability in profile['professionalWork']['capabilities']:
        check(capability['area'] in visible and capability['description'] in visible,
              'Professional capability differs from visible content')
    check('availability' not in person, 'Public recruitment availability must remain absent')
    recruitment = re.compile(r'open to (?:full-time )?systems,\s*platform and integration roles', re.I)
    for filename in ('index.html', 'index.md', 'llms.txt', 'profile.json'):
        check(not recruitment.search((root / filename).read_text(encoding='utf-8')),
              f'{filename}: public recruitment wording reintroduced')
        content = (root / filename).read_text(encoding='utf-8')
        check(not re.search(r'(?m)^#{1,3} (?:Professional experience|Education|Employment history)', content),
              f'{filename}: detailed CV section reintroduced')


    blocks = [json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)]
    pages = [b for b in blocks if b.get('@type') == 'ProfilePage']
    check(len(pages) == 1, 'Expected one ProfilePage JSON-LD block')
    if pages:
        entity = pages[0]['mainEntity']
        check(entity.get('@type') == 'Person', 'Profile must describe a Person')
        check(entity.get('name') == person['name'], 'JSON-LD name mismatch')
        check(entity.get('jobTitle') == person['headline'], 'JSON-LD role mismatch')
        check(entity.get('description') == description, 'JSON-LD description mismatch')
        check(not any(key in entity for key in ('worksFor', 'alumniOf', 'memberOf')),
              'Structured identity must not add employment, education or memberships')
        check(pages[0]['dateModified'].startswith(profile['lastReviewed']), 'JSON-LD review date mismatch')
        for url in entity.get('sameAs', []):
            check(url in page.hrefs, f'Identity link is not visible: {url}')

    names = [p['name'] for p in profile['featuredProjects']]
    check(names == ['relay-shell', 'osint-workbench'], 'Unexpected featured project selection')
    for project in profile['featuredProjects']:
        check(project['url'] in page.hrefs, f"Project link absent: {project['name']}")
        check(project['name'] in visible, f"Project not visible: {project['name']}")
    for removed in ('infra', 'automation'):
        check('https://github.com/rmednitzer/' + removed not in page.hrefs, f'{removed} unexpectedly featured')
    for filename in ('index.md', 'llms.txt'):
        text = (root / filename).read_text(encoding='utf-8')
        check(person['name'] in text and person['headline'] in text, f'{filename}: identity mismatch')
        check(profile['lastReviewed'] in text, f'{filename}: stale review date')
        for project in profile['featuredProjects']:
            check(project['url'] in text, f'{filename}: missing featured project')
        check('AI-assisted' in text, f'{filename}: missing attribution boundary')
    check('AI-assisted' in visible, 'Visible AI attribution missing')
    check('My musical tastes lean towards' in visible, 'Personal music interests are missing')
    check(not any('open.spotify.com' in url for url in page.hrefs), 'Removed listening profile reintroduced')
    manifest = json.loads((root / 'site.webmanifest').read_text(encoding='utf-8'))
    check(manifest['description'] == description, 'Manifest description mismatch')
    sitemap = ElementTree.parse(root / 'sitemap.xml')
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    home = [url for url in sitemap.findall('s:url', ns) if url.findtext('s:loc', namespaces=ns) == canonical]
    check(len(home) == 1 and (home[0].findtext('s:lastmod', namespaces=ns) or '').startswith(profile['lastReviewed']), 'Sitemap profile date mismatch')
    return failures


def main() -> int:
    try:
        failures = validate(ROOT)
    except (OSError, ValueError, KeyError, TypeError, ElementTree.ParseError) as exc:
        print(f'Profile validation failed: {exc}', file=sys.stderr)
        return 1
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        return 1
    print('Public identity, metadata, project selection and attribution are consistent')
    return 0


if __name__ == '__main__':
    sys.exit(main())
