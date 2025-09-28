from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .place_of_worship import PlaceOfWorship

class Synagogue(PlaceOfWorship):
    """
A synagogue.
    """
    class_: Literal['https://schema.org/Synagogue'] = Field( # type: ignore
        default='https://schema.org/Synagogue',
        alias='@type',
        serialization_alias='@type'
    )
