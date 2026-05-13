from __future__ import annotations

import pytest

from src.llm_client import config as cfg


# 清理环境变量。
@pytest.fixture(autouse=True)
def clear_openai_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in (
        "OPENAI_MODEL",
        "OPENAI_TEMPERATURE",
        "OPENAI_MAX_TOKENS",
        "OPENAI_TIMEOUT",
    ):
        monkeypatch.delenv(name, raising=False)


def test_resolve_model_explicit_wins(monkeypatch: pytest.MonkeyPatch) -> None:
    """显式模型优先于环境变量。"""
    monkeypatch.setenv("OPENAI_MODEL", "from-env")
    assert cfg._resolve_model("  my-model  ") == "my-model"


def test_resolve_model_env_then_default(monkeypatch: pytest.MonkeyPatch) -> None:
    """环境变量模型优先于默认模型。"""
    monkeypatch.setenv("OPENAI_MODEL", "from-env")
    assert cfg._resolve_model(None) == "from-env"
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    assert cfg._resolve_model(None) == cfg.DEFAULT_MODEL



def test_resolve_model_blank_explicit_falls_through(monkeypatch: pytest.MonkeyPatch) -> None:
    """explicit 为仅空白时视为「未提供有效显式值」，走 env/默认。"""
    monkeypatch.setenv("OPENAI_MODEL", "env-model")
    assert cfg._resolve_model("   ") == "env-model"


def test_resolve_temperature_explicit_env_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """显式温度优先于环境变量。"""
    assert cfg._resolve_temperature(0.7) == 0.7
    monkeypatch.setenv("OPENAI_TEMPERATURE", "0.9")
    assert cfg._resolve_temperature(None) == 0.9
    monkeypatch.delenv("OPENAI_TEMPERATURE", raising=False)
    assert cfg._resolve_temperature(None) == cfg.DEFAULT_TEMPERATURE


def test_resolve_max_tokens_and_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    """显式最大令牌数优先于环境变量。"""
    assert cfg._resolve_max_tokens(512) == 512
    monkeypatch.setenv("OPENAI_MAX_TOKENS", "256")
    assert cfg._resolve_max_tokens(None) == 256
    monkeypatch.delenv("OPENAI_MAX_TOKENS", raising=False)
    assert cfg._resolve_max_tokens(None) == cfg.DEFAULT_MAX_TOKENS

    assert cfg._resolve_timeout_sec(30.0) == 30.0
    monkeypatch.setenv("OPENAI_TIMEOUT", "90")
    assert cfg._resolve_timeout_sec(None) == 90.0
    monkeypatch.delenv("OPENAI_TIMEOUT", raising=False)
    assert cfg._resolve_timeout_sec(None) == cfg.DEFAULT_TIMEOUT_SEC