from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class Museum(CivicStructure):
    """
A museum.
    """
    class_: Literal['https://schema.org/Museum'] = Field( # type: ignore
        default='https://schema.org/Museum',
        alias='@type',
        serialization_alias='@type'
    )
