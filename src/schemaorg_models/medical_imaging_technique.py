from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_enumeration import MedicalEnumeration

class MedicalImagingTechnique(MedicalEnumeration):
    """
Any medical imaging modality typically used for diagnostic purposes. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalImagingTechnique'] = Field( # type: ignore
        default='https://schema.org/MedicalImagingTechnique',
        alias='@type',
        serialization_alias='@type'
    )
