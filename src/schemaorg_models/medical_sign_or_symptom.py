from __future__ import annotations

from .medical_condition import MedicalCondition    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class MedicalSignOrSymptom(MedicalCondition):
    """
Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.
    """
    class_: Literal['https://schema.org/MedicalSignOrSymptom'] = Field( # type: ignore
        default='https://schema.org/MedicalSignOrSymptom',
        alias='@type',
        serialization_alias='@type'
    )
    possibleTreatment: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'possibleTreatment',
            'https://schema.org/possibleTreatment'
        ),
        serialization_alias='https://schema.org/possibleTreatment'
    )
