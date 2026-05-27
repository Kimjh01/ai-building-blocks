from __future__ import annotations

from pathlib import Path


def ensure_dir(path: str | Path) -> Path:
    """Create the directory if it does not exist and return the resolved path."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Read a text file with UTF-8 by default."""
    return Path(path).read_text(encoding=encoding)


def write_text(path: str | Path, content: str, encoding: str = "utf-8") -> Path:
    """Write text content and create parent directories when needed."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding=encoding)
    return file_path
