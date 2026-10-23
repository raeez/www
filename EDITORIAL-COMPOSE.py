from pathlib import Path
import re,html,json
p=Path('smart-buildings.html');s=p.read_text();changes=json.loads(Path('EDITORIAL-EDITS.json').read_text())
orig={int(m.group(1)):m.group(3) for m in re.finditer(r'^\[(\d+) ([^\]]+)\] (.*)$',Path('EDITORIAL-SOURCE.txt').read_text(),re.M)}
def text_of(raw):return ' '.join(html.unescape(re.sub('<[^>]+>','',raw)).split())
def block(n):
 text=changes.get(str(n),{}).get('after',orig[n])
 matches=[m for m in re.finditer(r'<(p|li|h[123])\b[^>]*>.*?</\1>',s) if text_of(m.group())==text]
 if len(matches)!=1:raise ValueError((n,len(matches),text))
 return matches[0]
def replace(n,new):
 global s
 m=block(n);r=m.group();spans=list(re.finditer(r'(<span\b[^>]*>)(.*?)(</span>)',r));assert len(spans)==1
 z=spans[0];r=r[:z.start(2)]+html.escape(new,quote=False)+r[z.end(2):];s=s[:m.start()]+r+s[m.end():]
 changes[str(n)]={'before':orig[n],'after':new}
replace(152,'The six foundations describe what must be established. The five HomeOS layers organize the running system, with each depending on the previous layer:')
replace(225,'The initial sites test the foundations under different residential, commercial, and regulatory conditions before features scale.')
replace(360,'The deployment tests require three preparatory workstreams: ontology, attestations, and alliance agreements. Validating these foundations before scaling features distinguishes HomeOS from earlier PropTech approaches.')
# Physical requirements precede the runtime layer walkthrough.
a,b=block(209).start(),block(222).end();segment=s[a:b];s=s[:a]+s[b:];at=block(152).start();s=s[:at]+segment+s[at:]
# Remove only the conclusion's duplicate failure/foundation exposition.
for n in [455,456]:
 m=block(n);s=s[:m.start()]+s[m.end():]
 changes[str(n)]['after']='[Removed duplicate exposition; claims retained in 146–147 and 416–417.]'
# Dates and current commitments give the concluding return its new purpose.
m=block(461);segment=m.group();s=s[:m.start()]+s[m.end():];at=block(457).start();s=s[:at]+segment+s[at:]
m=block(466);segment=m.group();s=s[:m.start()]+s[m.end():];at=block(460).end();s=s[:at]+segment+s[at:]
p.write_text(s);Path('EDITORIAL-EDITS.json').write_text(json.dumps(changes,indent=2))
Path('EDITORIAL-COMPOSITION.txt').write_text('Moved original blocks 209–222 before 152, establishing physical requirements before runtime layers. Rewrote 152 to distinguish six prerequisites from five system layers.\nRewrote 225 for site-validation purpose and 360 for implementation workstreams.\nRemoved duplicate conclusion blocks 455–456; all claims remain in 146–147 and 416–417.\nMoved 461 (calendar) before 457 (participants), and 466 (claimed current position) immediately after 460 (Mass role). Conclusion now develops market/thesis → timetable → participants → current commitments → competition/consequences.\n')
print('Composition complete')
