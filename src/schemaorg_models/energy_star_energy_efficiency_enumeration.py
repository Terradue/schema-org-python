from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .energy_efficiency_enumeration import EnergyEfficiencyEnumeration

class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
Used to indicate whether a product is EnergyStar certified.
    """
    class_: Literal['https://schema.org/EnergyStarEnergyEfficiencyEnumeration'] = Field( # type: ignore
        default='https://schema.org/EnergyStarEnergyEfficiencyEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
