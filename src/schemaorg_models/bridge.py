from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Bridge(CivicStructure):
    """
A bridge.
    """
    class_: Literal['https://schema.org/Bridge'] = Field( # type: ignore
        default='https://schema.org/Bridge',
        alias='@type',
        serialization_alias='@type'
    )
