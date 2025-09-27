from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page_element import WebPageElement


class WPFooter(WebPageElement):
    """
The footer section of the page.
    """
    type_: Literal['https://schema.org/WPFooter'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WPFooter'),serialization_alias='class') # type: ignore
