from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class SearchResultsPage(WebPage):
    """
Web page type: Search results page.
    """
    class_: Literal['https://schema.org/SearchResultsPage'] = Field(default='https://schema.org/SearchResultsPage', alias='class', serialization_alias='class') # type: ignore
