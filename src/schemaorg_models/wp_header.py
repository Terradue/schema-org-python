from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class WPHeader(WebPageElement):
    """
The header section of the page.
    """
    type_: Literal['https://schema.org/WPHeader'] = Field(default='https://schema.org/WPHeader', alias='@type', serialization_alias='@type') # type: ignore
