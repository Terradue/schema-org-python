from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .web_page import WebPage

class ItemPage(WebPage):
    '''
    A page devoted to a single item, such as a particular product or hotel.
    '''
    class_: Literal['https://schema.org/ItemPage'] = Field( # type: ignore
        default='https://schema.org/ItemPage',
        alias='@type',
        serialization_alias='@type'
    )
