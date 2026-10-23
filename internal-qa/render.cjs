const {chromium}=require('/Users/raeez/.npm/_npx/e41f203b7505f1fb/node_modules/playwright');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"});
 const report=[];
 for(const file of ['moxie.html','programmable-institutions.html']){
  for(const [label,width,height] of [['desktop',1200,900],['narrow',390,844]]){
   const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
   await page.route('**/www.googletagmanager.com/**',r=>r.abort());
   const started=Date.now();
   await page.goto('file://'+process.cwd()+'/'+file,{waitUntil:'networkidle'});
   await page.evaluate(()=>document.fonts.ready);
   await page.waitForTimeout(1200);
   let before=await page.evaluate(()=>document.body.scrollHeight);
   await page.waitForTimeout(400);
   let after=await page.evaluate(()=>document.body.scrollHeight);
   if(before!==after)throw Error('Unstable layout '+file);
   const state=await page.evaluate(()=>({chars:document.querySelector('.article-body').innerText.length,scrollWidth:document.documentElement.scrollWidth,viewport:innerWidth,fontStatus:document.fonts.status,heading:document.querySelector('.article-title').innerText}));
   if(state.chars<10000||state.scrollWidth>width||state.fontStatus!=='loaded')throw Error(JSON.stringify(state));
   const phrase=file==='moxie.html'?'Implementation and Legal Reliance':'These programmable institutions require integration across three layers';
   if(!await page.getByText(phrase,{exact:false}).count())throw Error('Missing edited phrase');
   const stem=file.replace('.html','')+'-'+label;
   await page.screenshot({path:'internal-qa/'+stem+'-full.png',fullPage:true});
   const cuts=await page.evaluate(()=>{
    const r=[0,...Array.from(document.querySelectorAll('.article-body > h1')).map(e=>Math.max(0,Math.floor(e.getBoundingClientRect().top+scrollY-24))),Math.ceil(document.documentElement.scrollHeight)];
    return [...new Set(r)].sort((a,b)=>a-b);
   });
   const screenshots=[];
   for(let i=0;i<cuts.length-1;i++){
    const filename='internal-qa/'+stem+'-'+String(i).padStart(2,'0')+'.png';
    await page.screenshot({path:filename,fullPage:true,clip:{x:0,y:cuts[i],width,height:cuts[i+1]-cuts[i]}}); screenshots.push(filename);
   }
   report.push({file,label,width,elapsedMs:Date.now()-started,...state,height:after,screenshots});
   await page.close();
  }
 }
 fs.writeFileSync('internal-qa/render-report.json',JSON.stringify(report,null,2));
 console.log(JSON.stringify(report.map(({screenshots,...r})=>({...r,sectionImages:screenshots.length})),null,2));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
