'use strict';

const assert = require('node:assert/strict');

module.exports = function checkThirdFlag({book, units, containsMath, prose}) {
  const collision = book.getElementById('ch04-irregular-collision');
  const open = book.getElementById('problem-composition-domains');
  assert.equal(collision.closest('article[data-chapter]').id, 'ch04');
  assert.equal(open.closest('article[data-chapter]').id, 'ch18');
  const section = book.createElement('section');
  section.id = collision.id;
  for (let el = collision.nextElementSibling; el && !el.matches('h1,h2,h3,h4'); el = el.nextElementSibling)
    section.append(el.cloneNode(true));
  containsMath(section,[String.raw`F_c[q\wedgep]=0`,String.raw`[q\wedge\eta]`,String.raw`(2\pii)^2`,
    '(1,0)','(-1,-1)','(0,1)','(1,3,4,2)','(0,0,2,2)']);
  assert.match(prose(section), /restriction .*on cohomology/);
  assert.match(prose(section), /independently defined sectorial specialization/);
  containsMath(open,['(1,3,4,2)','(0,0,2,2)']);
  assert.match(prose(open), /Any two of these three flag images span the boundary image/);
  assert.match(prose(open), /sectorial specialization remain open/);
  assert.ok(open.querySelector('a[href="#ch04-irregular-collision"]'));
  for (const id of [collision.id,open.id]) assert.ok(units.some(unit => unit.id === id && unit.page === 'index.html'), id);
  return {chapter_sections:[collision.id,open.id],cohomological_zero:true,ordered_two_torus_pairing:true,
    third_flag_ranks:[[1,3,4,2],[0,0,2,2]],sectorial_comparison:'open'};
};
