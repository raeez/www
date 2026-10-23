from pathlib import Path
import html,json
p=Path('sez-in-a-box.html');s=p.read_text();prior=json.loads(Path('scratch/final-source-boundary-repairs.json').read_text())
# Retain unique surrounding historical material; replace only the contradicted assertion.
for prefix in ['Environmental sustainability challenges everything','Social cohesion challenges grow','Yet Mauritius had advantages','The digital economy push from 2014']:
 row=next(x for x in prior if x.get('prefix')==prefix);assert s.count(row['new_html'])==1;s=s.replace(row['new_html'],row['old_html'])
rows=[
["Water comes entirely from energy-intensive desalination.","Desalination supplies much of the country's potable water, alongside groundwater and other sources used for different purposes.","UAE Government, water resources overview","https://u.ae/en/information-and-services/environment-and-energy/water-and-energy/water-"],
["The lack of integration means that despite decades of residence, expatriates have no path to citizenship and no real belonging.","Long residence does not by itself establish citizenship. Specified categories can acquire nationality under conditions, including reforms announced in January 2021 for investors, professionals, and people with particular talents. These routes leave a wider question about the participation and long-term security of expatriate residents.","Dubai Media Office, 30 January 2021","https://mediaoffice.ae/en/news/2021/jan/30-01/mohammed-bin-rashid"],
["No white settler population claimed the best land.","French colonists retained property after the British takeover in 1810, and the plantation economy carried substantial inequalities of ownership.","Mauritius Observatory of Environment, historical population account","https://ode.govmu.org/population-n-vital-stats"],
["Instead of trying to create innovation from scratch, Singapore focused on becoming the best place to deploy innovation. The Smart Nation initiative didn't aim to make Singapore a technology creator but a technology adopter.","The Smart Nation initiative linked technology adoption with opportunities for innovation. Its initial platform plan included sharing protected sensor data, improving public services, and enabling businesses to create new services.","IDA, Smart Nation Platform factsheet, June 2014, p. 3","https://www.imda.gov.sg/-/media/Imda/Files/Inner/About-Us/Newsroom/Media-Releases/2014/0617_smartnation/AnnexA_sn.pdf"],
["Sheikh Mohammed bin Rashid Al Maktoum, then Crown Prince, personally led delegations", "Sheikh Mohammed bin Rashid Al Maktoum personally led delegations"],
["Turnover exceeded 100% annually, meaning the entire workforce quit and was replaced every year.","Turnover exceeded 100% annually. That rate can include repeated departures from the same positions; it does not mean that every worker left."],
["Defever, F., & Suedekum, J. (2014).", "Mayer, T., Melitz, M. J., & Ottaviano, G. I. P. (2014)."],
["Aggarwal, A. (2012). \"Social and Economic Impact of SEZs in India.\"", "Aggarwal, A. (2012). Social and Economic Impact of SEZs in India."],
["Journal of International Commerce, Economics and Policy", "Oxford University Press"],
[". (2017). \"Industrial Clusters: The Case for Special Economic Zones in Africa.\"", ". (2017). \"Industrial Clusters: The Case for Special Economic Zones in Africa.\""]
]
for row in rows:
 old,new=row[:2];a,b=html.escape(old,quote=False),html.escape(new,quote=False);n=s.count(a);assert n==1,(old,n)
 if len(row)>2:b+=' <a href="'+html.escape(row[3],quote=True)+'">'+html.escape(row[2])+'</a>.'
 s=s.replace(a,b)
# Specific publication metadata, scoped to its actual paragraph.
import re
for prefix,old,new in [('Aggarwal, A.','3(1).',''),('Newman, C.', 'Journal of African Economies','WIDER Working Paper 15/2017, UNU-WIDER'),('Newman, C.',', 26(5), 570-595.','.')]:
 m=next(m for m in re.finditer(r'<p\b[^>]*>.*?</p>',s,re.S) if prefix in html.unescape(m.group()))
 assert old in m.group();s=s[:m.start()]+m.group().replace(old,new)+s[m.end():]
s=re.sub(r'<sup><a href="#cmnt\d+" id="cmnt_ref\d+">\[[a-z]+\]</a></sup>','',s)
p.write_text(s);Path('scratch/narrow-primary-repairs.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Applied narrow primary corrections')
