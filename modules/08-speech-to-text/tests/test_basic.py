from __future__ import annotations

import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from speech_to_text.main import main


def test_basic() -> None:
    result = main()
    assert result["module"] == "08-speech-to-text"
    assert result["package"] == "speech_to_text"
    assert result["status"] == "ok"
