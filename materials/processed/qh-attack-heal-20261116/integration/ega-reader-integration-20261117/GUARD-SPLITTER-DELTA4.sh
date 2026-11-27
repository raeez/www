#!/bin/sh
# reader-delta4: the splitter with element-only ids. Production runs the tools from reader-delta4/tools/.
#   sh GUARD-SPLITTER-DELTA4.sh --check            verify the frozen files
#   sh GUARD-SPLITTER-DELTA4.sh <copy of splitter> replace a copy that is reader-delta2's splitter
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
SRC=$HERE/reader-delta4/tools
sum() { shasum -a 256 "$1" | cut -c1-64; }
NEW=cd104f4a5dcf458f98290ee21ac4f4fefe47795e84fd6016c0fa06ee845c7637
OLD=1f312cdff275a2dddfdb3bfaaa52da877b54e0b2cd136dd5090d0c4309f1fadf
[ "$(sum "$SRC/split-reference.py")" = "$NEW" ] || { echo "the frozen splitter does not match its pin"; exit 1; }
[ "$(sum "$SRC/reader-index.cjs")" = 90cee2b6d1e49819983b31e66336b45a5cb9ce94f8d88fb9c74ab595907ca59f ] && [ "$(sum "$SRC/split-checks.cjs")" = 3048eb47f1fe7fce92faae7955f1e26ff9840633bfa079d9e1cb6c007f756af3 ] || { echo "a frozen tool does not match its pin"; exit 1; }
T=${1:?usage: GUARD-SPLITTER-DELTA4.sh --check | <copy of the splitter>}
[ "$T" = --check ] && { echo "reader-delta4 tools verified"; exit 0; }
case "$(sum "$T")" in "$OLD"|"$NEW") ;; *) echo "$T is not reader-delta2's splitter: merge by hand"; exit 1 ;; esac
chmod u+w "$T"; cp "$SRC/split-reference.py" "$T"; [ "$(sum "$T")" = "$NEW" ] && echo "installed reader-delta4 splitter $NEW"
