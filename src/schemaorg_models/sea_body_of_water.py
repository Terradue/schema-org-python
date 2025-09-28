from __future__ import annotations

from .body_of_water import BodyOfWater    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SeaBodyOfWater(BodyOfWater):
    """
A sea (for example, the Caspian sea).
    """
    class_: Literal['https://schema.org/SeaBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/SeaBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
