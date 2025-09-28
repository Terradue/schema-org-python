from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class PoliceStation(CivicStructure):
    """
A police station.
    """
    class_: Literal['https://schema.org/PoliceStation'] = Field( # type: ignore
        default='https://schema.org/PoliceStation',
        alias='@type',
        serialization_alias='@type'
    )
