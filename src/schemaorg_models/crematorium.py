from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class Crematorium(CivicStructure):
    """
A crematorium.
    """
    class_: Literal['https://schema.org/Crematorium'] = Field( # type: ignore
        default='https://schema.org/Crematorium',
        alias='@type',
        serialization_alias='@type'
    )
