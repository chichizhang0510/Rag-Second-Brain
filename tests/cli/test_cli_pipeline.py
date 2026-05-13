from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.cli.context import AskContext
from src.cli.pipeline import run_ask
from src.retrieve.types import RetrievalHit


def test_run_ask_empty_question_returns_1(tmp_path: Path) -> None:
    kb = tmp_path / "kb"
    kb.mkdir()
    ctx = AskContext(
        kb_dir=kb,
        query="q",
        question="",
        top_k=5,
        language="en",
        model=None,
        temperature=None,
        max_tokens=None,
        debug=False,
        dry_run=True,
    )
    assert run_ask(ctx) == 1


def test_run_ask_invalid_kb_dir(tmp_path: Path) -> None:
    bad = tmp_path / "nope"
    ctx = AskContext(
        kb_dir=bad,
        query="q",
        question="q",
        top_k=5,
        language="en",
        model=None,
        temperature=None,
        max_tokens=None,
        debug=False,
        dry_run=True,
    )
    assert run_ask(ctx) == 2


@patch("src.cli.pipeline.retrieve_from_directory", return_value=[])
@patch("src.cli.pipeline.build_messages", return_value=[{"role": "user", "content": "x"}])
def test_run_ask_dry_run(_bm: MagicMock, _rv: MagicMock, tmp_path: Path) -> None:
    kb = tmp_path / "kb"
    kb.mkdir()
    ctx = AskContext(
        kb_dir=kb,
        query="q",
        question="q",
        top_k=3,
        language="en",
        model=None,
        temperature=None,
        max_tokens=None,
        debug=False,
        dry_run=True,
    )
    assert run_ask(ctx) == 0


@patch("src.cli.pipeline.generate_answer", return_value="  ok  ")
@patch("src.cli.pipeline.build_messages", return_value=[{"role": "user", "content": "x"}])
@patch(
    "src.cli.pipeline.retrieve_from_directory",
    return_value=[
        RetrievalHit(
            chunk_id="c1",
            source="src.md",
            heading="h",
            heading_path="/a/b",
            text="body",
            score=0.42,
        ),
    ],
)
def test_run_ask_debug_and_llm_path(
    _rv: MagicMock,
    _bm: MagicMock,
    _ga: MagicMock,
    tmp_path: Path,
    capsys,
) -> None:
    kb = tmp_path / "kb"
    kb.mkdir()
    ctx = AskContext(
        kb_dir=kb,
        query="q",
        question="why?",
        top_k=2,
        language="en",
        model="gpt-test",
        temperature=0.1,
        max_tokens=16,
        debug=True,
        dry_run=False,
    )
    assert run_ask(ctx) == 0
    captured = capsys.readouterr()
    assert "hits: 1" in captured.err
    assert "score=" in captured.err
    assert captured.out.strip() == "ok"
    _ga.assert_called_once()