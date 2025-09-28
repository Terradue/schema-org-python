from __future__ import annotations

from .place_of_worship import PlaceOfWorship    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Mosque(PlaceOfWorship):
    """
A mosque.
    """
    class_: Literal['https://schema.org/Mosque'] = Field( # type: ignore
        default='https://schema.org/Mosque',
        alias='@type',
        serialization_alias='@type'
    )
