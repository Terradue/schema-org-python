from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class MusicVenue(CivicStructure):
    """
A music venue.
    """
    class_: Literal['https://schema.org/MusicVenue'] = Field( # type: ignore
        default='https://schema.org/MusicVenue',
        alias='@type',
        serialization_alias='@type'
    )
