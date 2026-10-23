from pathlib import Path
import json, html, sys
p=Path('sez-in-a-box.html')
s=p.read_text()
allrows=[]
for file in sys.argv[1:]:
 rows=json.loads(Path(file).read_text())
 for row in rows:
  old,new=row[:2]
  expected=row[2] if len(row)>2 else 1
  a,b=html.escape(old,quote=False),html.escape(new,quote=False)
  count=s.count(a)
  if count!=expected:
   raise SystemExit(f'{file}: expected {expected} occurrences, got {count}: {old[:150]}')
  s=s.replace(a,b)
  allrows.append((old,new))
p.write_text(s)
print('Applied',len(allrows),'specific replacements')
