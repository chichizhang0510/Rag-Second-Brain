from src.augment.formatter import format_hit
from src.retrieve.types import RetrievalHit


def test_format_hit_contains_source_heading_and_text() -> None:
    """
    Test that the format_hit function contains the source, heading, and text.
    """
    hit = RetrievalHit("A:1", "A.md", "H", "A.md > H", "body", 1.23)
    s = format_hit(hit, 1)
    assert "[1]" in s
    assert "source: A.md" in s
    assert "heading_path: A.md > H" in s
    assert "body" in s


def test_format_hit_includes_score_when_requested() -> None:
    hit = RetrievalHit("A:1", "A.md", "H", "A.md > H", "body", 1.23456)
    s = format_hit(hit, 1, include_score=True)
    assert "| score: 1.2346" in s