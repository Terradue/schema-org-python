from __future__ import annotations

from .place_of_worship import PlaceOfWorship    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Synagogue(PlaceOfWorship):
    """
A synagogue.
    """
    class_: Literal['https://schema.org/Synagogue'] = Field( # type: ignore
        default='https://schema.org/Synagogue',
        alias='@type',
        serialization_alias='@type'
    )
