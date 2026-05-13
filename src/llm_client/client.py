from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI
from src.llm_client.exceptions import LLMConfigurationError

_DOTENV_LOADED = False

def load_dotenv_once() -> None:
    """在首次需要读环境变量时调用；避免 import 副作用过重，但保证 CLI/脚本前已加载 .env。"""
    global _DOTENV_LOADED # 全局变量。
    if _DOTENV_LOADED:
        return # 如果环境变量已加载，则直接返回。
    # 练习仓库约定在 $REPO_ROOT 运行，load_dotenv() 默认会读取当前工作目录下的 .env
    load_dotenv() # 加载环境变量。
    _DOTENV_LOADED = True # 设置环境变量已加载。


def _require_api_key() -> str:
    """校验 API 密钥。"""
    load_dotenv_once() # 加载环境变量。
    key = (os.environ.get("OPENAI_API_KEY") or "").strip() # 获取 API 密钥。
    if not key: # 如果 API 密钥为空，则抛出 LLMConfigurationError 异常。
        raise LLMConfigurationError(
            "OPENAI_API_KEY is not set. "
            "Create a .env in the repo root (see docs/Environment_Setup_Guide.md) "
            "or export OPENAI_API_KEY before running."
        )
    return key # 返回 API 密钥。

    
def get_openai_client() -> OpenAI:
    """构造 OpenAI 兼容客户端；base_url 由 OPENAI_BASE_URL 决定（可选）。"""
    api_key = _require_api_key()  # 内部已调用 load_dotenv_once()
    raw_base = (os.environ.get("OPENAI_BASE_URL") or "").strip() # 获取基础 URL。
    base_url = raw_base or None # 如果基础 URL 为空，则设置为 None。
    return OpenAI(api_key=api_key, base_url=base_url) # 返回 OpenAI 客户端。

