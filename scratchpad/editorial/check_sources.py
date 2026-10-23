from pathlib import Path
import re,json,subprocess,hashlib,difflib
root=Path(__file__).resolve().parents[2]
raw=root/'materials/raw/2026-09-09-accessible-papers'; out=root/'content/reader-papers'
checks=[]

def parsed_tokens(text,fmt):
 if fmt=='markdown':
  text=text.split('\n## References')[0]
  text=re.sub(r'\\\[.*?\\\]','',text,flags=re.S)
 else:
  text=text.split(r'\begin{thebibliography}')[0]
  text=text.split(r'\begin{document}',1)[1]
  text=text.replace(r'\maketitle','').replace(r'\begin{abstract}','').replace(r'\end{abstract}','')
  text=re.sub(r'\\cite(?:\[[^]]*\])?\{[^}]*\}','',text)
  text=re.sub(r'\\(?:section|label)\{[^}]*\}','',text)
 res=subprocess.run(['pandoc','-f',fmt,'-t','json'],input=text,text=True,capture_output=True)
 if res.returncode:raise RuntimeError(res.stderr)
 data=json.loads(res.stdout)
 def walk(n):
  if isinstance(n,list):return ''.join(walk(x) for x in n)
  if not isinstance(n,dict):return ''
  t=n.get('t');c=n.get('c')
  if t=='Str':return c
  if t in ('Space','SoftBreak','LineBreak'):return ' '
  if t in ('Header','RawInline','RawBlock'):return ''
  if t=='Math':return ' MATH{'+re.sub(r'\s+','',c[1])+'} '
  if t=='Quoted':return '"'+walk(c[1])+'"'
  return walk(c)+' ' if t in ('Para','Plain') else walk(c)
 result=walk(data['blocks'])
 return re.sub(r'\s+',' ',result.replace('“','"').replace('”','"').replace('’',"'").replace('–','--')).strip(),res.stderr

for stem in ('title-remedies-and-institutional-change','when-institutional-programs-work-together'):
 for ext in ('.md','.tex'):
  a=raw/(stem+ext);b=out/(stem+ext)
  x=a.read_text();y=b.read_text()
  baseline=subprocess.check_output(['git','show','HEAD:'+str(a.relative_to(root))],cwd=root)
  assert a.read_bytes()==baseline
  assert a.read_bytes()==(Path('/Users/raeez/www')/a.relative_to(root)).read_bytes()
  assert re.findall(r'\d+(?:[.,]\d+)*',x)==re.findall(r'\d+(?:[.,]\d+)*',y),(stem,ext,'numeric tokens')
  if ext=='.md':
   math=lambda s:re.findall(r'\$\$.*?\$\$|(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)',s,re.S)
   links=lambda s:re.findall(r'\]\(([^)]*)\)',s)
   quotes=lambda s:re.findall(r'"([^"]*)"',s)
   assert links(x)==links(y)
   assert quotes(x)==quotes(y)
   ids=re.findall(r'\{#([^}]+)\}',y); targets=links(y)
   assert all(v[1:] in ids for v in targets if v.startswith('#'))
  else:
   math=lambda s:re.findall(r'\\\[.*?\\\]|(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)',s,re.S)
   citations=lambda s:re.findall(r'\\cite(?:\[[^]]*\])?\{[^}]*\}',s)
   quotes=lambda s:re.findall(r"``(.*?)''",s,re.S)
   assert citations(x)==citations(y)
   assert quotes(x)==quotes(y)
   assert x.split(r'\begin{thebibliography}')[1]==y.split(r'\begin{thebibliography}')[1]
  assert math(x)==math(y)
  assert not re.search(r'(?im)\b(v[0-9]+|version\s+[0-9]|prior\s+draft|previous\s+(draft|version)|superseded|post-(M|W|L|R|Z)[0-9]|phase\s+L[0-9]|to\s+our\s+knowledge|we\s+believe|essentially|basically)\b',y)
  private=r'~/(?:kernel|centcom|moxie|momentum|ecosystem)|/Users/[^/ ]+/(?:kernel|centcom|moxie|momentum|ecosystem)|kernel/(?:formal|docs|mez|\.claude)|centcom/'
  assert not re.search(private,y)
  checks.append({'file':b.name,'raw_sha256':hashlib.sha256(a.read_bytes()).hexdigest(),'maintained_sha256':hashlib.sha256(b.read_bytes()).hexdigest(),'raw_unchanged':True,'numbers_math_quotes_references_preserved':True,'public_source_and_external_metadata_scan':'zero hits'})
 md,md_warnings=parsed_tokens((out/(stem+'.md')).read_text(),'markdown')
 tex,tex_warnings=parsed_tokens((out/(stem+'.tex')).read_text(),'latex')
 (root/'scratchpad/editorial'/(stem+'.md.normalized')).write_text(md)
 (root/'scratchpad/editorial'/(stem+'.tex.normalized')).write_text(tex)
 if md!=tex:
  print('\n'.join(difflib.unified_diff(md.split(),tex.split(),n=5)))
  raise AssertionError((stem,'MD/TeX text differs'))
 checks.append({'work':stem,'pandoc_parse':'success','markdown_tex_body_and_math_alignment':'equal','warnings':{'md':md_warnings,'tex':tex_warnings}})
(root/'scratchpad/editorial/check-results.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
