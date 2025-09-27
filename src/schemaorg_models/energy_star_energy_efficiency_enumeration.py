from typing import Literal
from pydantic import Field
from schemaorg_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
Used to indicate whether a product is EnergyStar certified.
    """
    type_: Literal['https://schema.org/EnergyStarEnergyEfficiencyEnumeration'] = Field(default='https://schema.org/EnergyStarEnergyEfficiencyEnumeration', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
