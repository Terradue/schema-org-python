from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_therapy import MedicalTherapy

class RadiationTherapy(MedicalTherapy):
    """
A process of care using radiation aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/RadiationTherapy'] = Field( # type: ignore
        default='https://schema.org/RadiationTherapy',
        alias='@type',
        serialization_alias='@type'
    )
