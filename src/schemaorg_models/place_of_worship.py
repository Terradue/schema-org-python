from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class PlaceOfWorship(CivicStructure):
    """
Place of worship, such as a church, synagogue, or mosque.
    """
    class_: Literal['https://schema.org/PlaceOfWorship'] = Field( # type: ignore
        default='https://schema.org/PlaceOfWorship',
        alias='@type',
        serialization_alias='@type'
    )
