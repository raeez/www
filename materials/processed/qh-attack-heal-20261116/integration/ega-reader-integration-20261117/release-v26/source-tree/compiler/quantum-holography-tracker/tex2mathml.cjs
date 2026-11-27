// Render TeX to MathML at build time with Temml (vendor/temml.cjs, MIT licence).
// Reads a JSON list of {tex, display} on standard input and writes a JSON list of
// {html} or {error} in the same order. The page itself carries no renderer.
'use strict';
const temml = require('./vendor/temml.cjs');

let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => { input += chunk; });
process.stdin.on('end', () => {
  const items = JSON.parse(input);
  const out = items.map(({ tex, display }) => {
    try {
      return { html: temml.renderToString(tex, { displayMode: Boolean(display), annotate: true,
                                                 throwOnError: true, trust: false }) };
    } catch (error) {
      return { error: String(error && error.message ? error.message : error) };
    }
  });
  process.stdout.write(JSON.stringify(out));
});
