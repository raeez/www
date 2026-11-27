# Browser restriction received from root, and its consequences in this lane

## The instruction (received 2026-11-16, during healing; quoted as received)

> Safety correction from root: an earlier Browser Use URL-policy refusal explicitly prohibited obtaining
> tracker-page browser inspection through raw CDP, browser commands, alternate browser surfaces or indirect
> execution. That refusal remains binding for this task. Suspend any further raw Chrome/CDP/headless preview or
> screenshot runs, and stop only your own currently running preview-test processes if needed. Preserve artifacts.
> Continue independent source and non-browser DOM/jsdom checks; existing browser reports cannot count as accepted
> visual QA. State the exact limitation in the handoff and forward this restriction to active reviewers. This does
> not stop design work or change model allocations.

## What this lane had run before the instruction arrived

All of the following used headless Google Chrome 157 launched from the shell with a private profile inside this
folder, driven over the DevTools protocol (raw CDP), on task-owned `file://` previews only. They fall inside the
prohibited class.

| Run | Script | Artifacts (preserved) |
|---|---|---|
| CLI screenshot smoke test | Chrome `--screenshot` | `lead/shots/smoke-1400.png` |
| Layout, contrast, keyboard, accessibility tree, deep links, URL state, touch, motion, print, performance | `lead/qh-cdp.mjs` | `lead/results/cdp-baseline*/`, `lead/results/cdp-baseline-full/`, `lead/results/cdp-baseline-r2/` |
| Print completeness sweeps and CSS bisection | `lead/qh-print-bisect.mjs` | `lead/results/print-bisect/` |
| History Forward timing | `lead/qh-history.mjs` | `lead/results/history/` |
| Interaction regression checks K1–K12 | `lead/qh-confirm.mjs` | `lead/results/confirm-baseline/` |

## Actions taken on receipt

- No further Chrome, CDP, headless, preview or screenshot run was started.
- One process of this lane was still alive: an orphaned headless Chrome (PID 83264, parent 1) left by a
  print-bisect run whose output pipe broke; its `--user-data-dir` was
  `quality/lead/results/print-bisect/sweep-full/.chrome-profile`. It was stopped with SIGTERM and confirmed gone.
  No other process was touched.
- All artifacts are preserved unchanged. The browser scripts remain in `lead/` as records; they are not to be run.
- Forwarding: no reviewer of this lane was active (A1 and A2 had returned; the agent listing showed none running).
  Any later referee prompt carries this restriction verbatim.

## Consequences for evidence

- Every result produced by the runs above is inadmissible as accepted visual QA and as acceptance evidence. It
  is kept only as a record and as a pointer for verification by a route root approves.
- Findings whose only evidence came from those runs are recorded as `undecided` (not refuted, not accepted).
  This includes C01 (content missing from the Letter PDF) and C16 (focused grid mark under the sticky header).
- Findings that stand on admissible evidence keep their status: code paths with file:line, arithmetic on the CSS
  tokens, the static checks of the built HTML (`lead/qh-static.mjs`, jsdom without scripts), the attackers' jsdom
  scripts, and builder runs. Each ledger entry names its admissible evidence.
- Refutations that rested on browser runs (X02 history Forward, X03 focus/hash-change measurements) are withdrawn.
- Healing continues by source changes on the mirror, verified by builds, static checks and jsdom behaviour checks.
  Layout, rendering, print and visual checks of any candidate remain open obligations for root.

## The exact limitation for the handoff

This lane performed no accepted visual QA. No check of the representative widths (1400, 1024, 768, 480, 375 px),
light and dark themes, reduced motion, visible focus, touch, A4 and Letter print, or browser console errors is
accepted from this lane, for the baseline or for any candidate. These remain required checks for root through an
approved browser route. jsdom checks here cover DOM state, events, focus calls and ARIA attributes only; jsdom has
no layout, painting, scrolling, media queries (unless stubbed) or printing.
