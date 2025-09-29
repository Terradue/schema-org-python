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
from .medical_indication import MedicalIndication

class TreatmentIndication(MedicalIndication):
    '''
    An indication for treating an underlying condition, symptom, etc.
    '''
    class_: Literal['https://schema.org/TreatmentIndication'] = Field( # type: ignore
        default='https://schema.org/TreatmentIndication',
        alias='@type',
        serialization_alias='@type'
    )
