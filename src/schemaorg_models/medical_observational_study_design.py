from __future__ import annotations

from .medical_enumeration import MedicalEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalObservationalStudyDesign(MedicalEnumeration):
    """
Design models for observational medical studies. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalObservationalStudyDesign'] = Field( # type: ignore
        default='https://schema.org/MedicalObservationalStudyDesign',
        alias='@type',
        serialization_alias='@type'
    )
