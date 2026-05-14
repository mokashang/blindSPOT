"""LLMClient implementation using claude-agent-sdk (Claude Code subscription)."""

from __future__ import annotations

import json
from typing import Any

from claude_agent_sdk import ClaudeAgentOptions, TextBlock, query

from blindspot.llm.base import LLMClient


class ClaudeAgentClient(LLMClient):
    async def complete(
        self,
        system: str,
        user: str,
        model: str = "claude-opus-4-7",
        max_tokens: int = 4096,
        json_schema: dict[str, Any] | None = None,
    ) -> str | dict[str, Any]:
        prompt = user
        if json_schema is not None:
            prompt = (
                user
                + "\n\nReturn ONLY valid JSON conforming to this schema:\n"
                + json.dumps(json_schema, indent=2)
            )

        opts = ClaudeAgentOptions(
            system_prompt=system,
            model=model,
            max_turns=1,
        )

        result_text = ""
        async for message in query(prompt=prompt, options=opts):
            for block in getattr(message, "content", []) or []:
                if isinstance(block, TextBlock):
                    result_text += block.text

        if json_schema is not None:
            return self._parse_json_response(result_text)
        return result_text

    @staticmethod
    def _parse_json_response(text: str) -> dict[str, Any]:
        # Tolerate JSON wrapped in markdown fences.
        text = text.strip()
        if text.startswith("```"):
            text = text.strip("`")
            if text.startswith("json\n"):
                text = text[len("json\n") :]
        return json.loads(text)
