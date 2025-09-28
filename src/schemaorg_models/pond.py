from __future__ import annotations

from .body_of_water import BodyOfWater    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Pond(BodyOfWater):
    """
A pond.
    """
    class_: Literal['https://schema.org/Pond'] = Field( # type: ignore
        default='https://schema.org/Pond',
        alias='@type',
        serialization_alias='@type'
    )
