from __future__ import annotations

from .specialty import Specialty    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalSpecialty(Specialty):
    """
Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalSpecialty'] = Field( # type: ignore
        default='https://schema.org/MedicalSpecialty',
        alias='@type',
        serialization_alias='@type'
    )
