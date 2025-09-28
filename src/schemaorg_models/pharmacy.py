from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_organization import MedicalOrganization

class Pharmacy(MedicalOrganization):
    """
A pharmacy or drugstore.
    """
    class_: Literal['https://schema.org/Pharmacy'] = Field( # type: ignore
        default='https://schema.org/Pharmacy',
        alias='@type',
        serialization_alias='@type'
    )
