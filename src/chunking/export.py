"""
Write chunks to a jsonl file.
"""

import json
from pathlib import Path

from src.chunking.types import Chunk

def write_chunks_jsonl(chunks: list[Chunk], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for c in chunks:
            row = {
                "chunk_id": c.chunk_id,
                "source": c.source,
                "heading_path": c.heading_path,
                "text": c.text,
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")