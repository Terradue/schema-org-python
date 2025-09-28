from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_enumeration import MedicalEnumeration

class DrugCostCategory(MedicalEnumeration):
    """
Enumerated categories of medical drug costs.
    """
    class_: Literal['https://schema.org/DrugCostCategory'] = Field( # type: ignore
        default='https://schema.org/DrugCostCategory',
        alias='@type',
        serialization_alias='@type'
    )
