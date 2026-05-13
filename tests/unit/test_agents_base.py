from datetime import datetime, timezone

from blindspot.agents.base import serialize_documents_for_prompt
from blindspot.types import Document


def test_serialize_documents_marks_each():
    docs = [
        Document(
            doc_id="doc-1",
            source_view_id="x",
            community_tag="t",
            url="u",
            title="A",
            content="aaa",
            fetched_at=datetime.now(timezone.utc),
        ),
        Document(
            doc_id="doc-2",
            source_view_id="x",
            community_tag="t",
            url="u",
            title="B",
            content="bbb",
            fetched_at=datetime.now(timezone.utc),
        ),
    ]
    out = serialize_documents_for_prompt(docs)
    assert "[doc-1]" in out
    assert "[doc-2]" in out
    assert "aaa" in out
