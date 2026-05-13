from pathlib import Path

from src.chunking.export import write_chunks_jsonl
from src.chunking.pipeline import build_chunks_from_directory


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    kb_dir = repo_root / "knowledge_base"
    out_path = repo_root / "artifacts" / "kb_chunks.jsonl"

    chunks = build_chunks_from_directory(kb_dir)
    write_chunks_jsonl(chunks, out_path)
    print(f"wrote {len(chunks)} rows -> {out_path}")


if __name__ == "__main__":
    main()