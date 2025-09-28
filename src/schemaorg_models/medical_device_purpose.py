from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_enumeration import MedicalEnumeration

class MedicalDevicePurpose(MedicalEnumeration):
    """
Categories of medical devices, organized by the purpose or intended use of the device.
    """
    class_: Literal['https://schema.org/MedicalDevicePurpose'] = Field( # type: ignore
        default='https://schema.org/MedicalDevicePurpose',
        alias='@type',
        serialization_alias='@type'
    )
