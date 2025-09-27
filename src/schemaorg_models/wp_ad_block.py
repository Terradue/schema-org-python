from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class WPAdBlock(WebPageElement):
    """
An advertising section of the page.
    """
    type_: Literal['https://schema.org/WPAdBlock'] = Field(default='https://schema.org/WPAdBlock', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
