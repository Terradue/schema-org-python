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

class CafeOrCoffeeShop(FoodEstablishment):
    '''
    A cafe or coffee shop.
    '''
    class_: Literal['https://schema.org/CafeOrCoffeeShop'] = Field( # type: ignore
        default='https://schema.org/CafeOrCoffeeShop',
        alias='@type',
        serialization_alias='@type'
    )
