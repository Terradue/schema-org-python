from __future__ import annotations

from .medical_enumeration import MedicalEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalProcedureType(MedicalEnumeration):
    """
An enumeration that describes different types of medical procedures.
    """
    class_: Literal['https://schema.org/MedicalProcedureType'] = Field( # type: ignore
        default='https://schema.org/MedicalProcedureType',
        alias='@type',
        serialization_alias='@type'
    )
