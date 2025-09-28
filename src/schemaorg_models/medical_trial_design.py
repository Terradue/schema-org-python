from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_enumeration import MedicalEnumeration

class MedicalTrialDesign(MedicalEnumeration):
    """
Design models for medical trials. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalTrialDesign'] = Field( # type: ignore
        default='https://schema.org/MedicalTrialDesign',
        alias='@type',
        serialization_alias='@type'
    )
