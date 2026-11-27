// Runner: node tools/run.mjs <scenario.mjs> [args...]
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { launch } from './cdp.mjs';

const mod = await import(pathToFileURL(resolve(process.argv[2])).href);
const b = await launch('run');
let code = 0;
try {
  const out = await mod.default(b, process.argv.slice(3));
  if (out !== undefined) console.log(typeof out === 'string' ? out : JSON.stringify(out, null, 1));
} catch (e) {
  console.error((e && e.stack) || e);
  code = 1;
} finally {
  await b.close();
}
process.exit(code);
