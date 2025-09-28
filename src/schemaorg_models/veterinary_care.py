from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_organization import MedicalOrganization

class VeterinaryCare(MedicalOrganization):
    """
A vet's office.
    """
    class_: Literal['https://schema.org/VeterinaryCare'] = Field( # type: ignore
        default='https://schema.org/VeterinaryCare',
        alias='@type',
        serialization_alias='@type'
    )
