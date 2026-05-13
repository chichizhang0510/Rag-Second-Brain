from src.retrieve.tokenize import tokenize


def test_tokenize_mixed_text() -> None:
    toks = tokenize("Fibonacci 记忆化 DP")
    assert "fibonacci" in toks
    assert "dp" in toks
    assert "记" in toks and "忆" in toks