from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class StadiumOrArena(CivicStructure):
    """
A stadium.
    """
    class_: Literal['https://schema.org/StadiumOrArena'] = Field( # type: ignore
        default='https://schema.org/StadiumOrArena',
        alias='@type',
        serialization_alias='@type'
    )
