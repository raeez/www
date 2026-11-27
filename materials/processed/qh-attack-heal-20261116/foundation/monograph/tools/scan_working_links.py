"""Links in the chapters' prose that point at working files (not an anchor, a chapter file or a web address).
Formulas (inline and displayed) and code spans are skipped first: brackets inside mathematics are not links.
    python3 scan_working_links.py <chapters folder> <out.json>"""
import glob, json, os, re, sys
rows = []
for f in sorted(glob.glob(os.path.join(sys.argv[1], '*.md'))):
    raw = re.sub(r'<!--.*?-->', '', open(f, encoding='utf-8').read(), flags=re.S)
    # blank out mathematics and code, keeping line numbers
    blank = lambda m: re.sub(r'[^\n]', ' ', m.group(0))
    text = re.sub(r'\\\[.*?\\\]|\$\$.*?\$\$|\\\(.*?\\\)|`[^`\n]*`', blank, raw, flags=re.S)
    for n, line in enumerate(text.splitlines(), 1):
        for mm in re.finditer(r'\]\((<?)([^)\s]+)(>?)\)', line):
            t = mm.group(2)
            if not (t.startswith('#') or re.match(r'https?://', t) or re.fullmatch(r'(?:\./)?[\w-]+\.md(?:#[\w:.-]+)?', t)):
                rows.append({'file': os.path.basename(f), 'line': n, 'target': t})
        d = re.match(r'^\s{0,3}\[([^\]]+)\]:\s*<?(\S+?)>?\s*$', line)
        if d and not re.match(r'https?://|#', d.group(2)):
            rows.append({'file': os.path.basename(f), 'line': n, 'target': d.group(2), 'form': 'reference definition'})
json.dump(rows, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('working-file links outside mathematics:', len(rows))
