from __future__ import annotations

from .landform import Landform    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BodyOfWater(Landform):
    """
A body of water, such as a sea, ocean, or lake.
    """
    class_: Literal['https://schema.org/BodyOfWater'] = Field( # type: ignore
        default='https://schema.org/BodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
