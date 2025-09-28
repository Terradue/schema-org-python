from __future__ import annotations

from .food_establishment import FoodEstablishment    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Brewery(FoodEstablishment):
    """
Brewery.
    """
    class_: Literal['https://schema.org/Brewery'] = Field( # type: ignore
        default='https://schema.org/Brewery',
        alias='@type',
        serialization_alias='@type'
    )
