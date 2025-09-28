from __future__ import annotations

from .medical_indication import MedicalIndication    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TreatmentIndication(MedicalIndication):
    """
An indication for treating an underlying condition, symptom, etc.
    """
    class_: Literal['https://schema.org/TreatmentIndication'] = Field( # type: ignore
        default='https://schema.org/TreatmentIndication',
        alias='@type',
        serialization_alias='@type'
    )
