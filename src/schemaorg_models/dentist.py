from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_business import MedicalBusiness

class Dentist(MedicalBusiness):
    """
A dentist.
    """
    class_: Literal['https://schema.org/Dentist'] = Field( # type: ignore
        default='https://schema.org/Dentist',
        alias='@type',
        serialization_alias='@type'
    )
