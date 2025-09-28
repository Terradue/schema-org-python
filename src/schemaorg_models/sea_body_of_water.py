from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .body_of_water import BodyOfWater

class SeaBodyOfWater(BodyOfWater):
    """
A sea (for example, the Caspian sea).
    """
    class_: Literal['https://schema.org/SeaBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/SeaBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
