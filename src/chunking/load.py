from pathlib import Path

def iter_markdown_files(kb_dir: Path) -> list[Path]:
    """
    Iterate over all markdown files in the knowledge base directory.

    Args:
        kb_dir: The knowledge base directory to iterate over.

    Returns:
        A list of paths to the markdown files.
    """
    if not kb_dir.is_dir():
        raise FileNotFoundError(f"Knowledge base directory not found: {kb_dir}")
    
    # 遍历所有 markdown 文件，并返回排序后的路径列表
    # rglob 表示递归遍历子目录
    # - 如果目录下有子目录，则递归遍历子目录
    # - 如果目录下没有子目录，则返回空列表
    paths = sorted(p for p in kb_dir.rglob("*.md") if p.is_file())
    return paths