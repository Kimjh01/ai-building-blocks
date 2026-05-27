from __future__ import annotations

import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from ai_evaluation.main import main


def test_basic() -> None:
    result = main()
    assert result["module"] == "15-ai-evaluation"
    assert result["package"] == "ai_evaluation"
    assert result["status"] == "ok"
