from __future__ import annotations

from .medical_enumeration import MedicalEnumeration    

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
