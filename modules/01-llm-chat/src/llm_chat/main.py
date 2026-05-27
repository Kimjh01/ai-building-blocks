from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

MODULE_NAME = "01-llm-chat"
PACKAGE_NAME = "llm_chat"
MODULE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = MODULE_DIR / "data" / "output"
DEFAULT_HISTORY_PATH = DEFAULT_OUTPUT_DIR / "chat_history.json"
DEFAULT_RESULT_PATH = DEFAULT_OUTPUT_DIR / "last_response.json"


def _bootstrap_shared_path() -> None:
    repo_root = Path(__file__).resolve().parents[4]
    shared_src = repo_root / "shared" / "src"
    if shared_src.exists() and str(shared_src) not in sys.path:
        sys.path.insert(0, str(shared_src))


_bootstrap_shared_path()

from ai_shared.config import get_env, load_env
from ai_shared.file_utils import ensure_dir
from ai_shared.json_utils import read_json, write_json
from ai_shared.logger import get_logger

from .client import OpenAICompatibleChatClient


@dataclass
class ChatSettings:
    api_key: str
    base_url: str
    model: str
    system_prompt: str
    default_message: str
    temperature: float
    history_path: Path
    result_path: Path
    save_history: bool
    log_level: str


def _resolve_path(raw_path: str | Path | None, default_path: Path) -> Path:
    if raw_path is None:
        return default_path

    path = Path(raw_path)
    if path.is_absolute():
        return path
    return MODULE_DIR / path


def _parse_bool(value: str | bool | None, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def load_settings() -> ChatSettings:
    load_env(MODULE_DIR / ".env")

    return ChatSettings(
        api_key=get_env("OPENAI_API_KEY", default="") or "",
        base_url=get_env("OPENAI_BASE_URL", default="https://api.openai.com/v1") or "https://api.openai.com/v1",
        model=get_env("OPENAI_MODEL", default="gpt-4.1-mini") or "gpt-4.1-mini",
        system_prompt=get_env("SYSTEM_PROMPT", default="You are a helpful AI assistant.") or "You are a helpful AI assistant.",
        default_message=get_env("CHAT_MESSAGE", default="안녕하세요. 이 모듈을 어떻게 확장하면 좋을까요?") or "안녕하세요. 이 모듈을 어떻게 확장하면 좋을까요?",
        temperature=float(get_env("CHAT_TEMPERATURE", default="0.2") or "0.2"),
        history_path=_resolve_path(get_env("CHAT_HISTORY_PATH", default="data/output/chat_history.json"), DEFAULT_HISTORY_PATH),
        result_path=_resolve_path(get_env("CHAT_RESULT_PATH", default="data/output/last_response.json"), DEFAULT_RESULT_PATH),
        save_history=_parse_bool(get_env("CHAT_SAVE_HISTORY", default="true"), True),
        log_level=get_env("LOG_LEVEL", default="INFO") or "INFO",
    )


def load_history(history_path: Path) -> list[dict[str, str]]:
    if not history_path.exists():
        return []

    raw = read_json(history_path)
    if isinstance(raw, dict):
        raw = raw.get("messages", [])

    if not isinstance(raw, list):
        return []

    messages: list[dict[str, str]] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        role = str(item.get("role", "")).strip()
        content = str(item.get("content", "")).strip()
        if role and content:
            messages.append({"role": role, "content": content})
    return messages


def trim_history(history: list[dict[str, str]], max_messages: int = 10) -> list[dict[str, str]]:
    if len(history) <= max_messages:
        return history
    return history[-max_messages:]


def build_messages(
    system_prompt: str,
    history: list[dict[str, str]],
    user_message: str,
) -> list[dict[str, str]]:
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_message})
    return messages


def render_dry_run_reply(user_message: str, model: str, history_size: int) -> str:
    return (
        "[dry-run] API 키가 없어 실제 호출 대신 입력만 확인했습니다. "
        f"model={model}, history_messages={history_size}, user_message={user_message}"
    )


def persist_outputs(
    result: dict[str, Any],
    result_path: Path,
    history: list[dict[str, str]] | None,
    history_path: Path | None,
) -> None:
    ensure_dir(result_path.parent)
    write_json(result_path, result)

    if history is not None and history_path is not None:
        ensure_dir(history_path.parent)
        write_json(history_path, history)


def main(
    message: str | None = None,
    system_prompt: str | None = None,
    history_path: str | Path | None = None,
    result_path: str | Path | None = None,
    dry_run: bool | None = None,
    save_history: bool | None = None,
    reset_history: bool = False,
) -> dict[str, Any]:
    settings = load_settings()
    logger = get_logger(PACKAGE_NAME, level=settings.log_level)

    user_message = message or settings.default_message
    active_system_prompt = system_prompt or settings.system_prompt
    active_history_path = _resolve_path(history_path, settings.history_path)
    active_result_path = _resolve_path(result_path, settings.result_path)
    should_save_history = settings.save_history if save_history is None else save_history

    history = [] if reset_history else load_history(active_history_path)
    request_messages = build_messages(active_system_prompt, history, user_message)
    effective_dry_run = (not settings.api_key) if dry_run is None else dry_run

    logger.info("Running %s with model=%s dry_run=%s", MODULE_NAME, settings.model, effective_dry_run)

    raw_response: dict[str, Any]
    if effective_dry_run:
        assistant_text = render_dry_run_reply(user_message, settings.model, len(history))
        raw_response = {"dry_run": True, "reason": "OPENAI_API_KEY is missing or dry-run was requested."}
        status = "ok"
    else:
        try:
            client = OpenAICompatibleChatClient(
                api_key=settings.api_key,
                base_url=settings.base_url,
                model=settings.model,
            )
            assistant_text, raw_response = client.create_chat_completion(
                messages=request_messages,
                temperature=settings.temperature,
            )
            status = "ok"
        except Exception as error:
            assistant_text = f"LLM 호출 실패: {error}"
            raw_response = {"error": str(error)}
            status = "error"
            logger.exception("Chat completion failed")

    assistant_message = {"role": "assistant", "content": assistant_text}
    updated_history = trim_history(history + [{"role": "user", "content": user_message}, assistant_message])

    result = {
        "module": MODULE_NAME,
        "package": PACKAGE_NAME,
        "status": status,
        "dry_run": effective_dry_run,
        "input": {
            "user_message": user_message,
            "system_prompt": active_system_prompt,
        },
        "assistant": assistant_message,
        "history_size": len(updated_history),
        "settings": {
            "base_url": settings.base_url,
            "model": settings.model,
            "temperature": settings.temperature,
            "save_history": should_save_history,
        },
        "output_files": {
            "history_path": str(active_history_path),
            "result_path": str(active_result_path),
        },
        "raw_response": raw_response,
    }

    persist_outputs(
        result=result,
        result_path=active_result_path,
        history=updated_history if should_save_history else None,
        history_path=active_history_path if should_save_history else None,
    )
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the reusable 01-llm-chat module.")
    parser.add_argument("--message", help="사용자 메시지")
    parser.add_argument("--system", dest="system_prompt", help="시스템 프롬프트")
    parser.add_argument("--history-path", help="히스토리 JSON 파일 경로")
    parser.add_argument("--result-path", help="결과 JSON 파일 경로")
    parser.add_argument("--dry-run", action="store_true", help="실제 API 호출 없이 실행")
    parser.add_argument("--no-save-history", action="store_true", help="대화 히스토리를 저장하지 않음")
    parser.add_argument("--reset-history", action="store_true", help="기존 히스토리를 무시하고 새로 시작")
    return parser


def cli(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    result = main(
        message=args.message,
        system_prompt=args.system_prompt,
        history_path=args.history_path,
        result_path=args.result_path,
        dry_run=args.dry_run,
        save_history=not args.no_save_history,
        reset_history=args.reset_history,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(cli())
