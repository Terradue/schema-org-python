from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
Used to indicate whether a product is EnergyStar certified.
    """
    class_: Literal['https://schema.org/EnergyStarEnergyEfficiencyEnumeration'] = Field( # type: ignore
        default='https://schema.org/EnergyStarEnergyEfficiencyEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
