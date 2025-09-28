from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Zoo(CivicStructure):
    """
A zoo.
    """
    class_: Literal['https://schema.org/Zoo'] = Field( # type: ignore
        default='https://schema.org/Zoo',
        alias='@type',
        serialization_alias='@type'
    )
