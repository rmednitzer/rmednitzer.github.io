#!/usr/bin/env python3
"""Fail CI when a palette token drops below its WCAG contrast budget.

The site has no build step and no automated browser tests, so a colour
tweak in style.css is otherwise only checked by eye, in whichever theme
the author happened to have active. That is how --muted came to sit at
4.25:1 in dark mode while carrying most of the page's secondary text
(every tag, every section lede, the footer, the hero subtitle).

Every foreground token is checked against both surfaces it is painted on
(--bg for the page, --bg-surface for the cards), in every palette the
stylesheet defines: dark, light, their prefers-contrast: more variants,
and print. All of these tokens are used at small text sizes somewhere on
the page, so all of them are held to the AA small-text ratio of 4.5:1.
"""
import re
import sys

CSS = 'style.css'

# (token, minimum ratio against both --bg and --bg-surface)
FOREGROUNDS = (
    ('--fg', 4.5),
    ('--fg-strong', 4.5),
    ('--muted', 4.5),
    ('--accent', 4.5),
)

BACKGROUNDS = ('--bg', '--bg-surface')

# Each palette layers its overrides on top of an earlier one, mirroring the
# cascade: a media block only restates the tokens it changes.
PALETTES = (
    ('dark', None, r':root\s*\{'),
    ('light', 'dark', r'@media \(prefers-color-scheme: light\)\s*\{\s*:root\s*\{'),
    ('dark + more contrast', 'dark', r'@media \(prefers-contrast: more\)\s*\{\s*:root\s*\{'),
    ('light + more contrast', 'light',
     r'@media \(prefers-contrast: more\) and \(prefers-color-scheme: light\)\s*\{\s*:root\s*\{'),
    ('print', 'dark', r'@media print\s*\{\s*:root\s*\{'),
)


def relative_luminance(hex_colour: str) -> float:
    h = hex_colour.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    channels = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
              for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(fg: str, bg: str) -> float:
    lighter, darker = sorted((relative_luminance(fg), relative_luminance(bg)),
                             reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def tokens_in_block(css: str, opening: str) -> dict:
    """Pull `--token: value;` pairs out of the :root block that `opening`
    matches, reading up to the brace that closes it."""
    match = re.search(opening, css)
    if not match:
        raise LookupError(opening)
    body = css[match.end():css.index('}', match.end())]
    return dict(re.findall(r'(--[\w-]+)\s*:\s*([^;]+);', body))


def main() -> int:
    css = open(CSS, encoding='utf-8').read()

    resolved, failures, checked = {}, [], 0
    for name, inherits, opening in PALETTES:
        try:
            palette = dict(resolved[inherits]) if inherits else {}
            palette.update(tokens_in_block(css, opening))
        except LookupError as exc:
            failures.append(f'{CSS}: no :root block found for {name} ({exc})')
            continue
        resolved[name] = palette

        for fg_token, minimum in FOREGROUNDS:
            for bg_token in BACKGROUNDS:
                fg, bg = palette.get(fg_token), palette.get(bg_token)
                if fg is None or bg is None:
                    failures.append(
                        f'{name}: {fg_token} or {bg_token} is undefined')
                    continue
                fg, bg = fg.strip(), bg.strip()
                if not (fg.startswith('#') and bg.startswith('#')):
                    continue  # non-hex tokens carry no text
                ratio = contrast(fg, bg)
                checked += 1
                if ratio < minimum:
                    failures.append(
                        f'{name}: {fg_token} ({fg}) on {bg_token} ({bg}) is '
                        f'{ratio:.2f}:1, below the {minimum}:1 budget')

    if failures:
        print('\n'.join(failures))
        return 1
    print(f'Contrast budget met: {checked} token pairs across '
          f'{len(resolved)} palettes')
    return 0


if __name__ == '__main__':
    sys.exit(main())
