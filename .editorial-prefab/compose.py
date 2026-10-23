from pathlib import Path
from html import unescape
import json, re
p=Path('prefabricated-construction.html')
s=p.read_text()
edits=json.loads(Path('.editorial-prefab/replacements.json').read_text())

def change(old,new,reason):
 global s
 assert s.count(old)==1,(reason,s.count(old))
 s=s.replace(old,new,1)
 edits.append({'old':old,'new':new,'reason':reason,'kind':'composition'})

start=s.index('<div class="article-body">')+len('<div class="article-body">')
first_heading='<h2 class="c27"><span class="c17 c9">Challenges of Traditional Construction in the Middle East</span></h2>'
end=s.index(first_heading,start)
prefix=s[start:end]
toc=re.search(r'<div><div class="toc">(.*?)</div>(.*?)</div>',prefix,re.S)
assert toc
remainder=prefix[:toc.start()]+prefix[toc.end():]
tail=re.findall(r'<p class="c19[^\"]*">.*?</p>',remainder,re.S)
assert len(tail)==6
for item in tail: remainder=remainder.replace(item,'',1)
newtoc='<div class="toc">'+toc[1]+''.join(tail)+'</div>'
byline='<p class="c28"><span class="c31 c11 c2">王臻卓 (Lilith Wang) &amp; Raeez Lorgat, Momentum Capital</span></p>'
assert byline in remainder
remainder=remainder.replace(byline,byline+newtoc,1)
change(prefix,remainder,'Put the title, abstract and historical byline before one complete contents list; preserve all contents labels, page references and links.')

summary_heading='<h2 class="c27"><span class="c25 c9">Summary: A Flexible, Prefabricated Future</span></h2>'
comparison_heading='<h2 class="c27"><span class="c9 c25">PC vs Modular Construction: Technical Feature Comparison Table</span></h2>'
a=s.index(summary_heading); b=s.index(comparison_heading,a)
c=s.index('</table>',b)+len('</table>')
summary=s[a:b]; comparison=s[b:c]
change(summary+comparison,comparison+summary,'Place the technical comparison after both sets of case templates and before the closing synthesis, retaining every table cell and heading.')

summary_toc=next(t for t in tail if '#h.acvrvbj9sy13' in t)
comparison_toc=next(t for t in tail if '#h.bsujorjafsqy' in t)
change(summary_toc+comparison_toc,comparison_toc+summary_toc,'Match the contents order to the feature-comparison-before-synthesis structure while retaining historical page numbers.')

# Restore the targets already named by the existing contents links.
def plain(x): return ' '.join(unescape(re.sub(r'<[^>]*>','',x)).split())
links=re.findall(r'<a\b[^>]*href="#(h\.[^\"]+)"[^>]*>(.*?)</a>',s,re.S)
headings=list(re.finditer(r'<h[1-6]\b[^>]*>.*?</h[1-6]>',s,re.S))
seen=set()
for anchor,label in links:
 if anchor in seen: continue
 seen.add(anchor)
 label=re.sub(r'\s+\d+$','',plain(label))
 matches=[h[0] for h in headings if plain(h[0])==label]
 assert len(matches)==1,(anchor,label,len(matches))
 old=matches[0]; new=old.replace('>',f' id="{anchor}">',1)
 change(old,new,'Restore the existing contents target '+anchor+' on its unchanged heading.')

p.write_text(s)
Path('.editorial-prefab/replacements.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
print('Composition complete;',len(edits),'ordered replacement records,',len(seen),'heading targets restored.')
