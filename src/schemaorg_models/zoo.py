from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class Zoo(CivicStructure):
    """
A zoo.
    """
    class_: Literal['https://schema.org/Zoo'] = Field( # type: ignore
        default='https://schema.org/Zoo',
        alias='@type',
        serialization_alias='@type'
    )
