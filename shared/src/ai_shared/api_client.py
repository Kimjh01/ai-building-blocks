from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any


class BaseAPIClient:
    """Minimal JSON-oriented API client that can be extended per module."""

    def __init__(self, base_url: str, headers: dict[str, str] | None = None, timeout: int = 30) -> None:
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.timeout = timeout

    def _request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        body = json.dumps(payload).encode("utf-8") if payload is not None else None
        request = urllib.request.Request(url=url, data=body, method=method.upper())

        for key, value in self.headers.items():
            request.add_header(key, value)

        if body is not None:
            request.add_header("Content-Type", "application/json")

        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as error:
            raw = error.read().decode("utf-8", errors="ignore")
            return {
                "status": "error",
                "code": error.code,
                "message": raw or error.reason,
            }

    def get(self, path: str) -> dict[str, Any]:
        return self._request("GET", path)

    def post(self, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._request("POST", path, payload=payload)
