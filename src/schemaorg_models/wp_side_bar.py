from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class WPSideBar(WebPageElement):
    """
A sidebar section of the page.
    """
    class_: Literal['https://schema.org/WPSideBar'] = Field('class', alias='class', serialization_alias='class') # type: ignore
