from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

import src.llm_client.client as client_mod
from src.llm_client.exceptions import LLMConfigurationError


@pytest.fixture(autouse=True)
def reset_client_dotenv_flag() -> None:
    """重置客户端环境变量标志。"""
    client_mod._DOTENV_LOADED = False
    yield
    client_mod._DOTENV_LOADED = False


def test_load_dotenv_once_loads_first_time_only(monkeypatch: pytest.MonkeyPatch) -> None:
    """首次加载环境变量。"""
    calls: list[int] = []
    monkeypatch.setattr(client_mod, "load_dotenv", lambda *a, **k: calls.append(1))
    client_mod._DOTENV_LOADED = False
    client_mod.load_dotenv_once()
    assert calls == [1]
    assert client_mod._DOTENV_LOADED is True
    client_mod.load_dotenv_once()
    assert calls == [1]


def test_require_api_key_raises_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """缺少 API 密钥时抛出异常。"""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(client_mod, "load_dotenv_once", lambda: None)
    with pytest.raises(LLMConfigurationError, match="OPENAI_API_KEY"):
        client_mod._require_api_key()


def test_require_api_key_returns_key(monkeypatch: pytest.MonkeyPatch) -> None:
    """返回 API 密钥。"""
    monkeypatch.setenv("OPENAI_API_KEY", " sk-secret ")
    monkeypatch.setattr(client_mod, "load_dotenv_once", lambda: None)
    assert client_mod._require_api_key() == "sk-secret"


@patch("src.llm_client.client.OpenAI")
def test_get_openai_client_base_url_none_when_unset(
    mock_openai: MagicMock, monkeypatch: pytest.MonkeyPatch
) -> None:
    """基础 URL 为空时设置为 None。"""
    monkeypatch.setenv("OPENAI_API_KEY", "sk-x")
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    mock_openai.return_value = MagicMock()

    monkeypatch.setattr(client_mod, "load_dotenv_once", lambda: None) # 设置 load_dotenv_once 为 None。
    client_mod.get_openai_client()
    mock_openai.assert_called_once_with(api_key="sk-x", base_url=None)


@patch("src.llm_client.client.OpenAI")
def test_get_openai_client_passes_base_url(
    mock_openai: MagicMock, monkeypatch: pytest.MonkeyPatch
) -> None:
    """基础 URL 不为空时设置为基础 URL。"""
    monkeypatch.setenv("OPENAI_API_KEY", "sk-x")
    monkeypatch.setenv("OPENAI_BASE_URL", " https://gateway.example/v1 ")
    mock_openai.return_value = MagicMock()
    client_mod.get_openai_client()
    mock_openai.assert_called_once_with(
        api_key="sk-x", base_url="https://gateway.example/v1"
    )