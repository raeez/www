from pathlib import Path
import re,json,subprocess,hashlib
from lxml import html
root=Path.cwd();out={}
pattern=r'~/(kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|/Users/[^/ ]+/(kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|kernel/formal|kernel/docs|kernel/mez|kernel/\.claude|centcom/'
for f in ['moxie.html','programmable-institutions.html']:
 old=subprocess.check_output(['git','show','HEAD:'+f],text=True);new=(root/f).read_text()
 a,b=html.fromstring(old),html.fromstring(new)
 links=lambda d:sorted(d.xpath('//@href | //@src'))
 body=lambda d:d.xpath('//div[@class="article-body"]')[0].text_content()
 bn=body(b); an=body(a)
 ids=b.xpath('//@id');missing=[x[1:] for x in b.xpath('//a/@href') if x.startswith('#') and x[1:] not in ids]
 local=[x for x in b.xpath('//a/@href') if not re.match(r'^[a-z]+:|^#|^//',x)]
 payload={t:re.findall(fr'<{t}\b.*?</{t}>',old,re.S)==re.findall(fr'<{t}\b.*?</{t}>',new,re.S) for t in ['script','style','svg']}
 numbers=lambda t:sorted(set(re.findall(r'\b\d+(?:[.%-]\d+)*\b',t)))
 out[f]={'sha256':hashlib.sha256(new.encode()).hexdigest(),'links_and_sources_unchanged':links(a)==links(b),'payloads_unchanged':payload,'article_numeric_sets_equal':numbers(an)==numbers(bn),'baseline_numbers':numbers(an),'final_numbers':numbers(bn),'duplicate_ids':len(ids)!=len(set(ids)),'missing_fragment_targets':missing,'missing_local_links':[x for x in local if not (root/x.split('#')[0].split('?')[0]).exists()],'public_source_hits':re.findall(pattern,new),'body_chars':len(bn),'html_root_lang':b.get('lang'),'prose_semicolons':bn.count(';'),'article_paragraphs':len(b.xpath('//div[@class="article-body"]//p'))}
 assert out[f]['links_and_sources_unchanged'] and all(payload.values()) and out[f]['article_numeric_sets_equal'] and not missing and not out[f]['missing_local_links'] and not out[f]['public_source_hits']
Path('internal-qa/checks.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
