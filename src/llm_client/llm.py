"""Call Chat Completions (OpenAI-compatible SDK)."""


from src.llm_client.client import get_openai_client, load_dotenv_once
from src.llm_client.config import (
    _resolve_max_tokens,
    _resolve_model,
    _resolve_temperature,
    _resolve_timeout_sec,
)
from openai import APIError
from src.llm_client.exceptions import map_openai_exception, LLMEmptyAssistantContentError

def generate_answer(
    messages: list[dict[str, str]],
    *,
    model: str | None = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
    timeout_sec: float | None = None,
) -> str:
    """
    调用 Chat Completions，返回助手文本（strip 后）。

    不向调用方吞掉 SDK 异常；由上层 CLI 捕获并决定 exit code。
    """
    load_dotenv_once() # 加载环境变量。
    client = get_openai_client() # 获取 OpenAI 客户端。
    model_f = _resolve_model(model) # 解析模型。
    temperature_f = _resolve_temperature(temperature) # 解析温度。
    max_tokens_i = _resolve_max_tokens(max_tokens) # 解析最大令牌数。
    timeout_f = _resolve_timeout_sec(timeout_sec) # 解析超时时间。

    try:
        response = client.chat.completions.create(
            model=model_f,
            messages=messages,
            temperature=temperature_f,
            max_tokens=max_tokens_i,
            timeout=timeout_f,
        )
    except APIError as e:
        raise map_openai_exception(e) from e

    content: str | None = response.choices[0].message.content
    if content is None: # 如果内容为空，则抛出 RuntimeError 异常。
        rid = getattr(response, "id", "") # 获取响应 ID。
        raise LLMEmptyAssistantContentError(
            "Assistant message content is None (empty).",
            response_id=rid,
        )
    return content.strip() # 返回助手文本（strip 后）。