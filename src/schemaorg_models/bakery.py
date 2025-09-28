from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .food_establishment import FoodEstablishment

class Bakery(FoodEstablishment):
    """
A bakery.
    """
    class_: Literal['https://schema.org/Bakery'] = Field( # type: ignore
        default='https://schema.org/Bakery',
        alias='@type',
        serialization_alias='@type'
    )
