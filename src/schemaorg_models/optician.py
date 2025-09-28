from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_business import MedicalBusiness

class Optician(MedicalBusiness):
    """
A store that sells reading glasses and similar devices for improving vision.
    """
    class_: Literal['https://schema.org/Optician'] = Field( # type: ignore
        default='https://schema.org/Optician',
        alias='@type',
        serialization_alias='@type'
    )
