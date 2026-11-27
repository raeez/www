"""PDF links on the native chapter Markdown path."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from monograph import Book


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.anchors.append(dict(attrs))


class ChapterDownloads(unittest.TestCase):
    def test_native_files_and_ordinary_citations(self):
        book = Book.__new__(Book)
        book.current = "ch14"
        book.refdefs = {}
        book.chapter_files = {}
        book.pending_refs = []
        book.local_links = []
        book.tags = {}
        book.problems = []
        parser = Links()
        files = ("celestial-current-product.pdf", "celestial-residue.pdf")
        for name in files:
            parser.feed(book.inline(f"[Download *the paper* (PDF)]({name})"))
        for name in ("unpublished.pdf", "../celestial-residue.pdf",
                     "https://example.org/celestial-residue.pdf"):
            self.assertEqual(book.inline(f"[Source]({name})"), "Source")
        self.assertEqual([a["href"] for a in parser.anchors], list(files))
        self.assertTrue(all(a.get("type") == "application/pdf" and "download" in a
                            for a in parser.anchors))
        self.assertEqual(book.pending_refs, [])


if __name__ == "__main__":
    unittest.main()
