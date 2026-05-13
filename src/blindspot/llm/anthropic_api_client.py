"""LLMClient implementation using the Anthropic API directly.

Production backend. Requires ANTHROPIC_API_KEY env var.
"""

from __future__ import annotations

import os
from typing import Any

from anthropic import AsyncAnthropic

from blindspot.llm.base import LLMClient


class AnthropicAPIClient(LLMClient):
    def __init__(self, api_key: str | None = None):
        self._client = AsyncAnthropic(api_key=api_key or os.environ["ANTHROPIC_API_KEY"])

    async def complete(
        self,
        system: str,
        user: str,
        model: str = "claude-opus-4-7",
        max_tokens: int = 4096,
        json_schema: dict[str, Any] | None = None,
    ) -> str | dict[str, Any]:
        if json_schema is not None:
            tool = {
                "name": "respond_structured",
                "description": "Return the response in the required schema.",
                "input_schema": json_schema,
            }
            resp = await self._client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                tools=[tool],
                tool_choice={"type": "tool", "name": "respond_structured"},
                messages=[{"role": "user", "content": user}],
            )
            for block in resp.content:
                if block.type == "tool_use":
                    return block.input
            raise RuntimeError("Model did not produce structured output")

        resp = await self._client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        out = ""
        for block in resp.content:
            if block.type == "text":
                out += block.text
        return out
