from blindspot.filters.grounding import extract_citations, find_unmarked_claims


def test_extract_citations_finds_doc_markers():
    text = "Strike price matters [doc-3]. Also AMT [doc-7] [doc-12]."
    assert extract_citations(text) == {"3", "7", "12"}


def test_find_unmarked_claims_detects_sentences_without_citations():
    text = "First claim is supported [doc-1]. Second claim is naked. Third [doc-2]."
    claims = find_unmarked_claims(text)
    assert any("Second claim is naked" in c for c in claims)
    assert all("supported" not in c for c in claims)
