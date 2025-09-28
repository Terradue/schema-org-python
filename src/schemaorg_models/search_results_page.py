from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page import WebPage

class SearchResultsPage(WebPage):
    """
Web page type: Search results page.
    """
    class_: Literal['https://schema.org/SearchResultsPage'] = Field( # type: ignore
        default='https://schema.org/SearchResultsPage',
        alias='@type',
        serialization_alias='@type'
    )
