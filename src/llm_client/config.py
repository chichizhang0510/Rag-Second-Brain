from __future__ import annotations

import os

# 在「函数参数未传 + 环境变量未设置」时生效
DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_TEMPERATURE = 0.3
DEFAULT_MAX_TOKENS = 1024
DEFAULT_TIMEOUT_SEC = 60.0

def _resolve_model(explicit: str | None) -> str:
    """解析模型。"""
    if explicit is not None and explicit.strip():
        return explicit.strip() # 如果显式模型不为空，则返回显式模型。
    env = (os.environ.get("OPENAI_MODEL") or "").strip() # 获取环境变量模型。
    return env or DEFAULT_MODEL # 如果环境变量模型为空，则返回默认模型。


def _resolve_temperature(explicit: float | None) -> float:
    """解析温度。"""
    if explicit is not None:
        return float(explicit) # 如果显式温度不为空，则返回显式温度。
    env = (os.environ.get("OPENAI_TEMPERATURE") or "").strip() # 获取环境变量温度。
    if env:
        return float(env) # 如果环境变量温度不为空，则返回环境变量温度。
    return float(DEFAULT_TEMPERATURE) # 如果环境变量温度为空，则返回默认温度。


def _resolve_max_tokens(explicit: int | None) -> int:
    """解析最大令牌数。"""
    if explicit is not None:
        return int(explicit) # 如果显式最大令牌数不为空，则返回显式最大令牌数。
    env = (os.environ.get("OPENAI_MAX_TOKENS") or "").strip() # 获取环境变量最大令牌数。
    if env:
        return int(env) # 如果环境变量最大令牌数不为空，则返回环境变量最大令牌数。
    return int(DEFAULT_MAX_TOKENS) # 如果环境变量最大令牌数为空，则返回默认最大令牌数。


def _resolve_timeout_sec(explicit: float | None) -> float:
    """解析超时时间。"""
    if explicit is not None:
        return float(explicit) # 如果显式超时时间不为空，则返回显式超时时间。
    env = (os.environ.get("OPENAI_TIMEOUT") or "").strip()
    if env:
        return float(env) # 如果环境变量超时时间不为空，则返回环境变量超时时间。
    return float(DEFAULT_TIMEOUT_SEC) # 如果环境变量超时时间为空，则返回默认超时时间。
