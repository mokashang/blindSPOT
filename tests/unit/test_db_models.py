from datetime import datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from blindspot.db.models import (
    Base, BlindSpotRow, DocumentRow, SessionRow, TurnRow, TurnTagRow,
)


def test_can_create_full_session_graph():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as s:
        sess = SessionRow(user_id="local", situation="I got an offer", language="en")
        s.add(sess)
        s.flush()
        turn = TurnRow(session_id=sess.id, turn_number=1, user_input="I got an offer",
                       assistant_response="...")
        s.add(turn)
        s.flush()
        s.add(TurnTagRow(turn_id=turn.id, facet="entity", tag="ISO"))
        s.add(BlindSpotRow(turn_id=turn.id, hook="...", body="...", community_tag="x"))
        doc = DocumentRow(source_view_id="pmck-equity", url="https://x", title="t",
                          content="c", content_hash="abc", fetched_at=datetime.now(timezone.utc),
                          expires_at=datetime.now(timezone.utc))
        s.add(doc)
        s.commit()

        assert sess.id is not None
        assert turn.session_id == sess.id
