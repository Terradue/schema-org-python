from typing import Literal
from pydantic import Field
from schemaorg_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
Used to indicate whether a product is EnergyStar certified.
    """
    class_: Literal['https://schema.org/EnergyStarEnergyEfficiencyEnumeration'] = Field(default='https://schema.org/EnergyStarEnergyEfficiencyEnumeration', alias='class', serialization_alias='class') # type: ignore
