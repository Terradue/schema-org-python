from __future__ import annotations

from .energy_efficiency_enumeration import EnergyEfficiencyEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.
    """
    class_: Literal['https://schema.org/EUEnergyEfficiencyEnumeration'] = Field( # type: ignore
        default='https://schema.org/EUEnergyEfficiencyEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
