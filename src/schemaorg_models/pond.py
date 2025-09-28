from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .body_of_water import BodyOfWater

class Pond(BodyOfWater):
    """
A pond.
    """
    class_: Literal['https://schema.org/Pond'] = Field( # type: ignore
        default='https://schema.org/Pond',
        alias='@type',
        serialization_alias='@type'
    )
