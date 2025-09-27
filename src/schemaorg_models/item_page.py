from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class ItemPage(WebPage):
    """
A page devoted to a single item, such as a particular product or hotel.
    """
    type_: Literal['https://schema.org/ItemPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ItemPage'),serialization_alias='class') # type: ignore
