from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class WPHeader(WebPageElement):
    """
The header section of the page.
    """
    class_: Literal['https://schema.org/WPHeader'] = Field('class', alias='class', serialization_alias='class') # type: ignore
