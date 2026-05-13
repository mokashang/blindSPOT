import pytest

from blindspot.agents.community_analyst import run_community_analyst
from blindspot.config import Config
from blindspot.types import Facet, Situation


class StubLLM:
    async def complete(self, system, user, model="x", max_tokens=4096, json_schema=None):
        assert "Community profile" in system
        return {
            "prose": "Tech veterans would tell you... [doc-1]",
            "blind_spots": [
                {
                    "hook": "AMT exposure",
                    "body": "Your strike vs FMV gap drives AMT [doc-1]",
                    "citation_doc_ids": ["doc-1"],
                }
            ],
        }


@pytest.mark.asyncio
async def test_analyst_loads_profile_and_returns_structured():
    sit = Situation(raw_text="...", tags={Facet.DOMAIN: ["tech-career/equity"]})
    out = await run_community_analyst(
        "founder-engineer-bloggers", sit, [], StubLLM(), Config()
    )
    assert out.community_tag == "founder-engineer-bloggers"
    assert "[doc-1]" in out.prose
    assert len(out.blind_spots) == 1
    assert out.blind_spots[0].hook == "AMT exposure"
