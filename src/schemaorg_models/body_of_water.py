from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .landform import Landform

class BodyOfWater(Landform):
    """
A body of water, such as a sea, ocean, or lake.
    """
    class_: Literal['https://schema.org/BodyOfWater'] = Field( # type: ignore
        default='https://schema.org/BodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
