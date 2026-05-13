from src.chunking.chunk_build import (
    apply_heading_to_stack,
    append_no_heading_chunks,
    chunks_from_raw_section,
    heading_path,
    split_text_at_max_chars,
)

def test_heading_path_empty_stack_returns_source() -> None:
    assert heading_path("Doc.md", []) == "Doc.md"

def test_apply_heading_to_stack_replaces_same_or_deeper_level() -> None:
    stack: list[tuple[int, str]] = [(1, "A"), (2, "B")]
    apply_heading_to_stack(stack, 2, "B2")
    assert stack == [(1, "A"), (2, "B2")]


def test_chunks_from_raw_section_splits_parts_when_over_max_chars() -> None:
    chunks = chunks_from_raw_section(
        stem="Doc",
        source="Doc.md",
        display_heading="Sec",
        display_path="Doc.md > Sec",
        raw_text="abcdefghij",  # 10 chars
        start_line=3,
        end_line=3,
        max_chunk_chars=4,
    )
    assert len(chunks) == 3
    assert chunks[0].chunk_id == "Doc:00003_p1"
    assert chunks[1].chunk_id == "Doc:00003_p2"
    assert "(part 1/3)" in chunks[0].heading_path


def test_split_text_at_max_chars_returns_original_when_non_positive_limit() -> None:
    assert split_text_at_max_chars("abcdef", 0) == ["abcdef"]


def test_append_no_heading_chunks_splits_and_marks_parts() -> None:
    chunks = []
    append_no_heading_chunks(
        chunks,
        no_heading_tag="<no heading>",
        stem="Doc",
        source="Doc.md",
        lines=["abcdefghij"],
        max_chunk_chars=4,
    )
    assert len(chunks) == 3
    assert chunks[1].chunk_id == "Doc:00001_p2"
    assert "(part 2/3)" in chunks[1].heading_path