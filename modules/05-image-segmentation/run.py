from __future__ import annotations

import sys
from pathlib import Path
from pprint import pprint

SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from image_segmentation.main import main


if __name__ == "__main__":
    pprint(main())
