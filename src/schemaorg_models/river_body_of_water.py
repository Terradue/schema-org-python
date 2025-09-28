from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .body_of_water import BodyOfWater

class RiverBodyOfWater(BodyOfWater):
    """
A river (for example, the broad majestic Shannon).
    """
    class_: Literal['https://schema.org/RiverBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/RiverBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
