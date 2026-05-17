"""Coverage for ClaudeAgentClient._parse_json_response.

Targets the JSONDecodeError-at-Community-Analyst failure mode seen in
`bin/blindspot eval` (refinements/log.jsonl run-20260517-0936, PR #6):
models return text containing `{` but with prose / trailing text that
confuses `raw_decode`. The hardened parser must:

  - parse cleanly when the response is well-formed,
  - tolerate leading fences / prose before the object,
  - recover from prose AFTER the object,
  - raise ValueError WITH the response text when truly unparseable.
"""

from __future__ import annotations

import pytest

from blindspot.llm.claude_agent_client import ClaudeAgentClient

parse = ClaudeAgentClient._parse_json_response


def test_bare_json_object():
    assert parse('{"a": 1}') == {"a": 1}


def test_json_with_leading_fence():
    assert parse('```json\n{"a": 1}\n```') == {"a": 1}


def test_json_with_prose_before():
    assert parse('Here is the answer: {"a": 1}') == {"a": 1}


def test_json_with_prose_after():
    """The recovery target — prose appended after a valid object."""
    assert parse('{"a": 1} (this was my best effort)') == {"a": 1}


def test_json_with_prose_before_and_after():
    text = 'Here you go: {"a": 1, "b": [2, 3]} — let me know if that works.'
    assert parse(text) == {"a": 1, "b": [2, 3]}


def test_unparseable_input_raises_value_error_with_text():
    """The full response must be embedded in the error so eval failures are diagnosable."""
    bad = "{ this is not valid json at all, no closing brace"
    with pytest.raises(ValueError) as excinfo:
        parse(bad)
    # The response text must be in the message so upstream logs can recover it.
    assert "this is not valid json" in str(excinfo.value)


def test_unparseable_input_truncates_long_text():
    """Error text is bounded so a 50k-char response doesn't bloat logs."""
    bad = "{" + ("x" * 5000)
    with pytest.raises(ValueError) as excinfo:
        parse(bad)
    msg = str(excinfo.value)
    # Truncation marker appears; full 5000 x's do not.
    assert "truncated" in msg
    assert msg.count("x") < 3000
