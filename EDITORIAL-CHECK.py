from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import re,html,json,subprocess,hashlib
p=Path('smart-buildings.html');new=p.read_text();old=subprocess.check_output(['git','show','HEAD:smart-buildings.html'],text=True)
class Check(HTMLParser):
 def __init__(self):super().__init__();self.stack=[];self.errors=[];self.ids=[];self.links=[];self.tags=[]
 def handle_starttag(self,t,a):
  d=dict(a);self.tags.append((t,tuple(a)))
  if 'id' in d:self.ids.append(d['id'])
  if 'href' in d:self.links.append(d['href'])
  if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(t)
 def handle_endtag(self,t):
  if self.stack and self.stack[-1]==t:self.stack.pop()
  else:self.errors.append((t,self.stack[-5:]))
a,b=Check(),Check();a.feed(old);b.feed(new)
assert a.errors==b.errors,(a.errors,b.errors)
assert a.stack==b.stack,(a.stack,b.stack)
assert a.ids==b.ids,'ID order changed'
assert a.links==b.links,'Link order changed'
assert not [v for v,n in Counter(b.ids).items() if n>1],'Duplicate ids'
assert not [v for v in b.links if v.startswith('#') and v[1:] not in b.ids],'Missing local anchors'
for kind in ['script','style']:
 assert re.findall(fr'<{kind}\b.*?</{kind}>',old,re.S)==re.findall(fr'<{kind}\b.*?</{kind}>',new,re.S),kind
assert old.split('<div class="article-body">')[0].replace('Version 0.3 — September 2025','September 2025')==new.split('<div class="article-body">')[0],'page prefix changed beyond authorized version removal'
assert old[old.index('<footer'):]==new[new.index('<footer'):],'footer changed'
# The appendices, confidentiality notice, contact, and references are fixed payloads.
def appendix(z):return z[z.index('<h2',z.index('With the foundations established') if 'With the foundations established' in z else z.index('The foundations are laid')):z.index('<footer')]
assert appendix(old)==appendix(new),'appendix/footer boundary changed'
body=lambda z:' '.join(html.unescape(re.sub('<[^>]+>',' ',z.split('<div class="article-body">')[1])).split())
x,y=body(old),body(new)
for label,pat in [('numbers',r'(?<!\w)\d+(?:[.,-]\d+)*(?:%|\+|x)?'),('quotes',r'"([^"\n]+)"')]:
 c,d=Counter(re.findall(pat,x)),Counter(re.findall(pat,y));assert c==d,(label,list((c-d).elements()),list((d-c).elements()))
# Every dated/numbered heading and every top-level title remains intact.
heads=lambda z:[html.unescape(re.sub('<[^>]+>','',m.group(2))) for m in re.finditer(r'<(h[1-4])\b[^>]*>(.*?)</\1>',z)]
oldh,newh=heads(old),heads(new)
for text in oldh:
 if re.search(r'\d',text):assert text in newh,('dated/numbered heading',text)
# Exact instructed public-source patterns, plus bare private GitHub repository links.
pat=r'~/(kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|/Users/[^/ ]+/(kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|kernel/formal|kernel/docs|kernel/mez|kernel/\.claude|centcom/'
assert not re.search(pat,new),'Private source path'
public=['gstore','lex','op','stack']
for link in b.links:
 m=re.search(r'github.com/(?:momentum-sez|mass-os)/([^/#?]+)',link)
 if m:assert m.group(1) in public,('Nonwhitelisted repository',link)
for z in re.findall(r'<script type="application/ld\+json">(.*?)</script>',new,re.S):json.loads(z)
local=[v for v in b.links if not re.match(r'(?:https?:|mailto:|#)',v)]
assert all(Path(v.split('#')[0]).exists() for v in local),('Missing local path',local)
result={'file':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'baseline':'a0d011c46811837a7f5fb1d1aa60cd457b68dd00','body_numeric_tokens':len(re.findall(r'(?<!\w)\d+(?:[.,-]\d+)*(?:%|\+|x)?',y)),'body_quotation_tokens':len(re.findall(r'"([^"\n]+)"',y)),'html_errors_baseline':a.errors,'html_errors_revised':b.errors,'unclosed_tags_baseline':a.stack,'unclosed_tags_revised':b.stack,'links':len(b.links),'ids':len(b.ids),'headings':len(newh),'local_links':local,'checks':['numeric multiset preserved','quotation multiset preserved','IDs and links preserved in order','scripts and CSS byte-identical','page prefix preserved except authorized version-label removal; footer byte-identical','appendices/confidentiality/contact/references byte-identical','numbered and dated headings preserved','HTML stack preserved','JSON-LD parses','local links exist','public-source scan clear'],'visual':'Not performed: parent reported browser local-file restriction and instructed no workaround.'}
Path('EDITORIAL-CHECK-RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
