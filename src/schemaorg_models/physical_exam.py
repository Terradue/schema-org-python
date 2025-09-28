from __future__ import annotations

from .medical_enumeration import MedicalEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PhysicalExam(MedicalEnumeration):
    """
A type of physical examination of a patient performed by a physician. 
    """
    class_: Literal['https://schema.org/PhysicalExam'] = Field( # type: ignore
        default='https://schema.org/PhysicalExam',
        alias='@type',
        serialization_alias='@type'
    )
