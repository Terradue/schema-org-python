from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Park(CivicStructure):
    """
A park.
    """
    class_: Literal['https://schema.org/Park'] = Field( # type: ignore
        default='https://schema.org/Park',
        alias='@type',
        serialization_alias='@type'
    )
