from pathlib import Path
import re,html,subprocess,json,hashlib
p=Path('sez-in-a-box.html');s=p.read_text()
Path('scratch/sez-pre-composition.html').write_text(s)
def plain(t):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',t))).strip()
headings=list(re.finditer(r'<h([1-6])\b[^>]*>.*?</h\1>',s,re.S))
def heading(text):
 matches=[m for m in headings if plain(m.group())==text]
 assert len(matches)==1,(text,len(matches))
 return matches[0]
a=heading('Part I: The Historical Architecture of Success').start();b=heading('Part II: The Network State Evolution').start()
history=s[a:b]
Path('scratch/part-i-source-valid.html').write_text(history)
refs=heading('References');end=s.index('<div class="c23">',refs.end())
bibliography=s[refs.start():end]
# Trim the original wrapper-closing material after the final bibliography paragraph.
endp=bibliography.rfind('</p>')+4;bibliography=bibliography[:endp]
# Preserve only historical comment notes whose references remain in retained history.
ids=set(re.findall(r'href="#(cmnt\d+)"',history));notes=[]
for m in re.finditer(r'<div class="c23">.*?</div>',s,re.S):
 if any('id="'+i+'"' in m.group() for i in ids):notes.append(m.group())
assert len(notes)==len(ids),(len(notes),len(ids))
parts=[]
for name in ['summary','architecture','implementation','future','appendices']:
 src=Path('scratch/'+name+'-source-valid.md')
 out=subprocess.run(['/opt/homebrew/bin/pandoc','--from=markdown-smart','--to=html5','--shift-heading-level-by=1','--wrap=none',str(src)],capture_output=True,text=True,check=True).stdout
 Path('scratch/'+name+'-source-valid.html').write_text(out);parts.append(out)
body=parts[0]+history+'\n'+''.join(parts[1:])+bibliography+'\n'
if notes:body+='<h2 id="historical-notes">Historical Notes</h2>\n'+''.join(notes)+'\n'
# Every heading becomes reachable; retain original heading identifiers where present.
used=set(re.findall(r'\bid="([^"]+)"',body));toc=[]
def fixheading(m):
 tag=m.group(1);attrs=m.group(2);title=plain(m.group(3));idm=re.search(r'\bid="([^"]+)"',attrs)
 if idm:ident=idm.group(1)
 else:
  base=re.sub('[^a-z0-9]+','-',title.lower()).strip('-');ident=base;n=2
  while ident in used:ident=base+'-'+str(n);n+=1
  used.add(ident);attrs+=' id="'+ident+'"'
 if int(tag)<=3:toc.append((int(tag),ident,title))
 return '<h'+tag+attrs+'>'+m.group(3)+'</h'+tag+'>'
body=re.sub(r'<h([1-6])([^>]*)>(.*?)</h\1>',fixheading,body,flags=re.S)
toc_html='<nav class="toc" aria-label="Contents"><h2>Contents</h2><ul>\n'+''.join('<li><a href="#'+html.escape(i,quote=True)+'">'+html.escape(t)+'</a></li>\n' for level,i,t in toc)+'</ul></nav>\n'
body=toc_html+body
prefix=s[:s.index('<div class="article-body">')+len('<div class="article-body">')]
footer=s[s.index('            <footer class="article-footer">'):]
# Any style assets within the old body are retained byte for byte.
old_body=s[len(prefix):s.index('            <footer class="article-footer">')]
styles=re.findall(r'<style\b[^>]*>.*?</style>',old_body,re.S)
result=prefix+'\n'+''.join(styles)+body+'            </div>\n\n'+footer
result=result.replace('<p class="article-meta">v0.35 — October 2025</p>','<p class="article-meta">15 October 2025 · Historical analysis and design proposal</p>')
p.write_text(result)
Path('scratch/final-body.html').write_text(body)
print('Candidate assembled',len(result.encode()),'bytes; historicalnotes',len(notes),'TOCentries',len(toc))
print('Style assets retained',len(re.findall(r'<style\b',s)),len(re.findall(r'<style\b',result)))
