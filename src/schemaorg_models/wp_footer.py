from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class WPFooter(WebPageElement):
    """
The footer section of the page.
    """
    type_: Literal['https://schema.org/WPFooter'] = Field(default='https://schema.org/WPFooter', alias='@type', serialization_alias='@type') # type: ignore
