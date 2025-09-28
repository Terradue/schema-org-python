from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .food_establishment import FoodEstablishment

class FastFoodRestaurant(FoodEstablishment):
    """
A fast-food restaurant.
    """
    class_: Literal['https://schema.org/FastFoodRestaurant'] = Field( # type: ignore
        default='https://schema.org/FastFoodRestaurant',
        alias='@type',
        serialization_alias='@type'
    )
