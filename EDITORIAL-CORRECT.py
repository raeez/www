from pathlib import Path
import re,html,json,hashlib,difflib
p=Path('smart-buildings.html');s=p.read_text();before=s
assert hashlib.sha256(s.encode()).hexdigest()=='05d668d9b2ea566a763a0e8e2649df2083b76a21d802eadc06f799faa15bc373'
changes=json.loads(Path('EDITORIAL-EDITS.json').read_text())
orig={int(m.group(1)):m.group(3) for m in re.finditer(r'^\[(\d+) ([^\]]+)\] (.*)$',Path('EDITORIAL-SOURCE.txt').read_text(),re.M)}
corrections={
12:'This requires solving six problems current smart building initiatives ignore: shared semantic understanding, continuous provenance, collective learning, aligned incentives, transparent value attribution, and autonomous operation. Building intelligence depends on these foundations.',
19:'This is standard practice. Design, as-built, and as-operated records remain disconnected, with no reliable way to reconcile them. Each interface between disciplines requires translation. Every translation introduces errors that compound. By the time a building operates, its configuration only loosely resembles its design, and nobody has complete, accurate documentation of what exists.',
50:'As regulatory complexity and transaction volumes grow, every institution duplicates KYC, compliance, and reconciliation because assets carry no compliance context. Every cross-border transaction requires manual coordination between regulatory regimes, while every corporate action requires large operations teams to execute procedures manually. The marginal cost of financial operations never approaches zero because assets remain passive.',
87:'The building carries this intelligence as an intrinsic property. Attestation streams maintain its operational memory, executable compliance rules continuously prove adherence, and programmatic operating rules execute themselves.',
103:'Each perspective is a valid view of the same physical reality. When these views cannot be formally reconciled, coordination requires constant manual translation. The architect\'s "wall" becomes the engineer\'s wall model, then the contractor\'s wall assembly, then the operator\'s maintenance schedule. Each translation can introduce errors that compound. By project completion, the as-built wall diverges from the design in ways nobody fully understands.',
105:'This requires computational ontology: executable semantics that let machines reason about building concepts as humans do, beyond documentation standards alone. For a control command about "wall temperature," the system must identify the entity the architect designed, the contractor built, and the operator maintains. Automated operation depends on that shared understanding.',
109:'Cryptographic attestation solves incompleteness and unreliability together. Attestations are generated automatically as actions occur: the installer\'s device records completed work and signs it cryptographically. Once written to the attestation stream, the record cannot be altered or deleted without detection. Its complete context includes unit specifications, configuration, test results, and inspector verification, beyond the statement "HVAC installed".',
112:'Buildings should inherit lessons from one another. One HVAC failure should inform maintenance schedules for all similar buildings, and an energy optimization technique should propagate across the network. The results of experiments with new materials should be available to all future projects.',
115:'A shared ontology and attestation streams solve both problems. Operators can compare a building\'s HVAC performance with thousands of similar buildings using identical equipment. Cryptographic provenance verifies energy savings through recorded evidence rather than self-reports.',
124:'Aligned incentives with mediocre technology produce better results than misaligned incentives with excellent technology. Better tools in adversarial systems make dysfunction more efficient. The economic foundations must be fixed before technology can deliver value.',
125:'Aligned incentives and complete provenance make value attribution automatic: the building knows exactly who contributed what to its success or failure. Verified contributions allow excellent performers to increase their advantage and poor performers to be removed.',
134:'A Smart Building holds treasury assets, contracts with service providers, verifies completed work, and authorizes payment. It uses learned intelligence to optimize operations. It also negotiates better utility rates, reports compliance to regulators automatically, onboards occupants through programmable identity, and enforces governance rules through programmatic consent.',
136:'A Smart Building\'s sensors record the failing component in its attestation stream, and its predictive model evaluates failure likelihood and impact. If intervention is warranted, it solicits bids from pre-qualified providers and selects by verified performance history and current availability. It grants access credentials for the scheduled window, then uses sensor data to verify completed work and checks quality against its ontology\'s specifications. Finally, it pays from its treasury and records the complete maintenance history in the attestation stream. The entire process happens automatically in minutes.',
146:'Establishing foundations out of order or in parallel with feature deployment reliably fails. PropTech companies typically prioritize sensors, dashboards, and optimization algorithms. Improvements remain marginal because the building stays unintelligent, coordination stays manual, and incentives stay misaligned. Users leave after their initial enthusiasm because improvements cannot compound.',
155:'The ontology integrates with Compas.dev, an open-source Python framework for computational architecture, and BHoM, the Building and Habitat Object Model. These industry standards let computational architects use their existing concepts while extending them across the full operational lifecycle.',
171:'When a component is installed, the installer\'s device generates an attestation. The component\'s serial number and specifications are verified against manufacturer records, and AR visualization confirms its location. The inspector verifies code compliance, then all parties sign. The attestation enters the building\'s stream as a permanent verified record.',
172:'These streams become the building\'s authoritative history. They supply complete service histories for maintenance, continuous proof for compliance, and objective evidence for performance evaluation.',
184:'When performance triggers occur, the building\'s treasury automatically distributes compensation to members according to encoded rules. It manages its finances without invoices, approval workflows, or payment delays.',
198:'When the building detects changed occupancy patterns, energy optimization adjusts HVAC schedules and predictive maintenance moves service to the new low-occupancy periods. Space utilization proposes reconfiguring underused areas, while financial optimization renegotiates utility contracts for the new load profiles. Collective learning propagates these responses to similar buildings, so one building\'s adaptation benefits the others.',
207:'A building needing landscaping automatically solicits bids from network providers with verified track records and evaluates proposals using attestation-proven performance. It selects the optimal provider by price, quality, and availability, then grants time-limited access credentials. Sensor data and photographic evidence verify completion before the building pays from its treasury. The verified outcome updates the landscaper\'s reputation, and the building records the complete transaction in its attestation stream.',
208:'In this "operating system" model, HomeOS supplies core infrastructure in Layers 1-4, while the ecosystem supplies unlimited extensions in Layer 5. As iOS supports millions of apps, HomeOS supports an entire service economy around intelligent buildings.',
325:'Developer ecosystem: Third-party developers prefer a larger installed base. More buildings attract more developers and plug-ins, expanding the capabilities that attract further buildings.',
334:'The best architects, engineers, contractors, and operators then prefer HomeOS projects. Their superior performance produces stronger attestations, which attract premium projects. Those projects attract further top talent, reinforcing participants\' preference for the network.',
340:'Competitors cannot catch up simply by deploying sensors. Attestations cover the full lifecycle, from manufacturing through decades of operation, including verified actions, decisions, and outcomes alongside sensor data. Their value compounds in ways late entrants cannot replicate.',
360:'The deployment tests require three preparatory workstreams: ontology, attestations, and the alliance framework. Validating these foundations before scaling features distinguishes HomeOS from earlier PropTech approaches.',
416:'Most PropTech deployed features before establishing ontology, attestation streams, and aligned incentives. Gains remained marginal, and users left after their initial enthusiasm because improvements could not compound. This makes foundation validation the first implementation test.',
419:'HomeOS addresses economics first through Instance-Backed Alliance. Collective success becomes profitable for every participant, and everyone gains new revenue streams without threatening anyone\'s existing business model. This removes the adoption friction caused by misaligned incentives.',
428:'Physical replication is the final test. Many earlier initiatives used custom design and construction, leaving each building unique and preventing reliable automation, meaningful comparison, or collective learning. They produced individual demonstrations that could not scale economically.',
445:'When all participants profit from collective success, Instance-Backed Alliance changes construction work. Collaboration replaces conflict, information sharing replaces concealment, and early problem identification replaces blame-shifting. Innovation becomes rewarded rather than punished.',
448:'Smart Buildings also allow physical infrastructure to be managed as software. Buildings can gain new capabilities, operations can be optimized continuously, problems can be debugged systematically, and improvements can propagate automatically.',
449:'Infrastructure development then becomes product engineering. Traditional construction treats each building as a unique prototype requiring custom design, construction, and operation. Each Smart Building instead instantiates an evolving platform and inherits all improvements from previous instances.',
450:'Traditional infrastructure yields diminishing returns as buildings age and deteriorate. Programmable infrastructure yields increasing returns as network learning makes buildings smarter over time. Traditional infrastructure requires expensive periodic replacement, while programmable infrastructure undergoes continuous incremental improvement.',
454:'The proposal makes buildings Smart Assets: autonomous economic entities that carry their complete operational intelligence, enforce their rules, and execute their operations. Its six dependencies follow a specific order: shared semantic understanding, continuous provenance, collective learning, aligned incentives, transparent value attribution, and autonomous operation.',
461:'The calendar follows the validation sequence. Controlled pilots in 2026 establish that the foundations work operationally, and expansion to 1,000 buildings through 2027 validates network effects. Manufacturing scale from 2028 onward produces cost advantages through standardization. Each phase depends on the preceding validation, managing risk before further expansion.',
465:'Smart Assets have already changed financial markets, establishing the pattern. Physical infrastructure built on identical primitives will undergo a similar transformation. Buildings will become programmable, leaving who builds the operating system as the unresolved question.',
466:'Momentum, Broad Group, and Jan Bunge have established the foundations. The pilot deployments are funded and scheduled, the partnerships are formed, and the regulatory frameworks are operational. Network effects are beginning to compound.',
467:'The digital transformation of the built environment is underway. Those who understand that intelligence requires foundations will capture extraordinary value. Those who continue deploying features without them will fail as earlier PropTech initiatives did.'
}
def plain(raw):return ' '.join(html.unescape(re.sub('<[^>]+>','',raw)).split())
def locate(text,tagpattern='p|li|h[1-4]'):
 a=[m for m in re.finditer(r'<('+tagpattern+r')\b[^>]*>.*?</\1>',s) if plain(m.group())==text]
 if len(a)!=1:raise ValueError((len(a),text))
 return a[0]
rows=[]
for n,new in corrections.items():
 old=changes[str(n)]['after'];m=locate(old);r=m.group();spans=list(re.finditer(r'(<span\b[^>]*>)(.*?)(</span>)',r))
 if len(spans)==1:z=spans[0];newbody=new
 elif len(spans)==2:
  prefix=html.unescape(spans[0].group(2));assert new.startswith(prefix),(n,prefix);z=spans[1];newbody=new[len(prefix):]
 else:raise ValueError((n,len(spans)))
 r=r[:z.start(2)]+html.escape(newbody,quote=False)+r[z.end(2):];s=s[:m.start()]+r+s[m.end():]
 rows.append(f'Original block {n}\n'+''.join(difflib.unified_diff([old+'\n'],[new+'\n'],fromfile='candidate',tofile='corrected')))
 changes[str(n)]={'before':orig[n],'after':new}
# Move both section headings with their content.
m=locate('Integration with Broad Group Manufacturing','h4');heading=m.group();s=s[:m.start()]+s[m.end():]
at=locate(changes['209']['after']).start();s=s[:at]+heading+s[at:]
m=locate('The Layered Architecture','h4');heading=m.group();s=s[:m.start()]+s[m.end():]
at=locate(changes['152']['after']).start();s=s[:at]+heading+s[at:]
headings={
'The IoT Overlay Fallacy':'Limits of Adding Sensors',
'The Digital Twin Delusion':'Digital Twins Diverge from Building State',
'The Coordination Software Trap':'Coordination Software Preserves Existing Relationships',
"What's Missing: Foundations":'The Required Foundations',
'Instance-Backed Alliance Creates Participant Lock-In':'Instance-Backed Alliance Retains Participants',
'Attestation Data Creates Unique Moat':'Attestation Data Creates an Irreplaceable Advantage'
}
for old,new in headings.items():
 m=locate(old,'h4');r=m.group();assert old in r;r=r.replace(old,new);s=s[:m.start()]+r+s[m.end():];rows.append('Heading\n-'+old+'\n+'+new+'\n')
# Explicit root ruling: remove process version label, keep historical month/year.
assert s.count('Version 0.3 — September 2025')==1
s=s.replace('Version 0.3 — September 2025','September 2025')
rows.append('Article metadata\n-Version 0.3 — September 2025\n+September 2025\n')
p.write_text(s);Path('EDITORIAL-EDITS.json').write_text(json.dumps(changes,indent=2))
Path('EDITORIAL-CORRECTION-DELTA.txt').write_text('\n'.join(rows)+'\nHeading movement: Integration with Broad Group Manufacturing now precedes original209; The Layered Architecture now precedes original152.\n')
Path('EDITORIAL-CORRECTION.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),s.splitlines(True),fromfile='a/smart-buildings.html',tofile='b/smart-buildings.html')))
Path('EDITORIAL-HEADING-EDITS.json').write_text(json.dumps(headings,indent=2))
print('Corrected',len(corrections),'body blocks and',len(headings),'headings; moved2 headings; removed1 version label')
print(hashlib.sha256(s.encode()).hexdigest())
