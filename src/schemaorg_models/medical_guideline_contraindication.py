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
from .medical_guideline import MedicalGuideline

class MedicalGuidelineContraindication(MedicalGuideline):
    '''
    A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.
    '''
    class_: Literal['https://schema.org/MedicalGuidelineContraindication'] = Field( # type: ignore
        default='https://schema.org/MedicalGuidelineContraindication',
        alias='@type',
        serialization_alias='@type'
    )
