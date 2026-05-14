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


def test_parse_json_response_trailing_prose():
    """Models sometimes append commentary after the object despite "JSON only".

    Regression: a fixture in `blindspot eval` returned `{...}\\n\\n<prose>`,
    and json.loads() raised "Extra data" on the whole string.
    """
    out = ClaudeAgentClient._parse_json_response(
        '{"a": 1}\n\nThat is the structured answer you asked for.'
    )
    assert out == {"a": 1}


def test_parse_json_response_fenced_with_trailing_prose():
    out = ClaudeAgentClient._parse_json_response(
        '```json\n{"a": 1}\n```\n\nLet me know if you need anything else.'
    )
    assert out == {"a": 1}


def test_parse_json_response_leading_prose():
    out = ClaudeAgentClient._parse_json_response('Here is the JSON:\n{"a": 1}')
    assert out == {"a": 1}


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


async def test_complete_runs_as_pure_text_completion(monkeypatch):
    """complete() must hard-disable tools and the account's claude.ai MCP servers.

    The SDK leaves built-in tools (Bash, Task, ...) on by default and also
    surfaces the user's connected claude.ai MCP servers. With max_turns=1, the
    model can burn its only turn on a tool call → "Reached maximum number of
    turns (1)". blindspot's agents are text-in / JSON-out — no tools, ever.
    """
    captured = {}

    async def fake_query(*, prompt, options):
        captured["options"] = options
        yield AssistantMessage(
            content=[TextBlock(text="ok")], model="claude-opus-4-7"
        )

    monkeypatch.setattr("blindspot.llm.claude_agent_client.query", fake_query)
    await ClaudeAgentClient().complete(system="sys", user="hi")

    opts = captured["options"]
    assert opts.tools == [], "built-in tools must be disabled (--tools '')"
    assert opts.strict_mcp_config is True, "account claude.ai MCP servers must be ignored"
    assert opts.max_turns == 1
