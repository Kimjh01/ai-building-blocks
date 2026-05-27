from __future__ import annotations

import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rag_doc_search.main import main


def test_basic() -> None:
    result = main()
    assert result["module"] == "02-rag-doc-search"
    assert result["package"] == "rag_doc_search"
    assert result["status"] == "ok"
