from pathlib import Path
from html.parser import HTMLParser
class Extract(HTMLParser):
 def __init__(self):super().__init__();self.active=False;self.depth=0;self.tag=None;self.buf=[];self.blocks=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='div' and a.get('class')=='article-body':self.active=True;self.depth=1;return
  if not self.active:return
  if tag=='div':self.depth+=1
  if tag in ['h1','h2','h3','h4','p','li','th','td','blockquote']:
   if self.tag and ''.join(self.buf).strip():self.blocks.append((self.tag,' '.join(''.join(self.buf).split())))
   self.tag=tag;self.buf=[]
 def handle_endtag(self,tag):
  if not self.active:return
  if tag==self.tag:
   if ''.join(self.buf).strip():self.blocks.append((self.tag,' '.join(''.join(self.buf).split())))
   self.tag=None;self.buf=[]
  if tag=='div':
   self.depth-=1
   if not self.depth:self.active=False
 def handle_data(self,data):
  if self.active and self.tag:self.buf.append(data)
s=Extract();s.feed(Path('smart-buildings.html').read_text())
Path('EDITORIAL-REVISED-FULL.txt').write_text('\n\n'.join(f'[{i:03d} {tag}] {t}' for i,(tag,t) in enumerate(s.blocks)))
print(len(s.blocks),'blocks',sum(len(t.split()) for _,t in s.blocks),'words')

import subprocess
o=Extract();o.feed(subprocess.check_output(['git','show','HEAD:smart-buildings.html'],text=True))
Path('EDITORIAL-SOURCE-FULL.txt').write_text('\n\n'.join(f'[{i:03d} {tag}] {t}' for i,(tag,t) in enumerate(o.blocks)))
print('Original:',len(o.blocks),'blocks')
