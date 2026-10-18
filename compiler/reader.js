const { JSDOM } = require('jsdom');

const HEADING = 'h1, h2, h3, h4, h5, h6';
const CONTENTS = '.toc, .reader-contents';

function plainLabel(element) {
  const copy = element.cloneNode(true);
  copy.querySelectorAll('sup').forEach(node => node.remove());
  return copy.textContent.replace(/\s+/g, ' ').trim();
}

function key(text) {
  return text.normalize('NFKC').replace(/[\uE000-\uF8FF\u200B]/g, '').replace(/\s+/g, ' ').trim().toLowerCase();
}

function withoutPage(text) {
  return text.replace(/\s+\d+\s*$/, '').replace(/\.{2,}$/, '').trim();
}

/** Normalize an article body fragment without rewriting its manuscript text. */
function normalizeArticle(html, { title } = {}) {
  const dom = new JSDOM(`<body>${html}</body>`);
  const document = dom.window.document;
  const body = document.body;
  body.querySelectorAll('p').forEach(paragraph => {
    if (!paragraph.textContent.trim() && !paragraph.id &&
        !paragraph.querySelector('[id], a[name], img, svg, video, audio, iframe')) paragraph.remove();
  });
  const contents = [...body.querySelectorAll(CONTENTS)]
    .filter(node => !node.parentElement.closest(CONTENTS));

  if (title) {
    body.querySelectorAll('p').forEach(paragraph => {
      if (!paragraph.closest(CONTENTS) && !paragraph.id &&
          !paragraph.querySelector('[id], a[name]') && key(paragraph.textContent) === key(title)) {
        paragraph.remove();
      }
    });
  }

  let headings = [...body.querySelectorAll(HEADING)]
    .filter(heading => !heading.closest(CONTENTS) && plainLabel(heading));
  // Some exports split the printed contents around an author/title block.
  // Fold only standalone, page-numbered heading links before the first section.
  if (contents.length && headings.length) {
    body.querySelectorAll('p').forEach(paragraph => {
      const link = paragraph.querySelector('a[href^="#h."]');
      if (!paragraph.closest(CONTENTS) && link &&
          paragraph.textContent.trim() === link.textContent.trim() &&
          /\s+\d+\s*$/.test(link.textContent) &&
          (paragraph.compareDocumentPosition(headings[0]) & dom.window.Node.DOCUMENT_POSITION_FOLLOWING)) {
        contents.push(paragraph);
      }
    });
    contents.sort((left, right) => left.compareDocumentPosition(right) & dom.window.Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1);
  }
  const targets = new Map();
  body.querySelectorAll('[id], a[name]').forEach(node => {
    if (node.id) targets.set(node.id, node);
    if (node.matches('a[name]')) targets.set(node.getAttribute('name'), node);
  });
  const claimed = new Set();
  const matchedLinks = new Map();

  // Google Docs can reuse an incorrect href in its contents. Match each label,
  // rather than assuming that every occurrence of a fragment names one heading.
  body.querySelectorAll('a[href^="#"]').forEach(link => {
    let fragment;
    try { fragment = decodeURIComponent(link.getAttribute('href').slice(1)); }
    catch { return; }
    if (!fragment) return;
    const label = plainLabel(link);
    const possibleLabels = [key(label), key(withoutPage(label))];
    const candidates = headings.filter(heading => possibleLabels.includes(key(plainLabel(heading))));
    const existing = targets.get(fragment);
    const existingHeading = existing && (existing.matches(HEADING) ? existing : existing.closest(HEADING));
    if (existing && !link.closest(CONTENTS) && !fragment.startsWith('h.')) return;
    if (existingHeading && candidates.includes(existingHeading)) {
      matchedLinks.set(link, existingHeading);
      claimed.add(existingHeading);
      return;
    }
    const heading = candidates.find(candidate => !claimed.has(candidate)) || candidates[0];
    if (!heading) return;
    claimed.add(heading);
    matchedLinks.set(link, heading);
    if (!existing && !heading.id) {
      heading.id = fragment;
      targets.set(fragment, heading);
    } else if (!existing) {
      const alias = document.createElement('span');
      alias.id = fragment;
      alias.className = 'reader-anchor';
      heading.prepend(alias);
      targets.set(fragment, alias);
    } else if (existingHeading !== heading) {
      // A conflicting imported href receives the heading's unique target below.
      link.dataset.readerTarget = 'canonical';
    }
  });

  const minimumLevel = headings.length ? Math.min(...headings.map(node => Number(node.tagName.slice(1)))) : 2;
  const replacements = new Map();
  headings = headings.map(heading => {
    const level = Math.min(6, Number(heading.tagName.slice(1)) + 2 - minimumLevel);
    let current = heading;
    if (heading.tagName !== `H${level}`) {
      current = document.createElement(`h${level}`);
      [...heading.attributes].forEach(attribute => current.setAttribute(attribute.name, attribute.value));
      current.append(...heading.childNodes);
      heading.replaceWith(current);
    }
    if (!current.id) {
      const stem = key(plainLabel(current)).replace(/[^\p{L}\p{N}]+/gu, '-').replace(/^-|-$/g, '') || 'section';
      let id = stem;
      for (let suffix = 2; targets.has(id); suffix++) id = `${stem}-${suffix}`;
      current.id = id;
      targets.set(id, current);
    }
    replacements.set(heading, current);
    return current;
  });
  body.querySelectorAll('h1').forEach(heading => {
    if (heading.closest(CONTENTS)) return;
    const replacement = document.createElement('h2');
    [...heading.attributes].forEach(attribute => replacement.setAttribute(attribute.name, attribute.value));
    replacement.append(...heading.childNodes);
    heading.replaceWith(replacement);
  });
  matchedLinks.forEach((heading, link) => {
    if (link.dataset.readerTarget) {
      link.setAttribute('href', `#${replacements.get(heading).id}`);
      delete link.dataset.readerTarget;
    }
  });

  const entries = [];
  if (contents.length) {
    contents.forEach(container => {
      container.querySelectorAll('a[href]').forEach(link => {
        const heading = replacements.get(matchedLinks.get(link));
        entries.push({
          href: link.getAttribute('href'),
          label: heading ? plainLabel(heading) : withoutPage(plainLabel(link)),
          level: heading ? Number(heading.tagName.slice(1)) : 2
        });
      });
    });
  } else {
    headings.forEach(heading => entries.push({ href: `#${heading.id}`, label: plainLabel(heading), level: Number(heading.tagName.slice(1)) }));
  }

  if (entries.length) {
    const details = document.createElement('details');
    details.className = 'reader-contents';
    const summary = document.createElement('summary');
    summary.textContent = 'On this page';
    const nav = document.createElement('nav');
    nav.setAttribute('aria-label', 'On this page');
    const list = document.createElement('ol');
    const stack = [{ level: 2, list }];
    entries.forEach(entry => {
      while (stack.length > 1 && entry.level < stack[stack.length - 1].level) stack.pop();
      const previous = stack[stack.length - 1];
      if (entry.level > previous.level && previous.list.lastElementChild) {
        const nested = document.createElement('ol');
        previous.list.lastElementChild.append(nested);
        stack.push({ level: entry.level, list: nested });
      }
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.setAttribute('href', entry.href);
      link.textContent = entry.label;
      item.append(link);
      stack[stack.length - 1].list.append(item);
    });
    nav.append(list);
    details.append(summary, nav);
    // Keep any public fragment targets carried by the old contents itself.
    contents.forEach(container => {
      const nodes = [container, ...container.querySelectorAll('[id], a[name]')];
      nodes.forEach(node => {
        const ids = new Set([node.id, node.matches('a[name]') && node.getAttribute('name')]);
        ids.forEach(id => {
          if (!id) return;
          const alias = document.createElement('span');
          alias.id = id;
          alias.className = 'reader-anchor';
          details.append(alias);
        });
      });
    });
    if (contents.length) {
      contents[0].replaceWith(details);
      contents.slice(1).forEach(container => container.remove());
    } else {
      body.prepend(details);
    }
  }
  body.querySelectorAll('table').forEach((table, index) => {
    if (table.parentElement.classList.contains('table-scroll')) return;
    const region = document.createElement('div');
    region.className = 'table-scroll';
    region.tabIndex = 0;
    region.setAttribute('role', 'region');
    region.setAttribute('aria-label', `Table ${index + 1}`);
    table.before(region);
    region.append(table);
  });
  const result = body.innerHTML;
  dom.window.close();
  return result;
}

module.exports = { normalizeArticle };
