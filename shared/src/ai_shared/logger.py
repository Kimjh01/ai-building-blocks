from __future__ import annotations

import logging


def get_logger(name: str = "ai_shared", level: int | str = logging.INFO) -> logging.Logger:
    """Create a stream logger with a single shared handler."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    resolved_level = getattr(logging, level.upper(), logging.INFO) if isinstance(level, str) else level
    logger.setLevel(resolved_level)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))

    logger.addHandler(handler)
    logger.propagate = False
    return logger
