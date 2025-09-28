from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .food_establishment import FoodEstablishment

class BarOrPub(FoodEstablishment):
    """
A bar or pub.
    """
    class_: Literal['https://schema.org/BarOrPub'] = Field( # type: ignore
        default='https://schema.org/BarOrPub',
        alias='@type',
        serialization_alias='@type'
    )
