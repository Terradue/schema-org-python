from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .medical_sign_or_symptom import MedicalSignOrSymptom

class MedicalSymptom(MedicalSignOrSymptom):
    '''
    Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.
    '''
    class_: Literal['https://schema.org/MedicalSymptom'] = Field( # type: ignore
        default='https://schema.org/MedicalSymptom',
        alias='@type',
        serialization_alias='@type'
    )
