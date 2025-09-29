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

class PurchaseType(Enumeration):
    '''
    Enumerates a purchase type for an item.
    '''
    class_: Literal['https://schema.org/PurchaseType'] = Field( # type: ignore
        default='https://schema.org/PurchaseType',
        alias='@type',
        serialization_alias='@type'
    )
