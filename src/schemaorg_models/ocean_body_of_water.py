from __future__ import annotations

from .body_of_water import BodyOfWater    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OceanBodyOfWater(BodyOfWater):
    """
An ocean (for example, the Pacific).
    """
    class_: Literal['https://schema.org/OceanBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/OceanBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
