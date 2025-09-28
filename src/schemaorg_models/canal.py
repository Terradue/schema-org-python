from __future__ import annotations

from .body_of_water import BodyOfWater    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Canal(BodyOfWater):
    """
A canal, like the Panama Canal.
    """
    class_: Literal['https://schema.org/Canal'] = Field( # type: ignore
        default='https://schema.org/Canal',
        alias='@type',
        serialization_alias='@type'
    )
