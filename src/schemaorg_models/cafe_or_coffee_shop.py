from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .food_establishment import FoodEstablishment

class CafeOrCoffeeShop(FoodEstablishment):
    """
A cafe or coffee shop.
    """
    class_: Literal['https://schema.org/CafeOrCoffeeShop'] = Field( # type: ignore
        default='https://schema.org/CafeOrCoffeeShop',
        alias='@type',
        serialization_alias='@type'
    )
