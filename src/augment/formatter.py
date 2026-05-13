"""Format a retrieval hit into a string for context."""


from __future__ import annotations

from src.retrieve.types import RetrievalHit

# 格式化单条命中结果为 context 字符串。头部带序号、来源、路径、分数（可选），内容用三重引号包裹。
def format_hit(hit: RetrievalHit, idx: int, *, include_score: bool = False) -> str:
    """
    Format a retrieval hit into a string for context.
    The header includes index, source, heading path, and score (optional).
    The content is wrapped in triple quotes.
    
    Args:
        hit: RetrievalHit 对象
        idx: 命中序号
        include_score: 是否包含分数
    Returns:
        str: 格式化后的 context 字符串
    """
    
    header = f"[{idx}] source: {hit.source} | heading_path: {hit.heading_path}"
    if include_score: # 如果需要分数，在头部加上分数。
        header += f" | score: {hit.score:.4f}"
    return f"{header}\n\"\"\"\n{hit.text}\n\"\"\"" # 内容用三重引号包裹。