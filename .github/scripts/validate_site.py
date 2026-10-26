#!/usr/bin/env python3
"""Run the complete source validation gate without modifying the site."""
import json
from pathlib import Path
import re
import subprocess
import sys
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
HTML_VALIDATE_VERSION = '11.17.0'


def main() -> int:
    try:
        if not re.fullmatch(r'\d+\.\d+\.\d+', HTML_VALIDATE_VERSION):
            raise ValueError('HTML validator must have an exact release pin')
        subprocess.run(['npx', '-y', f'html-validate@{HTML_VALIDATE_VERSION}',
                        'index.html', 'legal.html'], cwd=ROOT, check=True)
        ElementTree.parse(ROOT / 'sitemap.xml')
        for name in ('site.webmanifest', 'profile.json', '.claude/settings.json'):
            json.loads((ROOT / name).read_text(encoding='utf-8'))
        for name in ('index.html', 'legal.html'):
            blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                                (ROOT / name).read_text(encoding='utf-8'), re.S)
            if not blocks:
                raise ValueError(f'{name}: no JSON-LD blocks')
            for block in blocks:
                json.loads(block)
        for script in ('check_csp_hashes.py', 'check_contrast.py', 'check_links.py',
                       'check_profile.py', 'check_asset_versions.py'):
            subprocess.run([sys.executable, str(ROOT / '.github/scripts' / script)],
                           cwd=ROOT, check=True)
        subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s',
                        '.github/scripts', '-p', 'test_*.py', '-v'], cwd=ROOT, check=True)
    except (OSError, ValueError, ElementTree.ParseError, subprocess.CalledProcessError) as exc:
        print(f'Site validation failed: {exc}', file=sys.stderr)
        return 1
    print('Complete site validation passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
