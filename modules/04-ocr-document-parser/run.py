from __future__ import annotations

import sys
from pathlib import Path
from pprint import pprint

SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from ocr_document_parser.main import main


if __name__ == "__main__":
    pprint(main())
