from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_therapy import MedicalTherapy

class OccupationalTherapy(MedicalTherapy):
    """
A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.
    """
    class_: Literal['https://schema.org/OccupationalTherapy'] = Field( # type: ignore
        default='https://schema.org/OccupationalTherapy',
        alias='@type',
        serialization_alias='@type'
    )
