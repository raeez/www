from pathlib import Path
import json,re
p=Path('prefabricated-construction.html');s=p.read_text()
edits=json.loads(Path('.editorial-prefab/replacements.json').read_text())
def change(old,new,reason):
 global s
 assert s.count(old)==1,(reason,s.count(old))
 s=s.replace(old,new,1)
 edits.append({'old':old,'new':new,'reason':reason,'kind':'box-recurrence-consolidation'})
for label in ['Installation Speed: ','Quality Uniformity: ','Reuse &amp; Mobility: ']:
 items=[m[0] for m in re.finditer(r'<li\b[^>]*>.*?</li>',s,re.S) if label in m[0]]
 assert len(items)==1
 change(items[0],'','Consolidate '+label.strip()+ ' with its government-response table row; preserve the complete claim there.')
old=[m[0] for m in re.finditer(r'<p\b[^>]*>.*?</p>',s,re.S) if 'Factories complete the structure, MEP, and interiors. Units take ' in m[0]]
assert len(old)==1
new='<p class="c3"><span class="c2">Crews can complete buildings in weeks and install each apartment in </span><span class="c9">&lt;24 hours</span><span class="c7 c2">&nbsp;with plug-and-play connections.</span></p>'
change(old[0],new,'Combine building-completion and apartment-installation times with the plug-and-play connection condition; factory completion remains in the definition.')
change('Pre-integrated bathrooms, kitchens, HVAC, and lighting minimize onsite integration risk.','Pre-integrated services minimize onsite integration risk.','The preceding functional list names the installed equipment; the table adds its integration-risk consequence.')
change('Factory-crafted interiors ensure consistent quality and design across deployments.','Factory-standardized interiors provide consistent finishes, quality, and design across deployments and reduce defects.','Combine the unique finish/defect claims with the across-deployment quality/design consequence.')
change('Select modules can be detached and reused, allowing owners to adapt their use over the long term.','Select modules can be detached and reused, allowing owners to adapt their use over the long term. Modules can sometimes be detached and relocated for temporary housing or flexible institutional projects.','Keep select-module reuse and conditional relocation with both temporary and institutional uses in the same response row.')
p.write_text(s)
Path('.editorial-prefab/replacements.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
print('BOX repetition consolidated;',len(edits),'ordered replacement records.')
