from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class ParkingFacility(CivicStructure):
    """
A parking lot or other parking facility.
    """
    class_: Literal['https://schema.org/ParkingFacility'] = Field( # type: ignore
        default='https://schema.org/ParkingFacility',
        alias='@type',
        serialization_alias='@type'
    )
