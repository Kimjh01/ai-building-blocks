from __future__ import annotations

import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv


def load_env(env_path: str | os.PathLike[str] | None = None, override: bool = False) -> None:
    """Load environment variables from a .env file when available."""
    if env_path is not None:
        load_dotenv(dotenv_path=Path(env_path), override=override)
        return

    discovered = find_dotenv(usecwd=True)
    if discovered:
        load_dotenv(discovered, override=override)


def get_env(key: str, default: str | None = None, required: bool = False) -> str | None:
    """Return an environment variable value, optionally enforcing presence."""
    load_env()
    value = os.getenv(key, default)
    if required and not value:
        raise ValueError(f"Required environment variable is missing: {key}")
    return value
