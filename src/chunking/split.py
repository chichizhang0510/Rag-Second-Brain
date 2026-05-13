"""Read markdown files and delegate line scanning to ``MarkdownSplitter``."""

from __future__ import annotations

import logging
from pathlib import Path

from src.chunking.chunk_build import append_no_heading_chunks
from src.chunking.MarkdownSplitter import MarkdownSplitter
from src.chunking.types import Chunk

logger = logging.getLogger(__name__)

_NO_HEADING = "<no heading>"


def split_markdown_file(path: Path, *, max_chunk_chars: int | None = None) -> list[Chunk]:
    """
    Read a markdown file and split it into chunks.

    Args:
        path: The path to the markdown file.
        max_chunk_chars: The maximum number of characters in a chunk.

    Returns:
        A list of chunks.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    source = path.name
    stem = path.stem

    if not lines:
        logger.warning("Empty markdown file: %s", path)
        return []

    splitter = MarkdownSplitter(source=source, stem=stem, max_chunk_chars=max_chunk_chars)

    for line_no, line in enumerate(lines, start=1):
        splitter.process_line(line_no, line)

    splitter.finalize_heading_document()

    if not splitter.has_any_heading and lines:
        append_no_heading_chunks(
            splitter.chunks,
            no_heading_tag=_NO_HEADING,
            stem=stem,
            source=source,
            lines=lines,
            max_chunk_chars=max_chunk_chars,
        )

    return splitter.chunks
