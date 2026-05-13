"""Extract [doc-N] citation markers from text; identify unmarked claims."""

from __future__ import annotations

import re

CITATION_RE = re.compile(r"\[doc-(\w+)\]")
SENTENCE_RE = re.compile(r"[^.!?\n]+[.!?]")


def extract_citations(text: str) -> set[str]:
    return set(CITATION_RE.findall(text))


def find_unmarked_claims(text: str) -> list[str]:
    """Return sentences that contain no [doc-X] marker.

    Used to populate the ungrounded_claims log so the refine routine can
    later spot coverage gaps in the source registry.
    """
    return [
        s.strip()
        for s in SENTENCE_RE.findall(text)
        if s.strip() and not CITATION_RE.search(s)
    ]
