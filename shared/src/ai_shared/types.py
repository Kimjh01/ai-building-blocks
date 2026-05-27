from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    success: bool = True
    message: str = "ok"
    data: dict[str, Any] = Field(default_factory=dict)
