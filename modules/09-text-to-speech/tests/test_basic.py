from __future__ import annotations

import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from text_to_speech.main import main


def test_basic() -> None:
    result = main()
    assert result["module"] == "09-text-to-speech"
    assert result["package"] == "text_to_speech"
    assert result["status"] == "ok"
