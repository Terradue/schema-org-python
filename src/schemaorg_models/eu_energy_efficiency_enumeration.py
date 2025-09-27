from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration


class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.
    """
    type_: Literal['https://schema.org/EUEnergyEfficiencyEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EUEnergyEfficiencyEnumeration'),serialization_alias='class') # type: ignore
