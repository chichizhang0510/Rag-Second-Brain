"""
Retrieve hits from a directory of chunks.

对接 chunking 的入口函数。
保持“简洁可替换”：之后你可以新增 EmbeddingRetriever，只替换 pipeline 内部构造逻辑。

pipeline 本质 是一个编排层（orchestration layer）：
- 负责把多个步骤按顺序串起来，把顺序明确下来，避免每个调用方自己拼流程时拼错。
- 负责模块对外的“高层入口”，外部不想关心内部细节，只想一句话调用。
- 尽量不放复杂业务细节（细节在子模块里）
- 以后换检索实现：只需要替换 pipeline 内部的 retriever 构造逻辑，不需要改动 pipeline 的对外接口。

chunking/pipeline.py：一个完整子流程（读取 + 切分 + 聚合） 目录 -> 逐文件 split -> 聚合 chunks。
retrieve/pipeline.py：一个完整子流程（准备语料 + 打分 + 过滤）query + 目录 -> build chunks -> 构建 retriever -> 返回 hits
"""

from __future__ import annotations

from pathlib import Path

from src.chunking.pipeline import build_chunks_from_directory
from src.retrieve.bm25_retriever import BM25Retriever
from src.retrieve.types import RetrievalConfig, RetrievalHit

def retrieve_from_directory(
    query: str,
    kb_dir: Path,
    config: RetrievalConfig | None = None,
) -> list[RetrievalHit]:
    chunks = build_chunks_from_directory(kb_dir)
    retriever = BM25Retriever(chunks, config)
    return retriever.retrieve(query)