from __future__ import annotations

import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TARGET_DIR_NAMES = {"__pycache__", ".pytest_cache", ".ipynb_checkpoints"}


def find_cache_dirs(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_dir() and path.name in TARGET_DIR_NAMES
    )


def main() -> int:
    removed = 0
    for path in find_cache_dirs(REPO_ROOT):
        shutil.rmtree(path, ignore_errors=True)
        print(f"Removed: {path}")
        removed += 1

    print(f"Done. Removed {removed} cache directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
