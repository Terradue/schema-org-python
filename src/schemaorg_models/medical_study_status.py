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

class MedicalStudyStatus(MedicalEnumeration):
    '''
    The status of a medical study. Enumerated type.
    '''
    class_: Literal['https://schema.org/MedicalStudyStatus'] = Field( # type: ignore
        default='https://schema.org/MedicalStudyStatus',
        alias='@type',
        serialization_alias='@type'
    )
