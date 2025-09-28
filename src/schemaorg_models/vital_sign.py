from __future__ import annotations

from .medical_sign import MedicalSign    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class VitalSign(MedicalSign):
    """
Vital signs are measures of various physiological functions in order to assess the most basic body functions.
    """
    class_: Literal['https://schema.org/VitalSign'] = Field( # type: ignore
        default='https://schema.org/VitalSign',
        alias='@type',
        serialization_alias='@type'
    )
