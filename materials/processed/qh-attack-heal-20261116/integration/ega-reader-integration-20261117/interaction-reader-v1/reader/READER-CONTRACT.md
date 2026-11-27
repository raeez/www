# Reader contract: DOM and events (reader-dom, revision 3)

- **From:** the interaction lane, which owns `compiler/quantum-holography-status/reader.js` and
  `tests/reader.test.cjs`.
- **For:** the foundation (the monograph renderer and CSS), the atlas lead (figures.render, atlas.js) and root.
- **Inputs read, verbatim and whole:**

  | File | sha256 |
  |---|---|
  | READER-ARCHITECTURE.md | `d6e881b1…` |
  | SCIENTIFIC-VISUAL-CONTRACT.md | `cc340b38…` |
  | FIGURE-RECORD-CONTRACT.md | `d711aac0…` |
  | AUTHOR-CONTRACT.md | `cda7fc3f…` |
  | reader-data/manifest.json | `16a3f0df…` |
  | chapters/01-physical-questions.md | `74bacba8…` |
  | foundation monograph/CHAPTER-MARKUP.md | `d78c75d7…` |
  | PROGRAMME-DIAGRAM-CONTRACT.md | `c678539d…` |
  | reader-data/diagram-records.json | `c96f67df…` |
  | reader-data/manifest.json (current, with `diagrams[]` and `routes`) | `a8dd97f6…` |
  | root messages 12 to 19 | (lane `ROOT-MESSAGE-*.txt`) |
  | the foundation's built book.html (checked) | `1ffe6054…` |
  | the foundation's monograph.css | `7d58f2b9…` |

- **Scope:**
  - This file fixes only the DOM that the renderer emits and the reader reads, the elements the reader creates, and
    the events.
  - The Markdown forms are the foundation's (CHAPTER-MARKUP.md), and the figure records are the author's
    (FIGURE-RECORD-CONTRACT.md).
  - The reader never changes the text it is served, and adds no words beyond its interface words.

## 1. What the renderer serves (everything optional is marked)

Without the script, the page is the whole book in reading order, and every link works.

`<main id="main" data-reader [data-chapter-count="18"] [data-label-<key>="…"]>` holds, in this order:

1. **The title page.** `header#front[data-reader-front]` holds the manifest's title (in an `h1`), its subtitle and its
   audience.
   - *Optional:* the routes, drawn from the manifest's `routes` with the author's titles. Each route is
     `<a href="#{first chapter}" data-route="{route id}" data-route-chapters="{chapter ids, space-separated}">{route title}</a>`.
2. **The contents.** `nav#contents[data-reader-toc][aria-labelledby="contents-h"]`, with its heading `#contents-h`.
   - Each part is a `li[data-part="{part id}"]`, holding `span#{part id}-title`, followed by one `li` per chapter. The
     chapter's link is `a[href="#{chapter id}"][data-chapter-link]`.
   - *Optional:* a nested list of section links, `a[href="#{section id}"]`.
   - *Optional:* links to the reference parts.
3. **The chapters.** One per served chapter, in manifest order:
   `article#{chapter id}[data-chapter][data-part="{part id}"][data-number="{n}"][aria-labelledby="{chapter id}-h"]`.
   Inside it:
   - the chapter title, `h2#{chapter id}-h`;
   - *optional:* the line giving the chapter's place in the book, `[data-chapter-kicker]`;
   - the prerequisites, `nav[data-prerequisites]`, with one `a[href="#{chapter id}"]` per manifest prerequisite;
   - *optional:* the manifest's summary, `[data-chapter-summary]`;
   - the opening passage;
   - the sections: each `##` is `section#{heading id}[data-section][aria-labelledby="{heading id}-h"]`, with its
     heading `h3#{heading id}-h`. A `###` subsection is nested the same way, with an `h4`.
   - the end of the chapter: `nav[data-chapter-end]`, with `a[rel=prev]` and `a[rel=next]`.

   A chapter the author has not yet supplied is simply not served. `data-chapter-count` keeps the bar's count
   honest ("Chapter 5 of 18").

   **Only an `article[data-chapter]` is a chapter, and only a `section[data-section]` is a section.** A component may
   carry `data-chapter` or `data-section` values; the figure renderer does, on its figures. On the built book, the
   loose match `[data-chapter]` made the figures into chapters, so that Next went from Chapter 1 to a figure. The
   strict match is tested on the fixture and on the built book.
4. **The reference parts.** `section#{id}[data-reference][aria-labelledby]`:
   - the glossary, `#glossary`, with `dl > dt[id] + dd`;
   - the atlas, `#atlas`, which also carries `data-atlas-mount`;
   - **the old reference DOM, kept whole with its old ids** (root message [15]: keeping the old reference DOM is
     preferred to redirects).

**Inside chapters (ids are the author's, verbatim; the reader never adds a prefix):**

- **Environments** (CHAPTER-MARKUP §1–2) are `div[data-env="{class}"][id]`. The class is one of: definition, theorem,
  proposition, lemma, corollary, conditional, conjecture, heuristic, example, counterexample, construction, remark,
  notation, convention, open-problem, question, proof.
  - The label line, as the renderer numbers it ("Theorem 6.3 (Bar–cobar equivalence)"), is the element marked
    `[data-block-title]`.
  - A definition's defined term may be marked `dfn`.
  - The hypotheses are part of the visible text.
  - (`[data-term]` and `[data-result]` are read as other names for a definition and for any other environment.)
- **A labelled display formula** carries its id on the element that holds the formula and its number:
  `div.math-display#eq-…`. **The id must not sit on an empty marker after the formula.**
- **A figure** is the element that figures.render returns (FIGURE-RECORD-CONTRACT.md):
  `figure#{manifest id}[data-figure][data-qh-figure][data-figure-type]`, with a `figcaption` holding the author's
  caption.
  - Its title may be marked `[data-block-title]`.
  - The figure owns its controls and its state, and the reader never moves focus into it unless the address names
    the figure.
  - **The diagrams** (PROGRAMME-DIAGRAM-CONTRACT.md: five recurring context views and eight construction and
    comparison diagrams) use the same hook and the same element.
    - A node's link to its local definition, `a[href="#{section id}"]`, opens a reminder with that section's heading
      and first paragraph. It is a definition link, never a claim.
    - Labels drawn as SVG text are searched with the figure's caption.
    - The reader adds no arc, mark or relation of its own.
- **Cross-references** are ordinary links, `a[href="#{id}"]` (CHAPTER-MARKUP §3).
  - A link in running text to a place of the book opens a reminder.
  - `data-ref="{kind}"` may name the kind explicitly.
  - `data-ref="none"` keeps an ordinary link.
  - Links in a `nav` (the contents, the prerequisites list, the chapter end) and in the chapter's place line
    (`[data-chapter-kicker]`, "Part I") navigate. The prerequisites list is the exception: its links open a reminder
    when they carry `data-ref`.

**Without section wrappers,** the reader falls back on `h2[id]` to `h4[id]` as section marks. It still works, but the
wrappers are the contract.

## 2. What the reader creates (exact classes; the foundation's CSS styles each, see reader-css-proposal.css)

| Element | Where | Markup |
|---|---|---|
| Reading bar | in a served `[data-reader-bar]` slot, else a `nav` inserted before `main` | `.reader-bar` holds `a#reader-home.reader-home` (book title), `button#reader-contents-toggle.reader-contents-toggle` (`aria-expanded`, `aria-controls="contents"`), `a#reader-prev.reader-prev[rel=prev]`, `a#reader-next.reader-next[rel=next]`, `span.reader-route` (`.reader-route-text`, `button.reader-route-leave`; hidden unless a route is followed), `button#reader-search-toggle.reader-search-toggle` (`aria-keyshortcuts="/"`), and the search panel |
| Place | inside the contents toggle | `.reader-position`, holding `.reader-position-part` ("Part II"), `.reader-position-chapter` ("Chapter 6 of 18"), `.reader-position-title` and `.reader-position-section` |
| Step links | in the bar | `.reader-step-arrow[aria-hidden]`, `.reader-step-label` ("Previous", "Next", "Begin", "Back to the text"), `.reader-step-title`; the full name is in `aria-label` |
| Notices (**C12**) | the first child of `main` | `div.reader-notices[role=status]` (always present, empty when silent) holds `div.reader-notice[data-notice="resume|unknown"]`, made of `p.reader-notice-text[tabindex=-1]` and `p.reader-notice-actions` (`a.reader-notice-action` or `button.reader-notice-action`, then `button.reader-notice-close`). It aligns to the reading column, not full-bleed |
| Reminder | the last child of `body` | `div#reader-peek.reader-peek[role=dialog][aria-label][data-placement="below|above"][data-kind]`, holding `.reader-peek-head` (`p#reader-peek-where.reader-peek-where`, `button.reader-peek-close`), `.reader-peek-body` (a copy of the target, with no ids or controls), and `p.reader-peek-foot > a.reader-peek-go` ("Go to …"). Custom properties `--peek-x` and `--peek-y` give the link's position, for wide screens only; a narrow screen shows it as a bottom sheet |
| Search panel | inside the bar | `div#reader-search.reader-search[role=search]`, holding `.reader-search-field` (`label.reader-search-label`, `input#reader-q.reader-search-input`, `button.reader-search-close`), `.reader-search-scopes[role=toolbar]` (`button.reader-scope[data-scope][aria-pressed]` with `.reader-scope-label`, `.reader-scope-count` and `[data-none]`), `p#reader-search-status.reader-search-status`, `p.reader-search-news[role=status]` and `#reader-results.reader-results` |
| Results | inside `#reader-results` | `.reader-group[data-group="best"|{place id}]`, holding `p.reader-group-head` (`.reader-group-where`, `.reader-group-title`, `.reader-group-count`), `ol.reader-hits > li.reader-hit > a.reader-hit-link` (`.reader-hit-where`, `.reader-hit-title`, `.reader-hit-text` with `mark`, `.reader-hit-formula`, `.math-long`), and `button.reader-group-more` |

**Light and dark:** when the page serves no `.theme` control, the reader adds `button#reader-theme.theme.reader-theme`
to the bar, with the page's own label ("Switch between light and dark", `data-label-theme`) and icon. It uses the page's
mechanism: `data-theme` on the root, with the choice kept as `localStorage['qh-theme']`, which the page's head script
restores before the page is drawn. One press switches once whichever other script binds `.theme`. The page's
`.theme` and `.icon` styles apply.

**Titles:** a chapter's title is its heading without a first element that holds only the chapter's number, since the
page may set the number apart. Every other heading is read with a space between its parts. The bar's
"Chapter 1 · Boundary observables and reconstruction", the accessible names, the reminders, the search results and
the resume notice therefore never fuse or repeat a number (native QA O3).

**States the reader sets:**

| State | Where |
|---|---|
| `data-reader-view="front|chapter|reference"` | `main` |
| `data-current` | the shown place, and the current chapter's `li` in the contents |
| `hidden="until-found"` | every other place, and the title page |
| `hidden` | the contents, when they are not opened |
| `data-drawer` | the contents, when opened from the bar |
| `aria-current="page"` | the current chapter's link |
| `aria-current="location"` | the link to the section at the top of the screen |
| `data-revealed` | the element an address led to |
| `data-search-open` | the bar |
| `--reader-bar-h` | the root (measured) |
| `::highlight(reader-find)` | the search words in the place a result led to |

## 3. Behaviour

Evidence:

- `tests/reader.test.cjs`, 57 tests on books built from the manifest's structure, all passing;
- `--page` mode on the foundation's built book, with this reader.js in place of the earlier copy:
  - on `1ffe6054…`, 19 of 19 checks, both alone and with status.js;
  - on `b83033f3…` (the six figures and diagrams), with status.js, 19 of 20. The failing check is a renderer
    attribute: `fig-state-line-cap` lacks `data-qh-figure`.
- `tools/reader-mutations.cjs`: 11 of 11 mutations caught;
- status.js reader mode on the five tracker builds: 92 of 92 each, with fidelity and content checks passing.

- **One place at a time.**
  - A bare visit shows the title page and the contents.
  - Every chapter and every reference part is hidden until found. **The atlas register is never the default scroll
    (C1, C14).**
  - The browser's find reaches hidden text. When it does, the reader shows that place as a history entry and
    leaves the scrolling to the browser (`beforematch`).
- **Addresses:**
  - `#chapter`, `#section`, `#eq-…`, `#fig-…`, `#def-…` or `#thm-…`, and any id inside a place, show the place and
    reach the element.
  - The old reference ids resolve directly.
  - An unknown address is offered to components first (`qh:unknown-anchor`). If none claims it, it is named in a
    notice with "Search for …".
  - The optional `script#reader-redirects` (`{old: new}`) is a fallback only.
- **History.**
  - Each change of place is an entry.
  - The entry being left keeps the place, the scroll position and the focused control.
  - Back and Forward restore all three.
  - A search that led to a result is kept in its entry, so Back reopens the search with focus on that result.
- **Sequential reading:**
  - Previous and Next go by chapter, skipping chapters not served; the end-of-chapter links do the same.
  - A followed route makes Previous and Next follow it, with "Leave this route" in the bar.
  - Focus goes to the new chapter title.
- **Reminders:**
  - A cross-reference shows a copy of its target beside the text (as a sheet on phones), without leaving the place:
    - a definition, environment or equation, whole;
    - a section, as its heading and first paragraph;
    - a chapter, as its title, summary (or opening) and prerequisites;
    - a figure, as its title and caption.
  - "Go to …" moves there as an entry, and Back returns focus to the cross-reference.
  - Escape returns focus to the link.
  - Tab past the end goes on in the text.
  - On a fine pointer, resting on a link opens the reminder without taking focus.
- **Search (C17):**
  - `/` or the bar opens it. The query goes into `?q=`.
  - Results are grouped by place: **the chapters in the book's order first, then the glossary and the reference
    parts**.
  - In "All", each place shows its first 3 results and offers "n more in …". The reference scope lists 100 at a time.
  - A whole title or defined word typed exactly leads with a "Best match" (an environment's name in brackets, a
    bold lead-in, a `dfn` or a bold defined word).
  - Search matching follows the tested search core of the status page: TeX, Greek and quotes.
  - A block found without an id takes the id of the element that holds it alone, such as a numbered formula's
    `#eq-…`. Otherwise it gets `{nearest id}-p{n}`, which holds on a fresh visit.
- **Keyboard:**
  - Tab order is the reading order.
  - `/` opens the search. It is not taken from inside a control, such as a figure's slider.
  - Escape closes, in turn, the reminder, the search and the contents.
  - Arrows move within the results and the scopes.
  - There is no other single-key shortcut.
- **Narrow screens (C18):** the bar has five controls whatever the length of the book. The place sits inside the
  contents toggle; the contents open as a full-height panel; the reminder is a bottom sheet.
- **Kept on this device:**
  - `localStorage['qh-reader-place']` holds `{id, title, at}`, offered on a later bare visit if the title still
    matches;
  - `sessionStorage['qh-reader-route']`.
  - Refused storage costs nothing.

## 4. Events (the names the tracker and the atlas already use)

- **From the reader:**
  - `qh:chapter {id, number, part}` when the chapter shown changes;
  - `qh:state {q, view, id}` after every change of address (the atlas syncs on it);
  - `qh:reveal {id}`, cancelable, dispatched on a target inside `[data-atlas-mount]` when the reader leads there.
    The atlas cancels it when it scrolls and focuses itself.
- **To the reader:**
  - `qh:navigate {id}`, bubbling and cancelable. The reader shows the place and cancels the event.
  - `qh:unknown-anchor {id}`. A component claims an address by cancelling it.
  - `qh:content-changed`, which rebuilds the search units.
- **Links inside `[data-atlas-mount]`** are left to the atlas, which follows its own address.

## 5. Open interface points (for root)

- **R1 Equation ids:** on the display block, never on an empty marker. Ask the foundation.
- **R2 Section wrappers:** `section[data-section]` with an `h3#{id}-h`. The reader degrades to heading ids without
  them.
- **R3 Environments:** `data-env` with the CHAPTER-MARKUP class, and `[data-block-title]` on the numbered label line.
- **R4 Chapter count:** `main[data-chapter-count]`, from the manifest, while chapters arrive.
- **R5 The old tracker sections are composed as reference parts** (the built book holds them: 548 term buttons, 160
  table cells, 8 column heads, 6 filters, 2 expand buttons). Their behaviour needs status.js, which the built book does
  not run. **Done:** status.js now has a reader mode, active where `[data-reader]` exists.
  - status.js keeps the term and scope cards, the example table's keys, the filters, the expand buttons, the
    disclosures and their history (restored on Back), and print.
  - It leaves to the reader the place, the address, Back and Forward, the search, the notices and the reading place.
    It builds no search, no notice area and no "/" key.
  - Without status.js, the reader still opens a term button's glossary entry in its reminder. The table cells and
    filters then do nothing.
  - **Required integration: include status.js in the monograph page, before reader.js.** Then status.js restores
    disclosures on Back before the reader restores the scroll.
- **R7 CSS:** `reader/monograph-css-required.css` holds six rules, each needed by present behaviour. They are to be
  appended to the foundation's monograph.css:
  - the live region visually hidden (otherwise the count shows twice);
  - the find highlight;
  - the "n more" control;
  - the group count's mark;
  - empty scopes;
  - plain hidden kept hidden.

  `reader-css-proposal.css` is reference only.
- **R6 C10 on the old tracker page:** the term hook already accepts inline `a.term` (status.js r4). The fix is the
  foundation serving terms as links (proposal P5). In the monograph, cross-references are inline links, so a
  multi-word reference wraps like text.
