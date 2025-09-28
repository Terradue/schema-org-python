from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .landform import Landform

class Continent(Landform):
    """
One of the continents (for example, Europe or Africa).
    """
    class_: Literal['https://schema.org/Continent'] = Field( # type: ignore
        default='https://schema.org/Continent',
        alias='@type',
        serialization_alias='@type'
    )
