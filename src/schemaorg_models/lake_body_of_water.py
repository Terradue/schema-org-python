from __future__ import annotations

from .body_of_water import BodyOfWater    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LakeBodyOfWater(BodyOfWater):
    """
A lake (for example, Lake Pontrachain).
    """
    class_: Literal['https://schema.org/LakeBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/LakeBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
