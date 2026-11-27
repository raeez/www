"""A supplied supplement reaches the page exactly (render criteria for an exact author handoff).

    python3 -I check_supplement.py <page.html> <supplement.md> <part id> <after part id> <out.json>

<page.html> is the combined page or the split reference.html. Checks:
- placement: section[data-reference]#<part id> is the next reference part after #<after part id>;
- heading: its h2 is the file's "# " title, character for character; a dateline <time> equals the file's date line;
- sections: one section per "## " heading, in order, each h3 equal to the heading;
- words: every word of the file outside formulae, headings included, reaches the part's text in the same order;
- formulae: every \\(...\\) and \\[...\\] of the file reaches the part as MathML whose TeX annotation is the same
  formula (whitespace aside), in the same order, and the part holds no other formula;
- contents: when the page has the book's contents (#contents), it lists the part by its title right after the
  part it follows;
- ids: no id occurs twice on the page.
Reads the two files; writes only <out.json>."""
import html
import json
import re
import sys

page_path, md_path, pid, after, out = sys.argv[1:6]
page = open(page_path, encoding='utf-8').read()
md = open(md_path, encoding='utf-8').read()
res = {'page': page_path, 'supplement': md_path, 'checks': {}}
ok = res['checks']

TEX = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)
norm = lambda s: re.sub(r'\s+', '', s)  # noqa: E731


def words(text):
    return re.findall(r"[^\W_]+(?:['’-][^\W_]+)*", text)


# The part, depth-counted.
m = re.search(r'<section data-reference id="%s"[^>]*>' % re.escape(pid), page)
if not m:
    print('part not found'); sys.exit(1)
depth = 0
for t in re.finditer(r'<(/?)section\b[^>]*>', page[m.start():]):
    depth += -1 if t.group(1) else 1
    if depth == 0:
        part = page[m.start():m.start() + t.end()]
        break
refs = [x.group(1) for x in re.finditer(r'<section data-reference id="([^"]+)"', page)]
ok['placement'] = {'next_after': refs[refs.index(after) + 1] if after in refs and refs.index(after) + 1 < len(refs) else None}
ok['placement']['pass'] = ok['placement']['next_after'] == pid

title = md.lstrip().split('\n', 1)[0][2:].strip()
h2 = re.search(r'<h2 id="%s-h">(.*?)</h2>' % re.escape(pid), part, re.S)
h2_text = html.unescape(re.sub(r'<[^>]+>', '', h2.group(1))).strip() if h2 else None
ok['heading'] = {'file': title, 'page': h2_text, 'pass': h2_text == title}
date_line = md.lstrip().split('\n')[2].strip() if len(md.lstrip().split('\n')) > 2 else ''
tm = re.search(r'<time datetime="([^"]+)">(.*?)</time>', part)
ok['dateline'] = {'file': date_line, 'page': html.unescape(tm.group(2)) if tm else None, 'datetime': tm.group(1) if tm else None,
                  'pass': bool(tm) and html.unescape(tm.group(2)) == date_line}

heads = [h.strip() for h in re.findall(r'^## (.+)$', md, re.M)]
h3s = [html.unescape(re.sub(r'<annotation\b.*?</annotation>|<[^>]+>', '', h)).strip()
       for h in re.findall(r'<h3 class="mg-sec-head" id="[^"]+">(.*?)</h3>', part, re.S)]
ok['sections'] = {'file': heads, 'page': h3s, 'pass': heads == h3s}

# Formulae, in order: the file's against the part's TeX annotations.
src_tex = [norm(a or b) for a, b in TEX.findall(md)]
page_tex = [norm(html.unescape(a)) for a in re.findall(r'<annotation encoding="application/x-tex">(.*?)</annotation>', part, re.S)]
first_bad = next((k for k, (x, y) in enumerate(zip(src_tex, page_tex)) if x != y), None)
ok['formulae'] = {'file': len(src_tex), 'page': len(page_tex), 'first_difference': first_bad,
                  'pass': src_tex == page_tex}

# Words, in order, outside formulae (the file's headings and date included).
src_plain = TEX.sub(' ', md)
src_plain = re.sub(r'^#+\s*', '', src_plain, flags=re.M)
part_plain = re.sub(r'<math\b.*?</math>', ' ', part, flags=re.S)
part_plain = html.unescape(re.sub(r'<[^>]+>', ' ', part_plain))
kicker = re.search(r'<p class="kicker">(.*?)</p>', part)
if kicker:  # the website's own kicker word is not the file's
    part_plain = part_plain.replace(html.unescape(kicker.group(1)), ' ', 1)
sw, pw = words(src_plain), words(part_plain)
missing, j = [], 0
for w in sw:
    while j < len(pw) and pw[j] != w:
        j += 1
    if j == len(pw):
        missing.append(w)
        j = 0
        continue
    j += 1
extra = len(pw) - len(sw)
ok['words'] = {'file': len(sw), 'page': len(pw), 'missing_in_order': missing[:20], 'page_minus_file': extra,
               'pass': not missing and extra == 0}

toc = re.search(r'<nav class="mg-toc" id="contents"[^>]*>(.*?)</nav>', page, re.S)
if toc:
    items = re.findall(r'<li><a href="#([^"]+)">(.*?)</a></li>', toc.group(1))
    hrefs = [h for h, _ in items]
    entry = dict(items).get(pid)
    nxt = hrefs[hrefs.index(after) + 1] if after in hrefs and hrefs.index(after) + 1 < len(hrefs) else None
    ok['contents'] = {'entry': html.unescape(entry) if entry else None, 'after': after, 'next_after': nxt,
                      'pass': entry is not None and html.unescape(entry) == title and nxt == pid}

ids = re.findall(r'\sid="([^"]+)"', page)
dups = sorted({i for i in ids if ids.count(i) > 1}) if len(ids) < 20000 else sorted(
    {i for i, n in __import__('collections').Counter(ids).items() if n > 1})
ok['ids'] = {'duplicates': dups[:10], 'pass': not dups}

res['pass'] = all(v.get('pass') for v in ok.values())
json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in ok.items():
    print(f'{k:10s} {"PASS" if v.get("pass") else "FAIL"}  ' + json.dumps({a: b for a, b in v.items() if a != 'pass'},
                                                                       ensure_ascii=False)[:180])
print('ALL PASS' if res['pass'] else 'FAILURES ABOVE')
