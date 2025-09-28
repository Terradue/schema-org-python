from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class BoatTerminal(CivicStructure):
    """
A terminal for boats, ships, and other water vessels.
    """
    class_: Literal['https://schema.org/BoatTerminal'] = Field( # type: ignore
        default='https://schema.org/BoatTerminal',
        alias='@type',
        serialization_alias='@type'
    )
