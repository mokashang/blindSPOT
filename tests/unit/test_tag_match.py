import pytest

from blindspot.config import Config
from blindspot.sources.base import SourceView
from blindspot.sources.tag_match import select_top_n
from blindspot.types import Facet, Situation


def _view(
    id_,
    community,
    reliability=3,
    domains=None,
    notes="",
):
    return SourceView(
        id=id_,
        adapter="rss",
        fetch_config={},
        domains=domains or [],
        community_tag=community,
        reliability=reliability,
        freshness_required=False,
        notes=notes,
    )


@pytest.mark.asyncio
async def test_diversity_constraint_limits_two_per_community():
    situation = Situation(
        raw_text="...",
        tags={
            Facet.DOMAIN: ["tech-career/equity"],
            Facet.ENTITY: ["ISO"],
            Facet.RISK_SURFACE: [],
            Facet.PERSONA: [],
        },
    )
    views = [
        _view("a", "founder-engineer-bloggers", 5, domains=["tech-career/equity"]),
        _view("b", "founder-engineer-bloggers", 5, domains=["tech-career/equity"]),
        _view("c", "founder-engineer-bloggers", 5, domains=["tech-career/equity"]),
        _view("d", "reddit-tech-collective", 4, domains=["tech-career/equity"]),
        _view("e", "vc-blogosphere", 3, domains=["tech-career/equity"]),
    ]

    class NullEmbedder:
        async def embed(self, texts):
            return [[0.0]] * len(texts)

    selected = await select_top_n(views, situation, Config(), NullEmbedder())
    chosen_ids = [v.id for v in selected]
    assert sum(1 for v in selected if v.community_tag == "founder-engineer-bloggers") == 2
    assert "d" in chosen_ids
    assert "e" in chosen_ids
