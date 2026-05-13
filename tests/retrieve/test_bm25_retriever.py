from src.chunking.types import Chunk
from src.retrieve.bm25_retriever import BM25Retriever
from src.retrieve.types import RetrievalConfig


def _chunks() -> list[Chunk]:
    return [
        Chunk("A:00001", "A.md", "Fib", "A.md > Fib", "fibonacci memoization", 1, 3),
        Chunk("B:00001", "B.md", "Sort", "B.md > Sort", "quick sort partition", 1, 3),
    ]

def test_init_with_empty_chunks_sets_bm25_none_and_retrieve_empty() -> None:
    r = BM25Retriever([], RetrievalConfig())
    assert r.retrieve("anything") == []  # 覆盖 32 + 79
def test_build_index_text_respects_max_chunk_chars() -> None:
    c = Chunk("X:1", "X.md", "H", "X.md > H", "abcdefghij", 1, 1)
    r = BM25Retriever([c], RetrievalConfig(max_chunk_chars=4, include_heading_in_index_text=False))
    assert r._index_texts[0] == "abcd"  # 覆盖 52 + 57
def test_retrieve_returns_empty_when_top_k_is_zero_or_negative() -> None:
    r0 = BM25Retriever(_chunks(), RetrievalConfig(top_k=0))
    rneg = BM25Retriever(_chunks(), RetrievalConfig(top_k=-3))
    assert r0.retrieve("fibonacci") == []
    assert rneg.retrieve("fibonacci") == []  # 覆盖 84
def test_retrieve_returns_empty_when_query_tokens_are_empty() -> None:
    r = BM25Retriever(_chunks(), RetrievalConfig())
    assert r.retrieve("!!! ??? ---") == []  # 覆盖 90


def test_retrieve_returns_scored_hits() -> None:
    r = BM25Retriever(_chunks(), RetrievalConfig(top_k=2))
    hits = r.retrieve("fibonacci")
    assert len(hits) >= 1
    assert hits[0].source == "A.md"
    assert hits[0].score >= 0.0


def test_retrieve_respects_min_score() -> None:
    r = BM25Retriever(_chunks(), RetrievalConfig(top_k=2, min_score=999.0))
    assert r.retrieve("fibonacci") == []


def test_retrieve_empty_query_returns_empty() -> None:
    r = BM25Retriever(_chunks(), RetrievalConfig())
    assert r.retrieve("   ") == []