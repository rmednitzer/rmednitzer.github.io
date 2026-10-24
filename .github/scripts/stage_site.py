#!/usr/bin/env python3
"""Package only explicitly approved public files; never copy the repository tree."""
from __future__ import annotations

import argparse
import os
from pathlib import Path, PurePosixPath
import stat
import sys

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = '.github/pages-files.txt'
REQUIRED = {'index.html', 'legal.html', 'index.md', 'llms.txt', 'profile.json',
            'robots.txt', 'sitemap.xml', 'site.webmanifest', 'style.css',
            '.nojekyll', '.well-known/security.txt', 'LICENSE', 'NOTICE',
            'fonts/fonts.css', 'fonts/OFL-Outfit.txt', 'fonts/OFL-DMMono.txt'}
REPOSITORY_ONLY = {'AGENTS.md', 'CLAUDE.md', 'README.md', 'CHANGELOG.md',
                   'BACKLOG.md', 'CONTRIBUTING.md', 'SECURITY.md',
                   'CODE_OF_CONDUCT.md', 'renovate.json5'}
PRIVATE_DIRS = {'.git', '.github', '.forgejo', '.claude', 'audit', 'docs'}
MAX_FILE_BYTES = 5 * 1024 * 1024


def public_paths(root: Path) -> tuple[str, ...]:
    names: list[str] = []
    for line in (root / MANIFEST).read_text(encoding='utf-8').splitlines():
        name = line.strip()
        if not name or name.startswith('#'):
            continue
        path = PurePosixPath(name)
        if (path.is_absolute() or path.as_posix() != name or
                any(part in {'.', '..'} for part in path.parts) or
                any(c in name for c in '\\*?[]\x00') or not path.parts):
            raise ValueError(f'Invalid public path: {name!r}')
        if (path.parts[0] in PRIVATE_DIRS or name in REPOSITORY_ONLY or
                (name.endswith('.md') and name != 'index.md')):
            raise ValueError(f'Repository-only path cannot be published: {name}')
        if name in names:
            raise ValueError(f'Duplicate public path: {name}')
        current = root
        for part in path.parts:
            current = current / part
            if current.is_symlink():
                raise ValueError(f'Symbolic link not allowed: {name}')
        info = current.stat()
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise ValueError(f'Expected a regular, unlinked file: {name}')
        if info.st_size > MAX_FILE_BYTES:
            raise ValueError(f'Public file exceeds size budget: {name}')
        names.append(name)
    missing = REQUIRED - set(names)
    if missing:
        raise ValueError(f'Required public files missing: {sorted(missing)}')
    return tuple(names)


def verify(root: Path, destination: Path) -> tuple[str, ...]:
    names = public_paths(root)
    if destination.is_symlink() or not destination.is_dir():
        raise ValueError('Public artifact is not a regular directory')
    actual: set[str] = set()
    for base, dirs, files in os.walk(destination, followlinks=False):
        for name in dirs + files:
            path = Path(base) / name
            if path.is_symlink():
                raise ValueError('Public artifact contains a symbolic link')
        for name in files:
            path = Path(base) / name
            info = path.stat()
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise ValueError('Public artifact contains a special or linked file')
            actual.add(path.relative_to(destination).as_posix())
    if actual != set(names):
        raise ValueError(f'Artifact file set mismatch; extra={sorted(actual-set(names))}, '
                         f'missing={sorted(set(names)-actual)}')
    for name in names:
        if (root / name).read_bytes() != (destination / name).read_bytes():
            raise ValueError(f'Artifact content differs from reviewed source: {name}')
    return names


def stage(root: Path, destination: Path) -> tuple[str, ...]:
    root = root.resolve()
    destination = destination.absolute()
    if destination.exists() or destination.is_symlink():
        raise ValueError('Destination already exists; refusing to overwrite it')
    resolved = destination.resolve()
    if resolved == root or root.is_relative_to(resolved):
        raise ValueError('Destination cannot replace the source or an ancestor')
    names = public_paths(root)  # Validate all inputs before creating output.
    destination.mkdir(parents=True, exist_ok=False)
    for name in names:
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((root / name).read_bytes())
    return verify(root, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / '_site')
    parser.add_argument('--verify', action='store_true', help='Check an existing artifact')
    args = parser.parse_args()
    try:
        paths = (verify if args.verify else stage)(ROOT, args.output)
    except (OSError, ValueError) as exc:
        print(f'Publication check failed: {exc}', file=sys.stderr)
        return 1
    total = sum((args.output / name).stat().st_size for name in paths)
    print(f'Public artifact verified: {len(paths)} allowlisted files, {total} bytes')
    return 0


if __name__ == '__main__':
    sys.exit(main())
