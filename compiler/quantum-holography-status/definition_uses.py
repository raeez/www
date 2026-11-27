"""Set an author's selected occurrence as a link to its precise mathematical definition."""
import html
import json
from pathlib import Path
import re


class DefinitionUses:
    def __init__(self, reader_directory):
        path = Path(reader_directory) / "definition-uses.json"
        rows = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else []
        self.by_scope = {}
        self.by_id = {}
        for row in rows:
            ident = row["id"]
            if ident in self.by_id or not re.fullmatch(r"[a-z][a-z0-9-]*", ident):
                raise ValueError(f"Duplicate or invalid definition use {ident}")
            if not re.fullmatch(r"[A-Za-z][\w:.-]*", row["target"]):
                raise ValueError(f"Invalid definition destination for {ident}")
            self.by_scope.setdefault(row["scope"], []).append(row)
            self.by_id[ident] = row

        path = Path(reader_directory) / "definition-passages.json"
        passages = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else []
        self.passages = {}
        for row in passages:
            scope, paragraph, ident = row["scope"], row["paragraph"], row["id"]
            if not re.fullmatch(r"[a-zA-Z][\w:.-]*", ident):
                raise ValueError(f"Invalid definition passage {ident}")
            targets = self.passages.setdefault(scope, {})
            if paragraph in targets:
                raise ValueError(f"Two anchors select the same definition paragraph in {scope}")
            targets[paragraph] = ident

    def anchor_passages(self, scope, blocks):
        """Attach selected source paragraphs to the same address before and after the native split."""
        targets = self.passages.get(scope, {})
        if not targets:
            return
        seen = set()
        for block in blocks:
            if block['t'] != 'p':
                continue
            text = re.sub(r'\[([^\[\]\n]+)\]\(definition-use:[a-z0-9-]+\)', r'\1', block['text'])
            ident = targets.get(text)
            if ident:
                if ident in seen:
                    raise ValueError(f"Ambiguous defining paragraph for {ident}")
                seen.add(ident)
                block['passage_id'] = ident
        missing = set(targets.values()) - seen
        if missing:
            raise ValueError(f"Changed defining paragraph in {scope}: {sorted(missing)}")

    def mark(self, scope, text):
        """Locate exact context on the unmodified source, then insert ordinary inline links right to left."""
        matches = []
        for row in self.by_scope.get(scope, []):
            quote, phrase = row["quote"], row["phrase"]
            if text.count(quote) != 1 or quote.count(phrase) != 1:
                raise ValueError(f"Definition use {row['id']} has changed context in {scope}")
            start = text.index(quote) + quote.index(phrase)
            if not phrase or any(ch in phrase for ch in "[]\n"):
                raise ValueError(f"Definition use {row['id']} is outside plain inline prose")
            matches.append((start, start+len(phrase), row))
        end_of_previous = len(text)
        for start, end, row in sorted(matches, key=lambda m:m[0], reverse=True):
            if end > end_of_previous:
                raise ValueError(f"Overlapping definition use {row['id']}")
            text = text[:start]+"["+text[start:end]+"](definition-use:"+row["id"]+")"+text[end:]
            end_of_previous = start
        return text

    def link(self, ident, visible):
        row = self.by_id[ident]
        target = html.escape(row["target"], quote=True)
        preview = html.escape(row["preview"], quote=True)
        return (f'<a href="#{target}" data-ref="definition" data-definition-use="{ident}" '
                f'data-definition-target="{target}" data-definition-preview="{preview}">{visible}</a>')
