from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SubwayStation(CivicStructure):
    """
A subway station.
    """
    class_: Literal['https://schema.org/SubwayStation'] = Field( # type: ignore
        default='https://schema.org/SubwayStation',
        alias='@type',
        serialization_alias='@type'
    )
