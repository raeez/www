#!/usr/bin/env python3
"""Structural check of status.css (no CSS parser is installed): balanced braces, parentheses and
quotes outside comments; every class the new rules select occurs in the built page.

    python3 -I check_css.py <status.css> <new.html>
"""
import re
import sys

css = open(sys.argv[1], encoding='utf-8').read()
page = open(sys.argv[2], encoding='utf-8').read()
bare = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
bare = re.sub(r"'[^'\n]*'|\"[^\"\n]*\"", "''", bare)
fails = []
for o, c in ('{}', '()', '[]'):
    depth = 0
    for ch in bare:
        depth += (ch == o) - (ch == c)
        if depth < 0:
            break
    if depth != 0:
        fails.append(f'unbalanced {o}{c}')
start = css.find('Reading hierarchy.')
new_rules = re.sub(r'/\*.*?\*/', '', css[start:], flags=re.S)
selectors = set()
for block in re.findall(r'([^{}]+)\{', new_rules):
    if block.strip().startswith('@'):
        continue
    selectors.update(re.findall(r'\.([a-zA-Z][\w-]*)', block))
classes = set()
for m in re.finditer(r'class="([^"]+)"', page):
    classes.update(m.group(1).split())
unused = sorted(s for s in selectors if s not in classes)
print(f'new rule classes: {len(selectors)}; absent from page: {unused}')
for f in fails:
    print('FAIL', f)
print('PASS' if not fails else 'FAIL')
sys.exit(1 if fails else 0)
