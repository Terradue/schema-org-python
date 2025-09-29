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

class PriceTypeEnumeration(Enumeration):
    '''
    Enumerates different price types, for example list price, invoice price, and sale price.
    '''
    class_: Literal['https://schema.org/PriceTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/PriceTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
