from __future__ import annotations

from dataclasses import dataclass


# frozen 避免下游误改
@dataclass(frozen=True)
class Chunk:
    """One logical section of a Markdown knowledge file."""

    chunk_id: str
    source: str  # 存文件名
    heading: str  # 当前节主标题（最后一级）
    heading_path: str  # 可选，面包屑，供展示与日志。
    text: str  # 参与检索的正文（可拼接 `heading_path` 进检索域以增强主题词命中，见 4.4）。
    start_line: int
    end_line: int