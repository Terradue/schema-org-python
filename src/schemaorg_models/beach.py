from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class Beach(CivicStructure):
    """
Beach.
    """
    class_: Literal['https://schema.org/Beach'] = Field( # type: ignore
        default='https://schema.org/Beach',
        alias='@type',
        serialization_alias='@type'
    )
