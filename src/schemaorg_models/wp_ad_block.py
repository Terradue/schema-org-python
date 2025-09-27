from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page_element import WebPageElement


class WPAdBlock(WebPageElement):
    """
An advertising section of the page.
    """
    type_: Literal['https://schema.org/WPAdBlock'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WPAdBlock'),serialization_alias='class') # type: ignore
