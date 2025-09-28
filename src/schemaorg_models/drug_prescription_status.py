from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_enumeration import MedicalEnumeration

class DrugPrescriptionStatus(MedicalEnumeration):
    """
Indicates whether this drug is available by prescription or over-the-counter.
    """
    class_: Literal['https://schema.org/DrugPrescriptionStatus'] = Field( # type: ignore
        default='https://schema.org/DrugPrescriptionStatus',
        alias='@type',
        serialization_alias='@type'
    )
