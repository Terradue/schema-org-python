from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page_element import WebPageElement


class WPSideBar(WebPageElement):
    """
A sidebar section of the page.
    """
    type_: Literal['https://schema.org/WPSideBar'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WPSideBar'),serialization_alias='class') # type: ignore
