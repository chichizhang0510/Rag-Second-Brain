"""
Stateful scanner for fenced ``` blocks and ATX headings (``#``–``###``).

Outside a fence, a heading at the same level as or above the current section
anchor closes that section (flush); a deeper heading keeps one section and
only updates display heading and path. Body lines are ignored until a section
is opened (first heading); ``split.py`` may append a no-heading chunk for
files with no headings.
"""

from __future__ import annotations

import re

from src.chunking.chunk_build import (
    apply_heading_to_stack,
    chunks_from_raw_section,
    heading_path,
)
from src.chunking.types import Chunk

HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$")


class MarkdownSplitter:
    """Fence toggles, ATX headings (1–3), section boundaries, body buffer."""

    __slots__ = (
        "source",
        "stem",
        "max_chunk_chars",
        "_chunks",
        "in_fence",
        "heading_stack",
        "section_start_level",
        "section_title_line",
        "body_lines",
        "first_body_line",
        "last_body_line",
        "_has_any_heading",
        "display_heading",
        "display_path",
    )

    def __init__(self, source: str, stem: str, max_chunk_chars: int | None) -> None:
        self.source = source
        self.stem = stem
        self.max_chunk_chars = max_chunk_chars

        self._chunks: list[Chunk] = []
        self.in_fence = False

        self.heading_stack: list[tuple[int, str]] = []
        self.section_start_level: int | None = None
        self.section_title_line: int | None = None

        self.body_lines: list[str] = []
        self.first_body_line: int | None = None
        self.last_body_line: int | None = None

        self._has_any_heading = False
        self.display_heading = ""
        self.display_path = source

    @property
    def chunks(self) -> list[Chunk]:
        return self._chunks

    @property
    def has_any_heading(self) -> bool:
        return self._has_any_heading

    @staticmethod
    def is_fence_boundary(line: str) -> bool:
        return line.lstrip().startswith("```")

    @staticmethod
    def heading_level(line: str) -> int | None:
        match = HEADING_RE.match(line)
        if match:
            return len(match.group(1))
        return None

    @staticmethod
    def strip_heading_title(line: str) -> str:
        match = HEADING_RE.match(line)
        if match:
            return match.group(2).strip()
        return ""

    def process_line(self, line_no: int, line: str) -> None:
        # Order: fence toggle, inside fence (no heading parse), heading, plain.
        if MarkdownSplitter.is_fence_boundary(line):
            self._on_fence_boundary(line_no, line)
            return
        if self.in_fence:
            self._on_line_inside_fence(line_no, line)
            return

        level = MarkdownSplitter.heading_level(line)
        if level is not None:
            self._on_heading_line(line_no, level, MarkdownSplitter.strip_heading_title(line))
            return

        self._on_plain_line_outside_fence(line_no, line)
    
    def finalize_heading_document(self) -> None:
        """
        若文件里至少有一个结构标题，且有打开的节，则 flush 当前节。
        
        Args:
            None.
        
        Returns:
            None.
        """
        if self._has_any_heading and self._has_open_section():
            self._flush_open_section()

    # ----------------- 围栏边界 ----------------- 
    def _on_fence_boundary(self, line_no: int, line: str) -> None:
        # 写入正文（若已开节），便于保留 Markdown 代码块标记。
        self._append_body_line(line_no, line)
        # 翻转 in_fence。
        self.in_fence = not self.in_fence

    def _on_line_inside_fence(self, line_no: int, line: str) -> None:
        # 围栏内每一行都通过 _append_body_line 写入当前节（若已开节）；不做标题解析。
        self._append_body_line(line_no, line)
    
    # ----------------- 标题行 ----------------- 
    def _on_heading_line(self, line_no: int, level: int, title: str) -> None:
        # 标记「文件里至少有一个结构标题」。
        self._has_any_heading = True
        # 若需要先关旧节，则 flush_open_section()（并清空节标记）。
        if self._should_close_before_heading(level):
            self._flush_open_section()

        # 更新 heading_stack。
        apply_heading_to_stack(self.heading_stack, level, title)
        # 更新 display_heading 和 display_path。
        self.display_heading = title
        self.display_path = heading_path(self.source, self.heading_stack)

        if self._should_reset_section_counters(level):
            self._start_new_section(line_no, level)
    
    # 若当前有打开的节，且新标题级别 <= 当前节起始级别，则返回 True，表示需要先 flush 当前节（大纲上「上一主题结束」）。
    def _should_close_before_heading(self, new_level: int) -> bool:
        return (
            self._has_open_section()
            and self.section_start_level is not None
            and new_level <= self.section_start_level
        )
    
    # 若没有打开的节，或新标题级别 > 当前节起始级别，则返回 True，表示需要重置节锚点与缓冲。
    def _should_reset_section_counters(self, new_level: int) -> bool:
        """
        若没有打开的节，或新标题级别 > 当前节起始级别，则返回 True，表示需要重置节锚点与缓冲。
        
        Args:
            new_level: The level of the new heading.

        Returns:
            True if the section counters should be reset, False otherwise.
        """
        if not self._has_open_section():
            return True
        return self.section_start_level is not None and new_level <= self.section_start_level

    def _start_new_section(self, line_no: int, level: int) -> None:
        """
        若没有打开的节，或新标题级别 > 当前节起始级别，则返回 True，表示需要重置节锚点与缓冲。
        
        Args:
            line_no: The line number of the new heading.
            level: The level of the new heading.
        
        Returns:
            None.
        """
        self.section_start_level = level
        self.section_title_line = line_no
        self._clear_body_buffer()

    def _flush_open_section(self) -> None:
        """
        若没有打开的节则直接返回。
        
        Args:
            None.
        
        Returns:
            None.
        """
        # 若没有打开的节则直接返回。
        if not self._has_open_section():
            return

        # 将 body_lines 拼接为 raw_text。
        raw_text = "\n".join(self.body_lines)

        # 计算 start_line 和 end_line。
        if self.first_body_line is not None and self.last_body_line is not None:
            start_line = self.first_body_line
            end_line = self.last_body_line
        else:
            stl = self.section_title_line
            assert stl is not None
            start_line = stl
            end_line = stl

        self._chunks.extend(
            chunks_from_raw_section(
                stem=self.stem,
                source=self.source,
                display_heading=self.display_heading,
                display_path=self.display_path,
                raw_text=raw_text,
                start_line=start_line,
                end_line=end_line,
                max_chunk_chars=self.max_chunk_chars,
            )
        )

        self._clear_body_buffer()
        self.section_start_level = None
        self.section_title_line = None
    
    def _clear_body_buffer(self) -> None:
        """
        清空 body_lines。
        
        Args:
            None.
        
        Returns:
            None.
        """
        self.body_lines.clear()
        self.first_body_line = None
        self.last_body_line = None
    
    # ----------------- 普通行 ----------------- 
    def _on_plain_line_outside_fence(self, line_no: int, line: str) -> None:
        self._append_body_line(line_no, line)

    # ----------------- 辅助方法 ----------------- 
    def _has_open_section(self) -> bool:
        """
        若没有打开的节则直接返回。
        
        Args:
            None.
        
        Returns:
            True if the section is open, False otherwise.
        """
        return self.section_title_line is not None

    def _append_body_line(self, line_no: int, line: str) -> None:
        """
        若没有打开的节则直接返回。
        
        Args:
            line_no: The line number of the new heading.
            line: The line to append.
        
        Returns:
            None.
        """
        # 没有打开的节则直接返回。
        if not self._has_open_section():
            return

        # 追加到 body_lines。
        self.body_lines.append(line)

        # 第一次追加时记下 first_body_line。
        if self.first_body_line is None:
            self.first_body_line = line_no
        self.last_body_line = line_no
