from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .food_establishment import FoodEstablishment

class Brewery(FoodEstablishment):
    """
Brewery.
    """
    class_: Literal['https://schema.org/Brewery'] = Field( # type: ignore
        default='https://schema.org/Brewery',
        alias='@type',
        serialization_alias='@type'
    )
