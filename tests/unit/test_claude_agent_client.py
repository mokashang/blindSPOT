import pytest

from claude_agent_sdk import AssistantMessage, TextBlock

from blindspot.llm.claude_agent_client import ClaudeAgentClient


def test_parse_json_response_plain():
    out = ClaudeAgentClient._parse_json_response('{"a": 1}')
    assert out == {"a": 1}


def test_parse_json_response_fenced():
    out = ClaudeAgentClient._parse_json_response('```json\n{"a": 1}\n```')
    assert out == {"a": 1}


def test_parse_json_response_invalid_raises():
    with pytest.raises(Exception):
        ClaudeAgentClient._parse_json_response("not json")


async def test_complete_extracts_only_textblock_content(monkeypatch):
    """complete() reads text from AssistantMessage TextBlocks only.

    Mirrors the documented claude-agent-sdk pattern (isinstance message /
    block checks). Regressions guarded:
    - TextBlock has no `type` attr, so the old `block.type == "text"`
      guard matched nothing and complete() returned "".
    - non-AssistantMessage frames (SystemMessage, ResultMessage, ...) must
      be skipped even if they carry a `content` attribute.
    """

    class NotAText:
        text = "SHOULD NOT APPEAR"

    class NotAnAssistantMessage:  # a SystemMessage-like frame
        content = [TextBlock(text="SHOULD NOT APPEAR")]

    async def fake_query(*, prompt, options):
        yield NotAnAssistantMessage()
        yield AssistantMessage(
            content=[NotAText(), TextBlock(text="hel"), TextBlock(text="lo")],
            model="claude-opus-4-7",
        )

    monkeypatch.setattr("blindspot.llm.claude_agent_client.query", fake_query)

    out = await ClaudeAgentClient().complete(system="sys", user="hi")
    assert out == "hello"


async def test_complete_json_schema_path_parses_textblock(monkeypatch):
    """The json_schema path must parse text accumulated from TextBlocks."""

    async def fake_query(*, prompt, options):
        yield AssistantMessage(
            content=[TextBlock(text='{"answer": 42}')],
            model="claude-opus-4-7",
        )

    monkeypatch.setattr("blindspot.llm.claude_agent_client.query", fake_query)

    out = await ClaudeAgentClient().complete(
        system="sys", user="hi", json_schema={"type": "object"}
    )
    assert out == {"answer": 42}
