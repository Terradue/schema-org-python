from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TaxiStand(CivicStructure):
    """
A taxi stand.
    """
    class_: Literal['https://schema.org/TaxiStand'] = Field( # type: ignore
        default='https://schema.org/TaxiStand',
        alias='@type',
        serialization_alias='@type'
    )
