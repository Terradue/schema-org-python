from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class FoodEvent(Event):
    """
A sub property of location. The specific food event where the action occurred.
    """
    class_: Literal['https://schema.org/FoodEvent'] = Field( # type: ignore
        default='https://schema.org/FoodEvent',
        alias='@type',
        serialization_alias='@type'
    )
