from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EnergyEfficiencyEnumeration(Enumeration):
    """
Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.
    """
    class_: Literal['https://schema.org/EnergyEfficiencyEnumeration'] = Field( # type: ignore
        default='https://schema.org/EnergyEfficiencyEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
