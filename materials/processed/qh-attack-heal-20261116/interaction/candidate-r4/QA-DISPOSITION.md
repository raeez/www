# Native QA findings (foundation candidate b57caa1e): disposition by the interaction lane

Source: `/tmp/qh-primary-native-qa-20261116/QA-FINDINGS.md` (sha256 `bcc6e346…b5e9`), read whole. I viewed all eleven
images in `shots/` myself. That QA ran on the foundation lane's candidate `b57caa1e` at 13:31–13:55 UTC, which carried the
foundation's own copy of status.js, not this lane's. It is an observation of an older build: nothing below assumes a
defect is unchanged or already resolved without evidence.

Measured against this lane's last frozen bytes (candidate-r4):

- status.js `ddc7df31aae27343a5f5114f35f0d5a7f4ca4096682a74b77ef566be0ceb78bf`;
- tests `8a92a7a4…b279` (92 reader-task tests);
- CSS block `2b5df9e0…26bf`, print block `766babf2…f161`;
- the status.py proposals in `proposals/`.

(First written against status.js `b627d8d4…` with 84 tests; re-pinned after the later heals, which keep every disposition below. candidate-final, `3d063428…`, is the last revision with an independent review; the changes from it to candidate-r4 are lead-verified only: REVIEW-STATUS.md.)

**What evidence I have:**

- jsdom checks only. jsdom has no layout, so "healed" below means the behaviour is healed and its test passes; the look
  stays unseen until root's native QA of the exact composed candidate.
- I used no browser. Root's binding restriction on browser use by this lane still stands; the QA shots were only read
  as files.

| ID | Sev | Owner | Against this lane's current bytes | Action |
|---|---|---|---|---|
| F1 contents column flush to the right edge, 1280–1450 px | S2 | foundation (status.css overview grid) | Not this lane's code. status.js adds nothing to the contents column. | Foundation. Recheck at 1280, 1366 and 1440 on the composed candidate. |
| F2 hierarchy inverted in question cards | S2 | foundation (fold titles) | Not this lane's code. status.js only opens and closes the folds (details) and writes their state into the address and history. | Foundation (its newer build sets `.fold-title` to weight 400, per the QA's static reading). |
| F3 first formula clipped; the scroll cue is faint (light) or invisible (dark) | S2 | foundation CSS (the cue); this lane (which boxes scroll, focus) | status.js already marks every overflowing formula box (`tabindex=0`, `data-scroll-focus`, measured as boxes come near the screen). New: it now also names the edges where the box hides more, as `data-edge` = `start` / `end` / `start end`, updated on scroll. | **Healed on this lane's side:** `status.js` sets `data-edge`; the CSS block fades exactly those edges with a mask, which shows in both themes because it fades the formula itself, not a coloured shadow. The fade is lifted while the box (or, for the bar, anything in it) has keyboard focus, so a focus ring shows whole. Test: the same edge logic on the bar (below). Look unseen. The overflow count and box widths stay with the foundation. |
| F4 auto-hyphenated family names and column headers | S3 | foundation (status.css `hyphens: auto`) | Not this lane's code. | Foundation. |
| F5 hyphen ladders in prose | S3 | foundation | Not this lane's code. | Foundation. The QA's option: `hyphenate-limit-chars: 7 3 3` and/or `text-wrap: pretty`. |
| F6 multi-word glossary term cannot break across lines | S3 | cross-lane: foundation markup (`button.term`) with this lane's hook | A `<button>` lays out as inline-block, so no CSS can make it break across lines. The fix is markup: serve the term as a link, `a.term[href="#term-…"][data-term]`. **status.js already accepts that**: it opens the card on click or Enter without following the link, and returns focus on Escape. New: the in-page link handler leaves a term link alone, so it records no false focus-return place. Without the script, the link leads to the definition, which also removes 334 of the 502 controls that do nothing without the script (A2-B-21). | **Routed to the foundation:** P5 for terms (`proposals/STATUS-PY.md`), plus the link style. Test: "card: a term served as a link opens its card while the script runs, and leads to its definition without it" (passes on the current build). |
| F7 the measure changes within one section | S3 | foundation | Not this lane's code. One related item is this lane's: the "Open all / Close all" placement (F7) comes from the served markup, not from status.js. | Foundation. |
| F8 status repeated on every related-statement line | S3 | foundation (`fold-status`) | Not this lane's code. Note: status.js's Show filter counts and the search's status labels read the served status chips, so removing the visible repetition must keep each statement's `data-status` and chip, or give a visually hidden equivalent. | Foundation, with this constraint. |
| F9 essay byline justified and indented | S3 | foundation (cascade) | Not this lane's code. | Foundation: `.essay .essay-byline { text-align: center; text-indent: 0 }` (the QA's fix). |
| F10a no bar link looks current over the overview | S3 | foundation markup and CSS, with this lane | status.js marks the current section on the links inside `.nav`. The foundation's pinned `a.nav-top` (Programme) is outside `.nav`, so status.js does not mark it. The foundation's newer `:has()` rule styles it when the first item is current (per the QA's static reading). | Foundation; consistent with status.js. Recheck on the composed candidate. |
| F10b bar scroller fades only on the right, so words are cut on the left | S3 | this lane (where the bar is scrolled) and the foundation (the mask) | status.js scrolls the bar to keep the current link in sight (centred), so a link can be cut at the left with no fade. New: status.js names the bar's hidden edges (`data-edge`), and the CSS block fades exactly those, the left edge included. | **Healed on this lane's side.** Test: "bar: a bar that scrolls sideways names the edges where it hides links" (fails on candidate-r2, passes now). Look unseen. |
| F10c at 375 px only 144 of 680 px of links show, with a dead gap after "Programme" | S3 | foundation (bar layout) | Not this lane's code. | Foundation. |
| F11 two names for each section (bar against contents) | S4 | foundation (labels) | Not this lane's code. The search's Part chips take their names from the bar links, so they follow whatever the bar says. | Foundation. |
| F12 hover cards open when content scrolls under a resting pointer | S4 | this lane | Was: the card opened on any `mouseover`. **Now:** a card opens only when the pointer actually moves onto its trigger. A move reported at the same screen position, as browsers report after a scroll, is ignored; back on the trigger of the card that is shown, the card stays (cycle 3). | **Healed.** Test: "card: a card opens when the pointer moves onto a term, not when the page scrolls a term under a resting pointer" (fails on candidate-r2, passes now). |
| F13 a statement's title twice on arrival by address | S4 | foundation (`:target` head of a folded statement) | status.js opens the fold around the target and marks it `data-revealed`; the duplicate head is the foundation's documented `:target` drawing. | Foundation. |
| F14 footer repeats the name; "Published" chip alone on a line | S4 | foundation | Not this lane's code. | Foundation. |

**Seen in the shots and in this lane:**

- **E06 (baseline column, 375 px).** The search's placeholder, this lane's words ("Search statements, questions, examples
  and terms"), is cut at "…examples an…".
- **The same shot.** The keyboard hint ("Press / to search…") shows on a phone, where it does not apply.

Both are queued with the next heal round: a shorter placeholder when the field is narrow (with its own label key), and
the keyboard hint shown only with a fine pointer. They are not yet applied: the r3 freeze is not held up for them.

**Remaining for root's native QA of the exact composed candidate:**

- F1 to F14;
- the look of every state this lane adds (notices, the filter line, revealed marks, the drawn highlight, the
  crosshair, the legend switches and lit cells, edge fades on formulas and the bar, snippets with formulae, Show more,
  the touch sheet);
- both themes, reduced motion, forced colours, print (A4, Letter), and the keyboard matrix.
