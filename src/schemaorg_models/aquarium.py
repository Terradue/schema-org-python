from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class Aquarium(CivicStructure):
    """
Aquarium.
    """
    class_: Literal['https://schema.org/Aquarium'] = Field( # type: ignore
        default='https://schema.org/Aquarium',
        alias='@type',
        serialization_alias='@type'
    )
