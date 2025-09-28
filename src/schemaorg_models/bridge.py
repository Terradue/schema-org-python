from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class Bridge(CivicStructure):
    """
A bridge.
    """
    class_: Literal['https://schema.org/Bridge'] = Field( # type: ignore
        default='https://schema.org/Bridge',
        alias='@type',
        serialization_alias='@type'
    )
