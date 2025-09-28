from __future__ import annotations

from .medical_enumeration import MedicalEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicineSystem(MedicalEnumeration):
    """
The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
    """
    class_: Literal['https://schema.org/MedicineSystem'] = Field( # type: ignore
        default='https://schema.org/MedicineSystem',
        alias='@type',
        serialization_alias='@type'
    )
