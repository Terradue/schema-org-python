from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page_element import WebPageElement


class WPHeader(WebPageElement):
    """
The header section of the page.
    """
    type_: Literal['https://schema.org/WPHeader'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WPHeader'),serialization_alias='class') # type: ignore
