from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_entity import MedicalEntity

class MedicalIndication(MedicalEntity):
    """
A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.
    """
    class_: Literal['https://schema.org/MedicalIndication'] = Field( # type: ignore
        default='https://schema.org/MedicalIndication',
        alias='@type',
        serialization_alias='@type'
    )
