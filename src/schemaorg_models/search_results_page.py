from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.web_page import WebPage

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
