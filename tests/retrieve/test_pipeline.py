from pathlib import Path

from src.retrieve.pipeline import retrieve_from_directory
from src.retrieve.types import RetrievalConfig


def test_retrieve_from_directory_returns_hits_for_existing_term() -> None:
    kb_dir = Path("knowledge_base")
    hits = retrieve_from_directory("fibonacci", kb_dir, RetrievalConfig(top_k=3))
    assert isinstance(hits, list)