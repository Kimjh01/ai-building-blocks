from __future__ import annotations

import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from vector_db_template.main import main


def test_basic() -> None:
    result = main()
    assert result["module"] == "14-vector-db-template"
    assert result["package"] == "vector_db_template"
    assert result["status"] == "ok"
