from pathlib import Path

from src.chunking.MarkdownSplitter import MarkdownSplitter
from src.chunking.split import split_markdown_file

FIXTURES = Path(__file__).resolve().parent / "fixtures"

def test_split_empty_file(tmp_path: Path) -> None:
    p = tmp_path / "empty.md"
    p.write_text("", encoding="utf-8")
    assert split_markdown_file(p) == []


def test_split_no_heading_file_falls_back_to_no_heading_tag() -> None:
    chunks = split_markdown_file(FIXTURES / "chunking_no_heading.md")
    assert len(chunks) == 1
    assert chunks[0].heading == "<no heading>"


def test_split_keeps_hash_inside_fence_as_plain_text() -> None:
    chunks = split_markdown_file(FIXTURES / "chunking_simple.md")
    assert not any(c.heading == "not a heading" for c in chunks)
    assert any("# not a heading" in c.text for c in chunks)


def test_split_two_h1_produces_two_chunks() -> None:
    chunks = split_markdown_file(FIXTURES / "chunking_two_h1.md")
    assert len(chunks) == 2
    assert chunks[0].heading == "First"
    assert chunks[1].heading == "Second"


def test_strip_heading_title_returns_empty_for_non_heading() -> None:
    assert MarkdownSplitter.strip_heading_title("not a heading") == ""


def test_flush_open_section_is_noop_when_no_section_open() -> None:
    splitter = MarkdownSplitter("Doc.md", "Doc", None)
    splitter._flush_open_section()
    assert splitter.chunks == []


def test_flush_open_section_uses_heading_line_when_section_has_no_body() -> None:
    splitter = MarkdownSplitter("Doc.md", "Doc", None)
    splitter.process_line(1, "# Title")
    splitter._flush_open_section()
    assert len(splitter.chunks) == 1
    assert splitter.chunks[0].start_line == 1
    assert splitter.chunks[0].end_line == 1

