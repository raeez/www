from pathlib import Path
from html import unescape
import re,json
p=Path('archai.html');s=p.read_text()
def text(s):return ' '.join(unescape(re.sub('<[^>]+>','',s)).split())
links=re.findall(r'<a\b[^>]*href="(#h\.[^"]+)"[^>]*>(.*?)</a>',s,re.S)
headings=list(re.finditer(r'(<h[1-4]\b[^>]*>)(.*?)(</h[1-4]>)',s,re.S))
fixes=[]
for href,label in links:
 label=re.sub(r'\s+\d+$','',text(label))
 hits=[m for m in headings if text(m.group(2))==label]
 if len(hits)!=1:raise SystemExit((href,label,len(hits)))
 m=hits[0]
 if ' id=' in m.group(1):raise SystemExit('Existing id needs review')
 fixes.append((m.start(),m.end(),m.group(1)[:-1]+' id="'+href[1:]+'">'+m.group(2)+m.group(3),href,label))
assert len({x[3] for x in fixes})==len(fixes)
for start,end,content,_,_ in sorted(fixes,reverse=True):s=s[:start]+content+s[end:]
p.write_text(s)
Path('archai-anchor-repairs.json').write_text(json.dumps([{'href':x[3],'heading':x[4]} for x in fixes],indent=2))
print(f'Restored {len(fixes)} unique existing TOC targets by exact heading text')
