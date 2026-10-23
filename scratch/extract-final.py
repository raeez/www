from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import re,json,hashlib
class P(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.parts=[];self.links=[];self.ids=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t in ['style','script']:self.skip+=1
  if t in ['p','h1','h2','h3','h4','li','tr']:self.parts.append('\n')
  if 'href'in a:self.links.append(a['href'])
  if 'id'in a:self.ids.append(a['id'])
 def handle_endtag(self,t):
  if t in ['style','script']:self.skip-=1
 def handle_data(self,d):
  if not self.skip:self.parts.append(d)
s=Path('sez-in-a-box.html').read_text();p=P();p.feed(s)
lines=[re.sub(r'\s+',' ',x).strip() for x in ''.join(p.parts).splitlines()];lines=[x for x in lines if x]
Path('scratch/sez-final-readable.txt').write_text('\n'.join(f'{i:04} {x}' for i,x in enumerate(lines,1))+'\n')
r={'word_count':len(' '.join(lines).split()),'blocks':len(lines),'missing_fragments':[x for x in p.links if x.startswith('#') and x[1:] not in p.ids],'duplicate_ids':[x for x,n in Counter(p.ids).items() if n>1],'sha256':hashlib.sha256(s.encode()).hexdigest()}
for tag in ['style','script','svg']:
 pat=fr'<{tag}\b[^>]*>.*?</{tag}>';old=re.findall(pat,Path('scratch/sez-original.html').read_text(),re.S);new=re.findall(pat,s,re.S);r[tag+'_bytes_equal']=old==new
for i,x in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)):json.loads(x)
Path('scratch/static-checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
