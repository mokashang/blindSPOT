import pytest

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
