#!/usr/bin/env python3
"""WCAG 2.1 contrast of the page's colour tokens (no browser), light and dark themes.

    python3 tools/contrast_static.py <status.css>

Reads the light tokens from the first :root block and the dark tokens from :root[data-theme='dark'], and checks
the foreground/background pairs the page uses for text (4.5:1) and for status marks (3:1, WCAG 1.4.11).
"""
import re
import sys


def tokens(block):
    return dict(re.findall(r'--([\w-]+):\s*(#[0-9a-fA-F]{6})', block))


def lum(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda x: x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4  # noqa: E731
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


# (foreground token, background token, minimum, where it is used)
TEXT = [('ink', 'paper', 'body text'), ('ink-2', 'paper', 'secondary text, why it matters'),
        ('ink-3', 'paper', 'notes, contents counts, context lines'), ('ink-4', 'paper', 'kickers, labels, line status, set-aside family names'),
        ('ink-4', 'paper-2', 'labels on hovered rows'), ('ink-3', 'paper-3', 'card meaning, cell scope'), ('ink-4', 'paper-3', 'labels in cards and the table'),
        ('accent', 'paper', 'links'), ('accent', 'paper-3', 'links in cards, legend link'), ('accent', 'accent-soft', 'chips on tint')]
MARKS = ['st-checked', 'st-pending', 'st-conditional', 'st-conjecture', 'st-heuristic', 'st-open', 'st-published', 'st-partial',
         'st-not-posed', 'st-refuted-form']
# A statement's status chip sets its label in the status colour, on the statement's surface (paper-3; paper for dashed ones).
CHIP_TEXT = ['st-checked', 'st-refuted-form', 'st-pending', 'st-conditional', 'st-conjecture', 'st-heuristic', 'st-open', 'st-published']


def main():
    css = open(sys.argv[1], encoding='utf-8').read()
    light = tokens(re.search(r':root\s*\{(.*?)\}', css, re.S).group(1))
    dark = dict(light)
    dark.update(tokens(re.search(r":root\[data-theme='dark'\]\s*\{(.*?)\}", css, re.S).group(1)))
    ok = True
    for name, t in (('light', light), ('dark', dark)):
        for fg, bg, where in TEXT:
            r = ratio(t[fg], t[bg])
            good = r >= 4.5
            ok &= good
            print(f'{"PASS" if good else "FAIL"} {name:5} text {fg:>7} on {bg:<11} {r:5.2f} (4.5)  {where}')
        for m in CHIP_TEXT:
            for bg in ('paper', 'paper-3'):
                r = ratio(t[m], t[bg])
                good = r >= 4.5
                ok &= good
                if not good or bg == 'paper-3':
                    print(f'{"PASS" if good else "FAIL"} {name:5} chip text {m:>15} on {bg:<8} {r:5.2f} (4.5)')
        for m in MARKS:
            for bg in ('paper', 'paper-2', 'paper-3'):
                r = ratio(t[m], t[bg])
                good = r >= 3
                ok &= good
                if not good or bg == 'paper-2':
                    print(f'{"PASS" if good else "FAIL"} {name:5} mark {m:>15} on {bg:<8} {r:5.2f} (3.0)')
    print('ALL PASS' if ok else 'CONTRAST FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
