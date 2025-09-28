from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_enumeration import MedicalEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DrugCostCategory(MedicalEnumeration):
    """
Enumerated categories of medical drug costs.
    """
    class_: Literal['https://schema.org/DrugCostCategory'] = Field( # type: ignore
        default='https://schema.org/DrugCostCategory',
        alias='@type',
        serialization_alias='@type'
    )
