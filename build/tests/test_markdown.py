from __future__ import annotations

from pathlib import Path

from build.markdown import citation_metadata, render_citations
from build.stats import load_rows


FIXTURE = Path(__file__).parent / "fixtures"


def test_quote_ref_does_not_consume_an_unreferenced_quote():
    metadata = citation_metadata(load_rows(FIXTURE, 1))
    source = "示例标「非 MS 原文」。……「A buffer allows temporary storage of the data」⟦9618_s24_11:1⟧"

    rendered = render_citations(source, metadata, output="md")

    assert rendered == (
        "示例标「非 MS 原文」。……"
        '"A buffer allows temporary storage of the data" (s24/11 Q1)'
    )
