from pathlib import Path
import json,html,re
p=Path('sez-in-a-box.html');s=p.read_text();log=json.loads(Path('scratch/final-source-boundary-repairs.json').read_text());restored=[]
keep_prefixes={'The tax incentives, while important','The digital economy push from 2014','Environmental sustainability challenges everything','Social cohesion challenges grow','Yet Mauritius had advantages','Operational success within a zone','Shannon also demonstrated the limitations',"Shannon's record raises the next question",'Consider a company that spent five years'}
keep_exact={"The dirham was pegged to the dollar, eliminating currency risk.","145-159.1: The Irish Innovation - Birth of the Modern SEZ (1959-1990)"}
for row in reversed(log):
 if 'disposition' in row:continue
 if 'prefix' in row:
  if row['prefix'] in keep_prefixes:continue
  old,new=row['old_html'],row['new_html'];assert s.count(new)==1,(row['prefix'],s.count(new));s=s.replace(new,old);restored.append(row)
 else:
  if row['old_text'] in keep_exact:continue
  a,b=html.escape(row['old_text'],quote=False),html.escape(row['new_text'],quote=False)
  assert s.count(b)==row['occurrences'],(a,s.count(b));s=s.replace(b,a);restored.append(row)
s=re.sub(r'<sup><a href="#cmnt\d+" id="cmnt_ref\d+">\[[a-z]+\]</a></sup>','',s)
p.write_text(s);Path('scratch/restored-under-root-boundary.json').write_text(json.dumps(restored,ensure_ascii=False,indent=2)+'\n')
print('Restored',len(restored),'unverified-only historical repairs; kept exact primary contradictions and pending specific portability approval.')
