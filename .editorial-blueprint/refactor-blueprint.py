from pathlib import Path
import re, html, json
p=Path('licc-blueprint.html')
source=p.read_text()
start=source.index('<div class="article-body">')
stop=source.index('<footer',start)
body=source[start:stop]
pattern=re.compile(r'<(p|h1|h2|h3|li)\b[^>]*>(.*?)</\1>',re.S)
blocks=[]
for m in pattern.finditer(body):
 text=' '.join(html.unescape(re.sub('<[^>]*>','',m.group(2))).split())
 if text:blocks.append((m,text))
assert len(blocks)==700,len(blocks)
changes={
6:'Founding Blueprint',
7:'Dual-Sponsorship Model and Institutional Strategy,',
8:'Implementation Plan and Fundraising Strategy',
11:'CONFIDENTIAL',
13:'The Laboratory for Incentivization, Coordination and Cooperation (LICC) is proposed as a joint research institution. Its sponsors would be the Massachusetts Institute of Technology (MIT) and the Mohamed bin Zayed University of Artificial Intelligence (MBZUAI). LICC will develop the emerging field of coordination science. This field studies mathematically and computationally how programmable incentive mechanisms can shape economic agents, institutions, and jurisdictions to achieve optimal collective outcomes.',
15:'Cryptographic primitives, programmable compliance infrastructure, and Special Economic Zones used for experimentation now support the development of a new academic discipline. Institutions governing international trade and jurisdictions still use frameworks designed before the digital era. LICC will develop the theory and tools for "programmable institutions" that operate at software speed while preserving the legitimacy and stability of traditional governance.',
17:"The dual-sponsorship model combines MIT's theoretical expertise in mechanism design, institutional economics, and network science with MBZUAI's applied AI infrastructure. MBZUAI also provides direct routes to government implementation through the UAE's 27 free zones. The MIT-MBZUAI Collaborative Research Program, announced in October 2025, provides an institutional framework that could expand to include LICC's coordination science mandate.",
33:'Part I: Institutional Context and Rationale',
35:'LICC is a proposed interdisciplinary research institute for the mathematical, computational, and empirical study of coordination mechanisms. Its scope ranges from individual economic transactions to international institutional design. Appendix B specifies the initial programs for Years 1-3. The research agenda includes:',
40:'Multi-Scale Coordination Dynamics: Study of how coordination mechanisms interact across individual, organizational, and societal scales',
41:'1.2 MIT: Institutional Profile and Research Resources',
42:"MIT has expertise in the theoretical foundations LICC requires. Its annual research spending totals $2.1 billion. In fiscal year 2024, industry-sponsored research totaled $175 million from over 300 companies, approximately 20% of total MIT research expenditures. According to the National Science Foundation, MIT consistently ranks first or second in industry-funded research and development expenditures among universities without a medical school.",
43:'Relevant MIT Faculty',
49:"Computational mechanism design researcher, Nevanlinna Prize recipient (2018), and Simons Investigator. His work on Nash equilibrium complexity and multi-item auction design applies directly to LICC's cryptoeconomic research.",
55:"Co-architect of EU GDPR and the UN SDG data framework, and an ADIA Lab advisory board member. His network science and computational social science research aligns with LICC's coordination dynamics research.",
58:'Turing Award laureate, inventor of verifiable random functions and zero-knowledge proofs, and founder of Algorand. His work provides cryptographic foundations for programmable compliance.',
61:'Studies network economics, game theory, and distributed optimization. Her multi-agent dynamics research is essential to understanding coordination at scale.',
62:'1.3 MBZUAI: Institutional Profile and Research Resources',
63:'The Mohamed bin Zayed University of Artificial Intelligence was established in October 2019. It is the world\'s first graduate-level research university dedicated entirely to artificial intelligence. Based in Masdar City, Abu Dhabi, it operates under the UAE Strategy for Artificial Intelligence 2031. This national initiative positions the UAE as a global AI hub. The university is fully state-funded, with sovereign wealth backing through Mubadala Investment Company.',
96:"In October 2025, MIT's Schwarzman College of Computing and MBZUAI announced the MIT-MBZUAI Collaborative Research Program. The five-year agreement brings together faculty, students, and research staff from both institutions. LICC could be established within this framework.",
116:'Adding LICC to the Collaboration',
117:'The MIT-MBZUAI collaboration explicitly addresses "social and ethical responsibilities of computing in shaping global impact". This aligns with LICC\'s coordination science mandate. The current program emphasizes foundation models, robotics, and healthcare AI. To add coordination science as a fourth research area, LICC must show how it complements these priorities.',
120:"Three structures could establish LICC within the MIT-MBZUAI framework. Each has advantages and constraints that must be assessed against LICC's long-term research independence requirements.",
122:'Mechanism: Propose LICC as an additional research theme within the MIT-MBZUAI Collaborative Research Program. "Coordination Science" would become a fourth research area alongside scientific discovery, human thriving, and planetary health.',
129:'Steering committee provides a clear decision process',
133:"Assessment: High access to resources, low autonomy. Suitable for the bootstrap phase (Months 1-12), but insufficient for LICC's long-term independence requirements.",
135:'Mechanism: Establish LICC as a legally distinct research institute with formal affiliation agreements with MIT and MBZUAI. It would govern itself independently and access institutional resources through partnership agreements.',
142:'Allows partnerships with other institutions (Santa Fe Institute, ETH Z\u00fcrich, etc.)',
148:"Assessment: Best suited to LICC's interdisciplinary mandate and long-term independence. Recommended for mature LICC operations. Appendix C sets out the proposed governance.",
150:'Mechanism: Establish LICC as a trilateral joint venture between MIT, MBZUAI, and UAE government entities (ADGM, Dubai Free Zone Council, or similar). LICC would operate as a quasi-governmental research institution with direct access to regulators.',
153:'Direct access to regulators for implementation research',
157:'Access to 27 UAE free zones for field research',
161:'Assessment: Greatest capacity to support implementation, with the most complex structure. Suitable for Phase 2 after proof-of-concept through Options A or B.',
163:'The recommended approach combines all three options in phases to launch quickly while preserving long-term independence:',
164:'Phase 1 (Months 1-12): Start through Option A. Launch initial research projects within the MIT-MBZUAI program to build faculty relationships and demonstrate research value.',
165:'Phase 2 (Months 12-24): Move to Option B. Establish LICC as an affiliated independent institute, maintain the MIT-MBZUAI partnership, and secure independent funding and governance.',
166:'Phase 3 (Months 24-48): Adopt selected elements of Option C. Formalize government partnerships for implementation research and expand research to jurisdictions beyond the UAE.',
167:'2.3 Complementary Strengths and Gaps',
168:'The dual-sponsorship structure must account for the expertise, resources, and access each institution provides or lacks.',
169:"MIT's Contributions",
170:"Domain Expertise in Mechanism Design: MBZUAI has virtually no faculty in game theory, mathematical economics, or auction theory. MIT's Daskalakis, Acemoglu, and affiliated researchers lead research in these fields.",
171:"Network Science and Social Physics: Pentland's Connection Science initiative has no MBZUAI equivalent. Its work is essential to understanding coordination dynamics at scale.",
175:"MBZUAI's Contributions",
177:"Implementation Laboratory: The UAE's 27 free zones provide sites for testing coordination mechanisms. MIT research remains theoretical without such testing grounds.",
180:"Speed of Decision-Making: As a young institution, MBZUAI can approve new initiatives faster than MIT's established bureaucracy.",
187:'Pursue parallel relationships with Santa Fe Institute (complex systems), Oxford Mathematical Institute (category theory), Simons Institute Berkeley (mechanism design), and ETH Z\u00fcrich (distributed systems). Maintain multiple institutional affiliations. Section 6.1 lists the proposed partnership models.',
199:'Start with Pentland, whose ADIA Lab role shows an interest in the UAE. Build support before approaching others. Offer research opportunities unavailable elsewhere.',
200:'Part III: Implementation Plan',
247:'Controls approval of MIT-MBZUAI expansion. Approach via MBZUAI channel.',
251:'Current program director. Propose adding LICC to the program.',
260:'Final decision-maker. Propose expanding the MIT relationship.',
278:'Phase 1: Establish Relationships (Months 1-6)',
287:'Search the MIT alumni directory for connections to MBZUAI, ADIA, G42, and the UAE government. Contact relevant alumni.',
290:'Draft a LICC concept note (5 pages) explaining how coordination science would expand the MIT-MBZUAI program.',
296:'Present LICC to Eric Xing through existing UAE/ADGM relationships. Explain how it would strengthen the MIT relationship.',
305:'Objective: Launch initial research projects and demonstrate their value.',
313:'Place 1-2 LICC researchers at MBZUAI as visiting scholars to establish a physical presence in Abu Dhabi.',
319:"Present at the MIT Connection Science seminar and MBZUAI workshop series to build awareness of LICC's work.",
325:'Review the pilot phase internally. Document lessons and refine the LICC model.',
328:'Objective: Establish LICC as an affiliated institute with independent governance and sustainable funding.',
347:'Part IV: Budget',
492:'Capital required before operating funding begins:',
541:'Propose strengthening the MIT relationship',
639:'Site for testing programmable compliance, with regulatory sandbox access',
668:"Master Research Agreement (MRA): Covers multiple projects over several years. Recommended for LICC's ongoing relationship.",
669:'Individual Research Agreement (IRA): Covers a single research project.',
670:'Consortium Agreement: Allows multiple industry sponsors to join LICC research programs.',
677:"Develop a mathematical framework for optimal coordination among the UAE's 27 free zones. Design incentives that align individual zone policies with federation-wide objectives, and model inter-zone capital flows and regulatory arbitrage.",
679:'Formally specify programmable compliance primitives for cross-jurisdictional assets. Develop cryptographic mechanisms for privacy-preserving regulatory reporting and a framework for Mass Protocol integration.',
681:'Analyze empirically how regulatory competition affects institutional quality. Model jurisdiction selection by mobile capital and talent using game theory, and assess the implications for optimal regulatory design.',
683:'Proposed governance for LICC as an affiliated independent institute:'
}
records=[]
for i,new in sorted(changes.items(),reverse=True):
 m,old=blocks[i-1]
 inner=m.group(2)
 sm=re.fullmatch(r'(<span\b[^>]*>)(.*?)(</span>)',inner,re.S)
 if not sm or '<' in sm.group(2): raise ValueError((i,inner))
 replacement=m.group(0).replace(inner,sm.group(1)+html.escape(new,quote=False)+sm.group(3),1)
 body=body[:m.start()]+replacement+body[m.end():]
 records.append({'block':i,'old':old,'new':new})
# Remove the visible version label while preserving date and classification.
source=source[:start]+body+source[stop:]
assert source.count('December 2025 \u2022 Version 1.0 \u2022 CONFIDENTIAL')==1
source=source.replace('December 2025 \u2022 Version 1.0 \u2022 CONFIDENTIAL','December 2025 \u2022 CONFIDENTIAL')
p.write_text(source)
Path('blueprint-edits.json').write_text(json.dumps(list(reversed(records)),indent=2,ensure_ascii=False)+'\n')
print(f'Changed {len(records)} article blocks and visible version marker; structure preserved.')
