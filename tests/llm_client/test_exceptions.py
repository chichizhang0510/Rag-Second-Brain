from __future__ import annotations

from unittest.mock import MagicMock

import httpx
import pytest
from openai import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    AuthenticationError,
    RateLimitError,
)

from src.llm_client.exceptions import LLMClientError, map_openai_exception


def _auth_err() -> AuthenticationError:
    return AuthenticationError(
        "auth", response=MagicMock(), body=None
    )


def _rate_err() -> RateLimitError:
    return RateLimitError("rl", response=MagicMock(), body=None)


def _timeout_err() -> APITimeoutError:
    return APITimeoutError(request=httpx.Request("GET", "http://localhost"))


def _conn_err() -> APIConnectionError:
    return APIConnectionError(
        message="conn", request=httpx.Request("GET", "http://localhost")
    )


def _generic_api_err() -> APIError:
    return APIError(
        "api", httpx.Request("GET", "http://localhost"), body=None
    )


@pytest.mark.parametrize(  # 参数化测试。
    "exc,expected_substr",
    [
        (_auth_err(), "Authentication failed"),
        (_rate_err(), "Rate limited"),
        (_timeout_err(), "timed out"),
        (_conn_err(), "Could not reach"),
        (_generic_api_err(), "OpenAI API request failed"),
        (ValueError("nope"), "Unexpected error"),
    ],
)
def test_map_openai_exception_branches(exc: object, expected_substr: str) -> None:
    """映射 OpenAI 异常。"""
    out = map_openai_exception(exc)
    assert isinstance(out, LLMClientError)
    assert expected_substr in str(out)
    assert getattr(out, "detail", None) is not None