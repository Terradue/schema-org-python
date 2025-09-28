from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page import WebPage

class ItemPage(WebPage):
    """
A page devoted to a single item, such as a particular product or hotel.
    """
    class_: Literal['https://schema.org/ItemPage'] = Field( # type: ignore
        default='https://schema.org/ItemPage',
        alias='@type',
        serialization_alias='@type'
    )
