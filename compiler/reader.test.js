const test = require('node:test');
const assert = require('node:assert/strict');
const { JSDOM } = require('jsdom');
const { normalizeArticle } = require('./reader');

const parse = html => new JSDOM(html).window.document;

test('repairs imported contents while retaining manuscript text, comment references and existing IDs', () => {
  const input = '<div class="toc" id="contents"><p><a href="#h.chapter">Chapter 2: Singapore        14</a></p></div>' +
    '<h1 id="chapter">Chapter 2: Singapore<sup><a href="#cmnt8" id="cmnt_ref8">[h]</a></sup></h1>' +
    '<p id="prose">A claim with <em>precise wording</em> and <a href="https://example.com/source">a source</a>.</p>' +
    '<p id="cmnt8"><a href="#cmnt_ref8">Return</a> Commentary.</p>';
  const original = parse(input);
  const output = parse(normalizeArticle(input));
  assert.equal(output.querySelector('h1'), null);
  assert.equal(output.querySelector('h2').id, 'chapter');
  assert.ok(output.getElementById('h.chapter'));
  for (const id of ['contents', 'chapter', 'cmnt_ref8', 'cmnt8']) assert.ok(output.getElementById(id), id);
  assert.equal(output.getElementById('prose').outerHTML, original.getElementById('prose').outerHTML);
  assert.equal(output.getElementById('cmnt8').outerHTML, original.getElementById('cmnt8').outerHTML);
  assert.equal(output.querySelector('details.reader-contents > summary').textContent, 'On this page');
  assert.equal(output.querySelector('nav[aria-label="On this page"] a').textContent, 'Chapter 2: Singapore');
  assert.equal(output.querySelector('script'), null);
});

test('resolves reused imported hrefs by label and folds split printed contents', () => {
  const output = parse(normalizeArticle('<div class="toc"><p><a href="#h.same">Definition        4</a></p></div>' +
    '<p>Author name</p><p><a href="#h.same">Functional Characteristics        5</a></p>' +
    '<h2>Definition</h2><p>The definition remains.</p><h2>Functional Characteristics</h2><p>The characteristics remain.</p>'));
  const links = [...output.querySelectorAll('.reader-contents a')];
  assert.equal(links.length, 2);
  assert.notEqual(links[0].getAttribute('href'), links[1].getAttribute('href'));
  for (const link of links) assert.equal(output.getElementById(link.getAttribute('href').slice(1)).textContent, link.textContent);
  assert.deepEqual([...output.querySelectorAll('body > p')].map(node => node.textContent), ['Author name', 'The definition remains.', 'The characteristics remain.']);
});

test('matching ignores import artifacts without changing original heading text or footnotes', () => {
  const output = parse(normalizeArticle('<div class="toc"><a href="#h.appendix">C.2 Data        87</a></div>' +
    '<h3>\uec02C.2 Data<sup><a id="ftnt_ref1" href="#ftnt1">1</a></sup></h3>' +
    '<p id="ftnt1">Reference <a href="#ftnt_ref1">1</a></p>'));
  assert.equal(output.querySelector('h2').textContent, '\uec02C.2 Data1');
  assert.equal(output.querySelector('h2').id, 'h.appendix');
  assert.ok(output.getElementById('ftnt_ref1'));
  assert.ok(output.getElementById('ftnt1'));
});

test('generates usable contents and collision-free IDs without removing prose', () => {
  const input = '<p>Repeated title</p><h1>First section</h1><p>Repeated title</p>' +
    '<h2>Detail</h2><h2>Detail</h2><h1 id="empty"></h1>';
  const output = parse(normalizeArticle(input));
  assert.equal(output.querySelectorAll('h1').length, 0);
  assert.equal(output.querySelectorAll('.reader-contents a').length, 3);
  assert.equal(output.querySelectorAll('p').length, 2);
  assert.ok(output.getElementById('detail'));
  assert.ok(output.getElementById('detail-2'));
  assert.ok(output.getElementById('empty'));
});

test('removes duplicate title paragraphs only when the caller supplies that exact title', () => {
  const input = '<p>Example title</p><p>Example title and qualification</p><p id="keep">Example title</p><h2>Section</h2>';
  const output = parse(normalizeArticle(input, { title: 'Example title' }));
  assert.deepEqual([...output.querySelectorAll('p')].map(node => node.textContent), ['Example title and qualification', 'Example title']);
  assert.ok(output.getElementById('keep'));
});

test('normalization is stable across repeated builds and preserves already valid links', () => {
  const first = normalizeArticle('<div class="toc"><a href="#stable">Section    3</a></div><h2 id="stable">Section</h2><p>Text.</p>');
  assert.equal(normalizeArticle(first), first);
  const output = parse(first);
  assert.equal(output.querySelector('.reader-contents a').getAttribute('href'), '#stable');
});

test('wide tables remain keyboard accessible without changing their cells', () => {
  const table = '<table><tbody><tr><td>Observed value</td><td>Source record</td></tr></tbody></table>';
  const first = normalizeArticle('<h2>Evidence</h2>' + table);
  const output = parse(first);
  const region = output.querySelector('.table-scroll');
  assert.equal(region.getAttribute('role'), 'region');
  assert.equal(region.tabIndex, 0);
  assert.equal(region.firstElementChild.outerHTML, table);
  assert.equal(normalizeArticle(first), first);
});


test('printed page removal keeps a heading’s final period', () => {
  const output = parse(normalizeArticle('<div class="toc"><a href="#h.period">An explanatory heading.        6</a></div><h2>An explanatory heading.</h2>'));
  assert.equal(output.querySelector('.reader-contents a').getAttribute('href'), '#h.period');
  assert.equal(output.getElementById('h.period').textContent, 'An explanatory heading.');
});


test('compiler preserves source targets and builds a compact feed without running a fetch', () => {
  const { cleanGoogleDocsHtml, applyTemplate, generateComprehensiveAtomFeed } = require('./build');
  const source = '<h1 id="h.source">Source heading</h1><p><a href="#h.source">Return</a><a id="id.note">Note</a></p>';
  const cleaned = cleanGoogleDocsHtml(source);
  assert.ok(parse(cleaned).getElementById('h.source'));
  assert.ok(parse(cleaned).getElementById('id.note'));
  const rendered = parse(applyTemplate({ title: 'An article', slug: 'an-article', description: 'Summary.', meta: 'September 2026' }, cleaned));
  assert.equal(rendered.querySelectorAll('h1').length, 1);
  assert.ok(rendered.getElementById('h.source'));
  const feed = generateComprehensiveAtomFeed([{ slug: 'an-article', title: 'An article', description: 'Summary.',
    date: '2026-09-05T00:00:00Z', modified: '2026-09-05T00:00:00Z', categories: ['research'], images: [],
    content: '<p>Manuscript text</p><img src="data:image/png;base64,' + 'A'.repeat(100000) + '">', hash: 'abc' }]);
  assert.ok(feed.includes('https://raeez.com/an-article.html'));
  assert.ok(feed.includes('Summary.'));
  assert.ok(!feed.includes('data:image'));
  assert.ok(!feed.includes('Manuscript text'));
  assert.ok(feed.length < 10000);
  const xml = new JSDOM(feed, { contentType: 'text/xml' });
  assert.equal(xml.window.document.querySelector('parsererror'), null);
  xml.window.close();
});


test('embedded image extraction preserves bytes, image metadata and manuscript prose', () => {
  const { extractEmbeddedImages } = require('./build');
  const bytes = Buffer.from('An image fixture including binary bytes \x00\xff', 'latin1');
  const source = `data:image/png;base64,${bytes.toString('base64')}`;
  const input = `<p>Unchanged manuscript <em>text</em>.</p><img src="${source}" alt="An illustration" width="640"><img src="${source}" alt="Repeated image">`;
  const result = extractEmbeddedImages(input, 'fixture');
  assert.equal(result.assets.length, 1);
  assert.deepEqual(result.assets[0].bytes, bytes);
  assert.match(result.assets[0].relativePath, /^assets\/writing\/fixture\/[a-f0-9]{12}\.png$/);
  const output = parse(result.html);
  assert.equal(output.querySelector('p').outerHTML, parse(input).querySelector('p').outerHTML);
  const image = output.querySelector('img');
  assert.equal(image.getAttribute('src'), result.assets[0].relativePath);
  assert.equal(image.getAttribute('alt'), 'An illustration');
  assert.equal(image.getAttribute('width'), '640');
  assert.equal(image.getAttribute('loading'), 'lazy');
  assert.equal(image.getAttribute('decoding'), 'async');
  assert.ok(!result.html.includes('data:image'));
  assert.throws(() => extractEmbeddedImages(input, '../outside'), /Invalid article slug/);
});

test('manuscript cover supplies authorship and fails when source identity changes', () => {
  const { composeCover } = require('./covers');
  const source = '<header class="article-header"><h1>Prefabricated Construction</h1></header>' +
    '<div class="article-body"><p id="source-title">Prefabricated Construction Methodologies</p>' +
    '<p>王臻卓 (Lilith Wang) &amp; Raeez Lorgat, Momentum Capital</p><h2>Argument</h2><p id="prose">Original argument.</p></div>';
  const first = composeCover(source, 'prefabricated-construction');
  const output = parse(first);
  assert.equal(output.querySelector('h1').textContent, 'Prefabricated Construction Methodologies');
  assert.match(output.querySelector('.article-meta').textContent, /王臻卓 \(Lilith Wang\) & Raeez Lorgat/);
  assert.ok(output.getElementById('source-title'));
  assert.equal(output.getElementById('prose').textContent, 'Original argument.');
  assert.equal(output.querySelectorAll('.article-body p').length, 1);
  assert.equal(composeCover(first, 'prefabricated-construction'), first);
  assert.throws(() => composeCover(source.replace('Lilith Wang', 'A different author'), 'prefabricated-construction'), /Manuscript cover changed/);
});
