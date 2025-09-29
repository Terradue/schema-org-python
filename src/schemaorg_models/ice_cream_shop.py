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
from .food_establishment import FoodEstablishment

class IceCreamShop(FoodEstablishment):
    '''
    An ice cream shop.
    '''
    class_: Literal['https://schema.org/IceCreamShop'] = Field( # type: ignore
        default='https://schema.org/IceCreamShop',
        alias='@type',
        serialization_alias='@type'
    )
