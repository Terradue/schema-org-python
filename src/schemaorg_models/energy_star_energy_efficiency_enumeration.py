from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
Used to indicate whether a product is EnergyStar certified.
    """
    type_: Literal['https://schema.org/EnergyStarEnergyEfficiencyEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EnergyStarEnergyEfficiencyEnumeration'),serialization_alias='class') # type: ignore
