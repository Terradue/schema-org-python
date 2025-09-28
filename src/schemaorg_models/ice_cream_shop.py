from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .food_establishment import FoodEstablishment

class IceCreamShop(FoodEstablishment):
    """
An ice cream shop.
    """
    class_: Literal['https://schema.org/IceCreamShop'] = Field( # type: ignore
        default='https://schema.org/IceCreamShop',
        alias='@type',
        serialization_alias='@type'
    )
