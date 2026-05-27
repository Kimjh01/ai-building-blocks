from __future__ import annotations

import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from three_d_reconstruction_helper.main import main


def test_basic() -> None:
    result = main()
    assert result["module"] == "16-3d-reconstruction-helper"
    assert result["package"] == "three_d_reconstruction_helper"
    assert result["status"] == "ok"
