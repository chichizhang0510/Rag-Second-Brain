"""
In-memory BM25 retriever over chunk list.
"""

from __future__ import annotations

from dataclasses import replace

from rank_bm25 import BM25Okapi

from src.chunking.types import Chunk  # 输入语料单元
from src.retrieve.tokenize import tokenize  # 统一分词
from src.retrieve.types import RetrievalConfig, RetrievalHit  # 输入配置与输出契约


class BM25Retriever: # 定义“BM25 检索器”类。
    """In-memory BM25 retriever over chunk list."""

    # 构造函数接收 chunks 列表与可选的 config 配置。
    def __init__(self, chunks: list[Chunk], config: RetrievalConfig | None = None) -> None:
        self.config = config or RetrievalConfig()  # 没传 config 就用默认 RetrievalConfig()。
        self.chunks = chunks  # 保存原始 chunk 列表。

        self._index_texts = [self._build_index_text(c) for c in chunks]  # 对每个 chunk 先做“索引侧文本构建”。
        self._corpus_tokens = [tokenize(t) for t in self._index_texts]  # 再把索引文本分词，得到 BM25 语料 token 列表。

        # 把“每次 query 都重复做的预处理”前置到初始化，后续检索更快。
        self._bm25: BM25Okapi | None  # 声明 _bm25 可能为空（None）。
        if self._corpus_tokens:  # 有语料 token 才构建 BM25 索引对象；
            self._bm25 = BM25Okapi(self._corpus_tokens)
        else:
            self._bm25 = None  # 没语料就设为 None，后续 retrieve 直接返回空（避免异常）。

    # 私有方法：把 chunk 转换成 BM25 索引文本。
    def _build_index_text(self, chunk: Chunk) -> str:
        """
        Build index text for a chunk.

        Args:
            chunk: The chunk to build index text for.

        Returns:
            The index text for the chunk.

        Raises:
            None.
        """
        # 默认索引文本是 chunk.text。
        text = chunk.text
        # 如果配置了最大字符数，则裁剪文本
        if self.config.max_chunk_chars is not None:
            text = text[: self.config.max_chunk_chars]

        # 如果配置了包含标题路径，则返回标题路径和文本
        if self.config.include_heading_in_index_text:
            return f"{chunk.heading_path}\n\n{text}"
        return text

    # 公开方法：根据 query 检索命中。
    def retrieve(self, query: str) -> list[RetrievalHit]:
        """
        Retrieve hits from the retriever.

        Args:
            query: The query to retrieve hits for.

        Returns:
            The list of retrieval hits.
        """
        # 去除查询前后空白
        query = query.strip()

        # 如果查询为空，则返回空列表
        if not query:
            return []

        # 如果BM25为空，则返回空列表
        if self._bm25 is None:
            return []

        # 获取top_k
        top_k = max(0, self.config.top_k) # 防御非法负值。
        if top_k == 0:
            return []

        # query 分词
        q_tokens = tokenize(query)
        # 如果分词为空，则返回空列表
        if not q_tokens:
            return []

        # BM25 为每条语料给分。
        scores = self._bm25.get_scores(q_tokens)
        # 后按分数降序排序，保留“分数 + 对应 chunk 索引”。
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

        # 初始化命中列表。
        hits: list[RetrievalHit] = []
        # 遍历前 top_k 个候选。
        for idx, score in ranked[:top_k]:
            score_f = float(score)  # 把 numpy/scalar 统一成 Python float。
            if score_f < self.config.min_score:
                continue  # 低于阈值丢弃。
            # 用排序索引拿回原始 chunk。
            c = self.chunks[idx]
            # 映射成统一的 RetrievalHit（对外契约）。
            hits.append(
                RetrievalHit(
                    chunk_id=c.chunk_id,
                    source=c.source,
                    heading=c.heading,
                    heading_path=c.heading_path,
                    text=c.text,
                    score=score_f,
                )
            )
        return hits  # 返回命中列表。