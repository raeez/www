'use strict';

const assert = require('node:assert/strict');

module.exports = function check753({ book, containsMath, prose }) {
  const twelve = book.getElementById('ch12');
  const thirteen = book.getElementById('ch13');
  const rtt = prose(twelve);
  containsMath(twelve, [
    String.raw`\frac{K}{3y^2z^2(y-z)}`, String.raw`\frac{K}{3(y-z)}`,
    String.raw`\frac{K}{3yz(y-z)}`, String.raw`K=-2`, '1/3',
    String.raw`N\ge2`, 'V_4', 'V_2', 'V_0',
  ]);
  assert.match(rtt, /In rank two both auxiliary partial traces of each divided RTT defect also vanish/);
  assert.match(rtt, /all three projections of each defect vanish/);
  containsMath(twelve, [String.raw`D_0/\hbar^3D_0`, String.raw`\hookrightarrow`, String.raw`\barM_3`]);
  containsMath(twelve, [
    String.raw`D_0/\hbar^dD_0`, String.raw`\barM_d`, String.raw`\mathcalJ_2(f'';a)`,
    String.raw`\mathcalJ_1\bigl(\tfrac12f''-(P_-f)'';a\bigr)`,
    String.raw`D_K/\hbar^3D_K\hookrightarrow\barM_3`, '[p^{-2}u^0]', String.raw`\hbar^4`,
  ]);
  assert.match(rtt, /compatible injections with proper image for every/);
  assert.match(rtt, /adic inverse-limit maps are continuous injections with proper image/);
  assert.match(rtt, /With these images both half relations, the centered mixed relation and both divided determinants hold/);
  assert.match(rtt, /A full rank-two lift at fourth precision and a higher-rank lift at third precision remain open at nonzero level/);

  containsMath(thirteen, ['xy-x^2', '(m,-m)', String.raw`\eta(m,-m)`, String.raw`p_{\mathrm{Ran},!}`]);
  assert.match(prose(thirteen), /supplied global word system whose coefficients are finite at each arity/);
  assert.match(prose(thirteen), /ordinary closed-incidence integral retains a logarithmic class and its odd partner outside the compact image/);

  const disk = book.getElementById('ch11');
  containsMath(disk, [
    String.raw`\rho=\sum_j\lambda_j|F_j\rangle\langleF_j|`,
    String.raw`\lim_{N\to\infty}\operatorname{Tr}(\rhoL_N)`,
  ]);
  assert.match(prose(disk), /Every positive trace-class operator of trace one/);
  assert.ok(book.querySelector('#front .mg-front-intro a[href="#ch11-recovering-a-state-from-the-disk"]'));
  return {
    chapters: ['ch12', 'ch13'],
    mixed_at_critical_rank_two: '1/3',
    all_rank_zero_level_original_map: 'proper injections at finite precision and under inverse limits',
    rank_two_corrected_mod_hbar3: 'proper injection at all levels',
    global_word_system: true,
    compact_puncture_classes: ['(m,-m)', 'eta(m,-m)'],
  };
};
