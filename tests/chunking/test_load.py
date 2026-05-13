from pathlib import Path

import pytest

from src.chunking.load import iter_markdown_files


def test_iter_markdown_files_raises_when_dir_missing(tmp_path: Path) -> None:
    missing = tmp_path / "missing_kb"
    with pytest.raises(FileNotFoundError):
        iter_markdown_files(missing)

def test_iter_markdown_files_returns_sorted_md_only(tmp_path: Path) -> None:
    (tmp_path / "b.md").write_text("# B\n", encoding="utf-8")
    (tmp_path / "a.md").write_text("# A\n", encoding="utf-8")
    (tmp_path / "note.txt").write_text("x", encoding="utf-8")
    files = iter_markdown_files(tmp_path)
    assert [p.name for p in files] == ["a.md", "b.md"]
    