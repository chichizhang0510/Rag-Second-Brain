from __future__ import annotations

import sys

from src.augment.builder import build_messages
from src.augment.types import AugmentOptions
from src.cli.context import AskContext
from src.llm_client import generate_answer
from src.retrieve.pipeline import retrieve_from_directory
from src.retrieve.types import RetrievalConfig


def _eprint(*parts: object) -> None:
    """打印错误信息到 stderr。"""
    print(*parts, file=sys.stderr)


def run_ask(ctx: AskContext) -> int:
    """
    运行问答流程。
    
    Args:
        ctx: AskContext。
        
    Returns:
        int。
    """
    # 校验问题。
    if not ctx.question:
        _eprint("empty --question after strip")
        return 1
    # 校验知识库目录。
    if not ctx.kb_dir.is_dir():
        _eprint(f"knowledge base not found or not a directory: {ctx.kb_dir}")
        return 2

    # 调用 retrieve_from_directory 进行检索。
    hits = retrieve_from_directory(
        ctx.query,
        ctx.kb_dir,
        RetrievalConfig(top_k=ctx.top_k),
    )
    # 调试 输出检索结果。
    if ctx.debug:
        _eprint(f"hits: {len(hits)}") # 输出检索命中数。
        for i, h in enumerate(hits, start=1): # 输出每条命中。
            _eprint(
                f"[{i}] score={h.score:.4f} source={h.source!r} "
                f"path={h.heading_path!r} chunk_id={h.chunk_id!r}",
            )

    # 构建消息。
    messages = build_messages(
        hits,
        ctx.question,
        AugmentOptions(language=ctx.language),
    )
    # 调试 输出消息。
    if ctx.dry_run:
        _eprint(f"dry-run: skipped LLM call, {len(messages)} message(s).")
        return 0

    # 生成答案。
    answer = generate_answer(
        messages,
        model=ctx.model,
        temperature=ctx.temperature,
        max_tokens=ctx.max_tokens,
    )
    # 输出答案。
    print(answer)
    # 返回成功。
    return 0