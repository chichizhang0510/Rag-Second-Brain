from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class AugmentOptions:
    """Config knobs for message construction."""

    max_chars_per_chunk: int = 3000 # 单条命中进入 prompt 的上限
    max_total_context_chars: int = 12000 # 所有 context 的总预算
    truncation_suffix: str = "\n...[truncated]" # 截断提示
    language: str = "en" # "zh" or "en"
    include_score_in_context: bool = False # 默认关，调试时才开
