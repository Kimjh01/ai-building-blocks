from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from llm_chat.main import main


def test_basic() -> None:
    result = main(dry_run=True, save_history=False, reset_history=True)
    assert result["module"] == "01-llm-chat"
    assert result["package"] == "llm_chat"
    assert result["status"] == "ok"
    assert result["dry_run"] is True
    assert result["assistant"]["role"] == "assistant"


def test_history_and_result_files_are_created() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        history_path = Path(temp_dir) / "chat_history.json"
        result_path = Path(temp_dir) / "last_response.json"
        message = "test message"

        result = main(
            message=message,
            history_path=history_path,
            result_path=result_path,
            dry_run=True,
            save_history=True,
            reset_history=True,
        )

        assert result["status"] == "ok"
        assert history_path.exists()
        assert result_path.exists()

        history = json.loads(history_path.read_text(encoding="utf-8"))
        saved_result = json.loads(result_path.read_text(encoding="utf-8"))

        assert len(history) == 2
        assert history[0]["role"] == "user"
        assert history[0]["content"] == message
        assert saved_result["module"] == "01-llm-chat"
