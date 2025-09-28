from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BusStop(CivicStructure):
    """
A bus stop.
    """
    class_: Literal['https://schema.org/BusStop'] = Field( # type: ignore
        default='https://schema.org/BusStop',
        alias='@type',
        serialization_alias='@type'
    )
