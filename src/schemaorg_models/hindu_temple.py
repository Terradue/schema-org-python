from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .place_of_worship import PlaceOfWorship

class HinduTemple(PlaceOfWorship):
    """
A Hindu temple.
    """
    class_: Literal['https://schema.org/HinduTemple'] = Field( # type: ignore
        default='https://schema.org/HinduTemple',
        alias='@type',
        serialization_alias='@type'
    )
