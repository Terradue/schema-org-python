from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Crematorium(CivicStructure):
    """
A crematorium.
    """
    class_: Literal['https://schema.org/Crematorium'] = Field( # type: ignore
        default='https://schema.org/Crematorium',
        alias='@type',
        serialization_alias='@type'
    )
