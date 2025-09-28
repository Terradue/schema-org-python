from __future__ import annotations

from .medical_indication import MedicalIndication    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PreventionIndication(MedicalIndication):
    """
An indication for preventing an underlying condition, symptom, etc.
    """
    class_: Literal['https://schema.org/PreventionIndication'] = Field( # type: ignore
        default='https://schema.org/PreventionIndication',
        alias='@type',
        serialization_alias='@type'
    )
