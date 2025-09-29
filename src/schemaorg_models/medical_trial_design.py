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

class MedicalTrialDesign(MedicalEnumeration):
    '''
    Design models for medical trials. Enumerated type.
    '''
    class_: Literal['https://schema.org/MedicalTrialDesign'] = Field( # type: ignore
        default='https://schema.org/MedicalTrialDesign',
        alias='@type',
        serialization_alias='@type'
    )
