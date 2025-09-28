from __future__ import annotations

from .medical_sign_or_symptom import MedicalSignOrSymptom    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalSymptom(MedicalSignOrSymptom):
    """
Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.
    """
    class_: Literal['https://schema.org/MedicalSymptom'] = Field( # type: ignore
        default='https://schema.org/MedicalSymptom',
        alias='@type',
        serialization_alias='@type'
    )
