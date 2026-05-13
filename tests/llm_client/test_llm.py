from __future__ import annotations

from unittest.mock import MagicMock

import httpx
import pytest
from openai import APIError

from src.llm_client import llm as llm_mod
from src.llm_client.exceptions import (
    LLMClientError,
    LLMConfigurationError,
    LLMEmptyAssistantContentError,
)


def test_missing_api_key_raises(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    """缺少 API 密钥时抛出异常。"""
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr("src.llm_client.client.load_dotenv_once", lambda: None)
    monkeypatch.setattr(llm_mod, "load_dotenv_once", lambda: None)

    with pytest.raises(LLMConfigurationError, match="OPENAI_API_KEY"):
        llm_mod.generate_answer([{"role": "user", "content": "hi"}])


def test_generate_answer_returns_stripped_content(monkeypatch: pytest.MonkeyPatch) -> None:
    """返回助手文本（strip 后）。"""
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")
    monkeypatch.setattr(llm_mod, "load_dotenv_once", lambda: None)

    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value = MagicMock(
        id="resp-1",
        choices=[MagicMock(message=MagicMock(content="  hello  "))],
    )
    monkeypatch.setattr(llm_mod, "get_openai_client", lambda: fake_client)

    out = llm_mod.generate_answer([{"role": "user", "content": "hi"}])
    assert out == "hello"
    fake_client.chat.completions.create.assert_called_once()
    _, kwargs = fake_client.chat.completions.create.call_args
    assert kwargs["messages"] == [{"role": "user", "content": "hi"}]
    assert "model" in kwargs


def test_generate_answer_maps_openai_api_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """create 抛出 APIError 时经 map_openai_exception 包装后抛出。"""
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")
    monkeypatch.setattr(llm_mod, "load_dotenv_once", lambda: None)

    api_err = APIError("boom", httpx.Request("GET", "http://localhost"), body=None)
    fake_client = MagicMock()
    fake_client.chat.completions.create.side_effect = api_err
    monkeypatch.setattr(llm_mod, "get_openai_client", lambda: fake_client)

    with pytest.raises(LLMClientError) as exc_info:
        llm_mod.generate_answer([{"role": "user", "content": "hi"}])
    assert exc_info.value.__cause__ is api_err


def test_generate_answer_raises_when_assistant_content_none(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """助手 message.content 为 None 时抛出 LLMEmptyAssistantContentError。"""
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")
    monkeypatch.setattr(llm_mod, "load_dotenv_once", lambda: None)

    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value = MagicMock(
        id="resp-empty",
        choices=[MagicMock(message=MagicMock(content=None))],
    )
    monkeypatch.setattr(llm_mod, "get_openai_client", lambda: fake_client)

    with pytest.raises(LLMEmptyAssistantContentError, match="content is None") as exc_info:
        llm_mod.generate_answer([{"role": "user", "content": "hi"}])
    assert exc_info.value.response_id == "resp-empty"