from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class WPSideBar(WebPageElement):
    """
A sidebar section of the page.
    """
    type_: Literal['https://schema.org/WPSideBar'] = Field(default='https://schema.org/WPSideBar', alias='@type', serialization_alias='@type') # type: ignore
