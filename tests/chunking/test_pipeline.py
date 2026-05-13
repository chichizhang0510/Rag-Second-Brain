from pathlib import Path

from src.chunking.pipeline import build_chunks_from_directory


def test_build_chunks_from_directory_flattens_multiple_files(tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text("# A\n\na\n", encoding="utf-8")
    (tmp_path / "b.md").write_text("# B\n\nb\n", encoding="utf-8")
    chunks = build_chunks_from_directory(tmp_path)
    assert len(chunks) == 2
    assert {c.source for c in chunks} == {"a.md", "b.md"}