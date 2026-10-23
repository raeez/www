from pathlib import Path
import json,re
p=Path('sez-in-a-box.html'); s=p.read_text(); records=[]

def paragraph_start(text, body=True):
 i=s.rfind(text) if body else s.find(text)
 assert i>=0,text
 return s.rfind('<p ',0,i)
def heading_start(text, body=True):
 i=s.rfind(text) if body else s.find(text)
 assert i>=0,text
 starts=[s.rfind('<h'+str(n),0,i) for n in range(1,7)]
 return max(starts)
def move_sidebar(title,last_text,before_title,before_sidebar=False):
 global s
 i=s.find(title); a=s.rfind('<hr>',0,i)
 j=s.index(last_text,i); b=s.index('</p>',j)+4
 assert a>=0 and a<i<j<b
 piece=s[a:b];s=s[:a]+s[b:]
 if before_sidebar:
  dest=s.rfind('<hr>',0,s.find(before_title))
 else:dest=heading_start(before_title)
 assert dest>=0
 s=s[:dest]+piece+s[dest:]
 records.append({'type':'move_sidebar','title':title,'last_text':last_text,'before':before_title,'before_sidebar':before_sidebar,'bytes':len(piece.encode())})
move_sidebar("DIFC Dubai - Singapore's Lessons in the Desert",'audit cycles compressed from weeks to days.', 'Portugal Neuroplasticity Zone - Regulatory Innovation in Practice',True)
move_sidebar("Hangzhou Pilot - Applying Shenzhen's Lessons",'with over $100 million in letters of intent already signed.', 'Chapter 4: The UAE Revolution - Instant Cities in the Desert (1971-2024)')
move_sidebar('Chongqing Pilot - Beyond Manufacturing','This innovation serves the financing needs of the real economy.','Chapter 4: The UAE Revolution - Instant Cities in the Desert (1971-2024)')
move_sidebar("RAK Pilot - Learning from Dubai's Ambition",'the fastest, most efficient gateway to the region.','From Geographic Advantage to Network Position')
# Place the explanation of the future network before its 2030 projection.
a=heading_start('The Jurisdictional Future');b=heading_start('The Obligation to Build Well')
assert a<b
piece=s[a:b];s=s[:a]+s[b:];dest=heading_start('The 2030 Vision');s=s[:dest]+piece+s[dest:]
records.append({'type':'move_section','from':'The Jurisdictional Future','through':'The Emerging Topology of the Competitive Jurisdictional Network','before':'The 2030 Vision','bytes':len(piece.encode())})
# Keep the table of contents in the revised order. Page numerals belong to the source edition.
for title in ['The Jurisdictional Future','From Monopoly to Competition, From Capture to Exit','The Special Role of Special Economic Zones','The Emerging Topology of the Competitive Jurisdictional Network']:
 a=paragraph_start(title,False);b=s.index('</p>',a)+4;piece=s[a:b];s=s[:a]+s[b:];dest=paragraph_start('The 2030 Vision',False);s=s[:dest]+piece+s[dest:]
 records.append({'type':'move_toc_entry','title':title,'before':'The 2030 Vision'})
p.write_text(s)
Path('scratch/structural-edits.json').write_text(json.dumps(records,indent=2)+'\n')
print('Moved four pilot sidebars and the jurisdictional-future/topology section; TOC order follows section move.')
