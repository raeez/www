from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import sys,subprocess,re,html,json,hashlib
newpath=Path(sys.argv[1]) if len(sys.argv)>1 else Path('smart-buildings.html')
base=subprocess.check_output(['git','show','HEAD:smart-buildings.html'],text=True);new=newpath.read_text()
class P(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.stack=[];self.errors=[]
 def handle_starttag(self,t,a):
  self.tags.append((t,a))
  if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(t)
 def handle_endtag(self,t):
  if self.stack and self.stack[-1]==t:self.stack.pop()
  else:self.errors.append([t,self.stack[-5:]])
a=P();a.feed(base);b=P();b.feed(new)
assert a.errors==b.errors and a.stack==b.stack,(a.errors,b.errors,a.stack,b.stack)
body_start='<div class="article-body">'
assert base.split(body_start)[0].replace('Version 0.3 — September 2025','September 2025')==new.split(body_start)[0]
assert base[base.index('<footer'):]==new[new.index('<footer'):]
for tag in ['style','script']:assert re.findall(fr'<{tag}\b.*?</{tag}>',base,re.S)==re.findall(fr'<{tag}\b.*?</{tag}>',new,re.S)
for attr in ['href','src','id']:
 original=[v for t,attrs in a.tags for k,v in attrs if k==attr];revised=[v for t,attrs in b.tags for k,v in attrs if k==attr];assert original==revised,attr
ids=[v for t,attrs in b.tags for k,v in attrs if k=='id'];links=[v for t,attrs in b.tags for k,v in attrs if k=='href']
assert len(ids)==len(set(ids));assert not [v for v in links if v.startswith('#') and v[1:] not in ids]
local=[v for v in links if not re.match(r'(?:https?:|mailto:|#)',v)];assert all(Path(v.split('#')[0]).exists() for v in local)
def body(s):return html.unescape(re.sub('<[^>]+>',' ',s.split(body_start)[1].split('<footer')[0]))
x,y=body(base),body(new)
nums=r'(?<!\w)\d+(?:[.,-]\d+)*(?:%|\+|x)?'
assert Counter(re.findall(nums,x))==Counter(re.findall(nums,y))
quotes=r'"([^"\n]+)"';assert Counter(re.findall(quotes,x))==Counter(re.findall(quotes,y))
appendix_marker='<h2 class="c19"><span class="c15">Appendix A: Technical Specifications [Redacted]</span></h2>'
assert base[base.index(appendix_marker):]==new[new.index(appendix_marker):]
for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>',new,re.S):json.loads(data)
closed='kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem'
assert not re.search(rf'~/({closed})|/Users/[^/ ]+/({closed})|kernel/formal|kernel/docs|kernel/mez|kernel/\.claude|centcom/',new)
for l in links:
 m=re.search(r'github.com/(?:momentum-sez|mass-os)/([^/#?]+)',l)
 if m:assert m[1] in ['gstore','lex','op','stack']
result={'baseline':'a0d011c46811837a7f5fb1d1aa60cd457b68dd00','file':str(newpath.resolve()),'sha256':hashlib.sha256(new.encode()).hexdigest(),'numeric_body_tokens':len(re.findall(nums,y)),'quote_count':len(re.findall(quotes,y)),'checks':['HTML stack/errors identical to baseline','all href/src/id strings unchanged in order','all local and fragment links resolve; unique IDs','all body numbers and quotations preserved as multisets','styles and scripts byte-identical','appendices/confidentiality/contact/references/footer byte-identical','head/chrome unchanged except approved Version 0.3 prefix removal','JSON-LD valid','public-source scan zero hits'],'visual':'Not performed: browser security restriction; no alternate transport attempted'}
Path('smart-integration-checks.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
