from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .body_of_water import BodyOfWater

class Canal(BodyOfWater):
    """
A canal, like the Panama Canal.
    """
    class_: Literal['https://schema.org/Canal'] = Field( # type: ignore
        default='https://schema.org/Canal',
        alias='@type',
        serialization_alias='@type'
    )
