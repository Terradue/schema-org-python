from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class SubwayStation(CivicStructure):
    """
A subway station.
    """
    class_: Literal['https://schema.org/SubwayStation'] = Field( # type: ignore
        default='https://schema.org/SubwayStation',
        alias='@type',
        serialization_alias='@type'
    )
