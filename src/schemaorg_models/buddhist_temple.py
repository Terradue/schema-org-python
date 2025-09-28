from __future__ import annotations

from .place_of_worship import PlaceOfWorship    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BuddhistTemple(PlaceOfWorship):
    """
A Buddhist temple.
    """
    class_: Literal['https://schema.org/BuddhistTemple'] = Field( # type: ignore
        default='https://schema.org/BuddhistTemple',
        alias='@type',
        serialization_alias='@type'
    )
