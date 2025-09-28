from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class RVPark(CivicStructure):
    """
A place offering space for "Recreational Vehicles", Caravans, mobile homes and the like.
    """
    class_: Literal['https://schema.org/RVPark'] = Field( # type: ignore
        default='https://schema.org/RVPark',
        alias='@type',
        serialization_alias='@type'
    )
