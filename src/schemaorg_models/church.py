from __future__ import annotations

from .place_of_worship import PlaceOfWorship    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Church(PlaceOfWorship):
    """
A church.
    """
    class_: Literal['https://schema.org/Church'] = Field( # type: ignore
        default='https://schema.org/Church',
        alias='@type',
        serialization_alias='@type'
    )
