from __future__ import annotations

from .food_establishment import FoodEstablishment    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Winery(FoodEstablishment):
    """
A winery.
    """
    class_: Literal['https://schema.org/Winery'] = Field( # type: ignore
        default='https://schema.org/Winery',
        alias='@type',
        serialization_alias='@type'
    )
