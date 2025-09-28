from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class Park(CivicStructure):
    """
A park.
    """
    class_: Literal['https://schema.org/Park'] = Field( # type: ignore
        default='https://schema.org/Park',
        alias='@type',
        serialization_alias='@type'
    )
