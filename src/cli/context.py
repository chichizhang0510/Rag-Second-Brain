from __future__ import annotations

import argparse # 导入 argparse 模块。作用：解析命令行参数。
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class AskContext:
    """请求上下文，包含所有配置参数。"""
    kb_dir: Path
    query: str
    question: str
    top_k: int
    language: str
    model: str | None
    temperature: float | None
    max_tokens: int | None
    debug: bool
    dry_run: bool


def context_from_args(ns: argparse.Namespace, *, repo_root: Path) -> AskContext:
    """
    从 argparse 的 Namespace 创建 AskContext。
    
    Args:
        ns: argparse 的 Namespace。
        repo_root: 仓库根目录。
        
    Returns:
        AskContext。
    """
    # 解析知识库目录。
    kb_dir = (ns.kb_dir or (repo_root / "knowledge_base")).resolve()
    # 解析问题。
    question = ns.question.strip()
    # 解析查询。
    query = (ns.query or ns.question).strip()
    # 创建 AskContext。
    return AskContext(
        kb_dir=kb_dir,
        query=query,
        question=question,
        top_k=ns.top_k,
        language=ns.language,
        model=ns.model,
        temperature=ns.temperature,
        max_tokens=ns.max_tokens,
        debug=ns.debug,
        dry_run=ns.dry_run,
    )