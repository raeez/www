from pathlib import Path
import json,re
p=Path('prefabricated-construction.html');s=p.read_text()
edits=json.loads(Path('.editorial-prefab/replacements.json').read_text())
def change(old,new,reason):
 global s
 assert s.count(old)==1,(reason,s.count(old))
 s=s.replace(old,new,1)
 edits.append({'old':old,'new':new,'reason':reason,'kind':'heading-and-composition-refinement'})
for old,new in [
 ('Key Characteristics of PC and Modular Technologies','PC and Modular Construction: Strengths and Limits'),
 ('Modular construction application Scenarios &amp; Case Studies','Modular Construction: Applications and Case Studies'),
 ('Here we run through a wide range of use-cases of modular integrated building systems.','Housing and Tourism'),
 ('5. Comparative Performance Showcase: Modular vs Traditional','5. Modular vs Traditional Construction'),
 ('6. Technical System Performance Highlights','6. Technical Performance'),
 ('Common Use Cases for PC Construction','PC Construction for Housing Programs'),
 ('Summary: A Flexible, Prefabricated Future','Choosing a Construction System'),
 ('PC vs Modular Construction: Technical Feature Comparison Table','PC and Modular Construction: Technical Comparison')
]:
 headings=[m[0] for m in re.finditer(r'<h[1-6]\b[^>]*>.*?</h[1-6]>',s,re.S) if old in m[0]]
 assert len(headings)==1,(old, len(headings))
 change(headings[0],headings[0].replace(old,new,1),'Use a plain heading while retaining its anchor and technical scope: '+new+'.')
 toc=[m[0] for m in re.finditer(r'<a\b[^>]*href="#h\.[^\"]+"[^>]*>.*?</a>',s,re.S) if old in m[0]]
 assert len(toc)==1,(old,len(toc))
 change(toc[0],toc[0].replace(old,new,1),'Synchronize the contents label with the revised heading; retain target and historical page reference.')

old=re.search(r'<h3\b[^>]*id="h\.oodellg6gdg4"[^>]*>.*?</h3>',s,re.S)[0]
start=old.split('>',1)[0]+'>'
content=old.split('>',1)[1].rsplit('</h3>',1)[0]
label='<span class="c9 c11">Definition</span>'
assert content.startswith(label)
definition=content[len(label):].replace(': PC = ','PC = ',1)
new=start+label+'</h3><p class="c3">'+definition+'</p>'
change(old,new,'Keep the PC definition verbatim in body prose below a short heading, preserving the existing definition anchor.')
toc=[m[0] for m in re.finditer(r'<a\b[^>]*href="#h\.oodellg6gdg4"[^>]*>.*?</a>',s,re.S) if 'Definition: PC' in m[0]]
assert len(toc)==1
oldlabel='Definition: PC = Precast Concrete (sometimes broadened to "precast components"). Structural elements are cast in a controlled factory environment, cured, transported, and then assembled onsite.'
assert oldlabel in toc[0]
change(toc[0],toc[0].replace(oldlabel,'Definition',1),'Shorten the definition contents entry; keep the entire technical definition in the article and preserve the existing target/page reference.')

for old,new in [
 ('>Extreme Speed: </span>','>Installation Speed: </span>'),
 ('>Extreme Speed</span>','>Installation Speed</span>'),
 ('>Plug-and-Play Simplicity</span>','>Integrated Systems</span>'),
 ('>Youth-Focused Livability</span>','>Housing for Young Professionals</span>'),
 ('>Site Minimalism</span>','>Site Work</span>'),
 ('>Precision &amp; Aesthetics</span>','>Interior Quality and Design</span>'),
 ('>Regulatory Simplicity</span>','>Government Approval</span>')
]:change(old,new,'Use a concrete table/list label while preserving the associated technical response unchanged.')
change('Construction costs in the UAE are expected to increase ','UAE construction costs are expected to increase ','Shorten the cost forecast sentence while preserving both countries, ranges, forecast qualifications and citation.')
change('They serve complementary project types and conditions.<br><br></span><span class="c9">Precast Concrete (PC)</span>','They serve complementary project types and conditions.</span></p><p class="c3"><span class="c9">Precast Concrete (PC)</span>','Give the common mechanism and the PC-specific explanation separate paragraphs instead of an internal line-break pair.')

p.write_text(s)
Path('.editorial-prefab/replacements.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
print('Heading/layout refinement complete:',len(edits),'ordered old/new records.')
