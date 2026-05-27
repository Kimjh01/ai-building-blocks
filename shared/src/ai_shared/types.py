from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

try:
    from pydantic import BaseModel, Field
except ModuleNotFoundError:
    BaseModel = None
    Field = None


if BaseModel is not None and Field is not None:

    class ResponseModel(BaseModel):
        success: bool = True
        message: str = "ok"
        data: dict[str, Any] = Field(default_factory=dict)

else:

    @dataclass
    class ResponseModel:
        success: bool = True
        message: str = "ok"
        data: dict[str, Any] = field(default_factory=dict)

        def model_dump(self) -> dict[str, Any]:
            return asdict(self)
