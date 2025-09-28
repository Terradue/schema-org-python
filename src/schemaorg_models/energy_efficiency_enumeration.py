from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EnergyEfficiencyEnumeration(Enumeration):
    """
Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.
    """
    class_: Literal['https://schema.org/EnergyEfficiencyEnumeration'] = Field( # type: ignore
        default='https://schema.org/EnergyEfficiencyEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
