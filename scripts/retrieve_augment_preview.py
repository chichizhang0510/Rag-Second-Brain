"""
本地联调：检索（Retrieval）→ 拼消息（Augmentation）。

在仓库根目录执行（与 pytest / test_pipeline 一致），例如：
  python scripts/retrieve_augment_preview.py --query "fibonacci" --question "什么是记忆化？"
"""

from __future__ import annotations

import argparse # 解析命令行参数。
import json # 将 JSON 数据转换为字符串。
import sys # 系统路径。
from pathlib import Path # 路径。

_REPO_ROOT = Path(__file__).resolve().parents[1] # 仓库根目录。
if str(_REPO_ROOT) not in sys.path: # 如果仓库根目录不在系统路径中，则添加到系统路径。
    sys.path.insert(0, str(_REPO_ROOT))

from src.augment.builder import build_messages # 构建消息。
from src.augment.types import AugmentOptions # 构建选项。
from src.retrieve.pipeline import retrieve_from_directory # 检索。
from src.retrieve.types import RetrievalConfig # 检索配置。


def main() -> None:
    """
    Main function to run the retrieval and augmentation pipeline.
    """
    # 解析命令行参数。
    parser = argparse.ArgumentParser(
        description="Run BM25 retrieval on knowledge_base/ then build chat messages via augment.",
    )
    # 添加查询参数 --query。
    parser.add_argument(
        "--query",
        required=True,
        help="BM25 检索 query（可与用户问题不同；多数演示里可与 --question 相同）。",
    )
    # 添加问题参数 --question。
    parser.add_argument(
        "--question",
        required=True,
        help="写入 user 消息 ## Question 区块的完整用户问题。",
    )
    # 添加知识库目录参数 --kb-dir。
    parser.add_argument(
        "--kb-dir",
        type=Path,
        default=None,
        help="Markdown 知识库目录，默认 <repo>/knowledge_base",
    )
    # 添加返回条数参数 --top-k。
    parser.add_argument("--top-k", type=int, default=5, help="RetrievalConfig.top_k")
    # 添加语言参数 --language。 
    parser.add_argument(
        "--language",
        choices=("zh", "en"),
        default="zh",
        help="AugmentOptions.language（system 与上下文说明语言）。",
    )
    # 添加分数参数 --include-score。
    parser.add_argument(
        "--include-score",
        action="store_true",
        help="在 Retrieved context 每条命中 header 中附加 BM25 score（调试用）。",
    )
    # 添加 JSON 参数 --dump-json。
    parser.add_argument(
        "--dump-json",
        action="store_true",
        help="额外打印完整 messages 的 JSON（便于拷贝到 Postman / curl 调试）。",
    )


    # 解析命令行参数。
    args = parser.parse_args()
    # 解析知识库目录。如果知识库目录为空，则使用默认知识库目录。
    kb_dir = (args.kb_dir or (_REPO_ROOT / "knowledge_base")).resolve()
    # 如果知识库目录不存在，则抛出错误。    
    if not kb_dir.is_dir():
        raise SystemExit(f"knowledge base directory not found: {kb_dir}")
    # 创建检索配置。
    cfg = RetrievalConfig(top_k=args.top_k)
    # 检索命中。
    hits = retrieve_from_directory(args.query, kb_dir, cfg)
    
    # 创建构建选项。
    # 如果分数参数为 True，则设置分数参数。
    opts = AugmentOptions(
        language=args.language,
        include_score_in_context=args.include_score,
    )
    # 构建消息。
    messages = build_messages(hits, args.question, opts)
    # 打印知识库目录。  
    print(f"kb_dir: {kb_dir}")
    # 打印命中条数。
    print(f"hits: {len(hits)}")
    # 打印每条命中。
    for i, h in enumerate(hits, start=1):
        preview = (h.text[:120] + "…") if len(h.text) > 120 else h.text
        print(f"  [{i}] score={h.score:.4f} source={h.source!r} chunk_id={h.chunk_id!r}")
        print(f"      text_preview: {preview!r}")
    # 打印系统消息。
    print("\n--- system ---\n")
    print(messages[0]["content"])
    # 打印用户消息。
    print("\n--- user (full) ---\n")
    print(messages[1]["content"])

    # 如果 dump_json 参数为 True，则打印消息 JSON。
    if args.dump_json:
        # 打印消息 JSON。
        print("\n--- messages JSON ---\n")
        print(json.dumps(messages, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
