from pathlib import Path
from html.parser import HTMLParser
import subprocess,re,collections,json,hashlib
class P(HTMLParser):
 def __init__(self):super().__init__();self.t=None;self.b=[];self.blocks=[];self.tags=[]
 def handle_starttag(self,t,a):
  self.tags.append((t,a))
  if t in ('p','h1','h2','h3','h4','li'):self.t=t;self.b=[]
  if t=='br' and self.t:self.b.append('\n')
 def handle_endtag(self,t):
  if t==self.t:self.blocks.append((t,''.join(self.b).strip()));self.t=None;self.b=[]
 def handle_data(self,d):
  if self.t:self.b.append(d)
base=subprocess.check_output(['git','show','HEAD:archai.html'],text=True);new=Path('archai.html').read_text();a=P();a.feed(base);b=P();b.feed(new)
added_ids={x['href'][1:] for x in json.loads(Path('archai-anchor-repairs.json').read_text())}
def normalized(tags):return [(t,[(k,v) for k,v in attrs if not (k=='id' and v in added_ids)]) for t,attrs in tags if t!='br']
assert normalized(a.tags)==normalized(b.tags)
for tag in ['style','script']:assert re.findall(fr'<{tag}\b.*?</{tag}>',base,re.S)==re.findall(fr'<{tag}\b.*?</{tag}>',new,re.S)
assert [x for x in a.blocks if any(ord(c)>0x1D400 for c in x[1])]==[x for x in b.blocks if any(ord(c)>0x1D400 for c in x[1])]
assert re.findall(r'“The protocol token.*?underwriting\.”',base)==re.findall(r'“The protocol token.*?underwriting\.”',new)
assert re.findall(r'“stake-based, resident-weighted, trustee-checked\.”',base)==re.findall(r'“stake-based, resident-weighted, trustee-checked\.”',new)
assert re.findall(r'“all holders meet KYC tier X”',base)==re.findall(r'“all holders meet KYC tier X”',new)
for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>',new,re.S):json.loads(data)
ids=[v for _,attrs in b.tags for k,v in attrs if k=='id'];assert len(ids)==len(set(ids))
links=[v for _,attrs in b.tags for k,v in attrs if k=='href'];original_links=[v for _,attrs in a.tags for k,v in attrs if k=='href'];assert links==original_links
broken=[x for x in links if x.startswith('#') and x[1:] not in ids];assert not broken
local=[x for x in links if not x.startswith(('#','http:','https:','mailto:'))];missing=[x for x in local if not Path(x.split('#')[0]).exists()];assert not missing
removed_nums=collections.Counter(re.findall(r'\d+(?:[.,]\d+)*',' '.join(x[1] for x in a.blocks)))-collections.Counter(re.findall(r'\d+(?:[.,]\d+)*',' '.join(x[1] for x in b.blocks)));added_nums=collections.Counter(re.findall(r'\d+(?:[.,]\d+)*',' '.join(x[1] for x in b.blocks)))-collections.Counter(re.findall(r'\d+(?:[.,]\d+)*',' '.join(x[1] for x in a.blocks)));assert removed_nums=={'0.1':12,'0.2':1};assert not added_nums
closed_repos='kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem'
source_pattern=rf'~/({closed_repos})|/Users/[^/ ]+/({closed_repos})|kernel/formal|kernel/docs|kernel/mez|kernel/\.claude|centcom/'
source_hits=re.findall(source_pattern,new);assert not source_hits
checks={'baseline':'a0d011c46811837a7f5fb1d1aa60cd457b68dd00','sha256':hashlib.sha256(new.encode()).hexdigest(),'html_parse':'pass','markup':'same except six removed br tags and 65 restored existing TOC target IDs','style_script_blocks':'byte preserved','formula_blocks':'byte preserved','attributed_quotes':'byte preserved','json_ld':'valid','version_label_removals':dict(removed_nums),'numeric_additions':dict(added_nums),'all_href_strings':'byte preserved','local_links':local,'missing_local_links':missing,'repaired_fragments':len(added_ids),'unique_ids':'pass','public_source_scan_hits':len(source_hits),'render_inspection':'SKIPPED: Browser URL security policy blocked file:// URL; no bypass attempted','upstream_google_doc':'12TriV64rqMidmlzEXU5HdvbhpX_Fu4bNq5UUo7-125I (not edited)','inherited_source_residuals':['July 2025 wrapper date and June 2025 document date preserved','Duplicated mathematical Unicode/plain-text formula strings and unused beta parameter preserved; mathematical repair outside prose scope','External source claims and citation accessibility not fact-checked; dated design status preserved']}
Path('archai-checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
p=P();p.feed(new.split('<div class="article-body">',1)[1].split('<footer',1)[0]);Path('archai.html.txt').write_text('\n'.join(f'{i:03d} {t}: {x}' for i,(t,x) in enumerate(p.blocks) if x))
