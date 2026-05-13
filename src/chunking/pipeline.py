"""
Build chunks from a directory of markdown files.
"""

from pathlib import Path

from src.chunking.load import iter_markdown_files
from src.chunking.split import split_markdown_file
from src.chunking.types import Chunk

def build_chunks_from_directory(
    kb_dir: Path,
    *,
    max_chunk_chars: int | None = None,
) -> list[Chunk]:
    out: list[Chunk] = []
    for md in iter_markdown_files(kb_dir):
        out.extend(split_markdown_file(md, max_chunk_chars=max_chunk_chars))
    return out