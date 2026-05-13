from __future__ import annotations

import sys
import traceback # 导入 traceback 模块。作用：打印异常堆栈。
from pathlib import Path

from src.cli.context import context_from_args
from src.cli.parser import build_parser
from src.cli.pipeline import run_ask
from src.llm_client.exceptions import LLMClientError, LLMConfigurationError


# 仓库根目录 相对于 main.py 的位置。
# 因为 main.py 在 src/cli/ 目录下，而仓库根目录在 src/ 目录下。
# grammar: parents[2] 表示 从当前文件的父目录开始，往上数 2 级，得到仓库根目录。
REPO_ROOT = Path(__file__).resolve().parents[2]


def _print_llm_error(exc: LLMClientError) -> None:
    """打印 LLM 错误信息到 stderr。"""
    print(str(exc), file=sys.stderr)
    detail = getattr(exc, "detail", None)
    if detail:
        print(detail, file=sys.stderr)


def main(argv: list[str] | None = None) -> None:
    """
    运行问答流程。

    Args:
        argv: 命令行参数。
        
    Returns:
        None。
    """
    try:
        ns = build_parser().parse_args(argv) # 解析命令行参数。
        ctx = context_from_args(ns, repo_root=REPO_ROOT) # 创建 AskContext。
        code = run_ask(ctx) # 运行问答流程。
    except LLMConfigurationError as e:
        _print_llm_error(e) # 打印 LLM 配置错误。
        raise SystemExit(2) from e # 退出程序，返回 2。why 2? because LLMConfigurationError is a local error.
    except LLMClientError as e:
        _print_llm_error(e) # 打印 LLM 客户端错误。
        raise SystemExit(3) from e # 退出程序，返回 3。why 3? because LLMClientError is a upstream error.
    except SystemExit:
        raise # 直接抛出 SystemExit 异常。
    except Exception as e:
        traceback.print_exc(file=sys.stderr) # 打印异常堆栈。
        raise SystemExit(1) from e # 退出程序，返回 1。why 1? because it is a local error.
    raise SystemExit(code) # 退出程序，返回 code。