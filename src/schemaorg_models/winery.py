from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .food_establishment import FoodEstablishment

class Winery(FoodEstablishment):
    """
A winery.
    """
    class_: Literal['https://schema.org/Winery'] = Field( # type: ignore
        default='https://schema.org/Winery',
        alias='@type',
        serialization_alias='@type'
    )
