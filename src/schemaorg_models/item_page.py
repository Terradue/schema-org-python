from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class ItemPage(WebPage):
    """
A page devoted to a single item, such as a particular product or hotel.
    """
    class_: Literal['https://schema.org/ItemPage'] = Field(default='https://schema.org/ItemPage', alias='class', serialization_alias='class') # type: ignore
