from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any


class OpenAICompatibleChatClient:
    def __init__(self, api_key: str, base_url: str, model: str, timeout: int = 60) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def create_chat_completion(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.2,
    ) -> tuple[str, dict[str, Any]]:
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }
        request = urllib.request.Request(
            url=f"{self.base_url}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            method="POST",
        )
        request.add_header("Authorization", f"Bearer {self.api_key}")
        request.add_header("Content-Type", "application/json")

        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                raw_response = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"HTTP {error.code}: {body or error.reason}") from error
        except urllib.error.URLError as error:
            raise RuntimeError(f"Network error: {error.reason}") from error

        content = self._extract_content(raw_response)
        if not content:
            raise RuntimeError("No assistant message content found in API response.")
        return content, raw_response

    @staticmethod
    def _extract_content(raw_response: dict[str, Any]) -> str:
        choices = raw_response.get("choices") or []
        if not choices:
            return ""

        message = choices[0].get("message") or {}
        content = message.get("content")
        if isinstance(content, str):
            return content

        if isinstance(content, list):
            text_parts: list[str] = []
            for item in content:
                if not isinstance(item, dict):
                    continue
                text_value = item.get("text")
                if isinstance(text_value, str):
                    text_parts.append(text_value)
            return "\n".join(text_parts).strip()

        return ""
