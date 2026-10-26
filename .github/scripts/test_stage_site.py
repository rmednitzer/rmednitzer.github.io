#!/usr/bin/env python3
"""Offline tests for publication boundaries and the deployable site's own links."""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from stage_site import ROOT, public_paths, stage, verify


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='site-publication-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'source'
        self.root.mkdir()
        for name in (*public_paths(ROOT), '.github/pages-files.txt'):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        self.output = Path(self.tmp.name) / 'public'

    def append_manifest(self, name):
        path = self.root / '.github/pages-files.txt'
        path.write_text(path.read_text() + name + '\n')

    def test_complete_public_site_without_repository_files(self):
        for name in ('CHANGELOG.md', 'AGENTS.md', 'audit/private.md', '.env'):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('Synthetic excluded fixture')
        stage(self.root, self.output)
        self.assertEqual(set(public_paths(self.root)),
                         {p.relative_to(self.output).as_posix()
                          for p in self.output.rglob('*') if p.is_file()})
        for name in ('CHANGELOG.md', 'AGENTS.md', 'audit/private.md', '.env'):
            self.assertFalse((self.output / name).exists())
        # Existing validators run against the packaged site, not the repository.
        for script in ('check_links.py', 'check_csp_hashes.py', 'check_asset_versions.py'):
            subprocess.run(['python3', str(ROOT / '.github/scripts' / script)],
                           cwd=self.output, check=True, capture_output=True, text=True)
        spec = importlib.util.spec_from_file_location('profile_check',
                     ROOT / '.github/scripts/check_profile.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.validate(self.output), [])

    def test_unknown_file_and_modified_file_rejected(self):
        stage(self.root, self.output)
        extra = self.output / 'unexpected.txt'
        extra.write_text('synthetic')
        with self.assertRaises(ValueError): verify(self.root, self.output)
        extra.unlink()
        (self.output / 'index.html').write_text('modified')
        with self.assertRaises(ValueError): verify(self.root, self.output)

    def test_missing_required_file(self):
        (self.root / 'index.html').unlink()
        with self.assertRaises(OSError): stage(self.root, self.output)
        self.assertFalse(self.output.exists())

    def test_manifest_traversal_glob_and_repository_paths(self):
        original = (self.root / '.github/pages-files.txt').read_text()
        for name in ('../private.txt', '/etc/passwd', 'fonts/*.woff2', 'index.html',
                     'CHANGELOG.md', '.github/policy.txt', 'audit/report.txt'):
            with self.subTest(name=name):
                (self.root / '.github/pages-files.txt').write_text(original)
                self.append_manifest(name)
                with self.assertRaises(ValueError): stage(self.root, self.output)
                self.assertFalse(self.output.exists())

    def test_source_symlink(self):
        path = self.root / 'index.md'
        path.unlink()
        path.symlink_to(self.root / 'index.html')
        with self.assertRaises(ValueError): stage(self.root, self.output)

    def test_source_hardlink(self):
        path = self.root / 'index.md'
        path.unlink()
        os.link(self.root / 'index.html', path)
        with self.assertRaises(ValueError): stage(self.root, self.output)

    def test_parent_symlink(self):
        fonts = self.root / 'fonts'
        fonts.rename(self.root / 'fonts-original')
        fonts.symlink_to(self.root / 'fonts-original', target_is_directory=True)
        with self.assertRaises(ValueError): stage(self.root, self.output)

    def test_artifact_symlink(self):
        stage(self.root, self.output)
        path = self.output / 'index.md'
        path.unlink()
        path.symlink_to(self.root / 'index.md')
        with self.assertRaises(ValueError): verify(self.root, self.output)

    def test_existing_output_not_overwritten(self):
        self.output.mkdir()
        marker = self.output / 'keep.txt'
        marker.write_text('preserved')
        with self.assertRaises(ValueError): stage(self.root, self.output)
        self.assertEqual(marker.read_text(), 'preserved')


if __name__ == '__main__':
    unittest.main()
