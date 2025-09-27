from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class EnergyEfficiencyEnumeration(Enumeration):
    """
Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.
    """
    class_: Literal['https://schema.org/EnergyEfficiencyEnumeration'] = Field(default='https://schema.org/EnergyEfficiencyEnumeration', alias='class', serialization_alias='class') # type: ignore
