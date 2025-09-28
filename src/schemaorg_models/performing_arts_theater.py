from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class PerformingArtsTheater(CivicStructure):
    """
A theater or other performing art center.
    """
    class_: Literal['https://schema.org/PerformingArtsTheater'] = Field( # type: ignore
        default='https://schema.org/PerformingArtsTheater',
        alias='@type',
        serialization_alias='@type'
    )
