from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class SearchResultsPage(WebPage):
    """
Web page type: Search results page.
    """
    type_: Literal['https://schema.org/SearchResultsPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SearchResultsPage'),serialization_alias='class') # type: ignore
