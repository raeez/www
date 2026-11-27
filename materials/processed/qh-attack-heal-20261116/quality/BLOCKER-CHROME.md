# Native Chrome integration not connected (for root)

Checked 2026-11-16 after the relaunch with --chrome, in this session (job QH-MAX-QUALITY-20261116, account config
directory `.claude8`; the session's recorded relaunch flags are reported in the handoff message).

- The claude-in-chrome tools are present in the session and the claude-in-chrome skill was loaded first, as required.
- `tabs_context_mcp` (createIfEmpty) returned: "Browser extension is not connected. Please ensure the Claude browser
  extension is installed and running, and that you are logged into claude.ai with the same account as Claude Code."
- `list_connected_browsers` returned an empty list: no Chrome extension instance is connected to this account.
- No tab was created or touched, no site permission was requested, and nothing in the extension was changed (root's
  instruction: do not change the extension login).

What root needs to decide or do: connect a Chrome instance whose Claude extension is signed in to the same account
as this session (`.claude8`), or select an already-connected browser for this session. Once connected, the lane will
create its own tab group and inspect only `candidate/preview.html` and `baseline/preview.html` (file://). If Chrome
asks for file-URL access or a site permission, the lane will stop and report the exact prompt.

Until then, actual visual QA (page image, widths, themes, keyboard focus, print preview, console) remains unresolved
and is not claimed.

## Update: visual pass moved to root's primary session (same day)

Root reported that the Chrome extension is signed in to an account other than this session's, and instructed: no
`switch_browser` and no Connect request from this account; root's primary session, on the matching account, performs
the native visual pass. This lane sent no connection request and created no tab. Its part is the exact checklist for
root's integrated candidate: VQ1-VQ7 (VISUAL-ATTACK.md), PIC-01 to PIC-18 (attacks/R3-V-cycle3.yaml) and the inherited
checks (C01 and A2-A2-07 print on A4 and Letter, C16, C23, console). Visual QA is unresolved in this lane and is not
claimed.
