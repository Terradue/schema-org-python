from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .anatomical_structure import AnatomicalStructure

class Bone(AnatomicalStructure):
    """
Rigid connective tissue that comprises up the skeletal structure of the human body.
    """
    class_: Literal['https://schema.org/Bone'] = Field( # type: ignore
        default='https://schema.org/Bone',
        alias='@type',
        serialization_alias='@type'
    )
