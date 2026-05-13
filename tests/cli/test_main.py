import importlib
import sys
from unittest.mock import MagicMock

import pytest

from src.cli.main import main
from src.llm_client.exceptions import LLMClientError, LLMConfigurationError


def test_main_dry_run_zero_exit(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    kb = tmp_path / "knowledge_base"
    kb.mkdir()
    with pytest.raises(SystemExit) as ei:
        main(["--question", "hi", "--dry-run"])
    assert ei.value.code == 0


def test_main_missing_question_propagates_exit_1(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    kb = tmp_path / "knowledge_base"
    kb.mkdir()
    with pytest.raises(SystemExit) as ei:
        main([])
    assert ei.value.code == 1


def test_main_llm_configuration_maps_to_exit_2(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    kb = tmp_path / "knowledge_base"
    kb.mkdir()

    def boom(_ctx):
        raise LLMConfigurationError("no key", detail="detail-line")

    monkeypatch.setattr("src.cli.main.run_ask", boom)
    with pytest.raises(SystemExit) as ei:
        main(["--question", "x", "--dry-run"])
    assert ei.value.code == 2


def test_main_llm_client_maps_to_exit_3(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    kb = tmp_path / "knowledge_base"
    kb.mkdir()

    def boom(_ctx):
        raise LLMClientError("api failed", detail="more")

    monkeypatch.setattr("src.cli.main.run_ask", boom)
    with pytest.raises(SystemExit) as ei:
        main(["--question", "x", "--dry-run"])
    assert ei.value.code == 3


def test_main_unexpected_exception_maps_to_exit_1(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    kb = tmp_path / "knowledge_base"
    kb.mkdir()

    def boom(_ctx):
        raise RuntimeError("bug")

    monkeypatch.setattr("src.cli.main.run_ask", boom)
    with pytest.raises(SystemExit) as ei:
        main(["--question", "x", "--dry-run"])
    assert ei.value.code == 1


def test_main_llm_client_without_detail_maps_to_exit_3(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    kb = tmp_path / "knowledge_base"
    kb.mkdir()

    def boom(_ctx):
        raise LLMClientError("no detail kwarg")

    monkeypatch.setattr("src.cli.main.run_ask", boom)
    with pytest.raises(SystemExit) as ei:
        main(["--question", "x", "--dry-run"])
    assert ei.value.code == 3


def test_cli_dunder_main_invokes_main(monkeypatch) -> None:
    mock = MagicMock()
    import src.cli.main as cli_main_module

    monkeypatch.setattr(cli_main_module, "main", mock)
    sys.modules.pop("src.cli.__main__", None)
    importlib.import_module("src.cli.__main__")
    mock.assert_called_once_with()
