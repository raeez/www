#!/usr/bin/env python3
"""Reader-visible words: none of the baseline's is lost; list what the new page adds.

    python3 -I check_text.py <baseline.html> <new.html>
"""
import collections
import html
import re
import sys

def words(path):
    s = open(path, encoding='utf-8').read()
    s = s[s.find('<body'):]
    for tag in ('script', 'style', 'math', 'svg'):
        s = re.sub(rf'<{tag}\b.*?</{tag}>', ' ', s, flags=re.S)
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    return collections.Counter(re.findall(r'\S+', s))

b, n = words(sys.argv[1]), words(sys.argv[2])
lost = b - n
added = n - b
print(f'words: baseline {sum(b.values())}, new {sum(n.values())}, lost {sum(lost.values())}, added {sum(added.values())}')
print('added (word: count):', ', '.join(f'{w}: {c}' for w, c in added.most_common(40)))
if lost:
    print('FAIL lost:', dict(lost.most_common(20)))
sys.exit(1 if lost else 0)
