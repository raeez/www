'use strict';
const {JSDOM}=require('jsdom');
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const crypto=require('node:crypto');
const site=path.resolve(process.argv[2]);
const files={};
function documentFor(name){
  const data=fs.readFileSync(path.join(site,name));
  files[name]=crypto.createHash('sha256').update(data).digest('hex');
  return new JSDOM(data.toString()).window.document;
}
function literals(element){
  assert.ok(element);
  return Array.from(element.querySelectorAll('annotation[encoding="application/x-tex"]'),a=>a.textContent).join('\n');
}
function visible(element){
  const c=element.cloneNode(true);
  c.querySelectorAll('annotation,script,style,template').forEach(n=>n.remove());
  return c.textContent.replace(/\s+/g,' ');
}
const book=documentFor('index.html');
const c12=book.getElementById('ch12');
const c18=book.getElementById('ch18');
const ref=documentFor('reference.html');
const supplement=ref.getElementById('frontier-comparisons');
const atlas=documentFor('atlas.html');
const w4=atlas.querySelector('[data-claim-id="sc1620-alg-w-localization-remaining"]');
assert.ok(book.getElementById('ch12-exceptional-w4-fibres-and-the-algebra-of-extensions'));
assert.ok(literals(c12).includes('I^2=0') || /I\s*\^\s*\{?2\}?\s*=\s*0/.test(literals(c12)));
assert.ok(!visible(c12).includes('Its scalar has yet to be determined'));
for(const section of [c18,supplement]){
  assert.ok(literals(section).includes('24053.108799478066244'));
  assert.ok(/finite grid/i.test(visible(section)) && /positive diagonal/.test(visible(section)) && /uniformly bounded endpoint norm products/.test(visible(section)));
}
assert.ok(literals(supplement).includes('1,5,4') && literals(supplement).includes('0,4,4'));
assert.ok(w4 && /formal/i.test(visible(w4)), 'atlas lost the unresolved higher question');
console.log(JSON.stringify({status:'PASS',files,checks:[
  'exceptional binary ring and open higher formality point to the public chapter and atlas claim',
  'both reader routes give the exact 43-width lower bound and its finite interpolation limitation',
  'signed localization maps have their joint rank triples in the published comparison']},null,2));
