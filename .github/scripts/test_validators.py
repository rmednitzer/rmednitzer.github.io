#!/usr/bin/env python3
"""Regression cases for demonstrated false passes, using disposable site copies."""
import contextlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from stage_site import ROOT, public_paths
import check_csp_hashes as csp
import check_links as links
import check_profile as profile


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='site-validator-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in public_paths(ROOT):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def mutate(self, filename, old, new):
        path = self.root / filename
        content = path.read_text(encoding='utf-8')
        self.assertIn(old, content)
        path.write_text(content.replace(old, new), encoding='utf-8')

    def run_check(self, name):
        return subprocess.run(['python3', str(ROOT / '.github/scripts' / name)],
                              cwd=self.root, capture_output=True, text=True)

    def test_current_site_passes(self):
        self.assertEqual(profile.validate(self.root), [])
        for script in ('check_links.py', 'check_contrast.py', 'check_csp_hashes.py'):
            with self.subTest(script=script):
                result = self.run_check(script)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_project_description_drift(self):
        path = self.root / 'profile.json'
        data = json.loads(path.read_text())
        data['featuredProjects'][0]['reasonFeatured'] = 'Synthetic unrelated description.'
        path.write_text(json.dumps(data))
        self.assertTrue(any('shared profile statement' in f for f in profile.validate(self.root)))

    def test_markdown_background_drift(self):
        data = json.loads((self.root / 'profile.json').read_text())
        self.mutate('index.md', data['professionalWork']['background'], 'Synthetic contradictory background.')
        self.assertTrue(any('index.md: shared profile statement' in f for f in profile.validate(self.root)))

    def test_interest_and_boundary_drift(self):
        data = json.loads((self.root / 'profile.json').read_text())
        for field in (data['person']['personalPerspective'][0], data['featuredProjects'][0]['boundary']):
            with self.subTest(field=field):
                path = self.root / 'llms.txt'
                original = path.read_text()
                self.mutate('llms.txt', field, 'Synthetic changed text.')
                self.assertTrue(any('llms.txt: shared profile statement' in f for f in profile.validate(self.root)))
                path.write_text(original)

    def test_srcset_missing_file(self):
        self.mutate('index.html', '/profile_roman-mednitzer-400.webp', '/missing-fixture.webp')
        result = self.run_check('check_links.py')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('missing-fixture.webp', result.stdout)

    def test_cross_page_fragments(self):
        for href in ('/#missing-fixture', 'https://rmednitzer.github.io/#missing-fixture'):
            with self.subTest(href=href):
                path = self.root / 'legal.html'; original = path.read_text()
                self.mutate('legal.html', 'href="/"', f'href="{href}"')
                result = self.run_check('check_links.py')
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('no matching destination id', result.stdout)
                path.write_text(original)

    def test_valid_query_fragment_and_srcset_descriptors(self):
        self.mutate('legal.html', 'href="/"', 'href="/?v=fixture#stack"')
        self.mutate('index.html', 'srcset="/profile_roman-mednitzer-400.webp"',
                    'srcset="/profile_roman-mednitzer-400.webp 1x, /profile_roman-mednitzer-400.png 2x"')
        result = self.run_check('check_links.py')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_manifest_icon_missing(self):
        self.mutate('site.webmanifest', '/favicon-192.png', '/missing-icon.png')
        self.assertNotEqual(self.run_check('check_links.py').returncode, 0)

    def test_contrast_unsupported_and_unreadable_colours(self):
        path = self.root / 'style.css'; original = path.read_text()
        for value in ('rgb(10,14,19)', '#0a0e13', '#xyz'):
            with self.subTest(value=value):
                path.write_text(original.replace('--muted: #8996a8;', f'--muted: {value};'))
                result = self.run_check('check_contrast.py')
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertNotIn('Traceback', result.stderr)
        path.write_text(original)

    def test_attributed_scripts_and_effective_directive(self):
        body = "document.getElementById('y').textContent = '2099';"
        token = csp.sha256_token(body)
        for attrs in ('type="text/javascript"', "type='module'", 'defer'):
            with self.subTest(attrs=attrs):
                html = f'<meta http-equiv="Content-Security-Policy" content="script-src {token}"><script {attrs}>{body}</script>'
                self.assertEqual(csp.validate(html), [])
                self.assertTrue(csp.validate(html.replace(token, "'none'")))
                self.assertTrue(csp.validate(html.replace('script-src', 'style-src')))
                self.assertTrue(csp.validate(html.replace(f'script-src {token}', f'script-src {token}; script-src-elem \'none\'')))

    def test_jsonld_is_not_executable_and_inline_attributes_are_refused(self):
        html = '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'"><script type="application/ld+json">{}</script>'
        self.assertEqual(csp.validate(html), [])
        self.assertTrue(csp.validate(html + '<p style="color:red">x</p>'))
        self.assertTrue(csp.validate(html + '<p onclick="alert(1)">x</p>'))
        self.assertTrue(csp.validate(html + '<link rel="stylesheet" href="/page-only.css">'))

    def test_external_denials_are_inconclusive(self):
        with patch.object(links, 'PAGES', ('index.html',)), patch.object(links, 'references', return_value=['https://example.invalid/']), patch.object(links.urllib.request, 'urlopen', side_effect=links.urllib.error.HTTPError('https://example.invalid/', 403, 'Denied', {}, None)):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(links.check_external(), [])
            self.assertIn('inconclusive', output.getvalue())
            self.assertNotIn('  ok ', output.getvalue())


if __name__ == '__main__':
    unittest.main()
