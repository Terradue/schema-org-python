from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .body_of_water import BodyOfWater

class Waterfall(BodyOfWater):
    """
A waterfall, like Niagara.
    """
    class_: Literal['https://schema.org/Waterfall'] = Field( # type: ignore
        default='https://schema.org/Waterfall',
        alias='@type',
        serialization_alias='@type'
    )
