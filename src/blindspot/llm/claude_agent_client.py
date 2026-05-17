"""LLMClient implementation using claude-agent-sdk (Claude Code subscription)."""

from __future__ import annotations

import json
from typing import Any

from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, TextBlock, query

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

        # Pure text completion: blindspot's agents are text-in / JSON-out.
        # tools=[] strips the SDK's default built-in tools and
        # strict_mcp_config=True ignores the account's claude.ai MCP servers
        # — otherwise the model can spend its single turn on a tool call and
        # the run dies with "Reached maximum number of turns (1)".
        opts = ClaudeAgentOptions(
            system_prompt=system,
            model=model,
            max_turns=1,
            tools=[],
            strict_mcp_config=True,
        )

        result_text = ""
        async for message in query(prompt=prompt, options=opts):
            if not isinstance(message, AssistantMessage):
                continue
            for block in message.content:
                if isinstance(block, TextBlock):
                    result_text += block.text

        if json_schema is not None:
            return self._parse_json_response(result_text)
        return result_text

    @staticmethod
    def _parse_json_response(text: str) -> dict[str, Any]:
        """Extract the first JSON object from a model response.

        Tolerates a leading ```json fence, prose before the object, and any
        trailing fence-close / commentary after it — models sometimes append
        explanation despite a "JSON only" instruction.

        On `raw_decode` failure, attempts one recovery: re-try with the
        substring ending at the LAST `}` in the buffer (handles cases where
        prose after the object somehow confuses `raw_decode`). If that also
        fails, raises ValueError with the FULL response text (truncated to
        2000 chars) so the failure is diagnosable upstream — the prior
        behaviour let JSONDecodeError propagate with no payload, leaving
        eval failures undebuggable.
        """
        original = text
        text = text.strip()
        if text.startswith("```"):
            newline = text.find("\n")
            if newline != -1:
                text = text[newline + 1 :]
        start = text.find("{")
        if start == -1:
            raise ValueError(
                f"no JSON object in model response: {_truncate(original)!r}"
            )
        try:
            obj, _ = json.JSONDecoder().raw_decode(text[start:])
            return obj
        except json.JSONDecodeError:
            # Recovery: trim back to the last closing brace and retry.
            last_close = text.rfind("}")
            if last_close > start:
                try:
                    obj, _ = json.JSONDecoder().raw_decode(
                        text[start : last_close + 1]
                    )
                    return obj
                except json.JSONDecodeError:
                    pass
            raise ValueError(
                f"could not parse JSON object from model response: "
                f"{_truncate(original)!r}"
            ) from None


def _truncate(text: str, limit: int = 2000) -> str:
    """Truncate text to `limit` chars, appending an ellipsis marker if cut."""
    if len(text) <= limit:
        return text
    return text[:limit] + f"...[truncated {len(text) - limit} chars]"
