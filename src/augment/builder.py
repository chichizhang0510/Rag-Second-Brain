from __future__ import annotations

from src.augment.formatter import format_hit
from src.augment.templates import (
    SYSTEM_NO_CONTEXT_EN,
    SYSTEM_NO_CONTEXT_ZH,
    SYSTEM_WITH_CONTEXT_EN,
    SYSTEM_WITH_CONTEXT_ZH,
)
from src.augment.types import AugmentOptions
from src.retrieve.types import RetrievalHit


def _truncate(text: str, limit: int, suffix: str) -> str:
    """
    Truncate text to a maximum length. If the text is longer than the limit, the suffix will be added to the truncated text.
    
    Args:
        text: The text to truncate.
        limit: The maximum length of the text.
        suffix: The suffix to add to the truncated text.
    
    Returns:
        The truncated text.
    """
    
    if limit <= 0:
        return "" # 如果限制为 0 或负数，返回空字符串。
    if len(text) <= limit:
        return text # 如果文本长度小于等于限制，返回原文本。
    cut = max(0, limit - len(suffix)) # 计算截断位置。
    return text[:cut] + suffix # 返回截断后的文本。


def _pick_system_text(has_context: bool, language: str) -> str:
    """
    Pick the system text based on the context and language.
    
    Args:
        has_context: Whether the context is available.
        language: The language of the system text.
    
    Returns:
        The system text.
    """
    
    is_zh = language.lower().startswith("zh")
    if has_context:
        return SYSTEM_WITH_CONTEXT_ZH if is_zh else SYSTEM_WITH_CONTEXT_EN
    return SYSTEM_NO_CONTEXT_ZH if is_zh else SYSTEM_NO_CONTEXT_EN


def build_context_section(hits: list[RetrievalHit], options: AugmentOptions) -> str:
    """
    Build the context section for the messages.

    Args:
        hits: The hits to build the context section for.
        options: The options for the context section.
    
    Returns:
        The context section.
    """
    # 如果命中列表为空，返回空字符串。
    if not hits:
        return "## Retrieved context\n\n<no relevant context>\n"

    # 初始化上下文列表。
    lines = ["## Retrieved context", ""]
    used = 0 # 已使用字符数。
    dropped = 0 # 丢弃的命中数。

    # 遍历命中列表。
    for i, hit in enumerate(hits, start=1):
        # 截断命中文本。
        clipped = _truncate(hit.text, options.max_chars_per_chunk, options.truncation_suffix)
        # 格式化命中文本。
        rendered = format_hit(
            RetrievalHit(
                chunk_id=hit.chunk_id,
                source=hit.source,
                heading=hit.heading,
                heading_path=hit.heading_path,
                text=clipped,
                score=hit.score,
            ),
            i,
            include_score=options.include_score_in_context,
        )
        plus = len(rendered) + 2 # 计算加上换行符后的长度。
        if used + plus > options.max_total_context_chars:
            dropped += 1 # 如果超过总预算，丢弃该命中。
            continue
        lines.append(rendered) # 添加到上下文列表。
        lines.append("") # 添加换行符。
        used += plus # 更新已使用字符数。

    if dropped:
        lines.append(f"... ({dropped} hits omitted due to context budget)") # 添加丢弃提示。
        lines.append("") # 添加换行符。

    return "\n".join(lines) # 返回上下文列表。


def build_messages(
    hits: list[RetrievalHit],
    user_question: str,
    options: AugmentOptions | None = None,
) -> list[dict[str, str]]:
    """
    Build the messages for the user question.

    Args:
        hits: The hits to build the messages for.
        user_question: The user question to build the messages for.
        options: The options for the messages.

    Returns:
        The messages.
    """
    # 初始化选项。
    options = options or AugmentOptions()
    context = build_context_section(hits, options) # 构建上下文。
    system_text = _pick_system_text(bool(hits), options.language)
    # 构建用户内容。
    user_content = (
        f"{context}\n"
        "## Question\n\n"
        f"{user_question.strip()}"
    )

    return [
        {"role": "system", "content": system_text},
        {"role": "user", "content": user_content},
    ]