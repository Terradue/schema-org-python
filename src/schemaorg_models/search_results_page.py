from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class SearchResultsPage(WebPage):
    """
Web page type: Search results page.
    """
    type_: Literal['https://schema.org/SearchResultsPage'] = Field(default='https://schema.org/SearchResultsPage', alias='@type', serialization_alias='@type') # type: ignore
