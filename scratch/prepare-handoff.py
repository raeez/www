from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
from urllib.parse import urlsplit,unquote
import re,json,hashlib,difflib
root=Path.cwd();s=Path('sez-in-a-box.html').read_text();old=Path('scratch/sez-original.html').read_text()
orig=Path('scratch/sez-original.txt').read_text().splitlines();final=Path('scratch/sez-final-readable.txt').read_text().splitlines()
# Exact ordered map; each side uses its own immutable numbered extraction.
a=orig[188:466];b=final[40:281]
maplines=['# Part I exact original/final block map','','Original: scratch/sez-original.txt, blocks0189–0466. Final: scratch/sez-final-readable.txt, blocks0041–0281. Every block in both intervals appears once below. Numeric prefixes are the extraction positions, not publication page numbers.','']
ops=[]
for n,(tag,i,j,k,l) in enumerate(difflib.SequenceMatcher(None,[x[5:] for x in a],[x[5:] for x in b],autojunk=False).get_opcodes(),1):
 entry={'operation':tag,'original_blocks':[189+i,188+j] if j>i else [],'final_blocks':[41+k,40+l] if l>k else [],'original':a[i:j],'final':b[k:l]};ops.append(entry)
 maplines+=['## %s: %s'%(n,tag),'','Original blocks: '+str(entry['original_blocks'])+'; final blocks: '+str(entry['final_blocks']), '']
 if tag=='equal':maplines+=['Unchanged text (shown once):','']+a[i:j]+['']
 else:maplines+=['Before:','']+a[i:j]+['','After:','']+b[k:l]+['']
Path('scratch/part-i-exact-before-after.md').write_text('\n'.join(maplines)+'\n');Path('scratch/part-i-exact-before-after.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n')
Path('scratch/full-readable.diff').write_text('\n'.join(difflib.unified_diff(orig,final,fromfile='Original numbered readable text',tofile='Final numbered readable text',lineterm=''))+'\n')
# Parse balance, attributes, links, structured metadata, and preserved assets.
class Check(HTMLParser):
 def __init__(self):super().__init__();self.stack=[];self.errors=[];self.ids=[];self.links=[];self.titles=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append((t,self.getpos()))
  if 'id' in a:self.ids.append(a['id'])
  if 'href' in a:self.links.append(a['href'])
 def handle_endtag(self,t):
  if not self.stack:self.errors.append(['extra',t,self.getpos()]);return
  if self.stack[-1][0]!=t:self.errors.append(['mismatch',t,self.getpos(),self.stack[-1]]);return
  self.stack.pop()
p=Check();p.feed(s)
checks={'sha256':hashlib.sha256(s.encode()).hexdigest(),'bytes':len(s.encode()),'word_count':len(' '.join(x[5:] for x in final).split()),'blocks':len(final),'tag_errors':p.errors,'unclosed_tags':p.stack,'missing_fragments':[x for x in p.links if x.startswith('#') and x[1:] not in p.ids],'duplicate_ids':[x for x,n in Counter(p.ids).items() if n>1]}
checks['missing_local_links']=[x for x in p.links if not urlsplit(x).scheme and not x.startswith('#') and not (root/unquote(urlsplit(x).path)).exists()]
for tag in ['style','script','svg']:
 pattern=fr'<{tag}\b[^>]*>.*?</{tag}>';checks[tag+'_bytes_equal']=re.findall(pattern,old,re.S)==re.findall(pattern,s,re.S)
for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):json.loads(x)
checks['structured_metadata_parses']=True
checks['forbidden_reader_tokens']={pattern:re.findall(pattern,s,re.I) for pattern in [r'/Users/[^\s<]+',r'WIP\s*0\.?06',r'v0\.35',r'fifteen pilot',r'15 pilot',r'13\+? jurisdictions',r'10,000 companies',r'under 90 days',r'under \$10M']}
checks['rendered_browser_qa']='unverified; static-only lane boundary retained'
assert not any([checks['tag_errors'],checks['unclosed_tags'],checks['missing_fragments'],checks['duplicate_ids'],checks['missing_local_links']])
assert all(checks[x+'_bytes_equal'] for x in ['style','script','svg'])
assert not any(checks['forbidden_reader_tokens'].values())
Path('scratch/static-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
# Snapshot current conceptual source hashes without erasing original derivation manifest.
source_dir=Path('/Users/raeez/momentum-research-worktrees/writing-20261022-exposition/book/manuscript')
manifest=[]
for f in sorted(source_dir.glob('*.md')):manifest.append({'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'use':'Internal conceptual reference. Operational assertions filtered independently; no June portfolio assertion promoted to current public fact.'})
Path('scratch/final-conceptual-source-hashes.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# Complete public anchors with labels; duplicate destinations shown once per label.
links=[]
for m in re.finditer(r'<a\s+[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>',s,re.S):
 label=re.sub('<[^>]+>','',m.group(2));item={'label':label,'url':m.group(1)}
 if item not in links:links.append(item)
Path('scratch/final-public-source-links.json').write_text(json.dumps(links,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False,indent=2))
