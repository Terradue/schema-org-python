from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_enumeration import MedicalEnumeration

class MedicalObservationalStudyDesign(MedicalEnumeration):
    """
Design models for observational medical studies. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalObservationalStudyDesign'] = Field( # type: ignore
        default='https://schema.org/MedicalObservationalStudyDesign',
        alias='@type',
        serialization_alias='@type'
    )
