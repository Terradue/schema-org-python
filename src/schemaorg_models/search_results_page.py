from __future__ import annotations

from .web_page import WebPage    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SearchResultsPage(WebPage):
    """
Web page type: Search results page.
    """
    class_: Literal['https://schema.org/SearchResultsPage'] = Field( # type: ignore
        default='https://schema.org/SearchResultsPage',
        alias='@type',
        serialization_alias='@type'
    )
