#!/usr/bin/env python3
"""sha256 of a built page with embedded font payloads replaced (fontTools writes a save time into each subset)."""
import hashlib, re, sys
for p in sys.argv[1:]:
    s = open(p, encoding='utf-8').read()
    s = re.sub(r'url\(data:font/woff;base64,[A-Za-z0-9+/=]+\)', 'url(data:font/woff;base64,FONT)', s)
    print(hashlib.sha256(s.encode()).hexdigest(), p)
