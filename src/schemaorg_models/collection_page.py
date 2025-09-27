from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class CollectionPage(WebPage):
    """
Web page type: Collection page.
    """
    type_: Literal['https://schema.org/CollectionPage'] = Field(default='https://schema.org/CollectionPage', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
