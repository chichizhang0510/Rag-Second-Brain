from src.augment.builder import build_context_section, build_messages
from src.augment.types import AugmentOptions
from src.retrieve.types import RetrievalHit


def _hits() -> list[RetrievalHit]:
    return [
        RetrievalHit("A:1", "A.md", "H1", "A.md > H1", "alpha", 2.0),
        RetrievalHit("B:1", "B.md", "H2", "B.md > H2", "beta", 1.5),
    ]


def test_build_messages_with_context_has_retrieved_section_and_question() -> None:
    msgs = build_messages(_hits(), "what is alpha?")
    assert len(msgs) == 2
    assert msgs[0]["role"] == "system"
    assert "Retrieved context" in msgs[1]["content"]
    assert "## Question" in msgs[1]["content"]


def test_build_messages_without_context_uses_no_context_prompt() -> None:
    msgs = build_messages([], "question")
    assert "No relevant retrieved context is provided." in msgs[0]["content"]
    assert "<no relevant context>" in msgs[1]["content"]


def test_context_budget_truncates_and_omits() -> None:
    opts = AugmentOptions(max_chars_per_chunk=4, max_total_context_chars=30)
    section = build_context_section(_hits(), opts)
    assert "[truncated]" in section or "omitted due to context budget" in section


def test_zero_max_chars_per_chunk_yields_empty_hit_body_in_context() -> None:
    """Covers _truncate branch when limit <= 0."""
    opts = AugmentOptions(max_chars_per_chunk=0, max_total_context_chars=10_000)
    section = build_context_section(_hits(), opts)
    assert '"""\n\n"""' in section


def test_build_messages_uses_english_system_when_language_en() -> None:
    msgs = build_messages(_hits(), "q", AugmentOptions(language="en"))
    assert "strictly from the provided retrieved context" in msgs[0]["content"]


def test_build_messages_default_options_merges() -> None:
    """Covers build_messages branch where options is None."""
    msgs = build_messages(_hits(), "q", None)
    assert len(msgs) == 2
    assert msgs[0]["role"] == "system"
