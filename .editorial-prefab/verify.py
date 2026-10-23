from pathlib import Path
from collections import Counter
from html import unescape
from html.parser import HTMLParser
import hashlib,json,re,subprocess
root=Path('.editorial-prefab')
old=subprocess.check_output(['git','show','HEAD:prefabricated-construction.html']).decode()
new=Path('prefabricated-construction.html').read_text()
edits=json.loads((root/'replacements.json').read_text())
replay=old
for e in edits:
 assert replay.count(e['old'])==1,e['reason']
 replay=replay.replace(e['old'],e['new'],1)
assert replay==new
payload_pattern=r'data:([^;]+);base64,([A-Za-z0-9+/=\s]+)'
olddata=re.findall(payload_pattern,old);newdata=re.findall(payload_pattern,new)
assert olddata==newdata
payloads=[{'mime':m,'encoded_bytes':len(d),'sha256':hashlib.sha256(d.encode()).hexdigest()} for m,d in olddata]
sanitize=lambda x:re.sub(payload_pattern,r'data:\1;base64,[PRESERVED PAYLOAD]',x)
oldsan=sanitize(old);newsan=sanitize(new)
(root/'after-sanitized.html').write_text(newsan)
body=lambda x:x.split('<div class="article-body">',1)[1].split('<footer class="article-footer">',1)[0]
def textonly(x):return unescape(re.sub('<[^>]+>','',re.sub(r'<br\s*/?>','\n',x)))
def blocks(s):
 return [{'index':i,'tag':m[1],'text':textonly(m[2]).strip(),'markup':m[0],'body_start':m.start(),'body_end':m.end()} for i,m in enumerate(re.finditer(r'<(h[1-6]|p|li)\b[^>]*>(.*?)</\1>',body(s),re.S))]
oldblocks=blocks(oldsan);newblocks=blocks(newsan)
for phase,items in [('before',oldblocks),('after',newblocks)]:
 (root/f'{phase}-blocks.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
 (root/f'{phase}-prose.txt').write_text('\n\n'.join(f"{b['index']:03d} {b['tag']}: {b['text']}" for b in items if b['text']))
mapping=[]
for b in oldblocks:
 updated=b['markup']
 for e in edits:
  if e['old'] in updated:updated=updated.replace(e['old'],e['new'],1)
 parts=re.findall(r'<(?:h[1-6]|p|li)\b[^>]*>.*?</(?:h[1-6]|p|li)>',updated,re.S)
 targets=[]
 for part in parts:
  matches=[n['index'] for n in newblocks if n['markup']==part]
  if not matches and not b['text'] and '<img' not in part: continue
  assert matches,(b['index'],part[:100])
  targets.append(matches)
 row={'before_index':b['index'],'before_text':b['text'],'after_candidates_by_resulting_block':targets}
 if b['index']==56:row['role_claims_consolidated_at']=[n['index'] for n in newblocks if n['text'].startswith(('We specialize in both','Our consultation and implementation'))]
 if b['index']==72:row['claims_consolidated_at']=[n['index'] for n in newblocks if n['text'].startswith(('We specialize in both','Our consultation and implementation'))]
 if b['index'] in [78,79,80]:row['claim_consolidated_at']=[n['index'] for n in newblocks if n['text'].startswith({78:'Crews can complete buildings',79:'Factory-standardized interiors provide',80:'Select modules can be detached'}[b['index']])]
 if b['index']==238:row['claim_consolidated_at']=[n['index'] for n in newblocks if n['text'].startswith('Middle Eastern governments can adapt and deploy')]
 if b['index'] in [34,151]:row['disposition']='Removed meta-signposting; no substantive claim.'
 mapping.append(row)
(root/'block-mapping.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
assert old.split('<div class="article-body">',1)[0]==new.split('<div class="article-body">',1)[0]
assert old.split('<footer class="article-footer">',1)[1]==new.split('<footer class="article-footer">',1)[1]
attrs=lambda x,n:Counter(re.findall(r'\b'+n+r'="([^\"]*)"',x))
assert attrs(oldsan,'href')==attrs(newsan,'href')
assert re.findall(r'<img\b[^>]*>',oldsan)==re.findall(r'<img\b[^>]*>',newsan)
nums=lambda x:Counter(re.findall(r'\d+(?:[–/.,=+%×‑-]\d+)*[%×+]?',textonly(body(x))))
numeric_removed=nums(oldsan)-nums(newsan);numeric_added=nums(newsan)-nums(oldsan)
assert numeric_removed==Counter({'24':1}) and not numeric_added,(numeric_removed,numeric_added)
assert 'install each apartment in ' in newsan and '&lt;24 hours' in newsan
ids=re.findall(r'\bid="([^\"]*)"',newsan)
oldids=re.findall(r'\bid="([^\"]*)"',oldsan)
frags=re.findall(r'href="#([^\"]*)"',newsan)
assert len(ids)==len(set(ids))
assert set(oldids)<=set(ids)
assert not (set(frags)-set(ids))
assert len(re.findall(r'<table\b',oldsan))==len(re.findall(r'<table\b',newsan))==3
class Balance(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.stack=[];self.errors=[]
 def handle_starttag(self,t,a):
  if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(t)
 def handle_endtag(self,t):
  if not self.stack or self.stack[-1]!=t:self.errors.append({'closing':t,'stack_tail':self.stack[-5:]})
  elif self.stack:self.stack.pop()
 def handle_startendtag(self,t,a):pass
structure={}
for phase,s in [('before',oldsan),('after',newsan)]:
 p=Balance();p.feed(s);p.close();structure[phase]={'mismatched_closing_tags':p.errors,'unclosed_tags':p.stack}
 assert not p.errors and not p.stack
(root/'html-structure-check.json').write_text(json.dumps(structure,indent=2)+'\n')
report={'source_sha256':hashlib.sha256(old.encode()).hexdigest(),'revised_sha256':hashlib.sha256(new.encode()).hexdigest(),'ordered_replacement_replay':'exact match','payloads_byte_identical':True,'payloads':payloads,'head_and_footer_byte_identical':True,'image_tags_byte_identical':True,'href_multiset_identical':True,'original_ids_preserved':True,'heading_text_edits':'explicitly authorized; synchronized contents and preserved anchor identifiers','numeric_tokens_removed':dict(numeric_removed),'numeric_tokens_added':dict(numeric_added),'numeric_consolidation':'One duplicate 24-hour occurrence removed; complete weeks/building and <24 hours/apartment claims retained together in the BOX response row','table_count':3,'duplicate_ids':0,'unresolved_fragment_targets':0,'restored_heading_targets':23,'replacement_records':len(edits),'html_tag_balance':'no mismatched or unclosed tags before or after'}
(root/'preservation-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='payloads'},indent=2))
print('payload_count',len(payloads),'total_base64_bytes',sum(x['encoded_bytes'] for x in payloads))
print('all original blocks mapped; before',len(oldblocks),'after',len(newblocks))
