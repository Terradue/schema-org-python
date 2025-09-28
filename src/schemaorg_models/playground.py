from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class Playground(CivicStructure):
    """
A playground.
    """
    class_: Literal['https://schema.org/Playground'] = Field( # type: ignore
        default='https://schema.org/Playground',
        alias='@type',
        serialization_alias='@type'
    )
