from pathlib import Path
import re,html,json
p=Path('sez-in-a-box.html');s=p.read_text();log=[]
newrefs={
'Aggarwal, A.': 'Aggarwal, A. (2012). <a href="https://academic.oup.com/book/11183"><em>Social and Economic Impact of SEZs in India</em></a>. Oxford University Press.',
'Mayer, T.': 'Mayer, T., Melitz, M. J., &amp; Ottaviano, G. I. P. (2014). "Market Size, Competition, and the Product Mix of Exporters." <a href="https://www.aeaweb.org/issues/327"><em>American Economic Review</em>, 104(2), 495–536</a>.',
'Newman, C.': 'Newman, C., &amp; Page, J. (2017). <a href="https://doi.org/10.35188/UNU-WIDER/2017/239-7">"Industrial Clusters: The Case for Special Economic Zones in Africa."</a> WIDER Working Paper 15/2017, UNU-WIDER.'
}
for prefix,body in newrefs.items():
 matches=[m for m in re.finditer(r'<p\b[^>]*>.*?</p>',s,re.S) if prefix in html.unescape(m.group())];assert len(matches)==1;m=matches[0];new='<p class="c0"><span class="c1">'+body+'</span></p>';log.append({'old_html':m.group(),'new_html':new});s=s[:m.start()]+new+s[m.end():]
m=next(m for m in re.finditer(r'<p\b[^>]*>.*?</p>',s,re.S) if 'Mayer, T.' in m.group());mayer=m.group();s=s[:m.start()]+s[m.end():]
m=next(m for m in re.finditer(r'<p\b[^>]*>.*?</p>',s,re.S) if 'Mason, P.' in m.group());s=s[:m.end()]+mayer+s[m.end():]
p.write_text(s);Path('scratch/bibliography-primary-repairs.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
