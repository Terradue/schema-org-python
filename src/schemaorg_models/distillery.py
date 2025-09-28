from __future__ import annotations

from .food_establishment import FoodEstablishment    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Distillery(FoodEstablishment):
    """
A distillery.
    """
    class_: Literal['https://schema.org/Distillery'] = Field( # type: ignore
        default='https://schema.org/Distillery',
        alias='@type',
        serialization_alias='@type'
    )
