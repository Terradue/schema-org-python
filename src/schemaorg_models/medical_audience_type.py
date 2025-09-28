from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_enumeration import MedicalEnumeration

class MedicalAudienceType(MedicalEnumeration):
    """
Target audiences types for medical web pages. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalAudienceType'] = Field( # type: ignore
        default='https://schema.org/MedicalAudienceType',
        alias='@type',
        serialization_alias='@type'
    )
