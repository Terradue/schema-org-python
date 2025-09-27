from typing import Literal
from pydantic import Field
from schemaorg_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration


class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.
    """
    class_: Literal['https://schema.org/EUEnergyEfficiencyEnumeration'] = Field(default='https://schema.org/EUEnergyEfficiencyEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
