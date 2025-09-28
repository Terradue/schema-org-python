from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_enumeration import MedicalEnumeration

class PhysicalExam(MedicalEnumeration):
    """
A type of physical examination of a patient performed by a physician. 
    """
    class_: Literal['https://schema.org/PhysicalExam'] = Field( # type: ignore
        default='https://schema.org/PhysicalExam',
        alias='@type',
        serialization_alias='@type'
    )
