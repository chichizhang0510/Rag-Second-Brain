from pathlib import Path

from src.cli.context import context_from_args
from src.cli.parser import build_parser


def test_context_kb_default(tmp_path: Path) -> None:
    p = build_parser()
    ns = p.parse_args(["--question", "q"])
    repo = tmp_path
    ctx = context_from_args(ns, repo_root=repo)
    assert ctx.kb_dir == (repo / "knowledge_base").resolve()
    assert ctx.query == "q"