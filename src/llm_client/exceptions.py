"""Domain exceptions for llm_client (RAG Generation layer)."""


from __future__ import annotations

from openai import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    AuthenticationError,
    RateLimitError,
)


class LLMClientError(Exception):
    """本包对外统一的异常基类。消息应对用户/日志安全（勿包含 API Key）。"""

    def __init__(self, message: str, *, detail: str | None = None) -> None:
        super().__init__(message)
        self.detail = detail  # 可选：附加说明（仍勿写入密钥）


class LLMConfigurationError(LLMClientError):
    """本地配置问题：例如未设置 OPENAI_API_KEY。"""


class LLMEmptyAssistantContentError(LLMClientError):
    """模型返回了 choice，但 assistant 消息正文为空（content is None）。"""

    def __init__(self, message: str, *, response_id: str = "") -> None:
        super().__init__(message)
        self.response_id = response_id


def map_openai_exception(exc: BaseException) -> LLMClientError:
    """把常见 OpenAI SDK 失败映射为 LLMClientError；调用方应 ``raise map_openai_exception(e) from e``。"""
    if isinstance(exc, AuthenticationError):
        return LLMClientError(
            "Authentication failed: check OPENAI_API_KEY and OPENAI_BASE_URL.",
            detail=str(exc),
        )
    if isinstance(exc, RateLimitError):
        return LLMClientError("Rate limited by the API; retry later.", detail=str(exc))
    if isinstance(exc, APITimeoutError):
        return LLMClientError("Request timed out; try increasing OPENAI_TIMEOUT.", detail=str(exc))
    if isinstance(exc, APIConnectionError):
        return LLMClientError(
            "Could not reach the API; check network, proxy, or OPENAI_BASE_URL.",
            detail=str(exc),
        )
    if isinstance(exc, APIError):
        return LLMClientError("OpenAI API request failed.", detail=str(exc))
    return LLMClientError("Unexpected error while calling the language model.", detail=str(exc))
