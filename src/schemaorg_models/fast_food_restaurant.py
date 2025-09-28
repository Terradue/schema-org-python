from __future__ import annotations

from .food_establishment import FoodEstablishment    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class FastFoodRestaurant(FoodEstablishment):
    """
A fast-food restaurant.
    """
    class_: Literal['https://schema.org/FastFoodRestaurant'] = Field( # type: ignore
        default='https://schema.org/FastFoodRestaurant',
        alias='@type',
        serialization_alias='@type'
    )
