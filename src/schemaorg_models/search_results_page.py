from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class SearchResultsPage(WebPage):
    """
Web page type: Search results page.
    """
    class_: Literal['https://schema.org/SearchResultsPage'] = Field(default='https://schema.org/SearchResultsPage', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
