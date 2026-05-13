import pytest

from blindspot.agents.editor import run_editor
from blindspot.config import Config
from blindspot.types import Facet, RiskOfficerOutput, Situation


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        return "## Situation\nYou asked about a Series B offer.\n\n## Blind spots..."


@pytest.mark.asyncio
async def test_editor_returns_markdown():
    out = await run_editor(
        Situation(raw_text="s", tags={Facet.DOMAIN: ["tech-career/equity"]}),
        analyst_outputs=[],
        risk_output=RiskOfficerOutput([]),
        documents=[],
        llm=StubLLM(),
        cfg=Config(),
    )
    assert out.startswith("## Situation")
