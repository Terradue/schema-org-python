from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class BusStation(CivicStructure):
    """
A bus station.
    """
    class_: Literal['https://schema.org/BusStation'] = Field( # type: ignore
        default='https://schema.org/BusStation',
        alias='@type',
        serialization_alias='@type'
    )
