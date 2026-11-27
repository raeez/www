"""Copy a built monograph page with this worktree's reader.js in place of the page's reader script, and optionally
status.js inserted just before it, so that the reader's page checks run on the actual composed text:

    python3 -I tools/with-reader.py <book.html> <out.html> --reader <reader.js> [--status <status.js>]
    NODE_PATH=<jsdom> node --max-old-space-size=8192 --expose-gc <tests/reader.test.cjs> --page <out.html>

Reads the page and writes only <out.html>. The page's reader script is the inline script that begins with the
reader's opening comment; it is replaced whole. Prints the sha256 of the input, the scripts and the output."""
import hashlib
import re
import sys


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def main(argv):
    if len(argv) < 4 or '--reader' not in argv:
        print(__doc__)
        return 2
    src, out = argv[1], argv[2]
    reader = open(argv[argv.index('--reader') + 1], encoding='utf-8').read()
    status = open(argv[argv.index('--status') + 1], encoding='utf-8').read() if '--status' in argv else None
    page = open(src, encoding='utf-8').read()
    found = [m for m in re.finditer(r'<script>(.*?)</script>', page, re.S) if m.group(1).lstrip().startswith('/* The reader of the monograph.')]
    if len(found) != 1:
        print(f'expected one reader script, found {len(found)}')
        return 1
    m = found[0]
    block = (f'<script>{status}</script>' if status else '') + f'<script>{reader}</script>'
    new = page[:m.start()] + block + page[m.end():]
    open(out, 'w', encoding='utf-8').write(new)
    print('page   ', sha(page), src)
    print('reader ', sha(reader.strip()), '(replaces', sha(m.group(1).strip())[:16] + ')')
    if status:
        print('status ', sha(status.strip()))
    print('output ', sha(new), out)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
