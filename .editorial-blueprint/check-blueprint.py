from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import subprocess, re, hashlib, json
class P(HTMLParser):
 def __init__(self):super().__init__();self.active=None;self.parts=[];self.blocks=[];self.tags=[];self.links=[];self.ids=[]
 def handle_starttag(self,t,a):
  self.tags.append((t,a))
  d=dict(a)
  if 'href' in d:self.links.append(d['href'])
  if 'id' in d:self.ids.append(d['id'])
  if t in ['p','h1','h2','h3','li']:self.active=t;self.parts=[]
 def handle_data(self,d):
  if self.active:self.parts.append(d)
 def handle_endtag(self,t):
  if t==self.active:
   text=' '.join(''.join(self.parts).split())
   if text:self.blocks.append((t,text))
   self.active=None
old=subprocess.check_output(['git','show','HEAD:licc-blueprint.html'],text=True)
new=Path('licc-blueprint.html').read_text()
def parse(t):
 p=P();p.feed(t);return p
p0,p1=parse(old),parse(new)
b0,b1=parse(old.split('<div class="article-body">')[1].split('<footer')[0]),parse(new.split('<div class="article-body">')[1].split('<footer')[0])
Path('blueprint-revised-text.txt').write_text('\n'.join(f'{i:03d} {t}: {s}' for i,(t,s) in enumerate(b1.blocks,1)))
assert p0.links==p1.links
assert p0.ids==p1.ids
for tag in ['style','script','svg']:
 assert re.findall(fr'<{tag}\b.*?</{tag}>',old,re.S)==re.findall(fr'<{tag}\b.*?</{tag}>',new,re.S),tag
for tag in ['table','td','tr']:
 assert len(re.findall(fr'<{tag}\b',old))==len(re.findall(fr'<{tag}\b',new)),tag
num=lambda p:Counter(re.findall(r'\d+(?:[.,]\d+)*', ' '.join(s for t,s in p.blocks)))
c0,c1=num(p0),num(p1)
quotes=lambda p:Counter(re.findall(r'"[^"]*"', ' '.join(s for t,s in p.blocks)))
q0,q1=quotes(p0),quotes(p1)
assert q0==q1,(q0-q1,q1-q0)
report={'body_blocks_before':len(b0.blocks),'body_blocks_after':len(b1.blocks),'links_preserved':len(p1.links),'ids_preserved':p1.ids,'styles_scripts_svg':'byte identical','table_structure':'same counts','numbers_removed':dict(c0-c1),'numbers_added':dict(c1-c0),'quotations':'identical multiset','old_sha256':hashlib.sha256(old.encode()).hexdigest(),'new_sha256':hashlib.sha256(new.encode()).hexdigest()}
Path('blueprint-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
