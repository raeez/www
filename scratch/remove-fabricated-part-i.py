from pathlib import Path
import json
p=Path('sez-in-a-box.html');s=p.read_text(); records=[]
# Original document and pre-evidence-gate editorial work remain in scratch custody.
Path('scratch/sez-pre-evidence-gate.html').write_text(s)
sidebars=[
('Portugal Neuroplasticity Zone - Regulatory Innovation in Practice','the global center for regulated innovation.'),
("Hangzhou Pilot - Applying Shenzhen's Lessons",'with over $100 million in letters of intent already signed.'),
('Chongqing Pilot - Beyond Manufacturing','This innovation serves the financing needs of the real economy.'),
("RAK Pilot - Learning from Dubai's Ambition",'the fastest, most efficient gateway to the region.'),
('Nevada Pilot - Specialization in the American Context','the obvious choice for a new category.'),
('DIFC Upgrade - Addressing the Contradictions','technology can enable inclusion as well as efficiency.'),
("Nairobi Pilot - Applying Mauritius's Lessons",'African zones can succeed with the right approach.'),
('South Africa Pilot - Navigating Complexity','if they adapt to local realities rather than imposing foreign models.'),
('Zanzibar SEZ - A Different Chinese Partnership','Zanzibari partners value the protection against exploitation.')]
for title,last in sidebars:
 i=s.find(title);a=s.rfind('<hr>',0,i);j=s.index(last,i);b=s.index('</p>',j)+4
 assert a>=0 and a<i<j<b
 records.append({'type':'remove_known_invented_sidebar','title':title,'last_text':last,'text':s[a:b]})
 s=s[:a]+s[b:]
old="Our Mass deployment in DIFC builds on these Singapore-inspired foundations."
i=s.index(old);a=s.rfind('<p ',0,i);b=s.index('</p>',i)+4
records.append({'type':'remove_known_invented_deployment','first_text':old,'text':s[a:b]});s=s[:a]+s[b:]
a="The Dubai International Financial Centre, one of our brownfield pilots, explicitly modeled itself on Singapore's approach to financial center development."
b="The Dubai International Financial Centre explicitly modeled itself on Singapore's approach to financial center development."
assert s.count(a)==1;s=s.replace(a,b)
a="DIFC Dubai - Singapore's Lessons in the Desert";b="DIFC - Singapore's Lessons in the Desert";assert s.count(a)==2;s=s.replace(a,b)
p.write_text(s)
Path('scratch/evidence-removals.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Removed nine fabricated Part I sidebars and DIFC deployment paragraph; retained DIFC comparative history without pilot claim.')
