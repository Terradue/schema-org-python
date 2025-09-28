from __future__ import annotations

from .civic_structure import CivicStructure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GovernmentBuilding(CivicStructure):
    """
A government building.
    """
    class_: Literal['https://schema.org/GovernmentBuilding'] = Field( # type: ignore
        default='https://schema.org/GovernmentBuilding',
        alias='@type',
        serialization_alias='@type'
    )
