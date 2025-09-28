from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class FireStation(CivicStructure):
    """
A fire station. With firemen.
    """
    class_: Literal['https://schema.org/FireStation'] = Field( # type: ignore
        default='https://schema.org/FireStation',
        alias='@type',
        serialization_alias='@type'
    )
