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

class MedicalAudienceType(MedicalEnumeration):
    '''
    Target audiences types for medical web pages. Enumerated type.
    '''
    class_: Literal['https://schema.org/MedicalAudienceType'] = Field( # type: ignore
        default='https://schema.org/MedicalAudienceType',
        alias='@type',
        serialization_alias='@type'
    )
