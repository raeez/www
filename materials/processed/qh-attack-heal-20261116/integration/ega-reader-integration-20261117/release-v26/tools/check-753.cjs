'use strict';
const assert=require('node:assert/strict');
module.exports = function check753({book,containsMath,prose}) {
  const twelve=book.getElementById('ch12'), thirteen=book.getElementById('ch13');
  containsMath(twelve,[String.raw`\frac{K}{3y^2z^2(y-z)}`,String.raw`\frac{K}{3(y-z)}`,
    String.raw`\frac{K}{3yz(y-z)}`,String.raw`K=-2`,'1/3',String.raw`N\ge2`,'V_4','V_2','V_0']);
  assert.match(prose(twelve), /In rank two both auxiliary partial traces of each divided RTT defect also vanish/);
  assert.match(prose(twelve),/all three projections of each defect vanish/);
  assert.match(prose(twelve),/with proper image/);
  containsMath(twelve,[String.raw`D_0/\hbar^3D_0`,String.raw`\hookrightarrow`,String.raw`\barM_3`]);
  assert.match(prose(twelve),/rank-two map at higher precision and the higher-rank map/);
  containsMath(thirteen,['xy-x^2','(m,-m)',String.raw`\eta(m,-m)`,String.raw`p_{\mathrm{Ran},!}`]);
  assert.match(prose(thirteen),/supplied global word system whose coefficients are finite at each arity/);
  assert.match(prose(thirteen),/ordinary closed-incidence integral retains a logarithmic class and its odd partner outside the compact image/);
  const disk=book.getElementById('ch11');
  containsMath(disk,[String.raw`\rho=\sum_j\lambda_j|F_j\rangle\langleF_j|`,String.raw`\lim_{N\to\infty}\operatorname{Tr}(\rhoL_N)`]);
  assert.match(prose(disk),/Every positive trace-class operator of trace one/);
  assert.ok(book.querySelector('#front .mg-front-intro a[href="#ch11-recovering-a-state-from-the-disk"]'));
  return {chapters:['ch12','ch13'],mixed_at_critical_rank_two:'1/3',rank_two_zero_level_original_map_mod_hbar3:'proper injection',global_word_system:true,
    compact_puncture_classes:['(m,-m)','eta(m,-m)']};
};
