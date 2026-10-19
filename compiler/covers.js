const { JSDOM } = require('jsdom');

// These fields come from the cover of the manuscript being displayed. Historical
// catalogue dates and versions remain in git; they do not establish a newer text.
const covers = {
  'sez-in-a-box': {
    title: 'Special Economic Zones in a Box: from proof of scale to proof of network',
    subtitle: 'A blueprint for a federated, programmable network of economic zones, powered by Mass, Momentum, and the Laboratory for Incentivization, Coordination and Cooperation (LICC).',
    meta: 'Raeez Lorgat · Manuscript dated 15 October 2025 · Work in progress',
    note: 'Contents constitute an active-work-in-progress. Please report errors and inconsistencies to raeez@momentum.inc',
    sourceVersion: 'WIP 0.06',
    legacyCatalogue: 'v0.35 — October 2025',
    remove: [
      'Special Economic Zones in a Box: from proof of scale to proof of network',
      'A blueprint for a federated, programmable network of economic zones, powered by Mass, Momentum, and the Laboratory for Incentivization, Coordination and Cooperation (LICC).',
      'Author: Raeez Lorgat',
      'Version: WIP 0.06. Contents constitute an active-work-in-progress. Please report errors and inconsistencies to raeez@momentum.incDate: October 15 2025'
    ]
  },
  archai: {
    title: 'ARCHAI PROTOCOL WHITEPAPER',
    subtitle: 'Programmable ownership for land, housing, and community infrastructure',
    meta: 'Manuscript dated June 2025 · Research and design discussion',
    sourceVersion: '0.2',
    legacyCatalogue: 'July 2025',
    remove: ['ARCHAI PROTOCOL WHITEPAPER', 'Programmable ownership for land, housing, and community infrastructure', 'Version 0.2 – June 2025']
  },
  'smart-buildings': {
    title: 'Smart Buildings',
    subtitle: 'The Programmable Built Environment Operating System',
    meta: 'Momentum × Jan Bunge × Broad Group · Manuscript dated 28 October 2025',
    note: 'Confidential Strategic Specification',
    legacyCatalogue: 'Version 0.3 — September 2025',
    remove: ['The Programmable Built Environment Operating System', 'Momentum × Jan Bunge × Broad Group', 'Confidential Strategic Specification', 'October 28, 2025']
  },
  licc: {
    title: 'The Laboratory for Incentivization, Coordination and Cooperation (LICC)',
    subtitle: 'A Research Institute for Coordination Science',
    meta: 'Raeez Lorgat, Managing Partner Momentum · Manuscript dated July 2025',
    legacyCatalogue: 'December 2025 • Version 1.0',
    remove: ['The Laboratory for Incentivization,', 'Coordination and Cooperation (LICC)', 'A Research Institute for Coordination Science', 'Raeez Lorgat, Managing Partner Momentum, July 2025']
  },
  'licc-blueprint': {
    title: 'MIT-MBZUAI Laboratory for Incentivization, Coordination and Cooperation (LICC)',
    subtitle: 'Comprehensive Founding Blueprint',
    deck: 'Dual-Sponsorship Model, Strategic Framework, Tactical Execution Guide, and Fundraising Strategy',
    meta: 'Prepared for: Momentum Partners · December 2025 · Confidential',
    sourceVersion: '1.0',
    remove: ['MIT-MBZUAI', 'Laboratory for Incentivization,', 'Coordination and Cooperation', '(LICC)', '────────────────────────────', 'Comprehensive Founding Blueprint', 'Dual-Sponsorship Model, Strategic Framework,', 'Tactical Execution Guide, and Fundraising Strategy', 'Prepared for: Momentum Partners', 'December 2025', 'Version 1.0 | CONFIDENTIAL']
  },
  'prefabricated-construction': {
    title: 'Prefabricated Construction Methodologies',
    subtitle: 'Industrialized construction methods',
    meta: '王臻卓 (Lilith Wang) & Raeez Lorgat, Momentum Capital · August 2025',
    remove: ['Prefabricated Construction Methodologies', '王臻卓 (Lilith Wang) & Raeez Lorgat, Momentum Capital']
  }
};

const plain = text => text.replace(/\s+/g, ' ').trim();

/** Move a verified manuscript cover into its single web header. */
function composeCover(html, slug) {
  const cover = covers[slug];
  if (!cover) return html;
  const dom = new JSDOM(html);
  const document = dom.window.document;
  const header = document.querySelector('.article-header');
  const body = document.querySelector('.article-body');
  if (header?.dataset.cover === 'manuscript') { dom.window.close(); return html; }
  if (!header || !body) throw new Error(`Missing article shell: ${slug}`);
  const nodes = [...body.querySelectorAll('p,h1,h2,h3,h4,h5,h6')].filter(node => !node.closest('.reader-contents'));
  const moved = cover.remove.map(text => nodes.find(node => plain(node.textContent) === text));
  const missing = cover.remove.filter((text, index) => !moved[index] &&
    !(text === cover.title && plain(header.querySelector('h1')?.textContent || '') === text));
  if (missing.length) {
    throw new Error(`Manuscript cover changed in ${slug}; review these source fields before rebuilding: ${missing.join(' | ')}`);
  }
  const aliases = [];
  moved.filter(Boolean).forEach(node => {
    [node, ...node.querySelectorAll('[id],a[name]')].forEach(target => {
      for (const id of new Set([target.id, target.getAttribute('name')].filter(Boolean))) {
        const alias = document.createElement('span');
        alias.id = id;
        aliases.push(alias);
      }
    });
    node.remove();
  });
  header.replaceChildren();
  header.dataset.cover = 'manuscript';
  const title = document.createElement('h1');
  title.className = 'article-title';
  if (cover.title.length > 65) title.classList.add('long-title');
  title.textContent = cover.title;
  header.append(title);
  for (const [key, className] of [['subtitle', 'article-subtitle'], ['deck', 'article-deck'], ['meta', 'article-meta'], ['note', 'article-note']]) {
    if (!cover[key]) continue;
    const paragraph = document.createElement('p');
    paragraph.className = className;
    paragraph.textContent = cover[key];
    header.append(paragraph);
  }
  header.append(...aliases);
  const details = body.querySelector('.reader-contents');
  if (details) body.prepend(details);
  const result = dom.serialize();
  dom.window.close();
  return result;
}

module.exports = { covers, composeCover };
