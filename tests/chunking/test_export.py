import json
from pathlib import Path

from src.chunking.export import write_chunks_jsonl
from src.chunking.split import split_markdown_file

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def test_write_chunks_jsonl_emits_one_json_per_chunk(tmp_path: Path) -> None:
    chunks = split_markdown_file(FIXTURES / "chunking_two_h1.md")
    out_path = tmp_path / "chunks.jsonl"
    write_chunks_jsonl(chunks, out_path)

    lines = out_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == len(chunks)

    row = json.loads(lines[0])
    assert {"chunk_id", "source", "heading_path", "text"} <= set(row.keys())