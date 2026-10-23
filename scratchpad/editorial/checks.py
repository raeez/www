from pathlib import Path
import re,hashlib,json,subprocess,difflib
w=Path(__file__).resolve().parents[2]
src=Path('/Users/raeez/www/materials/raw/2026-09-09-accessible-papers')
names=['claims-and-continuing-obligations','prices-information-and-clearing-risk']
expected={
'claims-and-continuing-obligations.md':'c60a4e4ded4be1e3d4eedb7028d2475d750eb588bc5095bb01b956217705bd77',
'claims-and-continuing-obligations.tex':'63e2eef4cbcfff948d13d04e371329b87975c326d47088d5fa4078cfdd8336f9',
'prices-information-and-clearing-risk.md':'fb1bf327422b23088c2f08cf071065091a89aad2fd68eeadb506164e8a5d3e92',
'prices-information-and-clearing-risk.tex':'bf0468f4d8c4dc1ef88205e778caed5bcc0fdff55005f2214072086621264553'}
results=[]
def check(label,cond):
 results.append(('PASS' if cond else 'FAIL')+' '+label)
 if not cond: raise AssertionError(label)
def math(s):
 return [re.sub(r'\s+','',x) for x in re.findall(r'(?<!\\)(\$\$[\s\S]*?\$\$|\$[^$]*?\$|\\\[[\s\S]*?\\\])',s)]
private=re.compile(r'~/(?:kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|/Users/[^/ ]+/(?:kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|kernel/(?:formal|docs|mez|\.claude)|centcom/')
external=re.compile(r'\b(?:v[0-9]+|version\s+[0-9]|prior\s+draft|previous\s+(?:draft|version)|superseded|post-(?:M|W|L|R|Z)[0-9]|phase\s+L[0-9]|to\s+our\s+knowledge|we\s+believe|essentially|basically)\b',re.I)
compact=[]
for n in names:
 plain={}
 for ext,fmt in [('md','markdown'),('tex','latex')]:
  p=w/'content/reader-papers'/f'{n}.{ext}'; old=(src/p.name).read_text(); new=p.read_text()
  check(p.name+' source checksum preserved',hashlib.sha256((src/p.name).read_bytes()).hexdigest()==expected[p.name])
  check(p.name+' worker raw checksum preserved',hashlib.sha256((w/'materials/raw/2026-09-09-accessible-papers'/p.name).read_bytes()).hexdigest()==expected[p.name])
  check(p.name+' ordered mathematical payloads unchanged',math(old)==math(new))
  check(p.name+' ordered numeric tokens unchanged',re.findall(r'\d+(?:\.\d+)*',old)==re.findall(r'\d+(?:\.\d+)*',new))
  if ext=='md':
   check(p.name+' links and anchors unchanged',re.findall(r'\]\([^)]*\)|\{#[^}]*\}',old)==re.findall(r'\]\([^)]*\)|\{#[^}]*\}',new))
  else:
   check(p.name+' citation commands unchanged',re.findall(r'\\cite(?:\[[^]]*\])?\{[^}]*\}',old)==re.findall(r'\\cite(?:\[[^]]*\])?\{[^}]*\}',new))
   check(p.name+' labels and environments unchanged',re.findall(r'\\(?:label|begin|end)\{[^}]*\}',old)==re.findall(r'\\(?:label|begin|end)\{[^}]*\}',new))
   check(p.name+' metadata unchanged',old.split('\\begin{document}')[0]==new.split('\\begin{document}')[0])
  check(p.name+' public source boundary scan clean',not private.search(new))
  check(p.name+' reader-process/hedging scan clean',not external.search(new))
  parsed=subprocess.run(['pandoc','-f',fmt,'-t','json',str(p)],capture_output=True,text=True)
  check(p.name+' Pandoc structured parse',parsed.returncode==0 and not parsed.stderr)
  json.loads(parsed.stdout)
  rendered=subprocess.run(['pandoc','-f',fmt,'-t','plain','--wrap=none',str(p)],capture_output=True,text=True)
  original=subprocess.run(['pandoc','-f',fmt,'-t','plain','--wrap=none',str(src/p.name)],capture_output=True,text=True)
  check(p.name+' plain diagnostic warnings unchanged from raw',rendered.stderr==original.stderr)
  plain[ext]=rendered.stdout
  compact.extend(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='a/content/reader-papers/'+p.name,tofile='b/content/reader-papers/'+p.name,n=3))
  (w/'scratchpad/editorial'/f'{n}-{ext}.txt').write_text(rendered.stdout)
 md=plain['md']; tex=plain['tex']
 md=md[md.index('\n1 ')+1:]; md=md[:md.index('\nReferences')]
 tex=tex[:tex.index('\n9 ')]
 md=re.sub(r'(?m)^\d+(?:\.\d+)* ','',md)
 md=re.sub(r'\[\d+(?:,[^]]*)?\]','',md)
 norm=lambda s:re.sub(r'\s+','',s)
 check(n+' normalized Markdown/TeX body prose and tables equal',norm(md)==norm(tex))
 mdt=(w/'content/reader-papers'/f'{n}.md').read_text(); text=(w/'content/reader-papers'/f'{n}.tex').read_text()
 mda=mdt.split('## Abstract\n\n')[1].split('\n## 1 ')[0]
 texa=text.split('\\begin{abstract}\n')[1].split('\\end{abstract}')[0]
 check(n+' abstract wording equal',norm(mda)==norm(texa))
(w/'scratchpad/editorial/compact-editorial.patch').write_text(''.join(compact))
results+=['LIMIT: Pandoc plain conversion retains four pre-existing shorthand-TeX conversion warnings in each Prices format; structured parsing passes. Mathematical payloads are unchanged. This is not a site or PDF rendering check.','RESIDUAL: Parent owns derivative builds, hash/index refresh, desktop/narrow and rendered-page inspection.','RESIDUAL: Parent will apply verified P09/AOT section/theorem renumbering after receiving the exact map from the current research lane. Existing citation tokens are unchanged here.']
(w/'scratchpad/editorial/check-results.txt').write_text('\n'.join(results)+'\n')
print('\n'.join(results))
