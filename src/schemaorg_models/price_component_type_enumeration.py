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

class PriceComponentTypeEnumeration(Enumeration):
    '''
    Enumerates different price components that together make up the total price for an offered product.
    '''
    class_: Literal['https://schema.org/PriceComponentTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/PriceComponentTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
