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
from .enumeration import Enumeration

class ItemListOrderType(Enumeration):
    '''
    Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    '''
    class_: Literal['https://schema.org/ItemListOrderType'] = Field( # type: ignore
        default='https://schema.org/ItemListOrderType',
        alias='@type',
        serialization_alias='@type'
    )
