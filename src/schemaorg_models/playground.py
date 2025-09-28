from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Playground(CivicStructure):
    """
A playground.
    """
    class_: Literal['https://schema.org/Playground'] = Field( # type: ignore
        default='https://schema.org/Playground',
        alias='@type',
        serialization_alias='@type'
    )
