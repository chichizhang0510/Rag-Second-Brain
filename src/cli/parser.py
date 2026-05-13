"""
Command-line argument parser for the RAG practice repo.

--question    必填 str            build_messages 的用户问题
--query       可选 str            BM25 query；省略则由 context 用 question
--kb-dir      可选 Path           知识库根；省略则由 context 用默认
--top-k       可选 int            检索命中数；省略则由 context 用默认
--language    可选 choices zh/en  语言；省略则由 context 用默认
--model       可选 str            模型；省略则由 context 用默认
--temperature 可选 float          温度；省略则由 context 用默认
--max-tokens  可选 int            最大令牌数；省略则由 context 用默认
--debug       可选 bool           调试模式；省略则由 context 用默认
--dry-run     可选 bool           不调 LLM；省略则由 context 用默认
"""

from __future__ import annotations

import argparse # 导入 argparse 模块。作用：解析命令行参数。
import sys # 导入 sys 模块。作用：退出程序。
from pathlib import Path # 导入 Path 模块。作用：处理路径。


class _ArgParser(argparse.ArgumentParser):
    """覆盖 argparse 在 缺参数、非法选项 时的行为，统一 sys.exit(1)。"""
    
    def error(self, message: str) -> None:
        """
        将 argparse 的用法错误映射为退出码 1（本仓库约定）。
        
        Args:
            message: 错误信息。
            
        Returns:
            None。
        """
        # 打印用法错误。
        self.print_usage(sys.stderr)
        # 打印错误信息。
        print(f"{self.prog}: error: {message}", file=sys.stderr)
        # 退出程序。
        sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    p = _ArgParser(
        description="RAG: BM25 retrieve + augment + OpenAI-compatible chat.",
    )
    # 添加 --question 参数。
    # 用户真正想问的那句话，会原样进入 build_messages(..., user_question=...)，通常落在 prompt 里 ## Question 区块。
    # 它描述 「答什么」；检索用哪几个关键词可以由 --query 单独指定（见下）。
    p.add_argument(
        "--question",
        required=True,
        help="User question (passed to build_messages).",
    )
    # 添加 --query 参数。
    # 传给 retrieve_from_directory 的第一个参数（BM25 检索用的 query 字符串）。
    # 在 context_from_args 里会用 --question 的值来填充，如果用户没有提供 --query 参数，则使用 --question 的值。
    # 有时你希望 检索词 与 完整问题 不同，例如检索词比完整问题更短，或者检索词比完整问题更准确。让 BM25 更容易命中相关 chunk，同时模型仍看到完整问题。
    p.add_argument(
        "--query",
        default=None,
        help="BM25 query; default: same as --question.",
    )
    # 添加 --kb-dir 参数。
    # Markdown 知识库根目录（下面应有 .md 等，由 chunking/retrieve 扫描）。
    # 在 context 层回落到 <repo>/knowledge_base（相对你传入的 repo_root）。
    p.add_argument(
        "--kb-dir",
        type=Path,
        default=None,
        help="Knowledge base root; default: <repo>/knowledge_base.",
    )
    # 添加 --top-k 参数。
    # 检索最多返回多少条 RetrievalHit，对应 RetrievalConfig(top_k=...)。
    # 常见 RAG 演示在 覆盖面 和 上下文长度 之间的折中；加大可提高召回，但 prompt 更长、更贵、更易噪声。
    # 从默认 5 开始，你也可以增加它，但模型上下文预算有限，需要考虑 prompt 长度、token 成本与模型响应速度。
    p.add_argument("--top-k", type=int, default=5)
    # 添加 --language 参数。
    # 传给 AugmentOptions(language=...)，用于选 中文/英文 system 模板（以及无上下文时的说明风格）。
    p.add_argument("--language", choices=("zh", "en"), default="en")
    # 添加 --model 参数。
    # 传给 generate_answer(..., model=...)；为 None 时由 llm_client 用环境变量（如 OPENAI_MODEL）和模块默认模型决定。
    p.add_argument("--model", default=None)
    # 添加 --temperature 参数。
    # 传给 generate_answer(..., temperature=...)；None 时由 config/环境解析默认（练习里一般是偏低温度，利于摘录问答）。
    # 若要模型自行探索，可设置 0.7 以上。
    p.add_argument("--temperature", type=float, default=None)
    # 添加 --max-tokens 参数。
    # 传给 generate_answer(..., max_tokens=...)；None 时走 llm_client 的默认与环境。
    # 若设置，注意 prompt 长度 + 回答长度 + 模型上下文预算。
    p.add_argument("--max-tokens", type=int, default=None)
    # 添加 --debug 参数。
    # 在 pipeline 里把 每条 hit 的序号、分数、来源、路径、chunk_id 等打到 stderr，便于对照「检索到了什么」。
    # 通常不开启，除非在 chunking/retrieve 里 debug。
    p.add_argument("--debug", action="store_true")
    # 添加 --dry-run 参数。
    # 一直执行到 build_messages（检索 + 拼 prompt），但 **不调用 generate_answer。
    # 用于快速迭代 tokenizer 与分块规则。
    p.add_argument("--dry-run", action="store_true")
    return p