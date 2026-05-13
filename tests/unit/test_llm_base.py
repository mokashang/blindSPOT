from blindspot.llm.base import Embedder, LLMClient


class FakeLLM:
    async def complete(
        self, system, user, model="claude-opus-4-7", max_tokens=4096, json_schema=None
    ):
        return "ok"


class FakeEmbedder:
    async def embed(self, texts):
        return [[0.0] for _ in texts]


def test_protocols_accept_compatible_objects():
    assert isinstance(FakeLLM(), LLMClient)
    assert isinstance(FakeEmbedder(), Embedder)
