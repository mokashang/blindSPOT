import pytest

from claude_agent_sdk import TextBlock

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
    """complete() concatenates TextBlock text and ignores non-text blocks.

    Regression: claude-agent-sdk's TextBlock dataclass has no `type`
    attribute, so the old `block.type == "text"` guard matched nothing —
    complete() returned "" and json.loads() blew up one frame up.
    """

    class NotAText:
        text = "SHOULD NOT APPEAR"

    class FakeAssistantMessage:
        content = [NotAText(), TextBlock(text="hel"), TextBlock(text="lo")]

    async def fake_query(*, prompt, options):
        yield FakeAssistantMessage()

    monkeypatch.setattr("blindspot.llm.claude_agent_client.query", fake_query)

    out = await ClaudeAgentClient().complete(system="sys", user="hi")
    assert out == "hello"


async def test_complete_json_schema_path_parses_textblock(monkeypatch):
    """The json_schema path must parse text accumulated from TextBlocks."""

    class FakeAssistantMessage:
        content = [TextBlock(text='{"answer": 42}')]

    async def fake_query(*, prompt, options):
        yield FakeAssistantMessage()

    monkeypatch.setattr("blindspot.llm.claude_agent_client.query", fake_query)

    out = await ClaudeAgentClient().complete(
        system="sys", user="hi", json_schema={"type": "object"}
    )
    assert out == {"answer": 42}
