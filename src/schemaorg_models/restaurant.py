from __future__ import annotations

from .food_establishment import FoodEstablishment    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Restaurant(FoodEstablishment):
    """
A restaurant.
    """
    class_: Literal['https://schema.org/Restaurant'] = Field( # type: ignore
        default='https://schema.org/Restaurant',
        alias='@type',
        serialization_alias='@type'
    )
