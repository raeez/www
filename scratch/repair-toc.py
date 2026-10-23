from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from collections import defaultdict,Counter
import re,json
p=Path('sez-in-a-box.html');s=p.read_text();starts=[0]
for m in re.finditer('\n',s): starts.append(m.end())
class P(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.stack=[];self.nodes=[];self.ids=set()
 def off(self):l,c=self.getpos();return starts[l-1]+c
 def handle_starttag(self,t,a):
  attrs=dict(a)
  if 'id' in attrs:self.ids.add(attrs['id'])
  if t in ['p','h1','h2','h3','h4','h5','h6','a']:
   self.stack.append({'tag':t,'attrs':attrs,'start':self.off(),'open_end':self.off()+len(self.get_starttag_text()),'text':''})
 def handle_data(self,d):
  for n in self.stack:n['text']+=d
 def handle_endtag(self,t):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i]['tag']==t:
    n=self.stack.pop(i);n['end']=self.off()+len(t)+3;self.nodes.append(n);break
x=P();x.feed(s)
def norm(v):
 v=v.replace('\uec02','').replace('\uec03','')
 v=re.sub(r'\[[a-z]{1,2}\]$','',v)
 return re.sub(r'\s+',' ',v).strip()
links=[n for n in x.nodes if n['tag']=='a' and n['attrs'].get('href','').startswith('#h.')]
last_toc=max(n['end'] for n in links)
bytext=defaultdict(list)
for n in x.nodes:
 if n['start']>last_toc and n['tag'] in ['h1','h2','h3','h4','h5','h6','p']:
  bytext[norm(n['text'])].append(n)
repairs=[]; unresolved=[];used=set()
for a in links:
 target=a['attrs']['href'][1:]
 if target in x.ids:continue
 title=re.sub(r'\s+\d+$','',norm(a['text']))
 candidates=bytext.get(title,[])
 if len(candidates)!=1:
  unresolved.append({'target':target,'title':title,'matches':len(candidates)});continue
 n=candidates[0]
 if 'id' in n['attrs'] or n['start'] in used:
  unresolved.append({'target':target,'title':title,'matches':'existing_id_or_reuse'});continue
 used.add(n['start']); repairs.append({'target':target,'title':title,'offset':n['open_end']-1})
for n in sorted(repairs,key=lambda n:n['offset'],reverse=True):
 i=n['offset'];s=s[:i]+f' id="{n["target"]}"'+s[i:]
p.write_text(s)
Path('scratch/toc-repairs.json').write_text(json.dumps({'repairs':repairs,'unresolved':unresolved},ensure_ascii=False,indent=2)+'\n')
print('Repaired',len(repairs),'exact-title targets; unresolved',len(unresolved));print(json.dumps(unresolved,ensure_ascii=False))
