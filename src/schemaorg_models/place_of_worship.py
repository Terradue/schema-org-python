from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PlaceOfWorship(CivicStructure):
    """
Place of worship, such as a church, synagogue, or mosque.
    """
    class_: Literal['https://schema.org/PlaceOfWorship'] = Field( # type: ignore
        default='https://schema.org/PlaceOfWorship',
        alias='@type',
        serialization_alias='@type'
    )
