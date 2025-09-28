from __future__ import annotations

from .anatomical_structure import AnatomicalStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Bone(AnatomicalStructure):
    """
Rigid connective tissue that comprises up the skeletal structure of the human body.
    """
    class_: Literal['https://schema.org/Bone'] = Field( # type: ignore
        default='https://schema.org/Bone',
        alias='@type',
        serialization_alias='@type'
    )
