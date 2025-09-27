from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class EnergyEfficiencyEnumeration(Enumeration):
    """
Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.
    """
    type_: Literal['https://schema.org/EnergyEfficiencyEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EnergyEfficiencyEnumeration'),serialization_alias='class') # type: ignore
