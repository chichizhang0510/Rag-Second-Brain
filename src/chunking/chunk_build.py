"""Pure helpers to build Chunk lists from raw section text (no I/O, no MarkdownSplitter)."""

from __future__ import annotations

from src.chunking.types import Chunk


def apply_heading_to_stack(stack: list[tuple[int, str]], level: int, title: str) -> None:
    """
    Apply a heading to the stack.
    
    Args:
        stack: The stack to apply the heading to.
        level: The level of the heading.
        title: The title of the heading.

    Returns:
        None.
    """
    while stack and stack[-1][0] >= level:
        stack.pop()
    stack.append((level, title))


def heading_path(source: str, stack: list[tuple[int, str]]) -> str:
    """
    Generate a heading path from the stack.

    Args:
        source: The source of the heading.
        stack: The stack to generate the heading path from.

    Returns:
        The heading path.
    """
    if not stack:
        return source
    return source + " > " + " > ".join(t for _, t in stack)


def split_text_at_max_chars(text: str, max_chunk_chars: int) -> list[str]:
    """
    Split text at the maximum number of characters.

    Args:
        text: The text to split.
        max_chunk_chars: The maximum number of characters in a chunk.

    Returns:
        The list of parts.
    """
    if max_chunk_chars <= 0:
        return [text]
    parts: list[str] = []
    i = 0
    while i < len(text):
        parts.append(text[i : i + max_chunk_chars])
        i += max_chunk_chars
    return parts


def chunks_from_raw_section(
    *,
    stem: str,
    source: str,
    display_heading: str,
    display_path: str,
    raw_text: str,
    start_line: int,
    end_line: int,
    max_chunk_chars: int | None,
) -> list[Chunk]:
    """
    Split raw text into chunks.

    Args:
        stem: The stem of the source.
        source: The source of the text.
        display_heading: The display heading.
        display_path: The display path.
        raw_text: The raw text to split.
        start_line: The start line of the text.
        end_line: The end line of the text.
        max_chunk_chars: The maximum number of characters in a chunk.

    Returns:
        The list of chunks.
    """
    if max_chunk_chars is not None and len(raw_text) > max_chunk_chars:
        texts = split_text_at_max_chars(raw_text, max_chunk_chars)
    else:
        texts = [raw_text]

    out: list[Chunk] = []
    for part_index, part_text in enumerate(texts):
        sid = f"{stem}:{start_line:05d}"
        if len(texts) > 1:
            sid = f"{stem}:{start_line:05d}_p{part_index + 1}"
        hpath = display_path
        if len(texts) > 1:
            hpath = f"{display_path} (part {part_index + 1}/{len(texts)})"
        out.append(
            Chunk(
                chunk_id=sid,
                source=source,
                heading=display_heading,
                heading_path=hpath,
                text=part_text,
                start_line=start_line,
                end_line=end_line,
            )
        )
    return out


def append_no_heading_chunks(
    chunks: list[Chunk],
    *,
    no_heading_tag: str,
    stem: str,
    source: str,
    lines: list[str],
    max_chunk_chars: int | None,
) -> None:
    """
    Append no heading chunks to the list.

    Args:
        chunks: The list of chunks to append the no heading chunks to.
        no_heading_tag: The tag for the no heading.
        stem: The stem of the source.
        source: The source of the text.
        lines: The list of lines to append the no heading chunks to.
        max_chunk_chars: The maximum number of characters in a chunk.

    Returns:
        None.
    """
    full = "\n".join(lines)
    if max_chunk_chars is not None and len(full) > max_chunk_chars:
        parts = split_text_at_max_chars(full, max_chunk_chars)
    else:
        parts = [full]
    end_ln = len(lines)
    for pi, part in enumerate(parts):
        cid = f"{stem}:00001" if len(parts) == 1 else f"{stem}:00001_p{pi + 1}"
        hpath = f"{source} > {no_heading_tag}"
        if len(parts) > 1:
            hpath = f"{hpath} (part {pi + 1}/{len(parts)})"
        chunks.append(
            Chunk(
                chunk_id=cid,
                source=source,
                heading=no_heading_tag,
                heading_path=hpath,
                text=part,
                start_line=1,
                end_line=end_ln,
            )
        )
