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
from .medical_enumeration import MedicalEnumeration

class MedicalObservationalStudyDesign(MedicalEnumeration):
    '''
    Design models for observational medical studies. Enumerated type.
    '''
    class_: Literal['https://schema.org/MedicalObservationalStudyDesign'] = Field( # type: ignore
        default='https://schema.org/MedicalObservationalStudyDesign',
        alias='@type',
        serialization_alias='@type'
    )
