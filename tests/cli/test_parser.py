import pytest

from src.cli.parser import build_parser


def test_parser_question_required() -> None:
    p = build_parser()
    args = p.parse_args(["--question", "hi"])
    assert args.question == "hi"


def test_parser_defaults() -> None:
    p = build_parser()
    args = p.parse_args(["--question", "x"])
    assert args.top_k == 5
    assert args.language == "en"


def test_parser_missing_question_maps_to_exit_code_1() -> None:
    """触发自定义 _ArgParser.error → sys.exit(1)。"""
    with pytest.raises(SystemExit) as ei:
        build_parser().parse_args([])
    assert ei.value.code == 1