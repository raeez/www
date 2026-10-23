from pathlib import Path
from html import escape
import json
p=Path('sez-in-a-box.html');s=p.read_text()
links=[
("The courts may draw on decisions from England and Wales and other common-law jurisdictions.",'https://edge.sitecorecloud.io/dubaiintern0078-difcexperie96c5-production-3253/media/project/difcexperiences/difc/difcwebsite/documents/difc_docs/difc-law-no-3-of-2004_2024_updated.pdf','DIFC Law No. 3 of 2004, consolidated November 2024, articles 8 and 8A'),
("DIFC's own statutes and judgments determine its law; the jurisdiction is distinct from England and Wales.",'https://www.difccourts.ae/about/faq/courts-faq','DIFC Courts, applicable-law guidance'),
("Businesses gain access to an established body of commercial law within a distinct local jurisdiction.",'https://assets.adgm.com/download/assets/adgm-guidance-application-of-english-laws.pdf/58871c7eb0a711ef916e5ef481f270ea','ADGM English-law guidance, §§2.1–2.2 and 3.1–3.2'),
("subject to eligibility conditions and grounds for setting registration aside.",'https://assets.adgm.com/download/assets/AMENDED%2BCourts%2BRegulations%2B2015%2B-%2B17102025%2B%28FINAL%29.pdf/ae7e4a5045b611efbd775aec9993a0bd','ADGM Courts Regulations, consolidated 17 October 2025, §§171–175'),
("The scope of ownership rights remained subject to the applicable activity and legal regime.",'https://www.jafza.ae/resource-centre/downloads/jafza-rules-regulations/','Jafza Rules 2023, §3'),
("Other quadrants have different operators, including the southeast where the Dangote refinery is located.",'https://www.lekkizone.com.ng/quadrants/','Lekki Worldwide Investments, quadrant directory'),
("The Chinese joint venture, Lekki Free Zone Development Company, holds the 3,000-hectare southwest concession.",'https://lfzdc.org/signing-of-lfzdc-concession-agreement/','LFZDC, 19 May 2015'),
("Owned and managed by Jiangsu Qiyuan Group, the park aimed to apply Jiangsu's manufacturing experience in Ethiopia.",'https://ipp.unido.org/sites/default/files/knowledge/2020-11/Industrial%20park%20development%20in%20Ethiopia%20case%20study%20report.pdf','UNIDO, 2018, pp. 23–24')
]
for phrase,url,label in links:
 old=escape(phrase,quote=False);assert s.count(old)==1,(phrase,s.count(old));s=s.replace(old,old+' <a href="'+escape(url,quote=True)+'">'+escape(label)+'</a>.')
s=s.replace("Qualifying judgments from England and Wales's Commercial Court", "Qualifying money judgments from England and Wales's Commercial Court")
# Preserve the three substantive inquiries formerly left as outline notes.
additions=[
('The social impact extended far beyond the factory gates.', 'The move toward design and development also raises a question for later zones: are technology startups the highest-value form of activity a zone can support, and what evidence would establish that comparison?'),
('Within five years, the port was operating near capacity.', 'Whether new services change the risk of oversupply remains a question for an innovation-focused zone. The comparison should distinguish demand created by useful infrastructure from demand assumed in a conventional property development.'),
('These routes leave a wider question about the participation and long-term security of expatriate residents.', 'The integration question also applies to zones elsewhere, including China and Indonesia: how can development narrow the divide between different groups of workers and residents?')
]
for before,new in additions:
 a=escape(before,quote=False);assert s.count(a)==1,(before,s.count(a));s=s.replace(a,a+' '+escape(new,quote=False))
# Conventional publication and revision dates, not a draft/version banner.
assert s.count('15 October 2025 · Historical analysis and design proposal')==1
s=s.replace('15 October 2025 · Historical analysis and design proposal','15 October 2025 · Updated 22 October 2026 · Historical analysis and design proposal')
p.write_text(s);Path('scratch/final-primary-source-citations.json').write_text(json.dumps(links,ensure_ascii=False,indent=2)+'\n');Path('scratch/outline-inquiry-destinations.json').write_text(json.dumps(additions,ensure_ascii=False,indent=2)+'\n')
print('Added',len(links),'final source citations, preserved3inquiries, dated revision')
